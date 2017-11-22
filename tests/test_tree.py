from seriousgame import improvements
from seriousgame.effect import EffectDescriptor
from seriousgame.tree import ProgressionTree

tree = ProgressionTree()


def test_get_current_effects(mocker):
    value = {EffectDescriptor.INFLUENCE: 3}
    mocker.patch.object(improvements, 'merge_effects', return_value=value)
    mocker.patch.object(improvements.Improvements, 'get_current_effects', return_value=value)
    effects = tree.get_current_effects()
    assert effects == value
    assert improvements.merge_effects.call_count == len(tree.tree)


def test_get_improvements_available(mocker):
    improvement_one = improvements.Improvement(title='One')
    improvement_two = improvements.Improvement(title='Two')
    improvement_three = improvements.Improvement(title='Three')
    mocker.patch.object(improvements.Improvements, 'get_improvements_available',
                        side_effect=[[improvement_one, improvement_two], [improvement_three]])
    improvements_list = tree.get_improvements_available()
    assert improvements_list == [improvement_one, improvement_two, improvement_three]


def test_new_turn(mocker):
    mocker.patch.object(improvements.Improvements, 'new_turn', return_value= None)
    tree.new_turn()
    assert improvements.Improvements.new_turn.call_count == len(tree.tree)
