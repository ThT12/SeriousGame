import pytest

from seriousgame.player import Player

player = Player()


def test_one_new_turn():
    init_influence = player.influence
    player.new_turn()
    assert player.influence == init_influence + player.INITIAL_INFLUENCE_BY_TURN


def test_two_new_turn():
    init_influence = player.influence
    player.new_turn()
    player.new_turn()
    assert player.influence == init_influence + player.INITIAL_INFLUENCE_BY_TURN * 2


def test_new_turn_with_effect_not_influence():
    init_influence = player.influence
    player.new_turn(effects={'Not influence': 4})
    assert player.influence == init_influence + player.INITIAL_INFLUENCE_BY_TURN


def test_new_turn_with_effect_influence():
    init_influence = player.influence
    bonus_influence = 4
    player.new_turn(effects={'Influence': bonus_influence})
    assert player.influence == (init_influence + player.INITIAL_INFLUENCE_BY_TURN + bonus_influence)


def test_use_influence_without_error():
    current_influence = 2
    influence_to_use = 2
    player.influence = current_influence
    player.use_influence(influence_to_use)
    assert player.influence == current_influence - influence_to_use


def test_use_influence_with_error():
    current_influence = 2
    influence_to_use = 3
    player.influence = current_influence
    with pytest.raises(KeyError):
        player.use_influence(influence_to_use)
