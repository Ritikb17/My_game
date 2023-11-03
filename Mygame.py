def pt():
    print(lst[1],lst[2],lst[3],lst[4])
    print(lst[5],lst[6],lst[7],lst[8])
    print(lst[9],lst[10],lst[11],lst[12])
    print(lst[13],lst[14],lst[15],lst[16])
def closest(ref,next):
    lst2=[[],[2,6,5],[1,3,5,6,7],[2,4,6,7,8],[3,7,8],
          [1,2,6,9,10],[1,2,3,5,7,9,10,11],[2,3,4,6,8,10,11,12],[3,4,7,11,12],
          [5,6,10,11,14],[5,6,7,9,11,13,14,15],[6,7,8,10,12,14,14,16],[7,8,11,15,16],
          [9,10,14],[9,10,11,13,15],[10,11,12,14,16],[11,12,15]]
    return next in lst2[ref]

def check():
    lst3=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,11,15,16],
          [1,5,9,13],[2,6,10,14],[3,7,11,15],[4,8,12,16],
          [1,6,11,16],[4,7,10,13]]
    lst4=['','','','','','','']
    for i in range(10):
        x=0
        for k in lst3[i]:
            lst4[x]=lst[k]
            x+=1

        if lst4[0]==lst4[1]==lst4[2]==lst4[3] and lst4[0]!=' _ ':
            return True
    return False
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#MAIN

lst = [' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ',' _ ']
x = 0
y = 0
#pt()
while x < 4 and  y < 4:
    print("***THIS IS THE PHASE 1 OF THE GAME YOU HAVE TO PLACE YOUR DICE , MAKE SURE NO TO OVERRIDE AND DICE*** \n\n\n")
    
    hold=False
    pt()
    ref = int(input("\n\n\n ->Enter the postion of dice PLAYER X\n->Enter 0 for exit the game "))
    if ref==0:
        print("->GAME OVER")
        hold=True
        break
        

    if lst[ref] == " _ ":
        lst[ref] =" X "
        x += 1
    else:
        print("->Invalid Position")
    pt()
    if check():
        print("->PLAYER X won the game ")
        break
    ref = int(input("->Enter the postion of dice PLAYER O"))
    if lst[ref] == " _ ":
        lst[ref] = " O "
        y += 1
    else:
        print("->Invalid Position")
    pt()
    if check():
        print("->PLAYER O won the game ")
        break
    r=check()


# CODE FOR THE MOVEMENT OF THE DICE

while not check()and not hold:
    print("***THIS IS THE SECOUND PHASE OF THE GAME NOW YOU HAVE TO SELECT ONE OF YOUR DICE AND MOVE IT TO NEARBY EMPTY POSITION\n\n\n***")
    pt()
    ref=int(input("->Enter The Position Of The Dice PLAYER X\n->Enter 0 for exit the game "))
    if ref==0:
        print("GAME OVER ")
        break

    if lst[ref]==" X ":
        next=int(input("->Enter The Next Position Of The Dice"))
        if lst[next]!=" _ ":
            print("->Invalid Selection")
    else:
        print("->Invalid Selection")

    if closest(ref , next):

        lst[next] = " X "
        lst[ref] = " _ "
        if check():
            print("->PLAYER X Won The Game")
            pt()
            break
    else:
        print("->Invalid NEXT Pos ")
    pt()
#PLAYER O
    ref = int(input("->Enter The Position Of The Dice PLAYER O"))
    if lst[ref] == " O ":
        next = int(input("->Enter The Next Position Of The Dice"))
        if lst[next] != " _ ":
            print("->Invalid Selection")
    else:
        print("->Invalid Selection")

    if closest(ref, next):

        lst[next] = " O "
        lst[ref] = " _ "
        if check():
            pt()
            print("->PLAYER O Won The Game")
            break
    else:
        print("->Invalid NEXT Pos ")

    pt()