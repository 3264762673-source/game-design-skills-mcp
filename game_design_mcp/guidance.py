"""Bounded topic routing; no execution of returned instructions."""
import json
from pathlib import Path
from typing import Literal

Topic = Literal['character-art', 'environment-art', 'item-art', 'ui-layout',
                'icon-art', 'ui-interaction', 'vfx', 'character-animation',
                'item-animation', 'godot-project', 'godot-assets',
                'godot-scene-input', 'godot-animation', 'godot-ui', 'godot-export']
Stage = Literal['rules', 'implementation', 'evidence']

def catalog():
    return json.loads((Path(__file__).parent/'data/design-topics.json').read_text(encoding='utf-8'))

def list_topics():
    return {'topics': [{'topic': t['topic'], 'title': t['title'], 'skill_id': t['skill_id']}
                       for t in catalog()['topics']],
            'stages': ['rules', 'implementation', 'evidence']}

def get_guidance(topic: Topic, stage: Stage = 'rules'):
    from .core import read_skill
    record = next((t for t in catalog()['topics'] if t['topic'] == topic), None)
    if record is None or stage not in ('rules', 'implementation', 'evidence'):
        raise ValueError('Unknown topic or stage; use list_design_topics')
    skill = record.get('implementation_skill', record['skill_id']) if stage == 'implementation' else record['skill_id']
    return {'topic': topic, 'stage': stage, 'skill_id': skill, 'document': record[stage],
            'content': read_skill(skill, record[stage]),
            'limitations': 'Guidance only; no Godot editor connection, asset generation or runtime verification'}
