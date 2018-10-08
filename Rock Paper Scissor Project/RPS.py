import random
import time
def sleep(s):
 for k in range(3):
     print('.',end=' ')
     time.sleep(1)

#Total No OF Chances
play_rps_again=0
while(play_rps_again==0):
 print('\t','\t','\t','\t','WELCOME TO THE GAME OF ROCK/PAPER/SCISSOR','\n','\t','Things You Need To Know','\n','\t','1.You Need To Choose One of Rock/Paper/Scissor','\n','\t','2.Be Sure to Enter the Proper Name','\n','\t','3.Rock Takes Scissor,Scissor Takes Paper,Paper Takes Rock','\n','\t','4.So If You Wanna Win Make The Right Choice','\n','Thats All Have Fun And Enjoy','\n','\n','LETS START',end=' ')
 sleep(3)
 print('\n','\n')
    
#Computer Chooses From Rock Paper and Scissor
 Comp_Choice=random.randint(1, 3)# Directly Compare it Using 
 if(Comp_Choice==1):
     Comp_Choice='ROCK'
 elif(Comp_Choice==2):
     Comp_Choice='PAPER'
 elif(Comp_Choice==3):
     Comp_Choice='SCISSOR'

#For User To Choose Rock/Paper/Scissor 
 try_again=0
 while(try_again==0):
     try:
         User_Choice=input('SO WHATS YOUR CHOICE (ROCK/PAPER/SCISSOR):').upper()
         if User_Choice!='ROCK' and User_Choice!='PAPER' and User_Choice!='SCISSOR':
             raise NameError
         else:
             try_again=1
     except NameError:
         print('Please Enter Your Choice as (ROCK/PAPER/SCISSOR)')
                  
 if((User_Choice=='ROCK' and Comp_Choice=='SCISSOR') or (User_Choice=='SCISSOR' and Comp_Choice=='PAPER') or (User_Choice=='PAPER' and Comp_Choice=='ROCK')):
     print('LOL Do You Think You Can Win From Me?',end=' ')
     sleep(3)
     print('\n','\n','Your Choice >>',User_Choice,'<< Computer\'s Choice >>',Comp_Choice,'<< \n','\t','YOU WON','\n','Beginners Luck Lol If Not Then Try TO Win Again','\n','\n',)
     try_again=0
     while try_again==0:
         try:
             play_again=input('Do You Wanna Play Again(Y/N): ').upper()
             if play_again!='Y' and play_again!='N' and play_again!='YES' and play_again!='NO':
                 raise NameError
             else:
                 try_again=1
         except NameError:
             print('Please Enter (YES/NO) or (Y/N) To Play Again')
     if (play_again=='Y' or play_again=='YES'):
         play_rps_again=0
     elif (play_again=='N' or play_again=='NO'):
         play_rps_again=1
         print('THANKS FOR PLAYING')
     else:
         pass
                
     
 elif((Comp_Choice=='ROCK' and User_Choice=='SCISSOR') or (Comp_Choice=='SCISSOR' and User_Choice=='PAPER') or (Comp_Choice=='PAPER' and User_Choice=='ROCK')):
     print('LOL Do You Think You Can Win From Me?',end=' ')
     sleep(3)
     print('\n','\n','Your Choice >>',User_Choice,'<< Computer\'s Choice >>',Comp_Choice,'<< \n','\t','COMPUTER WON','\n','Lol You Can\'t Win From Me After All','\n','\n','Here\'s Another Chance For You Try to Win from Me','\n','\n')

 elif((Comp_Choice=='ROCK' and User_Choice=='ROCK') or (Comp_Choice=='SCISSOR' and User_Choice=='SCISSOR') or (Comp_Choice=='PAPER' and User_Choice=='PAPER')):
     print('LOL Do You Think You Can Win From Me?',end=' ')
     sleep(3)
     print('\n','Your Choice >>',User_Choice,'<< Computer\'s Choice >>',Comp_Choice,'<< \n','\t','IT\'S A TIE','\n','Try Again Bro We Will Play Till Someone Wins ','\n','\n')
     

