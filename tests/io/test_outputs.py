import sys
from io import StringIO

from seriousgame.country import Country
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


def test_display_improvements_with_improvement(mocker):
    mocker.patch('sys.stdout', new_callable=StringIO)
    mocker.spy(outputs, 'display_improvement')
    outputs.display_improvements(list_improvements, 5)
    assert outputs.display_improvement.call_count == len(list_improvements)


def test_display_improvements_without_improvement(mocker):
    mocker.patch('sys.stdout', new_callable=StringIO)
    mocker.spy(outputs, 'display_improvement')
    outputs.display_improvements([], 5)
    assert outputs.display_improvement.call_count == 0
    output = sys.stdout.getvalue()
    assert output.find('No improvement available') != -1


def test_display_influence_available(mocker):
    player = Player(influence=5)
    mocker.patch('sys.stdout', new_callable=StringIO)
    outputs.display_influence_available(player)
    assert sys.stdout.getvalue().find('5') != -1


def test_display_country_header(mocker):
    mocker.patch('sys.stdout', new_callable=StringIO)
    name = 'Name'
    outputs.display_country_header(name)
    assert sys.stdout.getvalue().find(name) != -1


def test_display_country_level(mocker):
    mocker.patch('sys.stdout', new_callable=StringIO)
    level = 0.28
    name = 'Name'
    outputs.display_country_level(name, level)
    output = sys.stdout.getvalue()
    assert output.find(name) != -1
    assert output.count('|') == int(level * 100)
    assert output.count(' ') == int((1-level) * 100) + 2
