import sys
from io import StringIO

from seriousgame.effect import Effect
from seriousgame.effect import Effects
from seriousgame.event import Event
from seriousgame.improvements import Improvement
from seriousgame.improvements import Improvements
from seriousgame.io import outputs
from seriousgame.player import Player
from seriousgame.tree import ProgressionTree

improvement_green = Improvement(title='My First improvement', influence_cost=5, number=2, description='Description')
improvement_red = Improvement(title='My Second improvement', influence_cost=9, number=4)
list_improvements = [improvement_green, improvement_red]


def test_display_improvement_green_with_number(mocker):
    mocker.patch('sys.stdout', new_callable=StringIO)
    outputs.display_improvement(improvement_green, 5, is_number_displayed=True)
    output = sys.stdout.getvalue()
    assert output.find('First improvement') != -1
    assert output.find('5') != -1
    assert output.find('2') != -1
    assert output.find('\033[92m') != -1


def test_display_improvement_red_without_number(mocker):
    mocker.patch('sys.stdout', new_callable=StringIO)
    outputs.display_improvement(improvement_red, 5,  is_number_displayed=False)
    output = sys.stdout.getvalue()
    assert output.find('Second improvement') != -1
    assert output.find('9') != -1
    assert output.find('4') == -1
    assert output.find('\033[91m') != -1


def test_display_improvement_no_color(mocker):
    mocker.patch('sys.stdout', new_callable=StringIO)
    outputs.display_improvement(improvement_red)
    output = sys.stdout.getvalue()
    assert output.find('Second improvement') != -1
    assert output.find('9') != -1
    assert output.find('\033') == -1


def test_display_improvement_details(mocker):
    mocker.patch('sys.stdout', new_callable=StringIO)
    mocker.patch.object(outputs, 'effects_to_str', return_value='My effects')
    outputs.display_improvement_details(improvement_green)
    output = sys.stdout.getvalue()
    assert output.find('First improvement') != -1
    assert output.find('Description') != -1
    assert output.find('5') != -1
    assert output.find('2') == -1
    assert output.find('My effects') != -1


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


def test_display_improvements_available(mocker):
    mocker.patch('sys.stdout', new_callable=StringIO)
    mocker.patch.object(outputs, 'display_improvements', return_value=None)
    improvements_name = 'Farming'
    improvements = Improvements(improvements_name, tuple(list_improvements))
    outputs.display_improvements_available(improvements)
    assert sys.stdout.getvalue().find(improvements_name) != -1
    assert outputs.display_improvements.call_args[0] == (improvements.get_improvements_available(), None)
    assert outputs.display_improvements.call_args[1] == {'is_number_displayed': True}


def test_display_improvements_done(mocker):
    mocker.patch('sys.stdout', new_callable=StringIO)
    mocker.patch.object(outputs, 'display_improvements', return_value=None)
    improvements_name = 'Farming'
    improvements = Improvements(improvements_name, tuple(list_improvements))
    outputs.display_improvements_done(improvements)
    assert sys.stdout.getvalue().find(improvements_name) != -1
    assert outputs.display_improvements.call_args[0] == (improvements.get_improvements_done(),)
    assert outputs.display_improvements.call_args[1] == {'is_number_displayed': False}


def test_display_tree_available(mocker):
    mocker.patch.object(outputs, 'display_improvements_available', return_value=None)
    tree = ProgressionTree()
    outputs.display_tree_available(tree)
    assert outputs.display_improvements_available.call_count == len(tree.tree)


def test_display_tree_done(mocker):
    mocker.patch.object(outputs, 'display_improvements_done', return_value=None)
    tree = ProgressionTree()
    outputs.display_tree_done(tree)
    assert outputs.display_improvements_done.call_count == len(tree.tree)


def test_display_influence_available_upper_than_zero(mocker):
    player = Player(influence=5)
    mocker.patch('sys.stdout', new_callable=StringIO)
    outputs.display_influence_available(player)
    assert sys.stdout.getvalue().find('5') != -1


def test_display_influence_available_lower_than_zero(mocker):
    player = Player(influence=-1)
    mocker.patch('sys.stdout', new_callable=StringIO)
    outputs.display_influence_available(player)
    assert sys.stdout.getvalue().find('0') != -1


def test_display_country_header(mocker):
    mocker.patch('sys.stdout', new_callable=StringIO)
    name = 'Name'
    year = 2017
    outputs.display_country_header(name, year)
    output = sys.stdout.getvalue()
    assert output.find(name) != -1
    assert output.find(str(year)) != -1


def test_display_country_level(mocker):
    mocker.patch('sys.stdout', new_callable=StringIO)
    level = 0.28
    name = 'Name'
    outputs.display_country_level(name, level)
    output = sys.stdout.getvalue()
    assert output.find(name) != -1
    assert output.count('|') == int(level * 100)
    assert output.count(' ') == int((1-level) * 100) + 2


def test_display_win(mocker):
    mocker.patch('sys.stdout', new_callable=StringIO)
    outputs.display_win()
    assert sys.stdout.getvalue().find('win') != -1


def test_display_lost(mocker):
    mocker.patch('sys.stdout', new_callable=StringIO)
    outputs.display_lost()
    assert sys.stdout.getvalue().find('loose') != -1


def test_display_effects(mocker):
    effects = Effects([Effect(),  Effect()])
    mocker.patch.object(Effect, '__str__', return_value='Effect')
    str_effects = outputs.effects_to_str(effects)
    assert Effect.__str__.call_count == len(effects.effects)
    assert str_effects.count('Effect') == len(effects.effects)


def test_display_introduction(mocker):
    mocker.patch('sys.stdout', new_callable=StringIO)
    mocker.patch('builtins.input', return_value=None)
    outputs.display_context_part_one()
    outputs.display_context_part_two()
    assert len(sys.stdout.getvalue()) > 0


def test_display_event(mocker):
    name = 'Name'
    description = 'Description'
    effects = 'Effects'
    mocker.patch('sys.stdout', new_callable=StringIO)
    mocker.patch.object(outputs, 'effects_to_str', return_value=effects)
    event = Event(name=name, description=description, effects=Effects())
    outputs.display_event(event)
    out = sys.stdout.getvalue()
    assert out.find(name) != -1
    assert out.find(description) != -1
    assert out.find(effects) != -1


def test_display_help(mocker):
    mocker.patch('sys.stdout', new_callable=StringIO)
    outputs.display_help()
    assert len(sys.stdout.getvalue()) > 0
