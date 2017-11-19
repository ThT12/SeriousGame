

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
    str_effects = str(improvement.effects)
    string_to_print = ''.join([suffix, improvement.title, ': Cost=', color, str(improvement.influence_cost), end_color,
                               ' ; Description=', improvement.description, ' ; Effects=', str_effects])
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


def display_country_header(name):
    """ Display the country name

    Args:
        name (str): Country name
    """
    print(''.join(['The current situation in ', name, ' is the following:']))


def display_country_level(name, level):
    """ Display a country level with a progression bar

    Args:
        name (str): name of the level
        level (float): level of the country between 0 and 1
    """
    level = int(level * 100)
    str_level = ''.join(['|' * level, ' ' * (100 - level)])
    print(''.join([name, ' level=[', str_level, ']', ' ', str(level), '%']))
