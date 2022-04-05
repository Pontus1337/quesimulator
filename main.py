



class Store:
    def __init__(self,hour:int,minute:int,line:list) -> None:
        self.hour=hour
        self.minute=minute
        self.line=line

    def New_Hour(self):
        self.hour+=1
        self.minute=0

    def Tell_Time(self):

        if self.minute<10 and self.hour<10:
           print(f"Time 0{self.hour}:0{self.minute}")
        elif self.hour<10: 
           print(f"Time 0{self.hour}:{self.minute}")
        elif self.minute<10:
           print(f"Time {self.hour}:0{self.minute}") 
        else:
            print(f"Time {self.hour}:{self.minute}")

def main():
    store1=Store(9,0,[])
    print("hej")
    while store1.hour<18:
        store1.minute+=1
        if store1.minute%60==0:
            store1.New_Hour()
        store1.Tell_Time()




if __name__=="__main__":
    main()