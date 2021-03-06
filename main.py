from random import randint, choice

class Store:
    def __init__(self,hour:int,minute:int,line:list,help:bool):
        """_summary_
        The constructor store class.

        Args:
            hour (int): The hour of a clock
            minute (int): The minute of a clock
            line (list): How many people are queueing for help in the store
            help (bool): True if someone is getting help at the moment False otherwise
        """
        self.hour=hour
        self.minute=minute
        self.line=line
        self.help=help

    def new_time(self):
        self.minute+=1
        if self.minute==60:
            self.hour+=1
            self.minute=0      


    def add_to_line(self,n,):
        """ Adds a person to the queue, will also write when said person came into the queue

        Args:
            n (Int): n is a variabel for the amount of people who have came into the queue
        """
        self.line.append(Person(f"Person {n}",task()))
        if self.minute<10 and self.hour<10:
            print(f"{self.line[-1].name} arrived at the time 0{self.hour}:0{self.minute} with {self.line[-1].tasks} tasks in place {len(self.line)}\n")
        elif self.hour<10: 
                print(f"{self.line[-1].name} arrived at the time 0{self.hour}:{self.minute} with {self.line[-1].tasks} tasks in place {len(self.line)}\n")
        elif self.minute<10:
            print(f"{self.line[-1].name} arrived at the time {self.hour}:0{self.minute} with {self.line[-1].tasks} tasks in place {len(self.line)}\n") 
        else:
                print(f"{self.line[-1].name} arrived at the time {self.hour}:{self.minute} with {self.line[-1].tasks} tasks in place {len(self.line)}\n")


    def the_queue(self):
        """ This function works as the queue and will check how many tasks the person 
        getting help needs help with and remove 0.5 tasks per time the function is called
        if said task goes down to 0 it will be removed from the queue
        """
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
    def __init__(self,name:str,tasks:int) -> None:
        """ Constructor for person class

        Args:
            name (str): Name of each person
            tasks (int): How many tasks each person has 
        """
        self.name=name
        self.tasks=tasks

def task():
    task=[3,3,2,2,2,2,1,1,1,1,1,1,1,1]
    return choice(task)

def save(q):
    """ Saves the string in the text file called "stats.txt"

    Args:
        q (str): The string that we will save
    """
    with open ("stats.txt","a",encoding="utf8") as f:
        f.write(f"{q}\n")

def stat(waiting,person):
    """ Calculates the statistics of the people who have been in the store so far (if used at the end will show total stats of the day)

    Args:
        waiting (int): How much total amount of time people have waited so far
        person (int): The total amount of people who have 

    Returns:
        str: The string with the statistical information
    """
    waited_sec=round(waiting*60
                            /person)
    results=f"{person} consumers vere served, total waiting time was {waiting} minutes long = {waited_sec} seconds per consumer "
    return results

def main():
    person=0
    waiting=0
    store1=Store(9,0,[],False)

    while store1.hour<18 or len(store1.line)>0:
        store1.new_time()

        if randint(0,100)<=20 and not store1.hour>=18:
            person+=1
            store1.add_to_line(person)

        store1.the_queue()
        if store1.help==True:
            waiting+=len(store1.line)-1
                
    print (stat(waiting,person))
    save(stat(waiting,person))


if __name__=="__main__":
    main()
