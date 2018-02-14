game =['a','f','g','a','b','w','c','m','b','d','l','g','w','l','e','f','e','c','g','m']
no=['1','2','3','4','5','6','7','8','9','0','1','2','3','4','5','6','7','8','9','0']
s=no
j=0
i=0
k=0
print("welcome to the memory game\n")
print(no)
while(True):
    if j%2==0:
        print("player 1 : it's your turn\n")
    else:
        print("player 2 : it's your turn\n")
    print("choose 2 numbers from (1:20)\n")
    no1=int(input())
    no2=int(input())
    while(no1==no2 or no1>20 or no2>20 or no1<1 or no2<1 or game[no1-1]=='*' or game[no2-1]=='*' or s[no1-1]=='*' or s[no2-1]=='*'):
        print("choose another 2 numbers\n")
        no1=int(input())
        no2=int(input())
    if game[no1-1]==game[no2-1]:
        s[no1-1]=game[no1-1]
        s[no2-1]=game[no2-1]
        print(s)
        print("\n")
        s[no1-1]='*'
        s[no2-1]='*'
        no=s
        print(s)
        print("\n")
        if j%2==0 :
            i=i+1
        else :
            k=k+1
        if s=="********************" :
            if i>k :
                print ("the winner is player 1\n")
                print ("the highest score is : ",i)
                print("\n")
                break
            elif(k>i) :
                print("the winner is player 2 \n")
                print("the highest score is : ",k)
                print("\n")
                break
            else:
                print("it's a draw")
                break
    else :
        x=s[no1-1]
        y=s[no2-1]
        s[no1-1]=game[no1-1]
        s[no2-1]=game[no2-1]
        print (s)
        print("\n")
        s[no1-1]=x
        s[no2-1]=y
        print(no)
        print("\n")
        s=no
    j=j+1
        
                
        
        
        
