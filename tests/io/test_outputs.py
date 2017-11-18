from io import StringIO
import sys

from seriousgame.improvements import Improvement
from seriousgame.io import outputs
from seriousgame.player import Player


improvement_green = Improvement(title='My First improvement', influence_cost=1, description='My First description')
improvement_red = Improvement(title='My Second improvement', influence_cost=9, description='My Second description')
list_improvements = [improvement_green, improvement_red]


def test_display_improvement_green(mocker):
    mocker.patch('sys.stdout', new_callable=StringIO)
    outputs.display_improvement(improvement_green, 5)
    output = sys.stdout.getvalue()
    assert output.find('First improvement') != -1
    assert output.find('1') != -1
    assert output.find('First description') != -1
    assert output.find('\033[92m') != -1


def test_display_improvement_red(mocker):
    mocker.patch('sys.stdout', new_callable=StringIO)
    outputs.display_improvement(improvement_red, 5)
    output = sys.stdout.getvalue()
    assert output.find('Second improvement') != -1
    assert output.find('9') != -1
    assert output.find('Second description') != -1
    assert output.find('\033[91m') != -1


def test_display_improvement_no_color(mocker):
    mocker.patch('sys.stdout', new_callable=StringIO)
    outputs.display_improvement(improvement_red)
    output = sys.stdout.getvalue()
    assert output.find('Second improvement') != -1
    assert output.find('9') != -1
    assert output.find('Second description') != -1
    assert output.find('\033') == -1


def test_display_improvements(mocker):
    mocker.patch('sys.stdout', new_callable=StringIO)
    mocker.spy(outputs, 'display_improvement')
    outputs.display_improvements(list_improvements, 5)
    assert outputs.display_improvement.call_count == len(list_improvements)


player = Player(influence=5)


def test_display_influence_available(mocker):
    mocker.patch('sys.stdout', new_callable=StringIO)
    outputs.display_influence_available(player)
    assert sys.stdout.getvalue().find('5') != -1
