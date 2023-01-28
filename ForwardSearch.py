import copy

from State import State


def forward_search(goal_state, initial_state, actions):
    fringe = [initial_state]
    in_fringe = [initial_state.hash()]
    explored = []

    while fringe:
        # if u want to run heuristic method, uncomment next line:
        # level_list = []
        # if u want to run igonore_preconds heuristic method, uncomment next lines:
        # for index in range(len(fringe)):
        #     level_list.append(igonore_preconds(fringe[index], in_fringe[index], actions, goal_state))
        # if u want to run ignore_del_list heuristic method, uncomment next lines:
        # for index in range(len(fringe)):
        #     level_list.append(ignore_del_list(fringe[index], in_fringe[index], actions, goal_state))

        # if u want to run heuristic method, uncomment next lines:
        # x = list(zip(fringe, level_list))
        # x.sort(key=lambda a: a[1])
        # fringe = [y[0] for y in x]
        current_state = fringe.pop(0)
        in_fringe.pop(0)
        explored.append(current_state.hash())
        successors = get_successors(current_state, actions)
        for successor in successors:
            # print(successor) if ('Height(MONKEY, HIGH)' in successor.positive_literals and
            #                      'At(BOX, B)' in successor.positive_literals) else None
            if goal_test(successor, goal_state):
                print_solution(successor)
                return
            else:
                if successor.hash() not in in_fringe and successor.hash() not in explored:
                    fringe.append(successor)
                    in_fringe.append(successor.hash())


def get_successors(state, actions):
    result = []
    for action in actions:
        if action.is_relevant_forward(state):
            successor = State(state, action, state.positive_literals, state.negative_literals)
            action.progress(successor)
            result.append(successor)
    return result


def get_successors2(state, actions):
    result = []
    for action in actions:
        successor = State(state, action, state.positive_literals, state.negative_literals)
        action.progress(successor)
        result.append(successor)
    return result


def get_successors3(state, actions):
    result = []
    for action in actions:
        if action.is_relevant_forward(state):
            successor = State(state, action, state.positive_literals, state.negative_literals)
            action.progress2(successor)
            result.append(successor)
    return result


def goal_test(state, goal_state):
    for positive_literal in state.positive_literals:
        if positive_literal not in goal_state.positive_literals:
            return False

    for negative_literal in state.negative_literals:
        if negative_literal in goal_state.positive_literals:
            return False

    return True


def print_solution(state):
    actions = []
    while True:
        if state.action == None or state.parent == None:
            break
        # print(state.action.to_string())
        actions.append(state.action.to_string())
        state = state.parent

    actions = actions[::-1]
    # print(actions)
    for action in actions:
        print(action)


def igonore_preconds(fringe, in_fringe, actions, goal_state):
    fringe_copy = [copy.deepcopy(fringe)]
    in_fringe_copy = [copy.deepcopy(in_fringe)]
    explored = []
    level = 0
    while fringe_copy:
        current_state = fringe_copy.pop(0)
        in_fringe_copy.pop(0)
        level += 1
        explored.append(current_state.hash())
        successors = get_successors2(current_state, actions)
        for successor in successors:
            if goal_test(successor, goal_state):
                return level
            else:
                if successor.hash() not in in_fringe_copy and successor.hash() not in explored:
                    fringe_copy.append(successor)
                    in_fringe_copy.append(successor.hash())
    return 1e9


def ignore_del_list(fringe, in_fringe, actions, goal_state):
    fringe_copy = [copy.deepcopy(fringe)]
    in_fringe_copy = [copy.deepcopy(in_fringe)]
    explored = []
    level = 0
    while fringe_copy:
        current_state = fringe_copy.pop(0)
        in_fringe_copy.pop(0)
        level += 1
        explored.append(current_state.hash())
        successors = get_successors3(current_state, actions)
        for successor in successors:
            if goal_test(successor, goal_state):
                return level
            else:
                if successor.hash() not in in_fringe_copy and successor.hash() not in explored:
                    fringe_copy.append(successor)
                    in_fringe_copy.append(successor.hash())
    return 1e9
