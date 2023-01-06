from State import State
from BackwardSearch import backward_search
from ForwardSearch import forward_search
from monkeyAndBanana import getActions


def main():
    print("Getting the set of all actions...")
    actions = getActions()
    print("Planning...")
    initial_state = State(None, None, positive_literals=['At(' + 'MONKEY' + ', ' + 'A' + ')', 'At(' + 'BANANA' + ', ' + 'B' + ')',
                                                         'At(' + 'BOX' + ', ' + 'C' + ')', 'Height(' + 'MONKEY' + ', LOW)',
                                                         'Height(' + 'BOX' + ', LOW)', 'Height(' + 'BANANA' + ', HIGH)',
                                                         'Pushable(' + 'BOX' + ')', 'Climable(' + 'BOX' + ')',
                                                         'Graspable(' + 'BANANA' + ')'],
                          negative_literals=[])
    goal_state = State(None, None, positive_literals=['Have(' + 'MONKEY, ' + 'BANANA)'], negative_literals=[])
    # actions = [Action("Generic", positive_preconditions=["A", "B"], negative_preconditions=[], add_list=["C"], delete_list=[]), \
    # Action("Generic", positive_preconditions=["B", "C"], negative_preconditions=[], add_list=["D"], delete_list=[])]
    forward_search(goal_state, initial_state, actions)


if __name__ == "__main__":
    main()
