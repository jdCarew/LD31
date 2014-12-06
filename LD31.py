import sys, pygame,random
pygame.init()

print ("Gravity Ain't The Same")
print ("By: jdCarew")
print ("Ludum Dare 31")
##no it aint
size = width, height= 200,200
black=0,0,0
square_width=40
colors=["red2.bmp"]
colorcount=len(colors)
screen=pygame.display.set_mode(size)
board=[[] for i in range(int(width/square_width))]
for index in range(len(board)):
    for c in range(int(height/square_width)):
        board[index].append(random.randint(1,colorcount))#0 reserve for empty
red=pygame.image.load("red2.bmp")
rect=pygame.Rect(0,0,square_width,square_width)
images=[pygame.image.load(j) for j in colors]


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    for r, row in enumerate(board):
        for c, item in enumerate(row):
            screen.blit(images[item-1],pygame.Rect(square_width*c,square_width*r,10,10))
    ##screen.fill(black)
    
    pygame.display.flip()
