import random
import time
def sleep(s):
 for k in range(3):
     print('.',end=' ')
     time.sleep(1)

#Total No OF Chances
Chances=1
while(Chances<4):
#Computer Chooses From Rock Paper and Scissor
 Comp_Choice=random.randint(1, 3)# Directly Compare it Using 
 if(Comp_Choice==1):
     Comp_Choice='ROCK'
 elif(Comp_Choice==2):
     Comp_Choice='PAPER'
 elif(Comp_Choice==3):
     Comp_Choice='SCISSOR'
 User_Choice=input('Enter Your Choice: ')
 if((User_Choice=='ROCK' and Comp_Choice=='SCISSOR') or (User_Choice=='SCISSOR' and Comp_Choice=='PAPER') or (User_Choice=='PAPER' and Comp_Choice=='ROCK')):
     print('LOL Do You Think You Can Win From Me?',end=' ')
     sleep(3)
     print('\n','Your Choice >>',User_Choice,'<< Computer\'s Choice >>',Comp_Choice,'<< \n','\t','YOU WON','\n','Beginners Luck Lol If Not Then Try TO Win Again')
     Chances=4
 elif((Comp_Choice=='ROCK' and User_Choice=='SCISSOR') or (Comp_Choice=='SCISSOR' and User_Choice=='PAPER') or (Comp_Choice=='PAPER' and User_Choice=='ROCK')):
     print('LOL Do You Think You Can Win From Me?',end=' ')
     sleep(3)
     print('\n','Your Choice >>',User_Choice,'<< Computer\'s Choice >>',Comp_Choice,'<< \n','\t','Lol You Can\'t Win From Your Dad')
     Chances=Chances+1
 elif((Comp_Choice=='ROCK' and User_Choice=='ROCK') or (Comp_Choice=='SCISSOR' and User_Choice=='SCISSOR') or (Comp_Choice=='PAPER' and User_Choice=='PAPER')):
     print('LOL Do You Think You Can Win From Me?',end=' ')
     sleep(3)
     print('\n','Your Choice >>',User_Choice,'<< Computer\'s Choice >>',Comp_Choice,'<< \n','\t','IT\'S A TIE','\n','Try Again')


