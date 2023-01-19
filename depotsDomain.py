from Action import Action


def getActions():

    actions = []
    locations = ['A','B','C']
    crates = ['c1','c2','c3']
    trucks = ['t1','t2']
    hoists = ['h1','h2','h3']
    pallets = ['p1','p2','p3','p4']


    for cr in crates:
        for ho in hoists:
             for loc in locations:
                for tr in trucks:
                    LoadToTruck = Action(name='LoadToTruck(' + cr + ', ' + tr + ', ' + ho + ', ' + loc + ')',
                                positive_preconditions=['Lifts(' + ho + ',' + cr +')',
                                'At('+tr +','+loc +')',
                                'At('+ho +','+loc +')'],
                                negative_preconditions=[],
                                add_list=['Vacant('+ho+')',
                                'InTruck('+cr+','+tr+')'],
                                delete_list=['Lifts(' + ho + ',' + cr +')'])
                    actions.append(LoadToTruck)
    for cr in crates:
        for ho in hoists:
             for loc in locations:
                for tr in trucks:
                    UnloadFromTruck = Action(name='UnloadFromTruck(' + cr + ', ' + tr + ', ' + ho + ', ' + loc + ')',
                                positive_preconditions=['Vacant(' + ho +')',
                                'At('+tr +','+loc +')',
                                'At('+ho +','+loc +')',
                                'InTruck('+cr+','+tr+')'],
                                negative_preconditions=[],
                                add_list=['Lifts(' + ho + ',' + cr +')'],
                                delete_list=['InTruck('+cr+','+tr+')'
                                ,'Vacant(' + ho +')'])
                    actions.append(UnloadFromTruck)
    for trucks in trucks:
        for loc1 in locations:
            for loc2 in locations:
                transport = Action(name='transport(' + tr + ', ' + loc1 + ', ' + loc2 + ')',
                            positive_preconditions=['At('+tr +','+loc1 +')'],
                            negative_preconditions=[],
                            add_list=['At('+tr +','+loc2 +')'],
                            delete_list=['At('+tr +','+loc1 +')'])
                actions.append(transport)
    for cr in crates:
        for pa in pallets:
             for loc in locations:
                for ho in hoists:
                    LiftUp = Action(name='LiftUP(' + cr + ', ' + ho + ', ' + pa + ', ' + loc + ')',
                                positive_preconditions=['vacant(' + ho +')',
                                'Available('+cr+')',
                                'In('+cr+','+pa+')',
                                'At('+cr +','+loc +')',
                                'At('+ho +','+loc +')'],
                                negative_preconditions=[],
                                add_list=[ 'Available('+pa+')',
                                'Lifts(' + ho + ',' + cr +')'],
                                delete_list=['In('+cr+','+pa+')',
                                'vacant(' + ho +')',
                                'Available('+cr+')',
                                'At('+cr +','+loc +')'])
                    actions.append(LiftUp)
    for cr in crates:
        for pa in pallets:
             for loc in locations:
                for ho in hoists:
                    PutDown = Action(name='PutDown(' + cr + ', ' + ho + ', ' + pa + ', ' + loc + ')',
                                positive_preconditions=['Available('+pa+')',
                                'At('+ho +','+loc +')',
                                'At('+pa +','+loc +')',
                                'Lifts(' + ho + ',' + cr +')'],
                                negative_preconditions=[],
                                add_list=['vacant(' + ho +')',
                                'Available('+cr+')',
                                'In('+cr+','+pa+')',
                                'At('+cr +','+loc +')'],
                                delete_list=['Lifts(' + ho + ',' + cr +')',
                                'Available('+pa+')'])
                    actions.append(PutDown)
    return actions
