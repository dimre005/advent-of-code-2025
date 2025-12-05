import csv

DATABASE = []
INGEDIENTS = []

FRESH_IDS = []

def read_csv():
    with open("test.csv") as f:
        before_blank = True

        for line in f:
            line = line.strip()
            
            if line == "":
                before_blank = False
                continue

            if before_blank:
                x_str, y_str = line.split('-')
                DATABASE.append((int(x_str), int(y_str)))
            else:
                INGEDIENTS.append(int(line))


def find_fresh_id(database, fresh_ids):
    print(f"count fresh IDs")
    for id in fresh_ids:
        #print(f"item_id:{id}")
        for range_item in database:
            if(id < range_item[0]):
                #print(f"id kisebb mint az iteráció kezdete, nem lehet benne a tömbbe")
                continue
            elif(id > range_item[1]):
                #print(f"id nagyobb mint az iteráció vége, nem lehet benne a tömbbe")
                continue
            else:
                #print(f"itt lesz benne")
                FRESH_IDS.append(id)
                break


def find_fresh_id_part_2(database):
    print(f"count fresh IDs")
    count_fresh_ids = 0
    merge_array = get_merge_arrays(database)
    
    for range_item in merge_array:
        count_fresh_ids += (range_item[1]+1) - range_item[0]
        
    return count_fresh_ids

def get_merge_arrays(database):
    intervals = []
    merged_array = []

    for i, j in database:
        intervals.append((i, j))

    intervals.sort()
    start, end = intervals[0]

    for s, e in intervals[1:]:
        if s <= end + 1:
            end = max(end, e)
        else:
            merged_array.append((start, end))
            start, end = s, e

    merged_array.append((start, end))
    #print(f"merged={merged_array}")
    
    return merged_array

def welcome():
    print("Welcom on 5. day!") 

### MAIN ###
welcome()
read_csv()

#rint(f"DATABASE={DATABASE}")
#print(f"INGEDIENTS={INGEDIENTS}")

#find_fresh_id(DATABASE, INGEDIENTS)

#print(f"password is={len(FRESH_IDS)}")

count_fresh_ids = find_fresh_id_part_2(DATABASE)

print(f"password2 is={count_fresh_ids}")
## password2 is 359913027576322
## password is 840


