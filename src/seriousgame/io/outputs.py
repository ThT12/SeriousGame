

def display_improvement(improvement, influence_available=None, suffix=''):
    """ display in a python console the improvement. Influence_cost display in red if influence_available <
        influence_cost, in green if influence_available >= influence_cost and without color if influence_available is
        None

    Args:
        improvement (Improvement): improvement to display
        influence_available (int): influence available to compare with to set the influence_cost color
        suffix (str): text to add before improvement is displayed
    """
    if influence_available is not None:
        if influence_available < improvement.influence_cost:
            color = '\033[91m'
        else:
            color = '\033[92m'
        end_color = '\033[0m'
    else:
        color = ''
        end_color = ''
    string_to_print = ''.join([suffix, improvement.title, ': Cost=', color, str(improvement.influence_cost), end_color,
                               ' ; Description=', improvement.description])
    print(string_to_print)


def display_improvements(improvements, influence_available=None):
    """ Calls display_improvement for each improvement in improvements

    Args:
        improvements (list): list of improvement
        influence_available (int): influence available to compare with to set the influence_cost color
    """
    if len(improvements) == 0:
        print('No improvement available.')
    else:
        for improvement in improvements:
            display_improvement(improvement, influence_available, suffix='* ')


def display_influence_available(player):
    """ display the influence available for a player

    Args:
        player (Player): influence of this player is displayed
    """
    print(''.join(['You have ', str(player.influence), ' influence point(s) available']))
