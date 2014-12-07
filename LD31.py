import sys, pygame,random
pygame.init()

##Gravity Ain't The Same (No, It Ain't!)
##By: jdCarew
##Ludum Dare 31

size = width, height= 600,400
square_width=40#size of blocks
images=["red2.bmp", "blue.bmp", "green.bmp", "yellow.bmp"]
g=0
started=0
black=0,0,0
for index, col in enumerate(images):
    images[index]=pygame.image.load(col)
imagescount=len(images)
maxx=int(width/square_width)
maxy=int(height/square_width)
score=0
myfont = pygame.font.SysFont("monospace", 18)
board=[[] for i in range(maxx)]
squares=[[] for i in range(maxx)]
for r in range(maxx):
    for c in range(int(height/square_width)):
        board[r].append(random.randint(1,imagescount))#0 reserve for empty
screen=pygame.display.set_mode(size)     

label=myfont.render("Score: 0",1,(255,255,255))
def print_board():#debug: prints board to shell as image indices
    for j in range(maxy):
        for i in range(maxx):
            print (board[i][j], end=" ")
        print()

def count_similar(x,y,b):#count around a coordinate to find
    result=1             #number that are connected that share color
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
            return score + (2 ** result)
        else:
            for i, row in enumerate(board):
                for j, item in enumerate(row):
                    if board[i][j]==-1:
                        board[i][j] = c
    return score

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
            offset=0
            while board[i][j-offset]==0:
                offset+=1
                if j-offset<0:
                    offset=0
                    break
            if offset > 0:
                board[i][j]=board[i][j-offset]
                board[i][j-offset]=0
def gravity_right():
    for j in range(maxy):
        for i in range(maxx)[::-1]:
            offset=0
            while board[i-offset][j]==0:
                offset+=1
                if i-offset<0:
                    offset=0
                    break
            if offset > 0:
                board[i][j]=board[i-offset][j]
                board[i-offset][j]=0
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
while started ==0:
    Title = myfont.render("Gravity Ain't The Same (No, It Ain't!)", 1, (255,255,255))
    Signoff = myfont.render("By: jdCarew", 1, (255,255,255))
    ld = myfont.render("Ludum Dare 31", 1, (255,255,255))
    instr = myfont.render("Click a box that is connected to at least two others", 1, (255,255,255))
    instr2 = myfont.render("of the same color to score points.", 1, (255,255,255))
    instr3 = myfont.render("Arrow keys control direction of gravity", 1, (255,255,255))
    instr4 = myfont.render("Click anywhere to begin", 1, (255,255,255))
    screen.blit(Title, (10, 50))
    screen.blit(Signoff, (10, 100))
    screen.blit(ld, (10, 150))
    screen.blit(instr, (10, 200))
    screen.blit(instr2, (10, 250))
    screen.blit(instr3, (10, 300))
    screen.blit(instr4, (10, 350))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            started=1

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
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
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            gravity()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            score=check_click(int(pos[0]/40),int(pos[1]/40))
            label = myfont.render("Score: "+str(score), 1, (255,255,255))
            gravity()
    ##draws       
    for r, row in enumerate(board):
        for c, item in enumerate(row):
            if item>=1:
                screen.blit(images[item-1],pygame.Rect(square_width*r,square_width*c,10,10))
    screen.blit(label, (10, 10))
    pygame.display.flip()
