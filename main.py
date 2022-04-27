from random import randint, random, uniform

class Store:
    def __init__(self,hour:int,minute:int,line:list,help:bool) -> None:
        self.hour=hour
        self.minute=minute
        self.line=line
        self.help=help

    def New_Time(self):
        # The time counter
        self.minute+=1
        if self.minute%60==0:
            self.hour+=1
            self.minute=0      

    # Tells whenever a new peroson has entered the queue, the time they entered queue and how many tasks they need help with
    def Add_To_Line(self,n,):
        self.line.append(Person(f"Person {n}",Task(),0))
        if self.minute<10 and self.hour<10:
            print(f"{self.line[-1].name} arrived at the time 0{self.hour}:0{self.minute} with {self.line[-1].tasks} tasks in place {len(self.line)}\n")
        elif self.hour<10: 
                print(f"{self.line[-1].name} arrived at the time 0{self.hour}:{self.minute} with {self.line[-1].tasks} tasks in place {len(self.line)}\n")
        elif self.minute<10:
            print(f"{self.line[-1].name} arrived at the time {self.hour}:0{self.minute} with {self.line[-1].tasks} tasks in place {len(self.line)}\n") 
        else:
                print(f"{self.line[-1].name} arrived at the time {self.hour}:{self.minute} with {self.line[-1].tasks} tasks in place {len(self.line)}\n")

    # This is the queue function deciding how thr queue works
    def thequeue(self):
        if len(self.line)>0:
            if self.help == False:
                self.line[0].tasks-=0.5
                self.help= True
            elif self.line[0].tasks>0:
                self.line[0].tasks-=0.5
            elif self.line[0].tasks==0:
                if len(self.line)>1:
                    print(f"{self.line[0].name} walked out at {self.hour}:{self.minute} and {self.line[1].name} starts getting help")
                else:
                    print(f"{self.line[0].name} walked out at {self.hour}:{self.minute}")
                    self.help=False
                del self.line[0]

class Person:
    def __init__(self,name:str,tasks:int,waited:int) -> None:
        self.name=name
        self.tasks=tasks
        self.waited=waited

def Task():
    n=1
    # rand=random()
    rand = round(uniform(0.01, 1), 2)
    print(rand)
    while rand<1/(2**n):
        n+=1
    return n

def main():

    person=0
    waiting=0
    store1=Store(9,0,[],False)

    while store1.hour<18 or len(store1.line)>0:
        store1.New_Time()

        if randint(0,100)<=20 and not store1.hour>=18:
            person+=1
            store1.Add_To_Line(person)

        store1.thequeue()
        if store1.help==True:
            waiting+=len(store1.line)-1
                
    waiting_per_consumer=round(waiting*60/person)
    statistics=f"{person} consumers vere served, total waiting time was {waiting} minutes long = {waiting_per_consumer} seconds per consumer "
    print (statistics)


if __name__=="__main__":
    main()