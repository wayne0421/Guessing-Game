import random

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

x = random.choice(list)
y = input(('Welcome to my game! To start pick a number from 1-15 \n'))

while isinstance(y,str) or (x - y) != 0:
        try:
            y=int(y)
            if y in list:
                if abs(x-y) <= 3:
                    y = int((input('That was within 3! Try again \n')))
                else:
                    y = int((input('That was not that close. Try again! \n')))
            else:
                 1/0
        except:
            y = input('That was not a number in the list, please choose a number from 1-15: \n')
        
print(str(y) + ' was correct! Good Job!')



    


    

 





