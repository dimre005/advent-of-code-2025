import csv

DIAL_POINTS = []

def read_csv():
    with open("test.csv", "r", encoding="utf-8") as f:
        DIRECTIONS = [line.strip() for line in f]
    return DIRECTIONS

def calc(pointer, direction):
    letter = direction[0]
    value = int(direction[1:])     
    result = None;
    
    value = check(value)
    
    # subtraction 
    if(letter == 'L'):
        if(pointer-value < 0):
            if(pointer != 0):
                DIAL_POINTS.append(0)
                
            result = rotation(pointer-value)
        else:
            result = pointer - value
            
    # addition
    elif(letter == 'R'):
        if(pointer+value == 100):
            result = 0
        elif(pointer+value > 99):
            if(pointer != 0):
                DIAL_POINTS.append(0)
            
            result = rotation(pointer+value)
        else:
            result = pointer+value
    else:
        print("Invalid direction!")
    
    return result


def rotation(value):
    if(value < 0):
        return 100 - abs(value)
    elif(value > 100):
        
        return value - 100
    else: return value

def check(value):
    count_rotations = value // 100
    if(count_rotations > 0):
        DIAL_POINTS.extend([0] * count_rotations)
        return value % 100
    else:
        return value

def do_spin(array, start_pointer):
    actual_pointer = start_pointer
    for direction in array:
        print(f"The dial is rotated {direction} to point at {actual_pointer}.")
        actual_pointer = calc(actual_pointer, direction)
        DIAL_POINTS.append(actual_pointer)

def welcome():
    print("Welcom on 1. day!")

### MAIN ###
welcome()
array = read_csv()

do_spin(array, 50)

#correct password is 1100
#correct Password is: 6358
print(f"Password is:", DIAL_POINTS.count(0))

## too low 5248
## too high 6822
## too high 6917
