import pytest

from seriousgame.improvements import Improvement, Improvements


improvement_done = Improvement(effects={'Influence': 1}, status=True)
another_improvement_done = Improvement(effects={'Influence': 4, 'Ecology': -0.01}, requirements=(improvement_done,),
                                       status=True)
improvement_available = Improvement(requirements=(improvement_done,), status=False)
improvement_not_available = Improvement(requirements=(improvement_done, improvement_available), status=False)
improvement_not_in_improvements = Improvement()
improvement_with_requirement_not_in_improvements = Improvement(
    requirements=(improvement_done, improvement_not_in_improvements))

improvements = Improvements(improvement_done, another_improvement_done, improvement_available, improvement_not_available)


def test_constructor_return_error_if_requirement_not_on_improvements():
    with pytest.raises(KeyError):
        Improvements(improvement_done, improvement_available, improvement_with_requirement_not_in_improvements)


def test_are_requirements_reached_return_error_if_not_in_list():
    with pytest.raises(KeyError):
        improvements.are_improvement_requirements_reached(improvement_not_in_improvements)


def test_are_requirements_reached_when_there_are():
    assert improvements.are_improvement_requirements_reached(improvement_available)


def test_are_requirements_reached_when_there_are_not():
    assert not improvements.are_improvement_requirements_reached(improvement_not_available)


def test_get_improvements_done():
    assert improvements.get_improvements_done() == [improvement_done, another_improvement_done]


def test_get_improvements_available():
    assert improvements.get_improvements_available() == [improvement_available]


def test_get_current_effects():
    assert improvements.get_current_effects() == {'Influence': 5, 'Ecology': -0.01}
