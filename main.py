import pygame


pygame.init()
WIDTH,HIGHT =500,500
BLACK= (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)

class Sprite:
    def __init__(self,x= 10,y=10,width=50,height=50,speed = 0 ,image =None ,color =(28,28,28)):
        self.image = image
        self.color = color
        self.speed = speed
        self.rect = pygame.Rect(x,y,width,height)
        self.load_img()



    def draw (self,window):
        if self.image:
              window.blit(self.image,self.rect)
        else:
            pygame.draw.rect(window,self.color,self.rect)

    def move (self,window):
        key = pygame.key.get_pressed()
        if key[pygame.K_w] and self.rect.y >= self.speed:
            self.rect.y -= self.speed
  
        if key[pygame.K_a] and self.rect.x >= self.speed:
            self.rect.x -= self.speed
        if key[pygame.K_d] and self.rect.right <= window.get_width() - self.speed:
            self.rect.x += self.speed 
        if key[pygame.K_s] and self.rect.bottom <= window.get_height() - self.speed:
            self.rect.y += self.speed

    def load_img(self):
        if self.image:
            self.image = pygame.image.load(self.image)
            self.image = pygame.transform.scale(self.image,(self.rect.width,self.rect.height))

        

    def draw(self,window):
        pygame.draw.rect(window,self.color,(self.x,self.y,self.width,self.height))

window = pygame.display.set_mode((WIDTH,HIGHT))
clock = pygame.time.Clock()
player = Sprite(speed=5,color=RED)



run = True

while run:
    window.fill(WHITE)
    player.draw(window)
    player.move(window)
    for event in pygame.event.get():
        if  event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
    clock.tick(60)

