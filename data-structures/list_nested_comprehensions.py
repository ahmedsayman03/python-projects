'''
Working with nested comprehensions.
'''

def m_t():
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        ]

    trans = [ [row[i] for row in matrix] for i in range(4) ]
    print(trans)

m_t()



def matrix_transpose():
    '''
    Takes a matrix, transposes it.
    e.g.

    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        ]

    trans = [
        [1, 5, 9],
        [2, 6, 10],
        [3, 7,11],
        [4, 8, 12]
        ]
    '''
    
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        ]

    trans = []
    for i in range(4):
        trans.append([])

    # OR
    # [ trans.append([]) for i in range(4) ]
    # matrix_creation() does the above
        
    ind = 0
    for row in matrix: # [1234] [5678] [9 10 11 12]
        for n in row: # 1234
            # all i'm doing here is trans[i].append(row[i])
            # where i = 0-3
            trans[ind].append(n)
            ind += 1
        ind = 0
        
    print(trans)
    '''
    This is easier:
    for row in matrix:
        for i in range(4):
            trans[i].append(row[i])

    efficient_mat_tra() does the above
    '''

    '''
    To do the above, but with comprehension:
    trans = [ [row[i] for row in matrix] for i in range(4)]
    efficient_mat_tra() does the above
    '''
    

    

    
def matrix_creation():
    '''Create [ [], [], [], [] ]
    '''
    mat = []
    [ mat.append([]) for i in range(4) ]
    print(mat)

    # [ [], [], [], [] ]

def efficient_mat_tra():
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        ]
    trans = [[], [], [], []]
    
    for row in matrix: # [1234] [5678] [9 10 11 12]
        # [1234]
        for i in range(4):
            trans[i].append(row[i])
        
    print('reg', trans)

    com_trans = [ [row[i] for row in matrix] for i in range(4)]
    print('com', com_trans)
    
            
        
        
    
def test():
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        ]

    #trans = []
    #trans.append([row[0] for row in matrix])
    #trans.append([row[1] for row in matrix])
    #trans.append([row[i] for row in matrix] for i in range(4))
    '''
    for i in range(4):
        trans.append([row[i] for row in matrix])
    '''
    trans = [ [row[i] for row in matrix] for i in range(4) ]
    print(trans)


