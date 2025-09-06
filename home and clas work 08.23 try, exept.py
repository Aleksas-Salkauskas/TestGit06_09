# def sum(a,b=100):
#     return a+b
#
# print (sum(a=10))
# -----------------------------
# def sum1(a:list):
#     res=0
#     for l in a:
#         res+=l
#     return res/len(a)
# nums=[1,3,4,55,5,4,7,6,66,54,43,69,67,54,3]
# result=sum1(nums)
# print(result)
# ----------------------------------
# def avg(a:list):
#     res=0
#     for l in a:
#         res+=l
#     return res/len(a)
# nums=[]
# while True:
#     n= input("enter youre numbers")
#
#     if n==0:
#         break
#     nums.append(n)
# print(avg(nums))
# ------------------------
# def avg(a:list):
#     res=0
#     for l in a:
#         res+=l
#     return res/len(a)
# def add10(x):
#     return  x+10
# myNums=[2,2.5,5,4,6,7]
# for n in myNums:
#     # print(add10(n))
#     print((lambda x: x+10)(n))
# -------------------------------------
# def getYear(x):
#     return 2025 - x
#
# studBirthYear=[2000,1997,1999,2006,2004,1986]
# studAges = list(map(getYear,studBirthYear))
# print(studAges)
# ---------------------------------------


# studBirthYear=[2000,1997,1999,2006,2004,1986]
# studAges = list(map(lambda x: 2025-x,studBirthYear))
# print(studAges)
# --------------------------------------------
# while True:
#     try:
#         amount=int(input("enter the amaunt of goods: "))
#         itemType=input("enter goods name: ")
#         print(10/amount)
#     except ValueError:
#         print("amount must be integer: ")
#         amount=1
#     except ZeroDivisionError:
#         print("enter right number")
#     except:
#         print("opps")
#     finally:
#         print("finally")
# ----------------------homeWork----task 1.0---------------------------------------
#
# def AddNumbers():
#    try:
#        a=float(input("enter first number: "))
#        b=float(input("enter second number: "))
#        result=a/b
#        return (f"result: {result}")
#    except ValueError:
#        return"Please enter valid number: "
#    except ZeroDivisionError:
#        return "cannot divide by zero."
#
# while True:
#
#     output=AddNumbers()
#     print(output)
#     if "result" in output:
#         print("division wass succesful go get yourself banana 🍌")
#         break

# --------------------task 1.1----------------------------------------------------

# while True:
#     try:
#      num1=float(input("enter first number@"))
#      num2=float(input("enter second number@"))
#      print("result:", num1/num2)
#      break
#     except ValueError:
#         print("wrong input Please enter only numbers:")
#     except ZeroDivisionError:
#         print("cannot divide by zero")
#     finally:
#         print("great job we can drink beer now")


# -------------------tasks 2,3,4,5------------------------------------------------------
import math
import random

def task1():
    """Task with index of number"""
    myList = [10, 20, 30, 40, 50]
    try:
        index = int(input("enter indef of element from list:"))
        print(f"Element at index {index} is {myList[index]}")
    except ValueError:
        print("wrong input you dumb ass!!!!")
    except IndexError:
        print("youre index is to to big or whatever just put number from 1 to 5 because list have only 5 elements")
    finally:
        print("you on the right way but dont push the horses")

def task2():
    """task with a result of sales"""
    try:
        salesInput = input("please enter sales amounts with spase for example  10 20 30... ")
        sales = list(map(float, salesInput.split()))
        total = sum(sales)
        print(f"Amount of saless: {total}")
    except ValueError:
        print("I hope you did it not on purpose NOW PUT NUMBERS WITH SPACE!!!!")
    finally:
        print("task finished,everything works thank you for attention")

def task3():
    """Square root from number"""
    try:
        number = float(input("enter number to find square root: "))
        if number < 0:
            raise Exception("no fucking way we can find square root from minus number")
        result = math.sqrt(number)
        print(f"square root  of {number} is {result}")
    except ValueError:
        print("I ask last time Just put CORRECT NUMBER")
    except Exception as e:
        print("error: ", e)
    finally:
        print("you're calculation is finished")

def task4():
    """parsing data about products"""
    try:
        productInnput = input("enter info about product example (product name, price, amount)")
        name, price_str, quantity_str = map(str.strip, productInnput.split(","))
        price = float(price_str)
        quantity = int(quantity_str)
        print(f"product: {name}, price {price}, amount{quantity}")
    except ValueError:
        print("wrong input: price must be number, quantity must be also number")
    finally:
        print("parsing finished.\n")

def task5():
    """connect to server"""
    def connect_to_server():
        if random.choice([True, False]):
            return "connection successful"
        else:
            raise ConnectionError("connecting error ")

    try:
        message = connect_to_server()
        print(message)
    except ConnectionError:
        print("connection promlem")
    finally:
        print("connection finished.\n")

def main_menu():
    while True:
        print("homework menu")
        print("1.index from list")
        print("2.Sum of sales")
        print("3. square root")
        print("4.parsing info ")
        print("5.connect to server")
        print("0 Quit")

        choice = input("chose task")

        if choice == "1":
            task1()
        elif choice == "2":
            task2()
        elif choice == "3":
            task3()
        elif choice == "4":
            task4()
        elif choice == "5":
            task5()
        elif choice == "0":
            print("Exit program")
            break
        else:
            print("wrong input please try again..\n")

main_menu()












