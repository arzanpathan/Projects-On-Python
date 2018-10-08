
import random
import time
import Dice #For Getting The Pattern Of Dice
def sleep(s):
 for k in range(3):
     print('.',end=' ')
     time.sleep(1)
 print()

class Dice_Game:
 print('\t','\t','\t','\t','WELCOME TO THE GAME OF DICE','\n','\t','Things You Need To Know','\n','\t','1.Two Dice are Roll','\n','\t','2.Sum Of Those Two Dice is Done','\n','\t','3.You Will Get Four Chance To Guess The Sum','\n','\t','4.Sum Should Be Between 2 to 12(Integer Values)','\n','\t','5.For Every Wrong Guess 1 Chance Will Be Detected','\n','\t','6.For Every Wrong Input 1 Chance Will Be Detected','\n','\t','7.You Will Win If you Guess the Sum Right','\n','Thats All Have Fun And Enjoy','\n','\n','LETS START',end=' ')
 sleep(3)
 print('\n','\n''Two Dice are Rolled','\n')
 def Dice (self,Chance_Count):
     while(Chance_Count<5):

         Dice1,Dice2=random.randint(1, 6),random.randint(1, 6)

#Sum Of The Two Dice To Be Entered By User
         try_again=0
         while try_again==0:
             try:
                 Dice_Num_User=int(input('GUESS THE SUM OF TWO DICE '))
                 if (Dice_Num_User<2 or Dice_Num_User>12):
                     raise ValueError
                 else:
                     try_again=1
             except ValueError:
                 Chance_Count,Chance_Rem=Chance_Count+1,4-Chance_Count
                 print('Please Enter The Sum in Range 2 to 12 in Integer Form','\n','\n','You Lose Your Chance','\n','\t','COMPUTER WON','\n','\n','You Have Only',Chance_Rem,'Chances Remaining')
             if Chance_Count==5:
                 break


#To Compare User Values with Computer and Declare Who Won                
         if Chance_Count==5:
             break
         elif(Dice1+Dice2==Dice_Num_User):
             print('\n','I Guess Winning Is Not in Your Destiny LOL ',end=' ')
             sleep(3)
             Dice.Dice_Value(Dice1),Dice.add(),Dice.Dice_Value(Dice2)
             print('Sum of Two Dice Rolls too: ',Dice1+Dice2,'\n','\n','\t','>>> YOU WON <<<','\n','\n','Beginner\'s Luck','\n','\n')
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
                 Chance_Count=1
             elif (play_again=='N' or play_again=='NO'):
                 Chance_Count=5
                 print('THANKS FOR PLAYING')
             else:
                 pass
                 
         else:
             Chance_Count,Chance_Rem=Chance_Count+1,4-Chance_Count
             print('I Guess Winning Is Not in Your Destiny LOL ',end=' ')
             sleep(3)
             Dice.Dice_Value(Dice1),Dice.add(),Dice.Dice_Value(Dice2)
             print('Sum of Two Dice Rolls too: ',Dice1+Dice2,'\n','\n','\t','>>> COMPUTER WON <<<','\n','\n','You Have Only',Chance_Rem,'Chances Remaining To Prove Yourself Kiddo','\n','\n')
 

      
#To Start The Game
Guess_Game=Dice_Game()
Guess_Game.Dice(1)

#Play again block
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
    Guess_Game.Dice(1)
elif (play_again=='N' or play_again=='NO'):
    print('THANKS FOR PLAYING')

else:
    pass





