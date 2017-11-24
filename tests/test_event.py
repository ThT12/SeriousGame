import random

import pytest

from seriousgame import event as ev
from seriousgame.country import Country
from seriousgame.effect import EffectDescriptor
from seriousgame.effect import Effects
from seriousgame.event import Event
from seriousgame.event import Events

country = Country()


def test_init_error():
    with pytest.raises(KeyError):
        Event(condition_direction='inp')


def test_is_event_possible_true(mocker):
    mocker.patch.object(Country, '__getattr__', return_value=0.5)
    event = Event(condition_type=EffectDescriptor.ECONOMY, condition_direction='inf', condition_value=0.6)
    assert event.is_event_possible(country)
    event = Event(condition_type=EffectDescriptor.ECONOMY, condition_direction='sup', condition_value=0.4)
    assert event.is_event_possible(country)


def test_is_event_possible_false(mocker):
    mocker.patch.object(Country, '__getattr__', return_value=0.5)
    event = Event(condition_type=EffectDescriptor.ECONOMY, condition_direction='inf', condition_value=0.4)
    assert not event.is_event_possible(country)
    event = Event(condition_type=EffectDescriptor.ECONOMY, condition_direction='sup', condition_value=0.6)
    assert not event.is_event_possible(country)


def test_get_effect(mocker):
    mocker.patch.object(Effects, 'get_current_effects', return_value={})
    event = Event()
    effect = event.get_effects()
    assert Effects.get_current_effects.call_count == 1
    assert effect == {}


def test_get_event_possible(mocker):
    mocker.patch.object(Event, 'is_event_possible', side_effect=[True, True, True, False, False])
    events = Events([Event(), Event(), Event(), Event(), Event()])
    events_possible = events.get_event_possible(country)
    assert events_possible == events.events[0:3]


def test_event_effect_with_event(mocker):
    effect_dict = {'effect': 0}
    mocker.patch.object(ev, 'is_event_occurs', return_value=True)
    mocker.patch.object(Events, 'get_event_possible', return_value=[Event(), Event()])
    mocker.patch.object(random, 'choice', return_value=Event())
    mocker.patch.object(Effects, 'get_current_effects', return_value=effect_dict)
    events = Events()
    effect = events.get_event_effect(country)
    assert effect == effect_dict
    assert random.choice.call_count == 1


def test_event_effect_event_not_occurs(mocker):
    effect_dict = {'effect': 0}
    mocker.patch.object(ev, 'is_event_occurs', return_value=False)
    mocker.patch.object(Events, 'get_event_possible', return_value=[Event(), Event()])
    mocker.patch.object(random, 'choice', return_value=Event())
    mocker.patch.object(Effects, 'get_current_effects', return_value=effect_dict)
    events = Events()
    effect = events.get_event_effect(country)
    assert effect == {}
    assert random.choice.call_count == 0


def test_event_effect_event_no_event(mocker):
    effect_dict = {'effect': 0}
    mocker.patch.object(ev, 'is_event_occurs', return_value=True)
    mocker.patch.object(Events, 'get_event_possible', return_value=[])
    mocker.patch.object(random, 'choice', return_value=Event())
    mocker.patch.object(Effects, 'get_current_effects', return_value=effect_dict)
    events = Events()
    effect = events.get_event_effect(country)
    assert effect == {}
    assert random.choice.call_count == 0


def test_is_event_occurs(mocker):
    mocker.patch.object(random, 'random', side_effect=[ev.PROBABILITY-0.01, ev.PROBABILITY+0.01])
    assert ev.is_event_occurs()
    assert not ev.is_event_occurs()
