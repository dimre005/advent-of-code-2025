import csv

BATTERIES = []
JOLTAGES = []

def read_csv():
    with open("test.csv", "r", encoding="utf-8") as f:
        BATTERIES = [line.strip() for line in f]
    return BATTERIES


def search_max_item(batteries):
    print(f"batteries", batteries)   
    for index in range(len(batteries)):
        battery = batteries[index]
        max_item = get_max_item_top_n(battery, 2, {})      
        JOLTAGES.append(ordering(max_item))        
    
def ordering(map):
    sorted_map = dict(sorted(map.items(), key=lambda item: item[0]))
    print(f"sorted_map={sorted_map}")

    all_keys = ''.join(sorted_map.values())

    return int(all_keys)


def get_max_item_top_n(string, limit, result, start=0, iteration=0):
    if(limit == iteration):
        return result

    item_max = string[start]
    index_max = start
    
    for index in range(start, len(string)):
        if(iteration > 0 and is_contains_key(index, result) == True):
            continue
               
        if(int(string[index]) == 9):
            item_max = str(string[index])
            index_max = int(index)
            break
        
        if(int(item_max) < int(string[index])):
            item_max = str(string[index])
            index_max = int(index)
    
    result[index_max] = item_max
    iteration+=1
    if(len(string) == index_max+1):
        start = 0
        
    else:
        start = index_max+1
    
    #print(f"result={result}, start={start}")
    return get_max_item_top_n(string, limit, result, start, iteration)


def is_contains_key(index, map):
    is_contains = index in map
    return is_contains


def get_max_item(array, iteration, max_value, execute_count=0, start=0):
    if(iteration == execute_count):
        return max_value
    
    item_max = array[start]
    index_max = start

    for index in range(start, len(array)):       
        if(int(item_max) == 9):
            break
        
        if(int(item_max) < int(array[index])):
            item_max = array[index]
            index_max = index
            print(f"item_max={item_max}; index_max={index_max}")
    
    max_value[item_max] = index_max
    print(f"max_value={max_value}")

    if(index_max == 0):
        array = array[1:]
        start = 0
    elif(len(array) == index_max+1):
        array = array[:-1]
        start = 0
    else:
        array = array[:index_max-2] + array[index_max+1:]
        start = index_max-2
    
    execute_count+=1
    return get_max_item(array, iteration, max_value, execute_count, start)   
        
        
def welcome():
    print("Welcom on 3. day!")

### MAIN ###
welcome()
batteries = read_csv()
search_max_item(batteries)

# result
print(f"JOLTAGES={JOLTAGES}")
print(f"password is {sum(JOLTAGES)}")

# addition=134216 #That's not the right answer; your answer is too high.

