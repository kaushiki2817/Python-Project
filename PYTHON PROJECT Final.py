
# coding: utf-8

# In[1]:


def class_bot():
    #Welcome to NetTech
    print('Course Guide')
    #Welcome the user
    print('Hello welcome to NetTech!!')
    #Ask user its name
    user_name=input('Please enter your name here: ')
    #greet the user
    print('Hello',user_name.title())
    #Ask user its interest
    user_int=input('please enter your interest here: ')
    if user_int.lower()=='yes':
        #user mobile number
        phone_number=input('Please enter your phone number: ')
        print('ph.NO.',phone_number)
        #emailID
        email_id=input('Please enter your emailID: ')
        print('emailID',email_id)
        #prefered course
        prefered_course=input('Please enter your Prefered course: ')
        print('Prefered course',prefered_course)
        #prefered location
        prefered_location=input('Please enter your prefered location: ')
        print('prefered location',prefered_location)
    else:
        print('invalid course')
    print('*'*30)


def hotel_bot():
    #Hotel Recomendation Bot
    print('Hotel Guide')
    #Welcome the user
    print('Welcome to the city of Dreams!!! MUMBAI')
    #Ask user its name
    user_name=input('Please enter your name here: ')
    #greet the user
    print('Hello!!',user_name)
    #ask user its budget
    budget=int(input('Please enter your budget here: '))
    #25000-->Taj Hotel
    if budget>=25000:
        print('experience of luxury at Hotel Taj')
    #15000-25000-->Oberoi Hotel
    elif budget>=15000 and budget<25000:
        print('Explore the Oberoi Hotel')
    #5000-15000-->holiday INN
    elif budget>=5000 and budget<15000:
        print('Stay at Holiday INN')
    #1000-5000-->OYO
    elif budget>=1000 and budget<5000:
        print('visit to OYO')
    #100-1000-->Lodge
    elif budget>=100 and budget<1000:
        print('Book a Lodge')
    #100--> Go Back Home
    else:
        print('Go back Home')
    print('*'*30)

def chance_bot():
    #Head and Tails Game
    print('Heads & Tails Game')
    #welcome the user
    print('Welcome to the game of chance!!')
    #ask user its name
    user_choice=input('Please enter heads or tails: ')
    if user_choice.lower()=='heads' or user_choice.lower()=='tails':
        #Users choice
        print('You chose',user_choice.title())
        #coin toss
        import random
        if (random.choice('ht'))=='h':
            coin_toss='heads'
        else:
            coin_toss='Tails'
        #display coin result
        print('coin result:',coin_toss.title())
        if user_choice.lower()==coin_toss:
            print('you won')
        else:
            print('computer won')
    else:
        print('Invalid Input')
    print('*'*30)


def dice_game():   
    #Welcome to Dice game
    print('Dice Game')
    #welcome the user
    print('Welcome to Dice Game!!')
    #ask user to roll dice
    user_roll=input('please enter the number: ')
    #display the user roll
    print('you have choose',user_roll)
    import random
    #dice rolled
    dice_rolled=random.choice('123456')
    #display result
    print('dice result',dice_rolled)
    if user_roll==dice_rolled:
        print('you won!!')
    else:
        print('you lose!!')
    print('*'*30)

def cube():    
    #Welcome the user
    print('Cubes')
    #cubes
    #ask user to enter a number
    user_number=int(input('Please enter a number here: '))
    for i in range(1,user_number+1):
        print(i,'cube of',i**3)
    print('*'*30)
        

def table():    
    #Welcome the user
    print('Tables')
    #Tables
    #ask user to enter a number
    user_number=int(input('Please enter a number here: '))
    for i in range(1,11):
        print(user_number,'x',i,'=',user_number*i)
    print('*'*30)

def factorial():    
    #Welcome the user
    print('Factorial')
    #Factorial
    #ask user to enter a number
    user_number=int(input('Please enter a number here: '))
    fact=1
    for i in range(1,user_number+1):
        fact=fact*i
    print('The Factorial of',user_number,'is',fact)
    print('*'*30)

def fibonacci():    
    #Welcome the user
    print('Fibonacci Series')
    #Fibonacci Series
    #ask user to enter a number
    user_number=int(input('Please enter a number here: '))
    #Define two variables a and b
    a=0
    b=1
    for i in range(user_number):
    #print the Result
        print(a)
        c=a+b
        a=b
        b=c
    print('*'*30)

def password():    
    #Welcome the user
    print('Generate Password')
    #Generate a Password
    #ask user to enter a number
    user_number=int(input('Please enter a number here: '))
    #define variable
    import random
    character='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~`!@#$%^&*)(_-+=|\:;"><?/'
    password=''
    for i in range(user_number):
        password=password+(random.choice(character))
    print('The password is here',password)
    print('*'*30)
    
def count_down():    
    print('Countdown Timer')
    minutes=int(input('enter minutes here: '))
    seconds=int(input('enter seconds here: '))
    import countdown
    # Create a countdown of 1 minute and 10 seconds
    countdown.countdown(mins=minutes, secs=seconds)
    print('*'*30)
    

def mind_game():    
    #welcome to Mind Games
    print('Welcome to Mind Games!!')
    import time
    #Ask user to guess a number Between 1-5000
    print('Think any number in your mind')
    #wait
    time.sleep(3)
    #Ask user to double the number
    print('double the number you thought')
    #wait
    time.sleep(3)
    #Ask user to add 50 in the above number
    print('add the above number with 50')
    #wait
    time.sleep(3)
    #Ask user to divide the number by 2
    print('divide the number with 2')
    #wait
    time.sleep(3)
    #ask user to minus the number with original number
    print('minus the the number with original number')
    #wait
    time.sleep(3)
    #Guess the user number
    print('The number you chose was 25!!!')
    print('*'*30)
    
    
import tkinter as tk
#main window
window=tk.Tk()
#title change
window.title('Python Project')
#window size
window.geometry('580x450')
#Label
tk.Label(window,text='PYTHON PROJECT',font=('Eras Bold ITC',20)).place(x=180,y=30)
#SubLabel
tk.Label(window,text='MADE BY: Kaushiki Nanarkar',font=('helvetica',10)).place(x=190,y=90)
#button
tk.Button(window,text='COURSE GUIDE',width=20,height=2,command=class_bot).place(x=50,y=130)
#button
tk.Button(window,text='HOTEL GUIDE',width=20,height=2,command=hotel_bot).place(x=225,y=130)
#button
tk.Button(window,text='HEADS & TAILS',width=20,height=2,command=chance_bot).place(x=400,y=130)
#button
tk.Button(window,text='DICE GAME',width=20,height=2,command=dice_game).place(x=50,y=200)
#button
tk.Button(window,text='CUBE',width=20,height=2,command=cube).place(x=225,y=200)
#button
tk.Button(window,text='TABLES',width=20,height=2,command=table).place(x=400,y=200)
#button
tk.Button(window,text='FACTORIAL',width=20,height=2,command=factorial).place(x=50,y=275)
#button
tk.Button(window,text='FIBONACCI SERIES',width=20,height=2,command=fibonacci).place(x=225,y=275)
#button
tk.Button(window,text='PASSWORD',width=20,height=2,command=password).place(x=50,y=350)
#button
tk.Button(window,text='COUNTDOWN TIMER',width=20,height=2,command=count_down).place(x=400,y=275)
#button
tk.Button(window,text='MIND GAMES',width=20,height=2,command=mind_game).place(x=225,y=350)
#window close 
window.mainloop()


# In[104]:




