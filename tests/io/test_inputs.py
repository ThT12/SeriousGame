from io import StringIO
import sys

from seriousgame.io import inputs
from seriousgame.improvements import Improvement
from seriousgame.player import Player


player = Player(influence=10)
improvement_one = Improvement(title='My First improvement', influence_cost=1)
improvement_two = Improvement(title='My Second improvement', influence_cost=1)
list_improvements = [improvement_one, improvement_two]


def test_ask_improvements_to_make_when_done(mocker):
    mocker.patch('sys.stdout', new_callable=StringIO)
    mocker.patch('builtins.input', side_effect=['Nothing', 'done'])
    out = inputs.ask_improvements_to_make(list_improvements, player)
    assert out is None
    output = sys.stdout.getvalue()
    assert output.find('try again') != -1


def test_ask_improvements_to_make_when_not_done_and_enough_influence(mocker):
    mocker.patch('sys.stdout', new_callable=StringIO)
    mocker.patch('builtins.input', side_effect=['Not an improvement', 'My Second improvement'])
    out = inputs.ask_improvements_to_make(list_improvements, player)
    assert isinstance(out, Improvement) and out == improvement_two
    output = sys.stdout.getvalue()
    assert output.find('try again') != -1


def test_ask_improvements_to_make_when_not_done_and_not_enough_influence(mocker):
    mocker.patch('sys.stdout', new_callable=StringIO)
    mocker.patch('builtins.input', side_effect=['My First improvement', 'done'])
    player.influence = 0
    out = inputs.ask_improvements_to_make(list_improvements, player)
    assert out is None
    output = sys.stdout.getvalue()
    assert output.find('not have enough influence') != -1
