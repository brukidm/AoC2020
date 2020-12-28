import numpy as np
from scipy.signal import convolve2d

def snake_print(mat): 
    M = N = 12

    image = [ [0]*12 for i in range(12)]
      
    # Traverse through all rows 
    for i in range(M): 
        if i % 2 == 0: 
            for j in range(N): 
                print(str(mat[i][j]), 
                          end = " ")
                image[i][j] = str(mat[i][j])

        else: 
            for j in range(N - 1, -1, -1): 
                print(str(mat[i][j]),  
                          end = " ")
                image[i][j] = str(mat[i][j])
        print()       
    return image

class Tile():
    def __init__(self, data):
        self.data = data
        self.top = None
        self.bot = None
        self.left = None
        self.right = None

def search_recursively(tiles, origin):
    where_to_go_next = []
    where_to_go_next.append(origin)
    visited = []
    visited_image = []
    image = {}
    coords = (0,0)
    while where_to_go_next:
        current_node = where_to_go_next.pop()
        image[coords] = tiles[current_node].data
        visited.append(current_node.split("-")[0])
        visited_image.append(current_node)
        if tiles[current_node].bot and tiles[current_node].bot.split("-")[0] not in visited:
            where_to_go_next.append(tiles[current_node].bot)
            coords = (coords[0], coords[1] + 1)
        elif tiles[current_node].top and  tiles[current_node].top.split("-")[0] not in visited:
            where_to_go_next.append(tiles[current_node].top)
            coords = (coords[0], coords[1] - 1)
        elif tiles[current_node].right and tiles[current_node].right.split("-")[0] not in visited:
            where_to_go_next.append(tiles[current_node].right)
            coords = (coords[0] + 1, coords[1])
    if len(visited) == 144:
        return visited_image, image
    return None, None

    
def check_line_up(m1, m2):
    if np.array_equal(m1.data[0], m2.data[-1]):
        return "top"
    elif np.array_equal(m1.data[-1], m2.data[0]):
        return "bot"
    elif np.array_equal([row[0] for row in m1.data], [row[-1] for row in m2.data]):
        return "left"
    elif np.array_equal([row[-1] for row in m1.data], [row[0] for row in m2.data]):
        return "right"
    else:
        return None

with open(r"input") as f:
    lines = f.read().split("\n")

    tiles = {}
    image = []

    key = ""
    for line in lines:
        if not line:
            tile = Tile(np.array(image))
            tiles[key] = tile
            image = []
            continue
        if "Tile" in line:
            key = line.split(" ")[1][:-1]
        else:
            image.append(list(line))

    final_tiles = {}
    for key, tile in tiles.items():
        final_tiles[key + "-1"] = tiles[key]
        final_tiles[key + "-2"] = Tile(np.rot90(tiles[key].data, 1))
        final_tiles[key + "-3"] = Tile(np.rot90(tiles[key].data, 2))
        final_tiles[key + "-4"] = Tile(np.rot90(tiles[key].data, 3))
        final_tiles[key + "-5"] = Tile(np.fliplr(tiles[key].data))
        final_tiles[key + "-6"] = Tile(np.rot90(np.fliplr(tiles[key].data), 1))
        final_tiles[key + "-7"] = Tile(np.rot90(np.fliplr(tiles[key].data), 2))
        final_tiles[key + "-8"] = Tile(np.rot90(np.fliplr(tiles[key].data), 3))


    total = {}
    for k1, t1 in final_tiles.items():
        for k2, t2 in final_tiles.items():
            if k1.split("-")[0] != k2.split("-")[0]:
                check = check_line_up(t1, t2)
                if check == "top":
                    final_tiles[k1].top = k2
                elif check == "bot":
                    final_tiles[k1].bot = k2
                elif check == "left":
                    final_tiles[k1].left = k2
                elif check == "right":
                    final_tiles[k1].right = k2
                else:
                    continue
    for k, v in final_tiles.items():
        if v.right and v.bot and not v.top and not v.left:
            image, image_dict = search_recursively(final_tiles, k)
            if image:
                break
    
    image = []
    for y in range(12):
        for i in range(1, len(image_dict[(0,0)]) - 1):
            row = ""
            for x in range(12):
                row += "".join(image_dict[(x,y)][i][1:-1])
            image.append(list(row))
    
    images = []
    images.append(image)
    images.append(np.rot90(image, 1))
    images.append(np.rot90(image, 2))
    images.append(np.rot90(image, 3))
    images.append(np.fliplr(image))
    images.append(np.rot90(np.fliplr(image), 1))
    images.append(np.rot90(np.fliplr(image), 2))
    images.append(np.rot90(np.fliplr(image), 3))

    monster = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0], 
    [1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,1],
    [0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0]])

    for image in images:
        count = 0
        image = [[val.replace('#', "1") for val in row] for row in image]
        image = [[val.replace('.', "0") for val in row] for row in image]
        image = np.array([[int(val) for val in row] for row in image])
        result_space = convolve2d(image, monster, mode='valid')
        result_space = result_space.astype(np.uint8)
        count_monsters = np.count_nonzero(result_space == monster.sum())
        if count_monsters:
            count = count_monsters

        if count:
            total = image.sum() - monster.sum() * count
            print(total)

       