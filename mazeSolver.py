import csv,os,time,sys,random

def get_maze(file):
    f = open(file,'r')
    reader = csv.reader(f)
    maze = []
    for line in reader:
        maze.append(line)
    return maze

def display_maze(m, path):
    m2 = m[:]
    os.system('cls') 
    
    for item in path:
        m2[item[0]][item[1]] = "."
    m2[path[-1][0]][path[-1][1]] = "M"
    
    draw = ""
    
    for row in m2:
        for item in row:
            item = str(item).replace("1","█")
            item = str(item).replace("2"," ")
            item = str(item).replace("0"," ")
            
            draw += item
        draw += "\n"
    print(draw)
   
def move(path):
    time.sleep(0.3)
    cur = path[-1]
    display_maze(maze,path)
    possibilities = [(cur[0],cur[1] + 1),(cur[0],cur[1]- 1),(cur[0] + 1, cur[1]),(cur[0]-1, cur[1]) ]
    # to create a different path each time
    random.shuffle(possibilities)
    
    
    for item in possibilities:
        if item[0] < 0 or item[1] < 0 or item[0] > len(maze) or item[1] > len(maze[0]):
            continue
        elif maze[item[0]][item[1]] in ["1","2"] :
            continue
        elif item in path:
            continue
        elif maze[item[0]][item[1]] == "B":
            path = path + (item,)
            display_maze(maze,path)
            input("Solution found! Press enter to finish")
            os.system('cls') 
            sys.exit()
        else:
            newpath = path + (item,)
            move(newpath)
            maze[item[0]][item[1]] = "2"
            display_maze(maze,path)
            time.sleep(0.3)
            

    

# maze = get_maze('maze1.csv')
maze = get_maze('maze2.csv')
width = len(maze)
height = len(maze[0])
# print(maze)


move(((1,0),))