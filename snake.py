x="snake"
y="water"
z="gun"

import random
a=['snake','water','gun']
b=random.choice(a)


i=1
p1=0
p2=0
while(i<=10):
    print("Enter your choice")
    c=input()
    if b==c:
        print("both loose")
    elif b==x and c==y:
        print("player 1 wins")
        p1=p1+1
    elif b==x and c==z:
        print("player 2 wins") 
        p2=p2+1   
    elif b==y and c==z:
         print("player 1 wins")
         p1=p1+1
    elif b==y and c==x:
        print("player 2 wins")
        p2=p2+1   
    elif b==z and c==x:
        print("player 1 wins ")
        p1=p1+1     
    elif b==z and c==y:
        print("player 2 wins")   
        p2=p2+1    
    i=i+1
print("score of player 1 is",p1, "and score of player 2 is",p2)
if p1>p2:
    print("player 1 wins the match")
elif p1<p2:
    print("player 2 wins the match")
else:
    print("no one wins")
  
print("Thank you!! ;)")