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
    def __str__(self):
        return (self.CarName + ", " + self.CarColour + ", " + self.CarSeats + ", " + self.CarDoors + ", " + self.CarGears + ", " + self.CarLP + ", " + self.CarMile + ", " + self.CarDayPrice + ", " + self.CarRentalDate)

def filterCars(cars,name=None,colour=None,seats=None,gearType=None,maxMiles=None,maxPrice=None):
    filterCars = cars

    if name:
        filterCars = [car for car in filterCars if car.CarName.lower() == name.lower()]
    if colour:
        filterCars = [car for car in filterCars if car.CarColour.lower() == colour.lower()]
    if seats:
        filterCars = [car for car in filterCars if int(car.CarSeats) == int(seats)]
    if gearType:
        filterCars = [car for car in filterCars if car.CarGears.lower() == gearType.lower()]
    if maxMiles:
        filterCars = [car for car in filterCars if int(car.CarMile) == int(maxMiles)]
    if maxPrice:
        filterCars = [car for car in filterCars if int(car.CarDayPrice) == int(maxPrice) ]
    return filterCars

allCars = [    
    Car("Honda Civic", "blue","5","5","Manual","j85409","150000","20","25/11/23"),
    Car("Ford Focus", "Green","5","5","Manual","p32516","350000","40","30/11/23"),
    Car("Ford Fiesta", "Orange","5","5","Manual","u76515","5000","25","20/12/23"),
    Car("Fiat 500", "Grey","5","3","Manual","p84712","10000","25","10/12/23"),
    Car("Vauxhall corsa", "White","5","5","Manual","u834914","20000","30","20/1/24"),
    Car("Kia Sportage","Brown","5","5","Manual","l902311","15000","50","N/A"),
    Car("Skoda Suberp","White","5","5","Automatic","u456809","100000","50","N/A"),
    Car("Ford Mondeo","Black","5","4","Automatice","lhk58411","10000","50","N/A"),
    Car("Skoda Octavia Combi","black", "5","4","Manual","ptr50310","20000","60","N/A"),
    Car("Kia Xceed","Black", "5","4","Manual","u73809","100000","60","21/12/23"),
    Car("Mercedes CLA","White","5","5","Automatic","o391317","20000","70","22/12/23"),
    Car("BMW 3 Series", "Blue","5","5","Automatic","o589112","30000","70","N/A"),
    Car("Vauxhall Mokka","Green","5","5","Manual", "p289113","10000","100","N/A"),
    Car("Niss Qashqai","Orange","5","5","Manual","T382112","10000","100","N/A"),
    Car("Kia Sportage","Blue","5","5","Manual","l732682","500","120","N/A") ]

textFile = open("Cars.txt", "w")
textFile.write("Car's model, Number of seats, Number of doors, Car Gear Type, Car License Plate, Car Mileage, Car's Price per day, Car's date rented until\n")
for car in allCars:
    textFile.write(str(car) + "\n")
textFile.close()

pickCar = None
print("Welcome to the Car Agency python code, please select a option!")
mainAnswer = input("0 = Unfiltered list of all cars\n1 = Filtered list of all cars\n2 = All rentable cars\n")
if mainAnswer == "0":
    for car in allCars:
        print(car)
    pickCar = input("Please type in the name of the car you would like to rent\n")
    
if mainAnswer == "1":
    colour = None
    seats = None
    gearType = None
    maxMiles = None
    maxPrice = None
    filterType = input("What would you like to filter by?\n0 = Colour\n1 = Seats\n2 = Gears\n3 = Max mileage\n4 = max price?\nor type done if your done\n")
    while filterType.lower() != "done": 
        while filterType == "0":  
            colour = input("Enter color: ")
            filterType = input("Do you want to filter by another attribute?\n0 = Colour\n1 = Seats\n2 = Gears\n3 = Max mileage\n4 = max price?\nor type done if your done\n")
        while filterType == "1":
            seats = input("Enter number of seats: ")
            filterType = input("Do you want to filter by another attribute?\n0 = Colour\n1 = Seats\n2 = Gears\n3 = Max mileage\n4 = max price?\nor type done if your done\n")
        while filterType == "2":
            gearType = input("Enter gear type (manual/automatic): ")
            filterType = input("Do you want to filter by another attribute?\n0 = Colour\n1 = Seats\n2 = Gears\n3 = Max mileage\n4 = max price?\nor type done if your done\n")
        while filterType == "3":
            maxMiles = input("Enter max mileage: ")
            filterType = input("Do you want to filter by another attribute?\n0 = Colour\n1 = Seats\n2 = Gears\n3 = Max mileage\n4 = max price?\nor type done if your done\n")
        while filterType == "4":
            maxPrice = input("Enter max price per day: ")
            filterType = input("Do you want to filter by another attribute?\n0 = Colour\n1 = Seats\n2 = Gears\n3 = Max mileage\n4 = max price?\nor type done if your done\n")
    if filterType.lower() == "done":
        filteredCars = filterCars(allCars, colour, seats, gearType, maxMiles, maxPrice)
        if filteredCars:
            print("Filtered results:\n")
            for car in filteredCars:
                print(car)
                pickCar = input("Please type in the anme of the car you would like to rent\n")
                break
        else:
            print("Im sorry but nothing matches that searching criteria, please restart the application to retry.")
if mainAnswer == "3":
    for car in allCars:
        if car.CarRentalDate == "N/A":
            print(car)
            pickCar = input("Please type in the name of the car you would like to rent\n")

if pickCar != None:
    for car in allCars:
        if car.CarName.lower() == pickCar.lower():
            print("Your chosen Car is ", car.CarName)
            print("It has ", car.CarSeats, "seats\n",car.CarGears, "gears\n",car.CarMile, "Miles")
            rentTime = int(input("How long would you like to rent this car in days?"))

            if rentTime > 14:
                DailyRentPrice = rentTime * float(car.CarDayPrice)
                print(DailyRentPrice * 1.2)
            else:
                DailyRentPrice = rentTime * float(car.CarDayPrice)
                print(DailyRentPrice * 1.8)
                ReceiptFile = open(receipt.txt, "w")
                recepitFile.write("")

            break
            


        
    
