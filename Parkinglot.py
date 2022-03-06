import sys
spaces = []
total_spaces = int(input("Enter total number of spaces: "))
avail_spaces = total_spaces
rows = int(input("Enter number of rows: "))





class Vehicle:
    def __init__(self, v_type, plate):
        self.type = v_type
        self.plate = plate

    def get_type(self):
        return self.type

    def get_type_string(self):
        return "Car" if self.type == 1 else "Truck" if self.type == 2 else "Motorcycle"

    def get_plate(self):
        return self.plate

    def get_vehicle(self):
        return self.type, self.plate

class Space:
    def __init__(self):
        self.vehicle = None
        self.occupied = False

    def add_vehicle(self, vehicle):
        self.vehicle = vehicle
        self.occupied = True

    def remove_vehicle(self):
        v_exit = self.vehicle
        self.vehicle = None
        self.occupied = False
        return v_exit

    def vehicle_info(self):
        return self.vehicle

    def is_available(self):
        return self.occupied

for i in range(total_spaces):
    
    spaces.append(Space())

    space_count = int(total_spaces / rows)

def enter_vehicle(v_type, plate, row, space):
    global spaces, avail_spaces, total_spaces, rows

    # If the lot is full
    if avail_spaces == 0:
        print("Error: No Available Spaces")
        return

    # Check if the spot is taken
    if spaces[(int(row) * space_count) + int(space)].is_available():
        print("Error: Vehicle Already In Space")
        return -1

    new_vehicle = Vehicle(v_type, plate)
    print("Vehicle Added to Lot!\n")
    avail_spaces -= 1
    return new_vehicle



def exit_lot(row, space):
    global avail_spaces

    removed = spaces[(int(row) * space_count) + int(space)].remove_vehicle()
    avail_spaces += 1
    print("Vehicle removed from the lot")

    
def command_handler(command):
    # command to park a car
    if command == "P":
        while True:
            new_type = input("Enter Vehicle Type:\n"
                             "1. Car\n"
                             "2. Truck\n"
                             "3. Motorcycle\n"
                             ">")
            if new_type == "1" or new_type == "2" or new_type == "3":
                break

        new_plate = input("Enter New Vehicle Plate Number:\n"
                          ">")
        
        ret_val = -1
        while ret_val == -1:
            while True:
                row = input("Select Row to Park In:\n"
                            ">")
                if row.isnumeric():
                    if int(row) < rows:
                        break
            while True:
                space = input("Select Space to Park In:\n"
                              ">")
                if space.isnumeric():
                    if int(space) < space_count:
                        break
            ret_val = enter_vehicle(int(new_type), new_plate, row, space) 

    # command for exiting the lot
    elif command == "E":

        while True:
            row = input("Select Row of Vehicle:\n"
                        ">")
            if row.isnumeric():
                if int(row) < rows:
                    break

        while True:
            space = input("Select Space of Vehicle:\n"
                          ">")
            if space.isnumeric():
                if int(space) < space_count:
                    break
        exit_lot(row, space)

    elif command == "Q":
        return sys.exit()

while True:        
    print("Please Select An Option:\n"
          "P - Park a Vehicle\n"
          "E - Exit the Lot\n"
          "Q - Quit Application\n")
    command = input("Enter your selection: ".upper())
    command_handler(command)

    



    
            
            




