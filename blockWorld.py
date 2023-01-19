from Action import Action


def getActions(n):

    actions = []
    blocks = []
    holding = ''
    for b in range(n):
        blocks.append('block' + str((b+1)))

    for b in blocks:
        for b2 in blocks:
            if b != b2:
                print(b,b2)
                PickUpFromStack = Action(name='PickUpFromStack(' + b + ','+b2+')',
                           positive_preconditions=['TopMostBlock('+b+')',
                           'ON('+b+','+b2+')'],
                           negative_preconditions=['Hand(Full)'],
                           add_list=['Hand(Full)',
                           'Hold('+b+')',
                           'TopMostBlock('+b2+')'],
                           delete_list=['On('+b+','+b2+')',
                           'TopMostBlock('+b+')'])
                actions.append(PickUpFromStack)

    for b in blocks:
            PickUpFromTable = Action(name='PickUpFromTable(' + b + ')',
                           positive_preconditions=['TopMostBlock('+b+')',
                           'OnTable('+b+')'],
                           negative_preconditions=['Hand(Full)'],
                           add_list=['Hand(Full)',
                           'Hold('+b+')'],
                           delete_list=['OnTable('+b+')',
                           'TopMostBlock('+b+')'])
            actions.append(PickUpFromTable)
    

    
    for b in blocks:
        for b2 in blocks:
            if b != b2:
                PutDownOnStack = Action(name='PutDownOnStack(' + b + ','+b2+')',
                           positive_preconditions=['TopMostBlock('+b2+')',
                           'Hand(Full)',
                           'Hold('+b+')'],
                           negative_preconditions=[],
                           add_list=['TopMostBlock('+b+')',
                           'On('+b+','+b2+')'],
                           delete_list=['TopMostBlock('+b2+')',
                           'Hand(Full)',
                           'Hold('+b+')'])
                actions.append(PutDownOnStack)

    for b in blocks:
            PutDownOnTable = Action(name='PutDownOnTable(' + b + ')',
                           positive_preconditions=['Hand(Full)',
                           'Hold('+b+')'],
                           negative_preconditions=[],
                           add_list=['OnTable('+b+')',
                           'TopMostBlock('+b+')'],
                           delete_list=['Hand(Full)',
                           'Hold('+b+')'])
            actions.append(PutDownOnTable)
    
    return actions
