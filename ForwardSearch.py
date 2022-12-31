from State import State


def forward_search(goal_state, initial_state, actions):
    fringe = [initial_state]


def get_successors(state, actions):
    result = []
    for action in actions:
        if action.is_relevant(state):
            successor = State(state, action, state.positive_literals, state.negative_literals)
            action.regress(successor)
            result.append(successor)
    return result


def goal_test(state, initial_state):
    # write your code here
    return


def print_solution(state):
    while True:
        if state.action == None or state.parent == None:
            break
        print(state.action.to_string())
        state = state.parent
