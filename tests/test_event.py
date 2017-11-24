import pytest

from seriousgame.country import Country
from seriousgame.effect import EffectDescriptor
from seriousgame.event import Event

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
