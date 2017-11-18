

def ask_improvements_to_make(improvements, player):
    """ ask to the player which improvement he want to do.

    Args:
        improvements (list): list of improvement in which the player can choose
        player (Player): player who want to do this improvement

    Returns:
        (Improvement): return the improvement choice. Return None if the player typed done
    """
    valid_input = False
    improvement = None
    print('Which improvement do you want to do? (type "done" if you do not want to do a new improvement)')
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
            else:
                print('I did not understand you. Please try again.')
    return improvement
