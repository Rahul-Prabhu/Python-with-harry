'''
1 2 3 4 5 6 7 8 9 10
'''

class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print("************")
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train are {len(self.seats)}")
        print("************")

    def fareInfo(self):
        print(f"The price of the ticket is: Rs {self.fare}")

    def bookTicket(self,seatno):
        self.seatno=seatno
        if(len(self.seats)>0):
            print(f"Your ticket has been booked! Your seat number is {self.seatno}")
            self.seats.remove(self.seatno)
        else:
            print("Sorry this train is full! Kindly try in tatkal")

    def cancelTicket(self, seatNo):
        self.seats.append(seatNo)

intercity = Train("Intercity Express: 14015", 90, [1,2,3,4,5,6,7,8,9,10])
intercity.getStatus() 
intercity.bookTicket(8)
intercity.bookTicket(9)
intercity.cancelTicket(4)
intercity.cancelTicket(11)
# intercity.bookTicket()
# intercity.bookTicket()
intercity.getStatus()