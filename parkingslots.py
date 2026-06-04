class SlotoccupiedError(Exception):
    pass
class InvalidSlotError(Exception):
    pass
parking_slots=[None]*5
try:
    while None in parking_slots:
        vehicle_number=input("Enter Vehicle Number: ")
        slot_number=int(input("Enter the slot number: "))

        if slot_number<1 or slot_number>5:
            raise InvalidSlotError("Slot number must be between 1 and 5")
        if parking_slots[slot_number-1] is not None:
            raise SlotoccupiedError("Your slot is already occupied!!")
        parking_slots[slot_number-1]=vehicle_number
        print("\nVehicle Parked Successfully!")
        print("Parking Status:")
        for i in range(len(parking_slots)):
            if parking_slots[i]:
                print(f"Slot {i+1}:{parking_slots[i]}")
            else:
                print(f"Slot {i+1}: Empty")
    print("All slots are full")
except ValueError:
    print("Please enter a valid slot number")
except InvalidSlotError as e:
    print("Invalid Slot Error: ",e)
except SlotoccupiedError as e:
    print("Parking Error:",e)
finally:
    print("\nParking Transaction Completed.")