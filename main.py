

from random import randint, random

class Store:
    def __init__(self,hour:int,minute:int,line:list) -> None:
        self.hour=hour
        self.minute=minute
        self.line=line

    def New_Time(self):
        # The time counter
        self.minute+=1
        if self.minute%60==0:
            self.hour+=1
            self.minute=0

            

    # Tells whenever a new peroson has entered the queue, the time they entered queue and how many tasks they need help with
    def Add_To_Line(self,n):
        self.line.append(
        Person(f"Person {n}",Task()))
        if self.minute<10 and self.hour<10:
               print(f"{self.line[-1].name} arrived at the time 0{self.hour}:0{self.minute} with {self.line[-1].tasks} tasks in place {len(self.line)}")
        elif self.hour<10: 
                print(f"{self.line[-1].name} arrived at the time 0{self.hour}:{self.minute} with {self.line[-1].tasks} tasks in place {len(self.line)}")
        elif self.minute<10:
               print(f"{self.line[-1].name} arrived at the time {self.hour}:0{self.minute} with {self.line[-1].tasks} tasks in place {len(self.line)}") 
        else:
                print(f"{self.line[-1].name} arrived at the time {self.hour}:{self.minute} with {self.line[-1].tasks} tasks in place {len(self.line)}")


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
    h=0
    n=0
    store1=Store(9,0,[])
    while store1.hour<18:
        store1.New_Time()
        if randint(0,100)>20:
            n+=1
            store1.Add_To_Line(n)

        if h==0 and len(store1.line)>0:
            h=store1.line[0].tasks
            del store1.line[0]
            h-=0.5

        else:
            h-=0.5





        

if __name__=="__main__":
    main()