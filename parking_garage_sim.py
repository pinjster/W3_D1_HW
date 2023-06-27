from time import process_time

class ParkingGarage():
    ticket_no = 0
    tickets = [True for x in range(0,50)]
    parking_spaces = ['1' for x in range(0,50)]
    current_ticket = {
        'ticket_number' : 0,
        'paid' : False,
        'time_in' : 0,
    }

    def __init__(self):
        self.current_ticket

    def take_ticket(self): 
        ParkingGarage.ticket_no += 1
        self.current_ticket['ticket_number'] = ParkingGarage.ticket_no
        for x in ParkingGarage.parking_spaces:
            if x == '1':
                self.parking_index = ParkingGarage.parking_spaces.index(x)
                x = '0'
                break
        ParkingGarage.tickets[self.parking_index] = False
        self.timer_start = process_time()
        self.current_ticket['time_in'] = self.timer_start

    def pay_for_parking(self):
        fee = self.calculate_fee()
        if self.current_ticket['paid'] == True:
            print("Payment already confirmed: You must leave the premises within 15 minutes")
        else:
            while True:
                payment = input(f"Credit/Debit: Your total is ${(format(fee, '.2f'))} . Enter payment amount here: $")
                try:
                    if payment == (format(fee, '.2f')):
                        print("Thank you, have a nice day!")
                        self.current_ticket['paid'] = True
                        break
                except:
                    print("Invalid amount. Must match fee")
    def leave_garage(self):
        if self.current_ticket['paid'] == True:
            print("Thank you, have a nice day!")
            ParkingGarage.parking_spaces[self.parking_index] = '1'
            ParkingGarage.tickets[self.parking_index] = True
            return
        else:
            self.pay_for_parking()

    def calculate_fee(self):
        self.timer_stop = process_time()
        return float((self.timer_stop - self.timer_start) * 0.005)

    def driver_function(self):
        print("Welcome to the Maxtrix Parking Garage: We've been waiting for you.")
        while True:
            choice =  input("Will you take the ticket? Y/N ").lower()
            if choice == 'y':
                print("You took the ticket. Woah.. ")
                self.take_ticket()
                break
            elif choice == 'n':
                print('"I can only show you the door. You are the one who has to walk through it" (you left)')
                return
            else:
                print("That's not an option - Please try again")
                continue
        while True:
            choice =  input("Would you like to 'pay' or 'leave'? ").lower()
            if choice == 'pay':
                print("You took the ticket. Woah.. ")
                self.pay_for_parking()
                continue
            elif choice == 'leave':
                self.leave_garage()
                print("You've made it out of the Matrix.. Parking Building")
                break
            else:
                print("That's not an option - Please try again")
                continue

while True:
    new_driver = ParkingGarage()
    choice = input("Would you like to approach the Matrix Parking Garage? Y/N ")
    if choice == 'y':
        print("You approach.. ")
        new_driver.driver_function()
        continue
    elif choice == 'n':
        print('"I can only show you the door. You are the one who has to walk through it" (you left)')
        break
    else:
        print("That's not an option - Please try again")
        continue
