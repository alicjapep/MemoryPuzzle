import pygame
import time
import random

# (width, height) = (1280, 720)
(width, height) = (1000, 500)
background_colour = (255,255,255)
#zdj = pygame.image.load('kwiat.jpg')

window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Memory puzzle')
window.fill(background_colour)

# image_number = random.randint(0,1)
# print("TEST IMAGE NUMBER:   !!   " + str(image_number))
#images = []
image0 = pygame.image.load('image0.jpg')
image1 = pygame.image.load('image1.jpg')
images = [image0, image1]

class Obrazek:
    def __init__(self, isClicked, locationX, locationY):
        self.isClicked = isClicked
        self.locationX = locationX
        self.locationY = locationY
        #self.obrazekType = obrazekType #do porownania czy klikniete to samo
        self.rect = pygame.Rect(locationX,locationY,50,50)
        self.default_image = pygame.image.load('kwiat.jpg')  #default image that loads at the begininng
        self.number = random.randint(0, 1) #0 = mialcus, 1 = karusia
        self.image = images[self.number]

        self.obrazekClickedAsFirst = False #
        self.wasClicked = False

    def load_flowers(self):
        #zdj = pygame.image.load('kwiat.jpg')
        window.blit(self.default_image, (self.locationX, self.locationY))
        pygame.display.flip()

    def location_change(self, a, b):
        print("wymiary test")
        self.locationX = a
        self.locationY = b

        pass


    def obrazek_Clicked(self, pos):
        #pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos) == True :
            # print("Clicked Obrazek!", self.numer)
            window.blit(self.image,(self.locationX,self.locationY))
            pygame.display.flip()
            pygame.time.wait(400)
            #self.default_image = pygame.image.load('kwiat.jpg')
            window.blit(self.default_image,(self.locationX,self.locationY))
            pygame.display.flip()

            self.isClicked = True

        return self.number

    def obrazek_Checked(self):
        if self.isClicked == True and self.number == 0:
            print(" Miałcuś ")
        elif self.isClicked == True and self.number == 1:
            print("Karusia")
        # if self.isClicked == True:
        #     if images[0] == images[0]
        #         print("takie same")
        #     elif images[0] == images[0]



    def compare_match(self, last_number):
        if last_number == self.number:
            print("MATCHED! +1")
        else:
            print("UUUUUUU! -1")


        pass

    def rewers(self):
        rewers_image = pygame.image.load("rewers_wygranko.jpg")
        window.blit(rewers_image, (self.locationX, self.locationY))
        pygame.display.flip()




