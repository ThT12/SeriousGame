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
