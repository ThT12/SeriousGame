from seriousgame.tree import ProgressionTree
from seriousgame import improvements


tree = ProgressionTree()


def test_get_current_effects(mocker):
    value = {'test': 3}
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
