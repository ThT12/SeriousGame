import sys
from io import StringIO

from seriousgame.improvements import Improvement
from seriousgame.io import inputs
from seriousgame.io import outputs
from seriousgame.player import Player
from seriousgame.tree import ProgressionTree

player = Player(influence=10)
tree = ProgressionTree()
improvement_one = Improvement(title='My First improvement', influence_cost=1, number=1)
improvement_two = Improvement(title='My Second improvement', influence_cost=1)
list_improvements = [improvement_one, improvement_two]


def test_ask_improvements_to_make_when_done(mocker):
    mocker.patch('sys.stdout', new_callable=StringIO)
    mocker.patch('builtins.input', side_effect=['Nothing', 'done'])
    out = inputs.ask_improvements_to_make(list_improvements, player, tree)
    assert out is None
    output = sys.stdout.getvalue()
    assert output.find('try again') != -1


def test_ask_improvements_to_make_when_not_done_and_enough_influence(mocker):
    mocker.patch('sys.stdout', new_callable=StringIO)
    mocker.patch('builtins.input', side_effect=['Not an improvement', 'My Second improvement'])
    out = inputs.ask_improvements_to_make(list_improvements, player, tree)
    assert isinstance(out, Improvement) and out == improvement_two
    output = sys.stdout.getvalue()
    assert output.find('try again') != -1


def test_ask_improvements_to_make_when_not_done_and_not_enough_influence(mocker):
    mocker.patch('sys.stdout', new_callable=StringIO)
    mocker.patch('builtins.input', side_effect=['My First improvement', 'done'])
    player.influence = 0
    out = inputs.ask_improvements_to_make(list_improvements, player, tree)
    assert out is None
    assert sys.stdout.getvalue().find('not have enough influence') != -1


def test_ask_improvements_to_make_when_improvement_details_asked(mocker):
    mocker.patch('sys.stdout', new_callable=StringIO)
    mocker.patch('builtins.input', side_effect=['Detail not understood', 'Detail 1', 'done'])
    mocker.spy(outputs, 'display_improvement_details')
    out = inputs.ask_improvements_to_make(list_improvements, player, tree)
    assert out is None
    assert outputs.display_improvement_details.call_count == 1
    assert sys.stdout.getvalue().find('try again') != -1


def test_ask_improvements_to_make_when_improvement_done_asked(mocker):
    mocker.patch('sys.stdout', new_callable=StringIO)
    mocker.patch('builtins.input', side_effect=['Improvement done', 'done'])
    mocker.spy(outputs, 'display_tree_done')
    out = inputs.ask_improvements_to_make(list_improvements, player, tree)
    assert out is None
    assert outputs.display_tree_done.call_count == 1


def test_ask_player_name_and_country(mocker):
    name = 'Name'
    country = 'Country'
    mocker.patch('sys.stdout', new_callable=StringIO)
    mocker.patch('builtins.input', side_effect=[name, country])
    [player_name, country_name] = inputs.ask_player_name_and_country()
    assert player_name == name
    assert country_name == country
