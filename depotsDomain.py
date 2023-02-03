from Action import Action


def getActions():

    actions = []
    locations = ['A','B','C']
    crates = ['c1','c2','c3']
    trucks = ['t1','t2']
    hoists = ['h1','h2','h3']
    pallets = ['p']

    for truck in trucks:
        for l1 in locations:
            for l2 in locations:
                if l1 != l2:
                    move = Action(name=f'Move({truck}, {l1}, {l2})',
                    positive_preconditions=[f'At({truck}, {l1})'],
                    negative_preconditions=[],
                    add_list=[f'At({truck}, {l2})'],
                    delete_list=[f'At({truck}, {l1})'])
                    actions.append(move)
    
    for hoist in hoists:
        for crate in crates:
            for pallet in pallets:
                for location in locations:
                    lift =Action(name=f'Lifting({hoist}, {crate}, {pallet}, {location})',
                    positive_preconditions=[f'At({hoist}, {location})', f'At({crate}, {location})', f'On({crate}, {pallet})', f'Available({hoist})'],
                    negative_preconditions=[],
                    add_list=[f'Lifting({hoist}, {crate})'],
                    delete_list=[f'On({crate}, {pallet})', f'Available({hoist})', f'At({crate}, {location})'])
                
                    actions.append(lift)

                    drop = Action(name=f'Drop({hoist}, {crate}, {pallet}, {location})',
                    positive_preconditions=[f'Lifting({hoist}, {crate})', f'At({hoist}, {location})'],
                    negative_preconditions=[],
                    add_list=[f'On({crate}, {pallet})', f'Available({hoist})', f'At({crate}, {location})'],
                    delete_list=[f'Lifting({hoist}, {crate})'])

                    actions.append(drop)
    

    for truck in trucks:
        for hoist in hoists:
            for crate in crates:
                for location in locations:
                    load = Action(name=f'Load({hoist}, {crate}, {truck}, {location})',
                    positive_preconditions=[f'At({hoist}, {location})', f'At({truck}, {location})', f'Lifting({hoist}, {crate})'],
                    negative_preconditions=[],
                    add_list=[f'In({crate}, {truck})', f'Available({hoist})'],
                    delete_list=[f'Lifting({hoist}, {crate})'])

                    actions.append(load)

                    unload = Action(name=f'Unload({hoist}, {crate}, {truck}, {location})',
                    positive_preconditions=[f'In({crate}, {truck})', f'Available({hoist})', f'At({truck}, {location})', f'At({hoist}, {location})'],
                    negative_preconditions=[],
                    add_list=[f'Lifting({hoist}, {crate})'],
                    delete_list=[f'In({crate}, {truck})', f'Available({hoist})'])
                    actions.append(unload)
    

    return actions
