import random
digit=5
name=input("enter name::")
print("______",name,"_______")
print("_______________")
print("____weicome to cowbull_____")
print("________________")
def getsecretnum():
    number=list(range(10))
    random.shuffle(number)
    return number
def getclues():
    numbers=getsecretnum()
    list=[]
    for i in range(digit):
        list.append(numbers[i])
    return list
def check_num():
    cow=[]
    bull=[]
    num=getclues()
    i=0
    print(num)
    maxguess=10
    while maxguess>0:
        guess=int(input("enter number::"))
        position=int(input("enter position of given number::"))
        if guess in num:
            index=num.index(guess)
            if index==position:
                if guess not in bull:
                    bull.insert(index,guess)
                    print("bull",bull)
                else:
                    print("You Already Used This digit Try  any Different digit")
            elif index!=position:
                cow.append(guess)
                print("cow",cow)
            else:
                print("this number is not exist in given list")
        if bull==num:
            print(name,"congratulations you are winner")
            break
        maxguess-=1
        print(maxguess,"turns are left")
    else:
        print("You ran out your tries, You Loose The Game")   
    return bull
check_num()
def play_again():
    while True:
        again=input("you want to play again this game yes=y or not =n::")
        if again=="y":
            check_num()
        else:
            break
play_again()