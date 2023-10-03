import multiprocessing
import os

def Task1(value):
    print("Executing the first task...")
    for i in range(value):
        print("Task1 : ",i)

def Task2(value):
    print("Executing the second task...")
    for i in range(value):
        print("Task2 : ",i)


def main():
    print("Demonstration of Multiprocessing")

    print("PID of running process is : ",os.getpid())
    No1 = 500
    No2 = 800
    p1 = multiprocessing.Process(target = Task1, args = (No1, ))
    p2 = multiprocessing.Process(target = Task2, args = (No2, ))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if __name__ == "__main__":
    main()    

# write logic for addition of even & odd numbers in task1 and task2    