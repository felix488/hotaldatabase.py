import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Felix@2001",
    database="hotal_taj_db"
)
mycursor=mydb.cursor()

class grandpalace:
    def __init__(self,rt='',s=0,r=0,a=1000,name='',address='',booking_date='',depature_data='',room_number=''):
       print ("\n*************WELCOME TO HOTEL TAJ ********\n") 
       
       self.rt=rt
       
       self.r=r
       self.s=s
       self.a=a
       self.name=name
       self.address=address
       self.booking_data=booking_date
       self.depature_data=depature_date    
       self.room_number=room_number
       
    def inputdata(self):
        self.name=input("\nenter your name:").strip().lower() 
        self.address=input("\n enter your address:").strip().lower()
        self.booking_date=input("\n enter your book the date:").strip()
        self.room_number=int(input("enter your room number.:"))
        
        x="insert into detailes(name,address,booking_date,depature_date,room_number)values(%s,%s,%s,%s,%s)"
          
        y=(self.name,self.address,self.booking_date,self.depature_date,self.room_number)
        mycursor.execute(x,y)
        mydb.commit()
        
        
    def room_rent(self):
        print("we have the fellowings rooms for you:-")
        
        print("1.  first_class------->rs 200000 pn\-")
        
        print("2.  second_class------->rs 12000 pn\-")
        
        print("3.  third_class-------->rs 80000 pn\-")
        
        print("4.  fourth_class-------->rs 5000 pn\-")
        
        print("5.  fifth_class--------->rs 3000 pn\-")
        
        print("6.  local_class--------->rs 1000 pn\-")
        
        
        x=int(input("enter your room for the fellowing classes-->"))
        n=int(input("enter the number of staying days:"))
        
        if(x==1):
            
            print("you may choose first_class")
            
            self.s=20000*n
            
        elif (x==2):
            print("you may choose second_class")
            
            self.s=12000*n
            
        elif (x==3):
            print("you may choose third_class")
            
            self.s=8000*n
            
        elif (x==4):
            print("you may choose fourth_class")
            
            self.s=5000*n
            
        elif (x==5):
            print("you may choose fifth_class") 
            
            self.s=3000*n
        elif(x==6):
            print("you may choose local_class")
            
            self.s=1000*n
            
        else:
            print("please choose the room")
        print("your room rent is =",self.s,"\n")    
        
    def restaurentbill(self):
        print("$$$$$$$$RESTAURANT MENU$$$$$$$$$$")
        
        print("1.tea--->10","2.coffee--->15","3.water--->20","4.breakfast_comboo--->100","5.lunch_comboo--->150","6.dinner_comboo--->200")
        
        while(1):
            
            b=int(input("enter your choice:"))
            
            if (b==1):
                d=int(input("enter the quantity:"))
                self.r=self.r+10*d
                
                
            elif(b==2):
                d=int(input("enter the quantity:"))
                self.r=self.r+15*d
                
                
            elif(b==3):
                d=int(input("enter the quantity:"))
                self.r=self.r+20*d
                
            elif(b==4):
                d=int(input("enter the quantity:"))
                self.r=self.r+100*d
            elif(b==5):
                d=int(input("enter the quantity:"))
                self.r=self.r+150*d
                
            elif(b==6):
                d=int(input("enter the quantity:"))
                self.r=self.r+200*d
                
            elif(b==7):
                break;
            else:
                print("invalid option")
                
                print("total food cost=Rs",self.r,"\n")
                
                
                
                
    def display(self):
        
        print("*********HOTEL BILL***********")
        print("customer details:")
        print("customer name:",self.name)
        print("customer address:",self.address)
        print("check in date:",self.booking_date)
        print("check out date:",self.depature_date)
        print("room_number:",self.room_number)
        print("your room rent is:",self.s)
        print("your food bill is",self.r)
        
        
        self.rt=self.s+self.r
        
        print("your sub total bill is:",self.rt)
        print("additional service charges is",self.rt)
        print("your grandtotal bill is:",self.rt+self.a,"\n")
        
    def main():
        
        a=grandpalace()
        
        
        
        while (1): 
            print("1.enter customer data")
            
            print("2.calculate roomrent")
            
            print("3.calculate restaurant bill")
            
            print("4.show total cost")
            
            print("5.exit")
            
            
            j=int(input("\nenter your choice:"))
            if (j==1):
                a.inputdata()
                
            if (j==2):
                
                a.roomrent()
                
            if (j==3):
                
                a.resturentbill()
                
            if (j==4): 
                
                a.display()
                
            if (j==5):
                
                quit()
                
main()                               
            
                
                                                      
                    
                         
                        