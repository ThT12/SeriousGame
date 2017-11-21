from seriousgame.effect import Effect
from seriousgame.effect import EffectDescriptor


def test_constructor_effect():
    effect_normal = Effect(effect_descriptor=EffectDescriptor.INFLUENCE, start_effect=2, end_effect=4)
    assert effect_normal.start_effect == 2
    assert effect_normal.end_effect == 4
    effect_lobbying = Effect(effect_descriptor=EffectDescriptor.LOBBYING, start_effect=2, end_effect=4)
    assert effect_lobbying.start_effect == 0
    assert effect_lobbying.end_effect == 1


def test_new_turn():
    effect = Effect()
    turn = effect.turn_since_done
    effect.new_turn()
    assert effect.turn_since_done == turn + 1


def test_get_current_effect_on():
    value = 4
    effect_in_progress = Effect(effect_descriptor=EffectDescriptor.INFLUENCE, value=value, start_effect=2, end_effect=4)
    effect_in_progress.turn_since_done = 3
    assert effect_in_progress.get_current_effect() == {EffectDescriptor.INFLUENCE: value}


def test_get_current_effect_off():
    effect_not_started = Effect(effect_descriptor=EffectDescriptor.INFLUENCE, start_effect=2, end_effect=4)
    effect_not_started.turn_since_done = 1
    assert effect_not_started.get_current_effect() == {}
    effect_finished = Effect(effect_descriptor=EffectDescriptor.INFLUENCE, start_effect=2, end_effect=4)
    effect_finished.turn_since_done = 5
    assert effect_finished.get_current_effect() == {}
