

def display_improvement(improvement, influence_available=None, suffix=''):
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
    for improvement in improvements:
        display_improvement(improvement, influence_available, suffix='* ')
