from seriousgame import effect
from seriousgame.effect import EffectDescriptor
from seriousgame.improvements import Improvement
from seriousgame.improvements import Improvements
from seriousgame.tree import ProgressionTree

tree = ProgressionTree()


def test_get_current_effects(mocker):
    value = {EffectDescriptor.INFLUENCE: 3}
    mocker.patch.object(effect, 'merge_effects', return_value=value)
    mocker.patch.object(Improvements, 'get_current_effects', return_value=value)
    effects = tree.get_current_effects()
    assert effects == value
    assert effect.merge_effects.call_count == len(tree.tree)


def test_get_improvements_available(mocker):
    improvement_one = Improvement(title='One')
    improvement_two = Improvement(title='Two')
    improvement_three = Improvement(title='Three')
    mocker.patch.object(Improvements, 'get_improvements_available',
                        side_effect=[[improvement_one, improvement_two], [improvement_three]])
    improvements_list = tree.get_improvements_available()
    assert improvements_list == [improvement_one, improvement_two, improvement_three]


def test_new_turn(mocker):
    mocker.patch.object(Improvements, 'new_turn', return_value= None)
    tree.new_turn()
    assert Improvements.new_turn.call_count == len(tree.tree)


def test_set_improvement_numbers(mocker):
    mocker.spy(Improvements, 'set_improvement_numbers')
    tree.set_improvement_numbers()
    assert Improvements.set_improvement_numbers.call_count == len(tree.tree)
