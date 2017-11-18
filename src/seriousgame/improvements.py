

class Improvement(object):

    def __init__(self, title='My improvement', influence_cost=1, effects=None, requirements=None, status=False,
                 description='Detail of this improvement'):
        """ Constructor

        Args:
            title (str): improvement title
            influence_cost (int): influence cost to make this improvement
            effects (dict): effect and intensity of the improvement
            requirements (:type: tuple of Improvement): tuple of Improvements that have to been done to have this one
                available
            status (bool): True if this improvement have been done
            description (str): Detail of this improvement
        """
        if not effects:
            effects = {}
        if not requirements:
            requirements = ()
        self.title = title
        self.influence_cost = influence_cost
        self.effects = effects
        self.requirements = requirements
        self.status = status
        self.description = description

    def __eq__(self, other):
        """ Compare if two Improvement are equal to each other.

        Args:
            other (object): object to be compared with. Return an error if other is not a str or a Improvement

        Returns:
            (bool): return True if other is an Improvement and other.title = self.title or if other is a str and
                other = self.title
        """
        if isinstance(other, str):
            return other == self.title
        if isinstance(other, Improvement):
            return other.title == self.title
        raise KeyError('An Improvement can only be compared to a str or an other Improvement')


class Improvements(object):

    def __init__(self, *args):
        """ Constructor. Verifies that all requirements are in the Improvements

        Args:
            *args (Improvement): all improvements in the same scale
        """
        self.improvements = args
        for improvement in self.improvements:
            for requirement in improvement.requirements:
                if requirement not in self.improvements:
                    raise KeyError('All requirements to match must be in the Improvements')

    def are_improvement_requirements_reached(self, improvement):
        """ test if the improvement have all his requirement reached. Return an error if the improvement is not in self

        Args:
            improvement (Improvement): improvement on which the test will be made

        Returns:
            (bool): True if all requirements are reached
        """
        if improvement not in self.improvements:
            raise KeyError('You cannot test verify a requirement which is not include in the requirements list')
        for improvement in improvement.requirements:
            if not improvement.status:
                return False
        return True

    def get_improvements_done(self):
        """
        Returns:
            (list): return a list of improvement that are already done
        """
        return [improvement for improvement in self.improvements if improvement.status]

    def get_improvements_available(self):
        """
        Returns:
            (list): return a list of improvement that are available to be done
        """
        return [improvement for improvement in self.improvements if
                not improvement.status and self.are_improvement_requirements_reached(improvement)]

    def get_current_effects(self):
        """
        Returns:
            (dict): return all effects currently applied. If two improvement have the same type of effects then their
                values are summed
        """
        effects = {}
        for improvement in self.get_improvements_done():
            for key in improvement.effects.keys():
                if key in effects:
                    effects[key] += improvement.effects[key]
                else:
                    effects.update({key: improvement.effects[key]})
        return effects
