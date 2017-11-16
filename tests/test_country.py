import pytest

from seriousgame.country import Country, verify_level_value


def test_new_turn_no_min():
    init_value = 0.5
    country = Country(init_ecology=init_value, init_economy=init_value, init_social=init_value)
    country.new_turn()
    assert country.ecology == init_value - country.INITIAL_REDUCTION
    assert country.economy == init_value - country.INITIAL_REDUCTION
    assert country.social == init_value - country.INITIAL_REDUCTION


def test_new_turn_with_min():
    country = Country(init_ecology=0, init_economy=0, init_social=0)
    country.new_turn()
    assert country.ecology == 0
    assert country.economy == 0
    assert country.social == 0


def test_is_win():
    country = Country(init_ecology=1, init_economy=1, init_social=1)
    assert country.is_win()


def test_is_not_win():
    country = Country(init_ecology=1, init_economy=0.99, init_social=1)
    assert not country.is_win()


def test_is_lost():
    country = Country(init_ecology=0)
    assert country.is_lost()
    country = Country(init_economy=0)
    assert country.is_lost()
    country = Country(init_social=0)
    assert country.is_lost()


def test_is_not_lost():
    country = Country(init_ecology=0.01, init_economy=0.01, init_social=0.01)
    assert not country.is_lost()


def test_verify_level_value():
    with pytest.raises(KeyError):
        verify_level_value(-0.01)
    with pytest.raises(KeyError):
        verify_level_value(1.01)
    verify_level_value(0.5)
