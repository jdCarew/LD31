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
board=[[] for i in range(maxx)]
squares=[[] for i in range(maxx)]
for r in range(maxx):
    for c in range(int(height/square_width)):
        board[r].append(random.randint(1,imagescount))#0 reserve for empty
screen=pygame.display.set_mode(size)

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

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            check_click(int(pos[0]/40),int(pos[1]/40))
            screen.fill(black)
            
    for r, row in enumerate(board):
        for c, item in enumerate(row):
            if item>=1:
                screen.blit(images[item-1],pygame.Rect(square_width*r,square_width*c,10,10))
    
    pygame.display.flip()
