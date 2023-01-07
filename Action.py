import State


class Action:
    def __init__(self, name, positive_preconditions, negative_preconditions, add_list, delete_list):
        self.name = name
        self.positive_preconditions = positive_preconditions
        self.negative_preconditions = negative_preconditions
        self.add_list = add_list
        self.delete_list = delete_list

    def regress(self, state):
        positive_literals = list(
            set(set(self.positive_preconditions).union(set(set(state.positive_literals) - set(self.add_list)))))
        negative_literals = list(
            set(set(self.negative_preconditions).union(set(set(state.negative_literals) - set(self.delete_list)))))
        state.positive_literals = positive_literals
        state.negative_literals = negative_literals

    def progress(self, state):
        positive_literals = list(set(state.positive_literals).union(set(self.add_list)))
        for del_element in self.delete_list:
            if del_element in positive_literals:
                positive_literals.remove(del_element)
        negative_literals = list(set(state.negative_literals).union(set(self.delete_list)))
        for add_element in self.add_list:
            if add_element in negative_literals:
                negative_literals.remove(add_element)
        state.positive_literals = positive_literals
        state.negative_literals = []

    def is_relevant_backward(self, state):
        if not self.is_unified(state):
            return False

        if self.is_conflicting(state):
            return False

        return True

    def is_relevant_forward(self, state):
        if set(self.positive_preconditions) <= set(state.positive_literals) and \
                set(self.negative_preconditions) <= set(state.negative_literals):
            return True
        return False

    def is_unified(self, state):
        status = 0
        for add_literal in self.add_list:
            if add_literal in state.positive_literals:
                status += 1
        if status != 0:
            return True

        status = 0
        for del_literal in self.delete_list:
            if del_literal in state.negative_literals:
                status += 1
        if status == 0:
            return False
        else:
            return True

    def is_conflicting(self, state):
        for add_literal in self.add_list:
            if add_literal in state.negative_literals:
                return True
        for del_literal in self.delete_list:
            if del_literal in state.positive_literals:
                return True
        return False

    def to_string(self):
        return f'action, name: {self.name}, positive preconditions: {self.positive_preconditions}, negative preconditions: {self.negative_preconditions}, add list: {self.add_list}, delete list: {self.delete_list}'
