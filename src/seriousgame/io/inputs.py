from seriousgame.io import outputs


def ask_improvements_to_make(improvements, player, tree):
    """ ask to the player which improvement he want to do.

    Args:
        improvements (list): list of improvement in which the player can choose
        player (Player): player who want to do this improvement
        tree (ProgressionTree): progress tree

    Returns:
        (Improvement): return the improvement choice. Return None if the player typed done
    """
    valid_input = False
    improvement = None
    print('Which improvement do you want to do?')
    outputs.display_help()
    while not valid_input:
        user_choice = input()
        if user_choice == 'done':
            valid_input = True
        else:
            if user_choice in improvements:
                improvement = improvements[improvements.index(user_choice)]
                if improvement.influence_cost <= player.influence:
                    valid_input = True
                else:
                    improvement = None
                    print('You do not have enough influence to make this improvement. Try again.')
            elif len(user_choice) > 7 and user_choice[0:6] == 'Detail':
                user_choice = user_choice[7:]
                if user_choice in improvements:
                    outputs.display_improvement_details(improvements[improvements.index(user_choice)])
                else:
                    print('I did not understand you. Please try again.')
            elif user_choice == 'Improvement done':
                outputs.display_tree_done(tree)
            elif user_choice == 'help':
                outputs.display_help()
            else:
                print('I did not understand you. Please try again.')
    return improvement


def ask_player_name_and_country():
    """ Ask the player name and country name """
    player_name = input('First, can you give me your name please?\n')
    print(' '.join(['Hello', player_name, 'and thanks!']))
    country_name = input('Now can you give me your country name please?\n')
    print(' '.join(['Thanks. So you are living in', country_name, '. Good to know!']))
    return [player_name, country_name]
