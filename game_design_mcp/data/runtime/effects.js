/* v0.1.0: presentation-only Canvas feedback. No damage, time-scale, audio or camera writes. */
(function(root) {
  const defaults = {effect:'impact',duration_ms:240,radius_px:36,particles:12,color:'#65d6ff',reduced_motion:false};
  function validate(input={}) {
    for(const k of Object.keys(input)) if(!(k in defaults)) throw new Error('Unknown config: '+k);
    const c={...defaults,...input};
    if(!['impact','burst','pulse'].includes(c.effect)) throw new Error('Invalid effect');
    for(const [k,min,max] of [['duration_ms',40,2000],['radius_px',1,160],['particles',0,48]])
      if(typeof c[k]!=='number'||!Number.isFinite(c[k])||c[k]<min||c[k]>max) throw new Error('Out of bounds: '+k);
    if(!Number.isInteger(c.duration_ms)||!Number.isInteger(c.particles)) throw new Error('Integer required');
    if(!/^#[0-9a-fA-F]{6}$/.test(c.color)||typeof c.reduced_motion!=='boolean') throw new Error('Invalid color/motion');
    return c;
  }
  function frame(config, elapsed) {
    const c=validate(config), t=Math.max(0,Math.min(1,elapsed/c.duration_ms));
    return {alpha:1-t,radius:c.reduced_motion?c.radius_px*.4:c.radius_px*(1-(1-t)**3),done:t>=1};
  }
  function createFeedback(canvas) {
    const ctx=canvas.getContext('2d');
    if(!ctx) throw new Error('Canvas 2D context required');
    let items=[], seen=new Set(), order=[], raf=0, destroyed=false;
    const reduced=()=>root.matchMedia?.('(prefers-reduced-motion: reduce)').matches||false;
    function draw(now) {
      ctx.clearRect(0,0,canvas.width,canvas.height);
      items=items.filter(i=>now-i.start<i.c.duration_ms);
      for(const i of items) {
        const f=frame(i.c,now-i.start);ctx.save();ctx.globalAlpha=f.alpha;ctx.strokeStyle=i.c.color;ctx.fillStyle=i.c.color;ctx.lineWidth=3;
        ctx.beginPath();ctx.arc(i.x,i.y,f.radius,0,Math.PI*2);ctx.stroke();
        if(!i.c.reduced_motion && i.c.effect!=='pulse') {
          for(let n=0;n<i.c.particles;n++) {
            const a=n/Math.max(1,i.c.particles)*Math.PI*2, r=f.radius*(i.c.effect==='burst'?1.5:1);
            ctx.beginPath();ctx.arc(i.x+Math.cos(a)*r,i.y+Math.sin(a)*r,2,0,Math.PI*2);ctx.fill();
          }
        }
        ctx.restore();
      }
      raf=items.length?root.requestAnimationFrame(draw):0;
    }
    return {
      emit(event, config={}) {
        if(destroyed) throw new Error('Feedback instance destroyed');
        if(!event||typeof event.id!=='string'||!event.id||event.id.length>128||typeof event.targetId!=='string'||!event.targetId||event.targetId.length>128) throw new Error('Event id and targetId required');
        if(!Number.isFinite(event.x)||!Number.isFinite(event.y)) throw new Error('Finite canvas coordinates required');
        const c=validate(config);
        if(event.kind!=='hit.confirmed'||event.confirmed!==true||seen.has(event.id)) return false;
        c.reduced_motion ||= reduced();
        if(items.length>=32) return false;
        seen.add(event.id);order.push(event.id);
        if(order.length>1024) seen.delete(order.shift());
        items.push({id:event.id,targetId:event.targetId,x:event.x,y:event.y,c,start:root.performance.now()});
        if(!raf) raf=root.requestAnimationFrame(draw);
        return true;
      },
      cancel(targetId) {items=items.filter(i=>i.targetId!==targetId);},
      clear() {items=[];seen.clear();order=[];if(raf)root.cancelAnimationFrame(raf);raf=0;ctx.clearRect(0,0,canvas.width,canvas.height);},
      destroy() {this.clear();destroyed=true;},
      activeCount() {return items.length;}
    };
  }
  root.GameFeedback={validate,frame,createFeedback};
  if(typeof module!=='undefined') module.exports=root.GameFeedback;
})(globalThis);
