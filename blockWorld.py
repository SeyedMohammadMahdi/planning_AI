from Action import Action


def getActions(n):

    # initial_state = State(None, None, positive_literals=['ON(' + 'block1' + ', ' + 'block2' + ')',
    #                                                      'ON(' + 'block4' + ', ' + 'block1' + ')',
    #                                                      'ON(' + 'block3' + ', ' + 'block4' + ')',
    #                                                      'TopMostBlock(' + 'block3' + ')',
    #                                                      'OnTable('+ 'block2' +')'],
    #                       negative_literals=['Hand(full)'])



    actions = []
    blocks = []
    holding = ''
    for b in range(n):
        blocks.append('block' + (b+1))

    for b in blocks:
        for b2 in blocks:
            if b != b2:
                PickUpFromStack = Action(name='PickUpFromStack(' + b + ','+b2+')',
                           positive_preconditions=['TopMostBlock('+b+')',
                           'ON('+b+','+b2+')'],
                           negative_preconditions=['Hand(full)'],
                           add_list=['Hand(full)',
                           'Hold('+b+')',
                           'TopMostBlock('+b+')'],
                           delete_list=['On('+b+','+b2+')',
                           'TopMostBlock('+b2+')'])
    actions.append(PickUpFromStack)

    for b in blocks:
            PickUpFromTable = Action(name='PickUpFromTable(' + b + ')',
                           positive_preconditions=['TopMostBlock('+b+')',
                           'OnTable('+b+')'],
                           negative_preconditions=['Hand(full)'],
                           add_list=['Hand(full)',
                           'Hold('+b+')'],
                           delete_list=['OnTable('+b+')',
                           'TopMostBlock('+b+')'])
    actions.append(PickUpFromTable)
    
    for b in blocks:
        for b2 in blocks:
            if b != b2:
                PutDownUnStack = Action(name='PutDownOnStack(' + b + ','+b2+')',
                           positive_preconditions=['TopMostBlock('+b2+')',
                           'Hand(Full)',
                           'Hold('+b+')'],
                           negative_preconditions=[],
                           add_list=['TopMostBlock('+b+')',
                           'On('+b+','+b2+')'],
                           delete_list=['TopMostBlock('+b2+')',
                           'Hand(Full)',
                           'Hold('+b+')'])
    actions.append(PutDownUnStack)

    for b in blocks:
            PutDownOnTable = Action(name='PutDownOnTable(' + b + ')',
                           positive_preconditions=['Hand(Full)',
                           'Hold('+b+')'],
                           negative_preconditions=[],
                           add_list=['OnTable('+b+')',
                           'TopMostBlock('+b+')'],
                           delete_list=['Hand(full)',
                           'Hold('+b+')'])
    actions.append(PutDownOnTable)
    
    return actions
