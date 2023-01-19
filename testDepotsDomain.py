from State import State
from BackwardSearch import backward_search
from ForwardSearch import forward_search
from depotsDomain import getActions


def main():
    print("Getting the set of all actions...")
    actions = getActions()
    print("Planning...")
    initial_state = State(None, None, positive_literals=['At('+'t1' +','+'C' +')',
                                                         'At('+'t2' +','+'B' +')',
                                                         'Available('+'c1'+')',
                                                         'In('+'c1'+','+'p1'+')',
                                                         'At('+'c1'+','+'A'+')',
                                                         'At('+'p1'+','+'A'+')',
                                                         'Available('+'c2'+')',
                                                         'In('+'c2'+','+'p2'+')',
                                                         'At('+'c2'+','+'A'+')',
                                                         'At('+'p2'+','+'A'+')',
                                                         'Available('+'c3'+')',
                                                         'In('+'c3'+','+'p3'+')',
                                                         'At('+'c3'+','+'B'+')',
                                                         'At('+'p3'+','+'B'+')',
                                                         'At('+'p4'+','+'C'+')',
                                                         'Available('+'p4'+')',
                                                         'Vacant('+'h1'+')',
                                                         'Vacant('+'h2'+')',
                                                         'Vacant('+'h3'+')',
                                                         'At('+'h1'+','+'A'+')',
                                                         'At('+'h2'+','+'B'+')',
                                                         'At('+'h3'+','+'C'+')'],
                          negative_literals=[])
    goal_state = State(None, None, positive_literals=['In('+'c1'+','+'p2'+')',
                                                      'In('+'c2'+','+'p1'+')',
                                                      'In('+'c3'+','+'p4'+')'], negative_literals=[])
    # actions = [Action("Generic", positive_preconditions=["A", "B"], negative_preconditions=[], add_list=["C"], delete_list=[]), \
    # Action("Generic", positive_preconditions=["B", "C"], negative_preconditions=[], add_list=["D"], delete_list=[])]
    backward_search(goal_state, initial_state, actions)


if __name__ == "__main__":
    main()
