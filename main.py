

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
               print(f"{self.line[-1].name} arrived at the time 0{self.hour}:0{self.minute} with {self.line[-1].tasks} tasks in place {len(self.line)}\n")
        elif self.hour<10: 
                print(f"{self.line[-1].name} arrived at the time 0{self.hour}:{self.minute} with {self.line[-1].tasks} tasks in place {len(self.line)}\n")
        elif self.minute<10:
               print(f"{self.line[-1].name} arrived at the time {self.hour}:0{self.minute} with {self.line[-1].tasks} tasks in place {len(self.line)}\n") 
        else:
                print(f"{self.line[-1].name} arrived at the time {self.hour}:{self.minute} with {self.line[-1].tasks} tasks in place {len(self.line)}\n")


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
    waiting=0
    store1=Store(9,0,[])
    while store1.hour<18 or len(store1.line)>0:
        store1.New_Time()

        if randint(0,100)<=20 and not store1.hour>=18:
            n+=1
            store1.Add_To_Line(n)

        if h==0 and len(store1.line)>0:
            h=store1.line[0].tasks
            t=store1.line[0].name
            h-=0.5
            del store1.line[0]
        elif h>0:
            h-=0.5
            if h==0:
                print(f"{t} removed from queue at {store1.hour}:{store1.minute}\n")                
                
        print(len(store1.line))
        waiting+=len(store1.line)
    waiting_per_consumer=round(waiting*60/n)
    statistics=f"{n} consumers vere served, total waiting time was {waiting} minutes long = {waiting_per_consumer} seconds per consumer "
    print (statistics)

        






        

if __name__=="__main__":
    main()