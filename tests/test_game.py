from seriousgame.game import Game
from seriousgame.player import Player
from seriousgame.country import Country
from seriousgame.io import outputs


game = Game()


def test_new_turn(mocker):
    mocker.spy(Player, 'new_turn')
    mocker.spy(Country, 'new_turn')
    mocker.patch.object(outputs, 'display_influence_available', return_value=None)
    mocker.patch.object(outputs, 'display_improvements', return_value=None)
    game.new_turn()
    assert Player.new_turn.call_count == 1
    assert Country.new_turn.call_count == 1


def test_play_win(mocker):
    mocker.patch.object(Country, 'is_win', side_effect=[False, False, False, True])
    mocker.patch.object(Country, 'is_lost', return_value=False)
    mocker.patch.object(Game, 'new_turn', return_value=None)
    mocker.spy(Game, 'new_turn')
    game.play()
    assert Game.new_turn.call_count == 3


def test_play_lost(mocker):
    mocker.patch.object(Country, 'is_win', return_value=False)
    mocker.patch.object(Country, 'is_lost', side_effect=[False, False, False, False, True])
    mocker.patch.object(Game, 'new_turn', return_value=None)
    mocker.spy(Game, 'new_turn')
    game.play()
    assert Game.new_turn.call_count == 4

