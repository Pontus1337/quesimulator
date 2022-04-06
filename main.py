

from random import randint, random

class Store:
    def __init__(self,hour:int,minute:int,line:list) -> None:
        self.hour=hour
        self.minute=minute
        self.line=line

    def New_Hour(self):
        self.hour+=1
        self.minute=0





        
    def Add_To_Line(self,n):

        self.line.append(
        Person(f"Person {n}",Task()))
        if self.minute<10 and self.hour<10:
               print(f"{self.line[-1].name} arrived at the time 0{self.hour}:0{self.minute} with {self.line[-1].tasks} tasks")
        elif self.hour<10: 
                print(f"{self.line[-1].name} arrived at the time 0{self.hour}:{self.minute} with {self.line[-1].tasks} tasks")
        elif self.minute<10:
               print(f"{self.line[-1].name} arrived at the time {self.hour}:0{self.minute} with {self.line[-1].tasks} tasks") 
        else:
                print(f"{self.line[-1].name} arrived at the time {self.hour}:{self.minute} with {self.line[-1].tasks} tasks")
class Person:
    def __init__(self,name:str,tasks:int) -> None:
        self.name=name
        self.tasks=tasks


def Task():
    n=1
    rand=random()
    while rand<1/2**n:
        n+=1
    return n
    




def main():
    n=0
    store1=Store(9,0,[])
    while store1.hour<18:
        store1.minute+=1
        if store1.minute%60==0:
            store1.New_Hour()


        if randint(0,100)>20:
            n+=1
            store1.Add_To_Line(n)
            


        




if __name__=="__main__":
    main()