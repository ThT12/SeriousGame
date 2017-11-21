import pytest

from seriousgame import improvements
from seriousgame.effect import Effect, EffectDescriptor
from seriousgame.improvements import Improvement, Improvements

effect_one = Effect(effect_descriptor=EffectDescriptor.INFLUENCE, value=1)
effect_two = Effect(effect_descriptor=EffectDescriptor.INFLUENCE, value=4)
effect_tree = Effect(effect_descriptor=EffectDescriptor.ECOLOGY, value=-0.01)


def test_improvement_comparator():
    improvement_one = Improvement(title='One')
    improvement_one_bis = Improvement(title='One')
    improvement_two = Improvement(title='Two')
    assert improvement_one == 'One'
    assert improvement_one == improvement_one_bis
    assert improvement_one != 'Two'
    assert improvement_one != improvement_two
    with pytest.raises(KeyError):
        improvement_one.__eq__(2)


def test_develop_improvement_already_done():
    improvement = Improvement(status=True)
    with pytest.raises(KeyError):
        improvement.develop()


def test_develop_improvement_ok():
    improvement = Improvement(status=False)
    improvement.develop()
    assert improvement.status


def test_improvement_get_current_effect(mocker):
    improvement = Improvement(effects=[effect_one, effect_two, effect_tree])
    value = {EffectDescriptor.INFLUENCE: 3}
    mocker.patch.object(improvements, 'merge_effects', return_value=value)
    mocker.patch.object(Effect, 'get_current_effect', return_value=None)
    effects = improvement.get_current_effects()
    assert improvements.merge_effects.call_count == len(improvement.effects)
    assert Effect.get_current_effect.call_count == len(improvement.effects)
    assert effects == value


improvement_done = Improvement(title='Done', effects=[effect_one], status=True)
another_improvement_done = Improvement(title='Another done', effects=[effect_two, effect_tree],
                                       requirements=(improvement_done,), status=True)
improvement_available = Improvement(title='Available', requirements=(improvement_done,), status=False)
improvement_not_available = Improvement(title='Not available', requirements=(improvement_done, improvement_available),
                                        status=False)
improvement_not_in_improvements = Improvement(title='Not in improvements')
improvement_with_requirement_not_in_improvements = Improvement(title='Requirement not in improvements', requirements=(
    improvement_done, improvement_not_in_improvements))

improvements_obj = Improvements('Farming', (improvement_done, another_improvement_done, improvement_available,
                                            improvement_not_available))


def test_constructor_return_error_if_requirement_not_on_improvements():
    with pytest.raises(KeyError):
        Improvements(improvements=(improvement_done, improvement_available,
                                   improvement_with_requirement_not_in_improvements))


def test_are_requirements_reached_return_error_if_not_in_list():
    with pytest.raises(KeyError):
        improvements_obj.are_improvement_requirements_reached(improvement_not_in_improvements)


def test_are_requirements_reached_when_there_are():
    assert improvements_obj.are_improvement_requirements_reached(improvement_available)


def test_are_requirements_reached_when_there_are_not():
    assert not improvements_obj.are_improvement_requirements_reached(improvement_not_available)


def test_get_improvements_done():
    assert improvements_obj.get_improvements_done() == [improvement_done, another_improvement_done]


def test_get_improvements_available():
    assert improvements_obj.get_improvements_available() == [improvement_available]


def test_improvements_get_current_effects(mocker):
    value = {EffectDescriptor.INFLUENCE: 3}
    mocker.patch.object(improvements, 'merge_effects', return_value=value)
    mocker.patch.object(Improvement, 'get_current_effects', return_value=None)
    effects = improvements_obj.get_current_effects()
    assert improvements.merge_effects.call_count == len(improvements_obj.get_improvements_done())
    assert Improvement.get_current_effects.call_count == len(improvements_obj.get_improvements_done())
    assert effects == value


def test_merge_effects():
    dict1 = {EffectDescriptor.INFLUENCE: 3, EffectDescriptor.ECOLOGY: -0.01}
    dict2 = {EffectDescriptor.INFLUENCE: -1, EffectDescriptor.ECONOMY: 0.01}
    effects = improvements.merge_effects(dict1, dict2)
    assert effects == {EffectDescriptor.INFLUENCE: 2, EffectDescriptor.ECOLOGY: -0.01, EffectDescriptor.ECONOMY: 0.01}
