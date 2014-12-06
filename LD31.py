import sys, pygame,random
pygame.init()

print ("Gravity Ain't The Same")
print ("By: jdCarew")
print ("Ludum Dare 31")
##no it aint
size = width, height= 600,400
black=0,0,0
square_width=40
images=["red2.bmp", "blue.bmp", "green.bmp", "yellow.bmp"]
for index, col in enumerate(images):
    images[index]=pygame.image.load(col)
imagescount=len(images)
maxx=int(width/square_width)
maxy=int(height/square_width)
g=2
board=[[] for i in range(maxx)]
squares=[[] for i in range(maxx)]
for r in range(maxx):
    for c in range(int(height/square_width)):
        board[r].append(random.randint(1,imagescount))#0 reserve for empty
screen=pygame.display.set_mode(size)
def print_board():
    for j in range(maxy):
        for i in range(maxx):
            print (board[i][j], end=" ")
        print()

        
def count_similar(x,y,b):
    result=1
    c=b[x][y]
    b[x][y]=-1
    if x<maxx-1 and b[x+1][y]==c:
        result+=count_similar(x+1,y,b)
    if x> 0 and b[x-1][y]==c:
        result+=count_similar(x-1,y,b)
    if y<maxy-1 and b[x][y+1]==c:
        result+=count_similar(x,y+1,b)
    if y> 0 and b[x][y-1]==c:
        result+=count_similar(x,y-1,b)
        
    return result

def check_click(x,y):
    if board[x][y] > 0:
        c=board[x][y]
        result=count_similar(x,y,board) 
        if result>=3:
            for i, row in enumerate(board):
                for j, item in enumerate(row):
                    if board[i][j]== -1:
                        board[i][j] = 0
        else:
            for i, row in enumerate(board):
                for j, item in enumerate(row):
                    if board[i][j]==-1:
                        board[i][j] = c

def gravity():
    if g==0:
        gravity_down()
    elif g==1:
        gravity_left()
    elif g==2:
        gravity_up()
    elif g==3:
        gravity_right()
    screen.fill(black)

def gravity_down():
    for i in range(maxx):
        for j in range(maxy)[::-1]:
            if board[i][j] == 0 and j>0:
                for k in range(j)[::-1]:
                    if board[i][k] >0:
                        board[i][j]=board[i][k]
                        board[i][k]=0
                        break
def gravity_right():
    for j in range(maxy):
        for i in range(maxx)[::-1]:
            if board[i][j] == 0 and i>0:
                for k in range(i)[::-1]:
                    if board[k][j] >0:
                        board[i][j]=board[k][j]
                        board[k][j]=0
                        break
def gravity_up():
    for i in range(maxx):
        for j in range(maxy):
            offset=0
            while board[i][j+offset]==0:
                offset+=1
                if offset+j==maxy:
                    offset=0
                    break
            if offset > 0:
                board[i][j]=board[i][j+offset]
                board[i][j+offset]=0
def gravity_left():
    for j in range(maxy):
        for i in range(maxx):
            offset=0
            while board[i+offset][j]==0:
                offset+=1
                if offset+i==maxx:
                    offset=0
                    break
            if offset > 0:
                board[i][j]=board[i+offset][j]
                board[i+offset][j]=0

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                g= 0
            if event.key == pygame.K_LEFT:
                g= 1
            if event.key == pygame.K_UP:
                g= 2
            if event.key == pygame.K_RIGHT:
                g= 3
            gravity()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            check_click(int(pos[0]/40),int(pos[1]/40))
            ##board[int(pos[0]/40)][int(pos[1]/40)]=0
            gravity()
            
            
    for r, row in enumerate(board):
        for c, item in enumerate(row):
            if item>=1:
                screen.blit(images[item-1],pygame.Rect(square_width*r,square_width*c,10,10))
    
    pygame.display.flip()
