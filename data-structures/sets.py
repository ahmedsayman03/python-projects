'''sets'''

def sets():
    # sets are not ordered!
    a = set('abcdefaa')
    b = set('ghiabj')
    
    
    print(a)
    print(b)
    print(a-b) # in a, not in b
    print(a|b) # in a, in b, in both
    print(a&b) # both in a and b
    print(a^b) # in a, in b, not in both



# sets have comprehensions too like lists
def set_com():
    a = {x for x in 'abcd' if x not in 'ab'}
    print(a)

set_com()
