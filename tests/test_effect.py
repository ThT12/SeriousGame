from seriousgame import effect as ef
from seriousgame.effect import Effect
from seriousgame.effect import Effects
from seriousgame.effect import EffectDescriptor


def test_constructor_effect():
    effect_normal = Effect(effect_descriptor=EffectDescriptor.INFLUENCE, start_effect=2, end_effect=4)
    assert effect_normal.start_effect == 2
    assert effect_normal.end_effect == 4
    effect_lobbying = Effect(effect_descriptor=EffectDescriptor.LOBBYING, start_effect=2, end_effect=4)
    assert effect_lobbying.start_effect == 0
    assert effect_lobbying.end_effect == 1


def test_str():
    effect_descriptor = EffectDescriptor.INFLUENCE
    value = 3
    start_effect = 5
    duration = 2
    effect = Effect(effect_descriptor=effect_descriptor, value=value, start_effect=start_effect,
                    end_effect=start_effect+duration)
    str_effect = str(effect)
    assert str_effect.find(effect_descriptor) != -1
    assert str_effect.find(str(value)) != -1
    assert str_effect.find(str(start_effect)) != -1
    assert str_effect.find(str(duration)) != -1

    effect_inf = Effect(effect_descriptor=effect_descriptor, value=value, start_effect=start_effect,
                        end_effect=float('inf'))
    str_effect_inf = str(effect_inf)
    assert str_effect_inf.find(effect_descriptor) != -1
    assert str_effect_inf.find(str(value)) != -1
    assert str_effect_inf.find(str(start_effect)) != -1
    assert str_effect_inf.find('permanently') != -1


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


def test_get_current_effects(mocker):
    value = {EffectDescriptor.INFLUENCE: 3}
    effects = Effects([Effect(), Effect(), Effect()])
    mocker.patch.object(ef, 'merge_effects', return_value=value)
    mocker.patch.object(Effect, 'get_current_effect', return_value=None)
    effects_dict = effects.get_current_effects()
    assert ef.merge_effects.call_count == len(effects.effects)
    assert Effect.get_current_effect.call_count == len(effects.effects)
    assert effects_dict == value


def test_effects_new_turn(mocker):
    mocker.patch.object(Effect, 'new_turn', return_value=None)
    effects = Effects([Effect(), Effect(), Effect()])
    effects.new_turn()
    assert Effect.new_turn.call_count == len(effects.effects)


def test_merge_effects():
    dict1 = {EffectDescriptor.INFLUENCE: 3, EffectDescriptor.ECOLOGY: -0.01}
    dict2 = {EffectDescriptor.INFLUENCE: -1, EffectDescriptor.ECONOMY: 0.01}
    effects = ef.merge_effects(dict1, dict2)
    assert effects == {EffectDescriptor.INFLUENCE: 2, EffectDescriptor.ECOLOGY: -0.01, EffectDescriptor.ECONOMY: 0.01}