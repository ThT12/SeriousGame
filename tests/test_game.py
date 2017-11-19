from seriousgame.country import Country
from seriousgame.game import Game
from seriousgame.improvements import Improvement
from seriousgame.io import inputs
from seriousgame.io import outputs
from seriousgame.player import Player
from seriousgame.tree import ProgressionTree

game = Game()


def test_new_turn(mocker):
    effects = {'Influence': 4}
    mocker.patch.object(ProgressionTree, 'get_current_effects', return_value=effects)
    mocker.patch.object(Player, 'new_turn', return_value=None)
    mocker.patch.object(Country, 'new_turn', return_value=None)
    mocker.patch.object(Country, 'display', return_value=None)
    mocker.patch.object(Game, 'let_player_play', return_value=None)
    game.new_turn()
    assert Player.new_turn.call_count == 1
    assert Player.new_turn.call_args[0] == (effects,)
    assert Game.let_player_play.call_count == 1
    assert Country.display.call_count == 1
    assert Country.new_turn.call_count == 1
    assert Country.new_turn.call_args[0] == (effects,)


def test_play_win(mocker):
    mocker.patch.object(Country, 'is_win', side_effect=[False, False, False, True, True])
    mocker.patch.object(Country, 'is_lost', return_value=False)
    mocker.patch.object(Country, 'display', return_value=None)
    mocker.patch.object(Game, 'new_turn', return_value=None)
    mocker.patch.object(outputs, 'display_win', return_value=None)
    game.play()
    assert Game.new_turn.call_count == 3
    assert outputs.display_win.call_count == 1


def test_play_lost(mocker):
    mocker.patch.object(Country, 'is_win', return_value=False)
    mocker.patch.object(Country, 'is_lost', side_effect=[False, False, False, False, True])
    mocker.patch.object(Game, 'new_turn', return_value=None)
    mocker.patch.object(Country, 'display', return_value=None)
    mocker.patch.object(outputs, 'display_lost', return_value=None)
    game.play()
    assert Game.new_turn.call_count == 4
    assert outputs.display_lost.call_count == 1


def test_let_player_play_no_improvement(mocker):
    mocker.patch.object(outputs, 'display_influence_available', return_value=None)
    mocker.patch.object(outputs, 'display_improvements_available', return_value=None)
    mocker.patch.object(ProgressionTree, 'get_improvements_available', return_value=[])
    influence_in = game.player.influence
    improvements_done_in = len(game.tree.get_improvements_available())
    game.let_player_play()
    assert influence_in == game.player.influence
    assert improvements_done_in == len(game.tree.get_improvements_available())


def test_let_player_play_player_done(mocker):
    mocker.patch.object(outputs, 'display_influence_available', return_value=None)
    mocker.patch.object(outputs, 'display_improvements_available', return_value=None)
    mocker.patch.object(ProgressionTree, 'get_improvements_available', return_value=[Improvement()])
    mocker.patch.object(inputs, 'ask_improvements_to_make', return_value=None)
    influence_in = game.player.influence
    improvements_done_in = len(game.tree.get_improvements_available())
    game.let_player_play()
    assert influence_in == game.player.influence
    assert improvements_done_in == len(game.tree.get_improvements_available())


def test_let_player_play_improvement(mocker):
    my_improvement = Improvement(status=False)
    mocker.patch.object(outputs, 'display_influence_available', return_value=None)
    mocker.patch.object(outputs, 'display_improvements_available', return_value=None)
    mocker.patch.object(ProgressionTree, 'get_improvements_available', return_value=[my_improvement])
    mocker.patch.object(inputs, 'ask_improvements_to_make', side_effect=[my_improvement, None])
    mocker.patch.object(my_improvement, 'develop', return_value=None)
    mocker.patch.object(Player, 'use_influence', return_value=None)
    game.let_player_play()
    assert my_improvement.develop.call_count == 1
    assert Player.use_influence.call_count == 1

