import serial, pygame, time, os

"""
    All the pixelated images are then converted to arrays 
    of bytes (1's and 0's) which are then passed to the 
    LCD display.
"""

FPS = 10
# ________________________________________________________ #

def get_color(color):
    r, g, b , a = color
    if r > 240 and g > 240 and b > 240 and a > 240:
        return 'white'
    else:
        return 'other'

count = 0
img_indx = 0

print('Creating file for new images...')
if not os.path.exists('convImages'):
    os.mkdir('convImages')
# ________________________________________________________ #
    
U1, U2, U3, U4 = [], [], [], []
D1, D2, D3, D4 = [], [], [], []

for i in range(1898):
    points = [
    [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
    [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
    [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0], 
    [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0], 
    [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0], 
    [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0], 
    [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0], 
    [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],

    [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
    [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0],
    [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0], 
    [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0], 
    [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0], 
    [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0], 
    [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0], 
    [0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0]]

    new_points = []

    count += 1
    img_indx += 1

    try:
        conv_img = pygame.transform.rotate(pygame.image.load(f'pngs/png ({img_indx}).png'), 90)
    except:pass

    for y in range(20):
        for x in range(16):
            image_c = conv_img.get_at((x, y))
            color = get_color(image_c)
            if color == 'white':
                try:
                    points[x][y] = 1
                except:pass
            else:
                try:
                    points[x][y] = 0
                except:pass

    with open(f'convImages/test{img_indx}.txt', 'w') as f:
        for fi in points:
            fi[4] = str(fi [4]) + ']'
            fi[5] = '[' + str(fi [5]) 
            fi[9] = str(fi [9]) + ']'
            fi[10] = '[' + str(fi [10])
            fi[15] = '[' + str(fi [15]) 
            fi[14] = str(fi [14]) + ']'
            fi = str(fi).replace("'", "")
            fi = str(fi).replace(' ', '')
            fi = str(fi).replace(',', '')
            f.write(str(fi) + '\n')

    with open(f'convImages/test{img_indx}.txt', 'r') as f:
        new_points = list(f.readlines())

    U1.append([])
    U2.append([])
    U3.append([])
    U4.append([])

    D1.append([])
    D2.append([])
    D3.append([])
    D4.append([])

    for u in range(8):
        U1[i].append('0b' + new_points[u][:7][1:-1])
        U2[i].append('0b' + new_points[u][7:14][1:-1])
        U3[i].append('0b' + new_points[u][14:21][1:-1])
        U4[i].append('0b' + new_points[u][21:28][1:-1])

    for d in range(8, 16):
        D1[i].append('0b' + new_points[d][:7][1:-1])
        D2[i].append('0b' + new_points[d][7:14][1:-1])
        D3[i].append('0b' + new_points[d][14:21][1:-1])
        D4[i].append('0b' + new_points[d][21:28][1:-1])

print(f'Done converting {count} images...')







    

        







