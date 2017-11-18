

def ask_improvements_to_make(improvements):
    """ ask to the player which improvement he want to do.

    Args:
        improvements: list of improvement in which the player can choose

    Returns:
        (Improvement): return the improvement choice. Return None if the player typed done
    """
    valid_input = False
    out = None
    print('Which improvement do you want to do? (type "done" if you do not want to do a new improvement)')
    while not valid_input:
        user_choice = input()
        if user_choice == 'done':
            valid_input = True
        else:
            if user_choice in improvements:
                out = improvements[improvements.index(user_choice)]
                valid_input = True
            else:
                print('I did not understand you. Please try again.')
    return out
