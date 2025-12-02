import csv

PRODUCT_IDS = []
INVALID_IDS = []

def read_csv():
    PRODUCT_IDS = []
    with open("input.csv", "r", encoding="utf-8") as f:
        for line in f:
            parts = [x for x in line.strip().split(",") if x]
            PRODUCT_IDS.extend(parts)
    return PRODUCT_IDS

def check_invalid(array):
    for ids in array:
        min_number = int(ids.split('-')[0])
        max_number = int(ids.split('-')[1])
        for number in range(min_number, max_number+1):
            if(is_invalid_number(number) == True):
                INVALID_IDS.append(number)


def is_invalid_number(number):   
    if((number // 10) == 0):
        return False

    digits = [int(d) for d in str(number)]
    if(len(set(digits)) == 1):
        return True
    
    return is_repeated(digits)

def is_repeated(digits):
    size = int(len(digits))
    if(size < 4):
        return False
    else:
        return search_splitting(digits, size, 2)
        
def search_splitting(digits, size, divider):
    if(size % divider == 0):
        splitting_arrays = create_array(digits, divider)
        first = splitting_arrays[0]
        if all(part == first for part in splitting_arrays):
            return True
    
    if(int(size / 2) < divider):
        return False

    return search_splitting(digits, size, divider + 1)
        
def create_array(array, divider):
    size = len(array) // divider
    return [array[i*size:(i+1)*size] for i in range(divider)]
    

def welcome():
    print("Welcom on 2. day!")
    
### MAIN ###
welcome()
array = read_csv()
check_invalid(array)

print(f"invalid numbers=", INVALID_IDS)
print(f"sum array item values=", sum(INVALID_IDS))
# extra     73 694 270 688

#           54 641 809 925
## too high 54 649 812 253