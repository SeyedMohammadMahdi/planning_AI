from State import State
from BackwardSearch import backward_search
from ForwardSearch import forward_search
from depotsDomain import getActions


def main():
    print("Getting the set of all actions...")
    actions = getActions()
    print("Planning...")
    initial_state = State(None, None, positive_literals=['At(t1, A)', 'At(t2, A)', 'At(h1, A)', 'At(h2, B)', 'At(h3, C)',
    'At(c1, A)', 'At(c2, A)', 'At(c3, A)', 'On(c1, p)', 'On(c2, p)', 'On(c3, p)', 'Available(h1)', 'Available(h2)', 'Available(h3)']
    , negative_literals=[])
    goal_state = State(None, None, positive_literals=['At(c1, B)', 'In(c2, t1)'], negative_literals=[])
    backward_search(goal_state, initial_state, actions)


if __name__ == "__main__":
    main()
