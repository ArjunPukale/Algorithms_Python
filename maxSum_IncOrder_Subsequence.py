'''
Using DFS to find a subsequence with maximum sum in the given input array such that it has increasing order .
'''

inp = [2,202,3,200,4,5]

from collections import deque

def valueOf(idx):
    return inp[idx]
    
def Childs(parentId):
    ''' 
    Returns a list of child indices of the given parent Id.
    A child is valid if it is greater than its parent and is located after its parent.
    '''
    childIds = []
    for i in range(parentId+1,len(inp)):
        if inp[i]>inp[parentId]:
            childIds.append(i)
    return childIds

def isLeaf(idx):
    if not Childs(idx):
        return True
    else:
        return False
# print(isLeaf(0))
# for idx in Childs(2):
#     print(inp[idx])

G = {} #Adjacency List
for i in range(len(inp)):
    G[i] = Childs(i)
    
records = []
maxSum = 0
def DFS(i): #i=>index (parent)
    global maxSum
    stack.append(valueOf(i))
    for idx,parentID in enumerate(parent_stack): 
        if parentID>=parent[i]: #if a node with same or greater level is already in the stack
            deleteIdx = idx
            parent_stack.remove(parent_stack[deleteIdx])
            stack.remove(stack[deleteIdx])
#     while parent[i] in parent_stack: #if a node with same level is already in the stack
#         deleteIdx = parent_stack.index(parent[i])
#         parent_stack.remove(parent_stack[deleteIdx])
#         stack.remove(stack[deleteIdx])
    parent_stack.append(parent[i])
    if isLeaf(i):
        #calculate the sum and record its path if new maxSum is found
        tempSum = sum(stack)
        if tempSum>=maxSum:
            records.append(list(stack)+[sum(stack)])
            maxSum = tempSum
        #pop the leaf node from the stack
        stack.pop()
        parent_stack.pop()
    for childId in G[i]:
        parent[childId] = i
        DFS(childId) 

for i in range(0,len(inp)-1):
    # repeat the DFS on every element in the input list as root
    stack = deque()
    parent_stack = deque()
    parent = [-1 for i in range(len(inp))]
    DFS(i)
#path with maximum sum
result = sorted(records,key=lambda x:x[-1],reverse=True)[0]
print(f"Max Sum: {result[-1]}, path : {result[:-1]}")
    
    
    
    
    
    
    
    
    
