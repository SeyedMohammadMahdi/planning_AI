from State import State
from BackwardSearch import backward_search
from ForwardSearch import forward_search
from blockWorld import getActions


def main():
    print("Getting the set of all actions...")
    actions = getActions(3)
    print("Planning...")
    initial_state = State(None, None, positive_literals=["On(a, table)", "On(b, a)", "On(c, table)", "Clear(b)", "Clear(c)"], negative_literals=[])
    goal_state = State(None, None, positive_literals=["On(a, b)", "On(b, c)", 'Clear(a)', 'On(c, table)'], negative_literals=[])
    forward_search(goal_state, initial_state, actions)


if __name__ == "__main__":
    main()
