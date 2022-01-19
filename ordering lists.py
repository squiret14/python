keys=(768,7843,72,784,789,535,976,439,376)
HashTable=[None,None,None,None,None,None,None,None,None]
OverFlowTable=[None,None,None,None,None,None,None,None,None]
def DivisionMethod(k):
    position=k % max
    return position
key=784
def delete(k):
   position=DivisionMethod(k)
   if HashTable[position]==k:
       print(k,"delete at position",position)
   else:
       print(k,"not found in main hash table")
       j=0
       found=False
       while (found == False) and (j<overflowplace):
           if OverFlowTable[j]!=i:
               j=j+1
           else:
               found=True
               print(k,"deleted at position",i)

def Findkey(k):
   position=DivisionMethod(k)
   if HashTable[position]==k:
        HashTable[position]==None
        print(k,"found at position",position)
   else:
       print(k,"not found in main hash table")
       j=0
       found=False
       while (found == False) and (j<overflowplace):
           if OverFlowTable[j]!=i:
               j=j+1
           else:
               found=True
               print(k,"found at position",i)
        





max=len(HashTable)
overflowplace=0

for i in keys:
    location=DivisionMethod(i)
    if HashTable[location]==None:
        HashTable[location]=i
    else:
        print("collision:records=",i,"location",location)
        OverFlowTable[overflowplace]=i
        overflowplace=overflowplace+1




        
print(HashTable)
print(OverFlowTable)
Findkey(535)
