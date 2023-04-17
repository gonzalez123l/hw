class Parking_Garage:
    def __init__(self):
        self.tickets_availble = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.parking_available = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.paid = {'paid': False,
                            'ticket': None
                            }


    def issue_ticket(self):
        enter_garage = input(
            "Would you like to enter the garage? (y/n):").lower()
        if enter_garage == "y":
            if self.tickets_availble:
                ticket = self.tickets_availble.pop()
                self.paid['ticket'] = ticket
                print(f"Your ticket number is {ticket}. Please pay $5.00")
            else:
                print("No more tickets available at this time.")
        else:
            print("If you still need a spot, we'll be here.")
            return
        
        
    def paying_ticket(self):
        take_payment = input("Please enter payment amount.")
        payment = float(take_payment)
        if payment >= 5.0:
            change = payment - 5.0
            print(f"Your payment has been received. Please leave in the next 15 minutes.")
            self.paid['paid'] = True


    def leave_garage(self):
        if self.paid['paid'] == True:
            print("Thank you, have a nice day!")
            self.paid['paid'] = False
            self.parking_available.append(self.paid['ticket'])
            self.paid['ticket'] = None
        else:
            print("Payment is now due")
            payment_due = input("Please pay $5.00")
            payment = float(payment_due)
            if payment:
                print(
                    "Your payment has been received. Please leave in the next 15 minutes.")
                self.parking_available.append(self.paid['ticket'])
                self.paid['paid'] = False
                self.paid['ticket'] = None


parking_garage = Parking_Garage()
parking_garage.issue_ticket()
if parking_garage.paid['ticket']:
    parking_garage.paying_ticket()
    parking_garage.leave_garage()