

def display_improvement(improvement, influence_available=None, is_number_displayed=True):
    """ display in a python console the improvement. Influence_cost display in red if influence_available <
        influence_cost, in green if influence_available >= influence_cost and without color if influence_available is
        None

    Args:
        improvement (Improvement): improvement to display
        influence_available (int): influence available to compare with to set the influence_cost color
        is_number_displayed (bool): indicate if the improvements number are displayed or not
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
    if is_number_displayed:
        start = ''.join([str(improvement.number), ') '])
    else:
        start = '- '
    string_to_print = ''.join([start, improvement.title, ': Cost=', color,
                               str(improvement.influence_cost), end_color, ' ; Effects=',
                               effects_to_str(improvement.effects)])
    print(string_to_print)


def display_improvement_details(improvement):
    """ Display in detail an improvement

    Args:
        improvement (Improvement): improvement to display
    """
    print(''.join([improvement.title, ':']))
    print('-'*(len(improvement.title)+1))
    print(improvement.description)
    print(' '.join(['Influence cost:', str(improvement.influence_cost), 'influence(s)']))
    print(' '.join(['Effects:', effects_to_str(improvement.effects)]))


def display_improvements(improvements, influence_available=None, is_number_displayed=True):
    """ Calls display_improvement for each improvement in improvements

    Args:
        improvements (list): list of improvement
        influence_available (int): influence available to compare with to set the influence_cost color
        is_number_displayed (bool): indicate if the improvements number are displayed or not
    """
    if len(improvements) == 0:
        print('No improvement available.')
    else:
        for improvement in improvements:
            display_improvement(improvement, influence_available, is_number_displayed)


def display_improvements_available(improvements, influence_available=None):
    """ Display all improvements available for improvements

    Args:
        improvements (Improvements): improvements to display
        influence_available (int): influence available to compare with to set the influence_cost color
    """
    print(' '.join(['Improvements available in', improvements.name, 'area:']))
    display_improvements(improvements.get_improvements_available(), influence_available, is_number_displayed=True)


def display_improvements_done(improvements):
    """ Display all improvements available for improvements

    Args:
        improvements (Improvements): improvements to display
    """
    print(' '.join(['Improvements already done in', improvements.name, 'area:']))
    display_improvements(improvements.get_improvements_done(), is_number_displayed=False)


def display_tree_available(tree, influence_available=None):
    """ Display all improvements available in the tree

    Args:
        tree (Tree): tree to display
        influence_available (int): influence available to compare with to set the influence_cost color
    """
    for improvements in tree.tree:
        display_improvements_available(improvements, influence_available)


def display_tree_done(tree):
    """ Display all improvements done in the tree

    Args:
        tree (Tree): tree to display
    """
    for improvements in tree.tree:
        display_improvements_done(improvements)


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
        effects (Effects): list of effect

    Returns:
        (str): all effect in a string
    """
    return ' - '.join([str(effect) for effect in effects.effects])


def display_context_part_one():
    """ Display the game introduction part one """
    print('Welcome in my World simulator !')
    print('You are here to try to save a simulation of your country.')


def display_context_part_two():
    """ Display the game introduction part two """
    print('Your country is at a turning point. In one direction, the ecology will collapse, the economy will crash and '
          'the social revolution will start. \nIn the other direction, everything will move in a better direction to '
          'construct a better world. \nYou will have to influence wisely the people in your country to choose the right'
          ' direction.')
    input('Press enter to continue ...\n')


def display_event(event):
    """ Display an event that occurs"""
    print(' '.join(['An unexpected event has happen:', event.name]))
    print(event.description)
    print(' '.join(['This event will impact your country:', effects_to_str(event.effects)]))
