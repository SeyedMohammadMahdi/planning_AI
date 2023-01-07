from Action import Action


def getActions():
    actions = []
    locations = ['A', 'B', 'C']
    object = 'BOX'
    height = ['HIGH', 'LOW']

    for loc1 in locations:
        for loc2 in locations:
            if loc1 != loc2:
                Go = Action(name='GO(' + 'MONKEY' + ', ' + loc1 + ', ' + loc2 + ')',
                            positive_preconditions=['At(' + 'MONKEY' + ', ' + loc1 + ')',
                                                    'Height(' + 'MONKEY' + ', LOW)'],
                            negative_preconditions=[], add_list=['At(' + 'MONKEY' + ', ' + loc2 + ')'],
                            delete_list=['At(' + 'MONKEY' + ', ' + loc1 + ')'])
                actions.append(Go)

                Push = Action(name='Push(' + object + ', ' + loc1 + ', ' + loc2 + ')',
                              positive_preconditions=['At(' + 'MONKEY' + ', ' + loc1 + ')',
                                                      'Height(' + 'MONKEY' + ', LOW)',
                                                      'At(' + object + ', ' + loc1 + ')',
                                                      'Pushable(' + object + ')',
                                                      'Height(' + object + ', LOW)'],
                              negative_preconditions=[],
                              add_list=['At(' + object + ', ' + loc2 + ')', 'At(' + 'MONKEY' + ', ' + loc2 + ')'],
                              delete_list=['At(' + object + ', ' + loc1 + ')', 'At(' + 'MONKEY' + ', ' + loc1 + ')'])
                actions.append(Push)
    for loc in locations:
        Climb = Action(name='ClimbUp(' + loc + ', ' + object + ')',
                       positive_preconditions=['At(' + 'MONKEY' + ', ' + loc + ')', 'Height(' + 'MONKEY' + ', LOW)',
                                               'At(' + object + ', ' + loc + ')',
                                               'Climable(' + object + ')', 'Height(' + object + ', LOW)'],
                       negative_preconditions=[],
                       add_list=['On(' + 'MONKEY' + ', ' + object + ')', 'Height(' + 'MONKEY' + ', HIGH)'],
                       delete_list=['Height(' + 'MONKEY' + ', LOW)'])
        actions.append(Climb)

        for h in height:
            Grasp = Action(name='Grasp(' + loc + ', ' + 'BANANA, ' + h + ')',
                           positive_preconditions=['At(' + 'MONKEY' + ', ' + loc + ')',
                                                   'Height(' + 'MONKEY, ' + h + ')',
                                                   'At(' + 'BANANA, ' + loc + ')',
                                                   'Graspable(' + 'BANANA' + ')', 'Height(' + 'BANANA, ' + h + ')'],
                           negative_preconditions=[], add_list=['Have(' + 'MONKEY, ' + 'BANANA)'],
                           delete_list=['At(' + 'BANANA, ' + loc + ')', 'Height(' + 'BANANA, ' + h + ')'])
            actions.append(Grasp)
    return actions
