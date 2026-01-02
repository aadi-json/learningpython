import threading

# print("the thread executing is my system is",
#       threading.current_thread().name)
# def FirstThread():
#     for i in range(1,10):
#         print("child thread",threading.current_thread().name)
# th=threading.Thread(target=FirstThread)
# th2=threading.Thread(target=FirstThread)
# th.name='janvi'
# th2.name='sejal'
# th.start()
# th2.start()
# for j in range(1,10):
#     print("main thread")

# --------------------------------------------------------------------------------------------------

# from threading import *
# class Threads(Thread):
#     def run(self):
#         for i in [1,2,3,4,5]:
#             print(i**2,current_thread().name)
# obj=Threads()
# obj.name="Monkey D Luffy"
# obj.start()

# from time import *
# from threading import *
# class Threads(Thread):
#     def run(self):
#         for i in [1,2,3,4,5]:
#             print(i**2,current_thread().name)
#             sleep(1)
#         # print(end - start)
# obj=Threads()
# obj.name="Monkey D Luffy"
# st=time()
# obj.start()
# end=time()
# print(end-st)
# obj.join()

# =======================================================================================

"way-1:without using any class"

# from threading import *
#
# def disp():
#     for i in range(1,10):
#         print(i**2)
#     print(f"My current thread: ",current_thread().name)
# obj=Thread(target=disp,name="aditya")
# # obj.name='Aditya'
# obj.start()


"way-2 : with extending thread class"

# from threading import *
#
# class Demo(Thread):
#     def run(self):
#         print("Monkey Dr Luffy and my thread is :",current_thread().name)
#
# obj=Demo()
# obj.name="Aditya"
# obj.start()

"way-3 : without extending thread class"

# from threading import *
#

# class Demo:
#     def Indumati(self):
#         print("main bheem ki hu",current_thread().name)
#     def chutki(self):
#         print("main bhi bheem ki hu",current_thread().name)
#
# object=Demo()
# obj=Thread(target=object.chutki,name="kaliya")
# obj2=Thread(target=object.Indumati,name="raju")
# obj.start()
# obj2.start()

# import time
# l=[1,2,3]

# def squre(l):
#     for i in l:
#         print(i**2)
#         time.sleep(1)
# def cube(l):
#     for i in l:
#         print(i**3)
#         time.sleep(1)
#         end = time.time
# start=time.time()
# squre(l)
# cube(l)
# end=time.time()
# print(f"without using multithreading :{end-start} ")

# print()

"when we use threading the program execution time become less"

# from threading import *
# def square(l):
#     for i in l:
#         print(i**2)
# def cube(l):
#     for i in l:
#         print(i**3)
#         time.sleep(1)
# start=time.time()
# first=Thread(target=square,args=(l,))
# second=Thread(target=cube,args=(l,))
# first.start()
# second.start()
# first.join()
# second.join()
# end=time.time()
# print(end-start)
# print(first.ident)
# print(second.ident)


# from threading import *
# from time import *
# def disp():
#     print(current_thread().name,'started....')
#     for i in range(10):
#         print("Namrata")
#         sleep(2)
#     print(current_thread().name,'ended...')
#
# obj=Thread(target=disp,name="Aditya")
# # obj2=Thread(target=disp,name="Harsh")
# obj.start()
# obj.join()
# obj.join(5)
# print("I am main thread wait here")


# for i in enumerate([1,2,3],2):
#     print(i)

# enumerate(): it is an inbuilt function which is used to return the list of thread which is present
# our program

from threading import *
from time import *
def demo():
    print(current_thread().name,'Started....')
    sleep(2)
    print(current_thread().name,'ended')
    print("active thread is ",active_count())
    l=enumerate()
    for i in l:
        print(i)
c=Thread(target=demo,name='Aditya')
c1=Thread(target=demo,name='harsh')
c2=Thread(target=demo,name='Namrate')
c.start()
c1.start()
c2.start()
sleep(5)
l=enumerate()
for i in l:
    print(i)
print("active thread is ",active_count())

"active_count():it will print the number of active thread present in our program"