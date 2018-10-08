
#For Dice Values


def Dice_Value(d):
    for i  in range(0,11):#For Rows
        for j in range(1,15):#For Columns
            # For Dice Case
            if (i==1 or i==4 or i==7 or i==10) and (j==3 or j==7 or j==11):
                print('_',end='')
            elif (i>1 and (j==1 or j==5 or j==9 or j==13)): # For Straight lines
                print('|',end='')
            elif d==6 and ((i==3 or i==6 or i==9) and (j==3 or j==11)):
                print('\a',end='')
            elif d==5 and ((i==3 and j==3) or (i==6 and j==7) or (i==9 and j==11) or (i==3 and j==11) or (i==9 and j==3)):
                print('\a',end='')
            elif d==4 and ((i==3 or i==9) and (j==3 or j==11)):
                print('\a',end='')
            elif d==3 and ((i==3 and j==3) or (i==6 and j==7) or (i==9 and j==11)):
                print('\a',end='')
            elif d==2 and ((i==3 or j==11) and (i==9 or j==3)):
                print('\a',end='')
            elif d==1 and ((i==6) and (j==7)):
                print('\a',end='')
            else:
                print(' ',end='')
        print()
    print('\n')
    
def add():
    for i in range(1,8):
        for j in range(1,8):
            if (i==i and j==4) or (j==j and i==4):
                print('\a',end=' ')
            else:
                print(' ',end=' ')
        print()

       
'''
For 6
elif (i==3 or i==6 or i==9) and (j==3 or j==11):
    print('\a',end='')
For 5
if (i==3 and j==3) or (i==6 and j==7) or (i==9 and j==11) or (i==3 and j==11) or (i==9 and j==3):
         print('\a',end='')
For 4
elif (i==3 or i==9) and (j==3 or j==11):
         print('\a',end='')
For 3
if (i==3 and j==3) or (i==6 and j==7) or (i==9 and j==11):
         print('\a',end='')
For 2
elif (i==3 or j==11) and (i==9 or j==3):
         print('\a',end='')
For 1         
if (i==6) and (j==7):
         print('\a',end='')


(i==3 and j==3) or (i==6 and j==7) or (i==9 and j==11) or (i==3 and j==11) or (i==9 and j==3) or (i==6 and j==11) or (i==6 and j==3)


'''
