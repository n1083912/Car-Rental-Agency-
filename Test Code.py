class Car(object):
    def __init__(self, CarName, CarColour,CarSeats,CarDoors,CarGears,CarLP,CarMile,CarDayPrice,CarRentalDate):
        self.CarName = str(CarName)
        self.CarColour = str(CarColour)
        self.CarSeats = str(CarSeats)
        self.CarDoors = str(CarDoors)
        self.CarGears = str(CarGears)
        self.CarLP = str(CarLP)
        self.CarMile = str(CarMile)
        self.CarDayPrice = str(CarDayPrice)
        self.CarRentalDate = str(CarRentalDate) 
        
Car1 = Car("Honda Civic", "blue","5","5","Manual","j85409","150000","20","25/11/23")
Car2 = Car("Ford Focus", "Green","5","5","Manual","p32516","350000","40","30/11/23")
Car3 = Car("Ford Fiesta", "Orange","5","5","Manual","u76515","5000","25","20/12/23")
Car4 = Car("Fiat 500", "Grey","5","3","Manual","p84712","10000","25","10/12/23")
Car5 = Car("Vauxhall corsa", "White","5","5","Manual","u834914","20000","30","20/1/24")
Car6 = Car("Kia Sportage","Brown","5","5","Manual","l902311","15000","50","N/A")
Car7 = Car("Skoda Suberp","White","5","5","Automatic","u456809","100000","50","N/A")
Car8 = Car("Ford Mondeo","Black","5","4","Automatice","lhk58411","10000","50","N/A")
Car9 = Car("Skoda Octavia Combi","black", "5","4","Manual","ptr50310","20000","60","N/A")
Car10 = Car("Kia Xceed","Black", "5","4","Manual","u73809","100000","60","21/12/23")
Car11 = Car("Mercedes CLA","White","5","5","Automatic","o391317","20000","70","22/12/23")
Car12 = Car("BMW 3 Series", "Blue","5","5","Automatic","o589112","30000","70","N/A")
Car13 = Car("Vauxhall Mokka","Green","5","5","Manual", "p289113","10000","100","N/A")
Car14 = Car("Niss Qashqai","Orange","5","5","Manual","T382112","10000","100","N/A")
Car15 = Car("Kia Sportage","Blue","5","5","Manual","l732682","500","120","N/A") 
textFile = open("cars.txt", "a")
allCars = (Car1,Car2,Car3,Car4,Car5,Car6,Car7,Car8,Car9,Car10,Car11,Car12,Car13,Car14,Car15)
textFile.write(Car1.CarName-.CarRentalDate) 
textFile.close()
print("Welcome to the Car Agency python code!")
userReply = input("0 = See full of rentable cars\n 1 = Filter list of rentable cars\n  2 = Exit\n")
if userReply == 1:
    print(Car1)
if userReply == 2:
    filter = input("What would you like to filter it by?\n
    
