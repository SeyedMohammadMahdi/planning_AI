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




    # for cr in crates:
    #     for ho in hoists:
    #          for loc in locations:
    #             for tr in trucks:
    #                 LoadToTruck = Action(name='LoadToTruck(' + cr + ',' + tr + ',' + ho + ',' + loc + ')',
    #                             positive_preconditions=['Lifts(' + ho + ',' + cr +')',
    #                             'At('+tr +','+loc +')',
    #                             'At('+ho +','+loc +')'],
    #                             negative_preconditions=[],
    #                             add_list=['Vacant('+ho+')',
    #                             'InTruck('+cr+','+tr+')'],
    #                             delete_list=['Lifts(' + ho + ',' + cr +')'])
    #                 actions.append(LoadToTruck)
    # for cr in crates:
    #     for ho in hoists:
    #          for loc in locations:
    #             for tr in trucks:
    #                 UnloadFromTruck = Action(name='UnloadFromTruck(' + cr + ',' + tr + ',' + ho + ',' + loc + ')',
    #                             positive_preconditions=['Vacant(' + ho +')',
    #                             'At('+tr +','+loc +')',
    #                             'At('+ho +','+loc +')',
    #                             'InTruck('+cr+','+tr+')'],
    #                             negative_preconditions=[],
    #                             add_list=['Lifts(' + ho + ',' + cr +')'],
    #                             delete_list=['InTruck('+cr+','+tr+')'
    #                             ,'Vacant(' + ho +')'])
    #                 actions.append(UnloadFromTruck)
    # for truck in trucks:
    #     for loc1 in locations:
    #         for loc2 in locations:
    #             transport = Action(name=f'transport({truck},{loc1},{loc2})',
    #                         positive_preconditions=[f'At({truck},{loc1})'],
    #                         negative_preconditions=[],
    #                         add_list=[f'At({truck, loc2})'],
    #                         delete_list=[f'At({truck},{loc1})'])
    #             actions.append(transport)
    #
    # for cr in crates:
    #     for pa in pallets:
    #          for loc in locations:
    #             for ho in hoists:
    #                 LiftUp = Action(name=f'LiftUP({ho},{cr},{pa},{loc})',
    #                                 positive_preconditions=[f'At({ho},{loc})', f'Available({ho})', f'At({y},{p})'])
    #                 actions.append(LiftUp)
    #
    # for cr in crates:
    #     for pa in pallets:
    #          for loc in locations:
    #             for ho in hoists:
    #                 PutDown = Action(name='PutDown(' + cr + ',' + ho + ',' + pa + ',' + loc + ')',
    #                             positive_preconditions=['Available('+pa+')',
    #                             'At('+ho +','+loc +')',
    #                             'At('+pa +','+loc +')',
    #                             'Lifts(' + ho + ',' + cr +')'],
    #                             negative_preconditions=[],
    #                             add_list=['vacant(' + ho +')',
    #                             'Available('+cr+')',
    #                             'In('+cr+','+pa+')',
    #                             'At('+cr +','+loc +')'],
    #                             delete_list=['Lifts(' + ho + ',' + cr +')',
    #                             'Available('+pa+')'])
    #                 actions.append(PutDown)
    return actions
