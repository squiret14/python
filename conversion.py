
lineFill(x,oldcolour,newcolour)
    if x>= (len(line)) or line[x]!=oldcolour:#stopping condtion
        return
    else:
        line[x]=newcolour
        print(line)
        lineFill(x+1,0,2)

line=[0,0,0,0,0,0]#this is my 1d line
print(len(line))#length of line
lineFill(0,0,2)#assigns values to the linefill above
print(line)






def floodFill(x,y,oldcolour,newcolour):#a procedure to flood fill starting at a point
    if x>=5 or y>=5 or x<0 or y<0 or bitmap[x][y] != oldcolour:#creates 2d array
        return
    else:
            bitmap[x][y]=newcolour
            floodFill(x+1,y,oldcolour,newcolour)#goes right 1
            floodFill(x-1,y,oldcolour,newcolour)#goes left 1
            floodFill(x,y+1,oldcolour,newcolour)#goes down 1
            floodFill(x,y-1,oldcolour,newcolour)#goes up 1



bitmap = [[1,0,0,1,0],[1,0,1,0,0],[0,0,0,1,0],[1,0,0,0,1],[0,0,1,0,0]]#this is my grid
floodFill(0,2,0,2)#starting position and what we want the new colour to be
print(bitmap)#print the bitmap

for x in range(0,5):#print thm on top of eachother
    print(bitmap[x])





