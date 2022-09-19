
# make "parking_garage" class:
class ParkingGarage():
    # should have some attributes:
    tickets = ["parking ticket"]
    parking_spaces = ["parking space"]

    def __init__(self, current_ticket):
        current_ticket_paid = False
    # class should have the following methods:
    # takeTicket:
    def take_ticket():      
        # should dec. ticket count by 1
        ParkingGarage.tickets.remove("parking ticket")
        # should dec. parking space by 1
        ParkingGarage.parking_spaces.remove("parking space")
        print("Thank you! Remember, you have to pay for your ticket before you can leave!")
    # payForParking:
    def pay_for_parking():
        parking_cost = 5
        # should wait for user input, then store
        # it in a variable.
        # if paid, tell user they have 15 minutes to leave
        while True:
            cost = input(f"The cost of each ticket is ${parking_cost}. Pay here: ").lower().strip()
            if cost == "5":
                print("You have 15 minutes to leave the garage.")
                current_ticket_paid = True
                break
            # if not paid ask again for payment until user pays.
            else:
                print("That's not the correct amount.")
    # leaveGarage:
    def leave_garage():
        print("Thank you! Have a nice day!")
        # should inc. ticket count by 1
        ParkingGarage.tickets.append("parking ticket")
        # should inc. parking space by 1
        ParkingGarage.parking_spaces.append("parking space")


class Main():
    def start_program():
        while True:
            response = input('''Welcome to the Parking Garage! You can:
            Get Ticket
            Leave
            ''').lower().strip()
            if response == "leave":
                if len(ParkingGarage.tickets) == 0:
                    ParkingGarage.pay_for_parking()
                ParkingGarage.leave_garage()
                break
            elif response == "get" or response == "get ticket" or response == "ticket":
                if len(ParkingGarage.tickets) != 0:
                    ParkingGarage.take_ticket()
                else:
                    print("I'm sorry, but we're out of parking spaces. Please come back at a later time.")
                    ParkingGarage.leave_garage()
                    break
            else:
                print("Please enter a command listed.")

Main.start_program()
