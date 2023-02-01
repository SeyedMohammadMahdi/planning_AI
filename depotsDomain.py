from Action import Action


def getActions():

    actions = []
    places = ['A','B','C']
    crates = ['c1','c2','c3']
    trucks = ['t1','t2']
    hoists = ['h1','h2','h3']
    surfaces = ['s1','s2','s3','s4']

    for truck in trucks:
        for p1 in places:
            for p2 in places:
                if p1 != p2:
                    drive = Action(name=f'Drive({truck}, {p1}, {p2})',
                                   positive_preconditions=[f'At({truck}, {p1})'],
                                   negative_preconditions=[],
                                   add_list=[f'At({truck}, {p2})'],
                                   delete_list=[f'At({truck}, {p1})'])
                    actions.append(drive)


    for hoist in hoists:
        for crate in crates:
            for surface in surfaces:
                for place in places:
                    lift = Action(name=f'Lift({hoist}, {crate}, {surface}, {place})',
                                  positive_preconditions=[f'At({hoist}, {place})', f'Available({hoist})',
                                                          f'At({crate}, {place})', f'On({crate}, {surface})',
                                                          f'Clear({crate})'],
                                  negative_preconditions=[],
                                  add_list=[f'Lifting({hoist}, {crate})', f'Clear({surface})'],
                                  delete_list=[f'At({crate}, {place}', f'Clear({crate})',
                                               f'Available({hoist})', f'On({crate}, {surface})'])
                    actions.append(lift)

                    drop = Action(name=f'Drop({hoist}, {crate}, {surface}, {place})',
                                  positive_preconditions=[f'At({hoist}, {place}', f'Clear({crate})',
                                                          f'Lifting({hoist}, {crate})'],
                                  negative_preconditions=[],
                                  add_list=[f'Available({hoist})', f'At({crate}, {place})',
                                            f'Clear({crate})', f'On({crate}, {surface})'],
                                  delete_list=[f'Lifting({hoist}, {crate})', f'Clear({surface})'])
                    actions.append(drop)



    return actions
