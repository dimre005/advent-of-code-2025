import csv

rows = 0
cols = 0
matrix = {}

PAPPER_ICON = '@'
ACCESS_POINTS = []
REPLACE_POINTS = []

COUNT_REPLACE = 0


def read_csv(path="input.csv"):
    matrix = {}
    rows = 0
    cols = 0
    with open(path, "r", encoding="utf-8") as f:
        for y, line in enumerate(f):
            line = line.rstrip("\n\r")
            rows = y + 1
            cols = max(cols, len(line))
            for x, ch in enumerate(line):
                matrix[(x, y)] = ch
    return matrix, rows, cols

def replace(matrix, rows, cols):
    global REPLACE_POINTS, COUNT_REPLACE
    for index in range(len(REPLACE_POINTS)):
        matrix[REPLACE_POINTS[index]] = 'X'
    
    #draw(matrix, rows, cols)
    
    if(len(REPLACE_POINTS) == 0):
        return
    else:
        COUNT_REPLACE+=len(REPLACE_POINTS)
        REPLACE_POINTS = []
        count_access(matrix, rows, cols)
        return replace(matrix, rows, cols)
     

def go_matrix(matrix, rows, cols, max_x, max_y):
    for y in range(rows):
        row = ""
        for x in range(cols):
            point = matrix[(x, y)]
            count_papper = count_pappers(matrix, (x,y), x, y, max_x, max_y)
            if(count_papper < 4):
                REPLACE_POINTS.append((x,y))
                ACCESS_POINTS.append(count_papper)

            row += point
    

def count_access(matrix, rows, cols):
    max_x = max(k[0] for k in matrix.keys())
    max_y = max(k[1] for k in matrix.keys())
    print(f"matrix={matrix}, rows={rows}, cols={cols}")
    
    # ezt kell ciklusba tenni
    go_matrix(matrix, rows, cols, max_x, max_y)
    

def count_pappers(matrix, point, x, y, max_x, max_y):
    if(matrix[point] != PAPPER_ICON):
        return 8
    
    neighbors = get_neighbors(point, x, y, max_x, max_y)
    count_papper = 0
    for n_point in list(neighbors):
        if(matrix[n_point] == PAPPER_ICON):
            count_papper+=1
            
    return count_papper

def get_neighbors(point, x, y, max_x, max_y): 
    result = []
    for i in range(-1,2):
        x_point = x+i
        for j in range(-1,2):
            y_point = y+j            
            n_point = (x_point, y_point)
            if(n_point != point and x_point <= max_x and y_point <= max_y and x_point >= 0 and y_point >= 0):
                result.append(n_point)
    
    return result


def draw(dict, rows, cols):
    for y in range(rows):
        row = ""
        for x in range(cols):
            row += dict[(x, y)]
        print(row)

def welcome():
    print("Welcom on 3. day!")

### MAIN ###
welcome()
matrix, rows, cols = read_csv()
#print(f"matrix={matrix}")

count_access(matrix, rows, cols)
print(f"ACCESS_POINTS={ACCESS_POINTS}")
print(f"password is={len(ACCESS_POINTS)}")
## ACCESS_POINTS.size=1372  ---> good

print(f"REPLACE_POINTS={REPLACE_POINTS}")
replace(matrix, rows, cols)
print(f"COUNT_REPLACE={COUNT_REPLACE}")

## password is 7922


#modify_matrix = 


#draw(matrix, rows, cols)