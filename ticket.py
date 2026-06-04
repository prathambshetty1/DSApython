class TicketLimitError(Exception):
    pass
available_tickets=50
try:
    tickets=int(input("Enter the number of tickets to book: "))
    if tickets<=0:
        raise ValueError("Number of tickets must be greater than 0")
    if tickets>available_tickets:
        raise TicketLimitError(f"Only {available_tickets} are available")
    available_tickets-=tickets
    print("Booking successfull")
except TicketLimitError as e:
    print("Ticket Limit Reached: ",e)
except ValueError as e:
    print("Value Error: ",e)
finally:
    print("Booking successful")