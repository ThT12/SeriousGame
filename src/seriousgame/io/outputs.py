

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
                               ' ; Description=', improvement.description, ' ; Effects=',
                               effects_to_str(improvement.effects)])
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


def display_improvements_available(improvements, influence_available=None):
    """ Display all improvements available for improvements

    Args:
        improvements (Improvements): improvements to display
        influence_available (int): influence available to compare with to set the influence_cost color
    """
    print(' '.join(['Improvements available in', improvements.name, 'area:']))
    display_improvements(improvements.get_improvements_available(), influence_available)


def display_tree_available(tree, influence_available=None):
    """ Display all improvements available in the tree

    Args:
        tree (Tree): tree to display
        influence_available (int): influence available to compare with to set the influence_cost color
    """
    for improvements in tree.tree:
        display_improvements_available(improvements, influence_available)


def display_influence_available(player):
    """ display the influence available for a player

    Args:
        player (Player): influence of this player is displayed
    """
    influence_to_display = max(player.influence, 0)
    print(''.join(['You have ', str(influence_to_display), ' influence point(s) available']))


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


def display_win():
    """ Display win message """
    print('Congratulation, you win !')


def display_lost():
    """ Display loose message """
    print('Sorry, you loose ! Try again !')


def effects_to_str(effects):
    """ construct a string with effects

    Args:
        effects (list): list of effect

    Returns:
        (str): all effect in a string
    """
    return ' - '.join([str(effect) for effect in effects])
