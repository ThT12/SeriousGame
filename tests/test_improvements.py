import pytest

from seriousgame import effect
from seriousgame.effect import Effect
from seriousgame.effect import EffectDescriptor
from seriousgame.effect import Effects
from seriousgame.improvements import Improvement
from seriousgame.improvements import Improvements

effect_one = Effect(effect_descriptor=EffectDescriptor.INFLUENCE, value=1)
effect_two = Effect(effect_descriptor=EffectDescriptor.INFLUENCE, value=4)
effect_tree = Effect(effect_descriptor=EffectDescriptor.ECOLOGY, value=-0.01)
improvement = Improvement(effects=Effects([effect_one, effect_two, effect_tree]))


def test_improvement_comparator():
    improvement_one = Improvement(title='One')
    improvement_one_bis = Improvement(title='One')
    improvement_two = Improvement(title='Two')
    improvement_one.number = 1
    assert improvement_one == 'One'
    assert improvement_one == improvement_one_bis
    assert improvement_one != 'Two'
    assert improvement_one != improvement_two
    assert improvement_one == 1
    assert improvement_one == '1'
    assert improvement_one != 2
    assert improvement_one != '2'
    with pytest.raises(KeyError):
        improvement_one.__eq__([2, 3])


def test_develop_improvement_already_done():
    improvement_already_done = Improvement(status=True)
    with pytest.raises(KeyError):
        improvement_already_done.develop()


def test_develop_improvement_ok():
    improvement_ok = Improvement(status=False)
    improvement_ok.develop()
    assert improvement_ok.status


def test_improvement_get_current_effect(mocker):
    value = {EffectDescriptor.INFLUENCE: 3}
    mocker.patch.object(Effects, 'get_current_effects', return_value=value)
    effects = improvement.get_current_effects()
    assert Effects.get_current_effects.call_count == 1
    assert effects == value


def test_improvement_new_turn(mocker):
    mocker.patch.object(Effects, 'new_turn', return_value=None)
    improvement.new_turn()
    assert Effects.new_turn.call_count == 1


improvement_done = Improvement(title='Done', effects=[effect_one], status=True)
another_improvement_done = Improvement(title='Another done', effects=[effect_two, effect_tree],
                                       requirements=(improvement_done,), status=True)
improvement_available = Improvement(title='Available', requirements=(improvement_done,), status=False)
improvement_not_available = Improvement(title='Not available', requirements=(improvement_done, improvement_available),
                                        status=False)
improvement_not_in_improvements = Improvement(title='Not in improvements')
improvement_with_requirement_not_in_improvements = Improvement(title='Requirement not in improvements', requirements=(
    improvement_done, improvement_not_in_improvements))

improvements = Improvements('Farming', (improvement_done, another_improvement_done, improvement_available,
                                        improvement_not_available))


def test_constructor_return_error_if_requirement_not_on_improvements():
    with pytest.raises(KeyError):
        Improvements(improvements=(improvement_done, improvement_available,
                                   improvement_with_requirement_not_in_improvements))


def test_are_requirements_reached_return_error_if_not_in_list():
    with pytest.raises(KeyError):
        improvements.are_improvement_requirements_reached(improvement_not_in_improvements)


def test_are_requirements_reached_when_there_are():
    assert improvements.are_improvement_requirements_reached(improvement_available)


def test_are_requirements_reached_when_there_are_not():
    assert not improvements.are_improvement_requirements_reached(improvement_not_available)


def test_get_improvements_done():
    assert improvements.get_improvements_done() == [improvement_done, another_improvement_done]


def test_get_improvements_available():
    assert improvements.get_improvements_available() == [improvement_available]


def test_improvements_get_current_effects(mocker):
    value = {EffectDescriptor.INFLUENCE: 3}
    mocker.patch.object(effect, 'merge_effects', return_value=value)
    mocker.patch.object(Improvement, 'get_current_effects', return_value=None)
    effects = improvements.get_current_effects()
    assert effect.merge_effects.call_count == len(improvements.get_improvements_done())
    assert Improvement.get_current_effects.call_count == len(improvements.get_improvements_done())
    assert effects == value


def test_improvements_new_turn(mocker):
    mocker.patch.object(Improvement, 'new_turn', return_value=None)
    improvements.new_turn()
    assert Improvement.new_turn.call_count == len(improvements.improvements)


def test_set_improvement_numbers(mocker):
    improvements_available = [improvements.improvements[0], improvements.improvements[2]]
    mocker.patch.object(Improvements, 'get_improvements_available', return_value=improvements_available)
    number_init = 2
    number_final = improvements.set_improvement_numbers(number_init)
    numbers = [imp.number for imp in improvements.improvements]
    assert number_final == number_init + len(improvements.get_improvements_available())
    assert numbers == [number_init, 0, number_final-1, 0]
