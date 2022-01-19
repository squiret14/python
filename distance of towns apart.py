
myTree=[[-1,None,-1]]
def addToTree(value):
    currentNode=0
    done=False
    #if it is root node
    if myTree[0][1]== None:
        myTree[0][1]= value
    else:
        while not done:
        #if the new value is<current node
            if value<myTree[currentNode][1]:
                #if the left pointer is null,it is a leaf node
                if myTree[currentNode][0]==-1:
                    #so creats anew node
                    myTree.append([-1,value,-1])
                    #calculate the pointer to the new code
                    end=len(myTree)-1
                    myTree[currentNode][0]=end
                    print(value,"added a postion",end)
                    done=True
                    return
                else:
                    currentNode=myTree[currentNode][0]
            else:
               if value>myTree[currentNode][1]:
                #if the left pointer is null,it is a leaf node
                if myTree[currentNode][2]==-1:
                    #so creats anew node
                    myTree.append([-1,value,-1])
                    #calculate the pointer to the new code
                    end=len(myTree)-1
                    myTree[currentNode][2]=end
                    print(value,"added a postion",end)
                    done=True
                    return
                else:
                    currentNode=myTree[currentNode][2] 

def inOrder(p):
    if myTree[p][0]!=1:
        inOrder(myTree[p][0])
    print(myTree[p][1])
    if myTree[p][2]!=-1:
        inOrder(myTree[p][2])

def postOrder(p):
    if myTree[p][0]!=-1:
        postOrder(myTree[p][0])
    if myTree[p][2]!=-1:
        postOrder(myTree[p][2])
    print(myTree[p][1])

def preOrder(p):
    print(myTree[p][1])
    if myTree[p][0]!=-1:
        preOrder(muTree[p][0])
    if myTree[p][2]!=-1:
        preOrder(myTree[p][2])
                  
    
    
    
    




                    
addToTree(98)
print(myTree)
addToTree(100)
print(myTree)
addToTree(4)
print(myTree)
addToTree(63)
print(myTree)
