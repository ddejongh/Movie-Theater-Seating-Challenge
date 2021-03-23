# --------------------------------------------------------------------------------------------------------------------------------------------
# File: movies.py
# Author: Devin DeJongh - devindejongh@gmail.com
# Site: github.com/ddejongh 

# Description: 
#       - To read in reservation requests from a file provided via command line arguments
#         we will read the information and assign seats accordingly. 
#       - x will be used to denote a taken seat
#       - s will be used to denote an open seat 

# Assumptions: 
#       - A buffer of three seats and one row is required
#       - A diagonal distance of one is good enough 
# --------------------------------------------------------------------------------------------------------------------------------------------
import sys  # used for command line arguments 
import os 

rows = {
    0: 'A',
    1: 'B',
    2: 'C',
    3: 'D',
    4: 'E',
    5: 'F',
    6: 'G',
    7: 'H',
    8: 'I', 
    9: 'J' 
}

seats = []
file_str = [] 
reservations = {}
marker = [0,0] 
fail_flag = False 

class Reservation:
    def __init__(self, id, num_seats):
        self.id = id
        self.num_seats = num_seats
        self.assignments = ""

    def set_assignments(self, labels):
        self.assignments = labels 

"""
This function will be used to generate the chart for seating.
"""
def create_seating():
    seats.append([])
    for i in range(20):
        seats.append([])
        for j in range(20):
            seats[i].append('s')

"""
Utility print theater function
"""
def print_grid():
    for i in range(10):
        for j in range(20):
            print(seats[i][j], end=' ')
        print()


"""
Look for the next empty spot in the seating chart. 
""" 
def open_seating(amount, reservation_instance):
    open_return = False 
    row = marker[0]
    col = marker[1]

    while row < 10:
        while col < 20:
            if(seats[row][col] == 's'):
                if(seats_available(amount, row, col)):
                    left = col 
                    right = left + amount - 1 
                    if not safe_location(amount, row, left, right):
                        col += 1 
                        continue
                    update_grid(amount, row, left)
                    update_reservation(amount, row, left, reservation_instance)
                    open_return = True 
                    marker[0] = row
                    marker[1] = right 
                    
                return open_return
            col += 1
            # marker[0] += 1
        col = 0 
        row += 1

    return open_return 

"""
Check if there is enough space at the newest location
"""
def seats_available(amount, row, col) -> bool:
    left = col
    right = left + amount - 1

    if right > 19:
        return False 

    for j in range(amount):
        if seats[row][col+j] == 'x':
            return False 
        #print('Seat found at {0} , {1}'.format(row, col+j))

    #print('location is safe')
    return True 


"""
Check horizontal and vertical spacing
"""
def safe_location(amount, row, left, right):
    if row_is_safe(row, left, right) and vertical_is_safe(amount, row, left):
        return True 
    return False 


"""
Check if the location meets the safety requirements in the row.
"""
def row_is_safe(row, left, right) -> bool: 
    # start by check to the left
    for j in range(1,4):
        if left - j < 0:
            break
        if seats[row][left - j] == 0 and seats[row][left - j] == 's':
            break
        elif seats[row][left-j] == 'x':
            return False
    
    # check to the right 
    for j in range(1,4):
        if right + j > 19:
            break
        if seats[row][right+j] == 19 and seats[row][right + j] == 's':
            break 
        elif seats[row][right+j] == 'x':
            return False 

    return True 


"""
Check if the vertical spacing meets the safety requirements.
"""
def vertical_is_safe(amount, row, left) -> bool:
    # check above if not the first row 
    if row != 0:
        for j in range(amount):
            if seats[row-1][left+j] == 'x':
                return False 

    # check below if not the last row 
    if row != 19:
        for j in range(amount):
            if seats[row+1][left+j] == 'x':
                return False 

    return True 

"""
Once locations are checked, change these new spots to x's 
"""
def update_grid(amount, row, left): 
    for j in range(amount):
        seats[row][left+j] = 'x' 


"""
Add the seating assignments to the class object 
"""
def update_reservation(amount, row, left, reservation_instance): 
    temp = "" 
    row_name = rows[row]

    for j in range(amount):
        temp += row_name
        temp += str(left+j+1)
        temp += " "
    
    reservation_instance.set_assignments(temp)

"""
Driver function. 
"""
if __name__ == "__main__":
    create_seating()
    # print_grid() 
    
    with open(sys.argv[1], 'r') as movie_file:
        file_str = movie_file.readlines()
        movie_file.close()

    for line in file_str:
        res = line.split(' ')[0] 
        amount = int(line.split(' ')[1])
        reservations[res] = Reservation(res, amount) 

    with open('output.txt', 'w') as output:
        for key in reservations:
            amount = reservations[key].num_seats
            if not open_seating(amount, reservations[key]):
                pass
                # while(not fail_flag):
                #     if marker[0] == 9 and marker[1] == 19:
                #         fail_flag = True 
                #     open_seating(amount, reservations[key])
            output.write('{0} {1}\n'.format(reservations[key].id, reservations[key].assignments))
        output.close()
    
    print('File output to {0}/output.txt'.format(os.getcwd()))
            
    