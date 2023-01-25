from State import State
from BackwardSearch import backward_search
from ForwardSearch import forward_search
from blockWorld import getActions


def main():
    print("Getting the set of all actions...")
    actions = getActions(2)
    print("Planning...")
    initial_state = State(None, None, positive_literals=["On(a, table)", "On(b, table)", "On(c, a)",
                                                         "Block(a)", "Block(b)", "Block(c)", "Clear(b)",
                                                         "Clear(c)", "Clear(table)"], negative_literals=[])
    goal_state = State(None, None, positive_literals=["On(a, b)", "On(b, c)"], negative_literals=[])
    # actions = [Action("Generic", positive_preconditions=["A", "B"], negative_preconditions=[], add_list=["C"], delete_list=[]), \
    # Action("Generic", positive_preconditions=["B", "C"], negative_preconditions=[], add_list=["D"], delete_list=[])]
    backward_search(goal_state, initial_state, actions)


if __name__ == "__main__":
    main()
