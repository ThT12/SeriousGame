from io import StringIO
import sys

from seriousgame.io import inputs
from seriousgame.improvements import Improvement


improvement_one = Improvement(title='My First improvement')
improvement_two = Improvement(title='My Second improvement')
list_improvements = [improvement_one, improvement_two]


def test_ask_improvements_to_make_when_done(mocker):
    mocker.patch('sys.stdout', new_callable=StringIO)
    mocker.patch('builtins.input', side_effect=['Nothing', 'done'])
    out = inputs.ask_improvements_to_make(list_improvements)
    assert out is None
    output = sys.stdout.getvalue()
    assert output.find('try again') != -1


def test_ask_improvements_to_make_when_not_done(mocker):
    mocker.patch('sys.stdout', new_callable=StringIO)
    mocker.patch('builtins.input', side_effect=['Not an improvement', 'My Second improvement'])
    out = inputs.ask_improvements_to_make(list_improvements)
    assert isinstance(out, Improvement) and out == improvement_two
    output = sys.stdout.getvalue()
    assert output.find('try again') != -1
