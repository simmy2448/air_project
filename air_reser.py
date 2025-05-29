class abc_airline:
    print("*************Welcome to ABC Airline*************")
class flight:
    def __init__(self,f_number,origin,destination,depart_time,arrival_time,price):
        self.flight_number= f_number
        self.origin = origin
        self.destination = destination
        self.departure_time = depart_time
        self.arrival_time = arrival_time
        self.price = price
    def f_info(self):
        return f"Flight {self.flight_number}:from {self.origin} to {self.destination} at Rs.{self.price}"

class passenger:
    def __init__(self,name,age,pass_number,contact):
        self.name = name
        self.age = age
        self.passport_number = pass_number
        self.contact = contact

    def p_info(self):
        return f"{self.name} (Passport: {self.passport_number})"

    


class booking:
    def __init__(self,flight,b_number,passenger,b_date):
        self.flight =flight
        self.booking_number=b_number
        self.passenger=passenger
        self.booking_date= b_date

    def b_info(self):
        return f"Booking {self.booking_number}: {self.passenger.name} on {self.flight.flight_number}"

    


class airline:
    def __init__(self):
        self.flights=[]
        self.passengers=[]
        self.bookings=[]
    
    def add_flight(self,flight):
        self.flights.append(flight)
    def add_passenger(self,passenger):
        self.passengers.append(passenger)
    def add_booking(self,booking):
        self.bookings.append(booking)

    def view_flight(self):
        for flight in self.flights:
            print(flight.f_info())
    def view_passenger(self):
        for passenger in self.passengers:
            print(passenger.p_info())
    def view_booking(self):
        for booking in self.bookings:
            print(booking.b_info())

    

abc_airline=airline()
flight1=flight("SS606","Amritsar","Canada","04:00","12:00",70000)
abc_airline.add_flight(flight1)
passenger1=passenger("Param",30,"S123456","7856241332")
abc_airline.add_passenger(passenger1)
booking1=booking(flight1,"S606",passenger1,"29-05-2025")
abc_airline.add_booking(booking1)
abc_airline.view_flight()
abc_airline.view_passenger()
abc_airline.view_booking()


    