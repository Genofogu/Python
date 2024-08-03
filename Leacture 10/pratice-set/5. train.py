#Write a class train which have a method to book a ticket, get status (no of seats) and get fare inm=formation of train running under indian railways

class train:
    def __init__(self) -> None:
        self.seat = 75
        self.fare = 120
    
    def bookTiket(self):
        
        self.seat -= 1       #after tiket get booked from indian railway servers
    
    def getStatus(self):
        print(self.seat)
    
    def getFareInformation(self):
        print(self.fare)
        
aman = train()
aman.getFareInformation()
aman.getStatus()
aman.bookTiket()
aman.getStatus()
    