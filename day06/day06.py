import csv

NUMBERS = []
CALCULATED = []

def read_csv():
    global NUMBERS
    print(f"Read file...")
    matrix = []

    with open("test.csv", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            matrix.append(line.split())

    # pivot
    NUMBERS = list(map(list, zip(*matrix)))
    #print(f"NUMNBERS={NUMBERS}")

def calc():
    global NUMBERS, CALCULATED
    ADDITI = '+'
    MULTIPLI = '*'
    
    print(f"calculating...")
    for arrays in NUMBERS:
        operator = arrays[(len(arrays)-1)]
        result = None
        if(operator == ADDITI):
            result = 0
        elif(operator == MULTIPLI):
            result = 1
        else:
            print(f"Invalid operator={operator}")
            return
        
        arrays.remove(operator)
        #print(f"arrays={arrays}")
        for digit in arrays:
            #print(f"digit={digit}")
            number = int(digit)
            if(isinstance(number, int)):
                if(operator == ADDITI):
                    result += number
                elif(operator == MULTIPLI):
                    result *= number
                else:
                    print(f"Invalid operator={operator}")
        
        CALCULATED.append(result)
    
    print(f"CALCULATED={CALCULATED}")
    
def welcome():
    print("Welcom on 6. day!") 
    
### MAIN ###
welcome()
read_csv()

print(f"NUMBERS={NUMBERS}")

calc()

print(f"password is={sum(CALCULATED)}")
# password is 3525371263915

