import pygame
from Obrazek import Obrazek



obrazki = []



a = 300
b = 100

# obrazki_X = int(input("podaj szerokosc: "))
# obrazky_Y = int(input("podaj wysokosc: "))

obrazky_Y = 3
obrazki_X = 3

for x in range(a, a+obrazki_X*60, 60):
    for y in range(b, b+obrazky_Y*60, 60):
        obrazki.append(Obrazek(False, x, y)) # creating list of objects of class Obrazek
#obrazki[0].location_change(300,300)


# i = 0
#
# for x in range(50, 200, 50):
#     for y in range(150, 300, 50):
#         obrazki[i].location_change(x,y)
#         i+=1


for obrazek in obrazki:
    print("Location X: " + str(obrazek.locationX))
    obrazek.load_flowers()

last_number = 100
current_number = 100 #100 is default, no obrazek chosen
first_obrazek_clicked = False


case_number = 0
            # 0 = start
            # 1 = clicked first obrazek, waiting for second in pair
            # 2 = clicked second obrazek, comparing them
            # go to 0

are_matched = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            #print(pos)
            print("================")
            print("DEBUG: CASE: " + str(case_number) + "    (case na starcie)")

            if case_number == 0:   #przypadek: żaden obrazek nie jest klikniety, klikamy pierwszy obrazek
                for obrazek in obrazki:
                    obrazek.obrazek_Clicked(pos)
                    if obrazek.isClicked:               #te 2 linjki mozna zmiescic w jednym ifie, pokombinuj
                        case_number = 1
                        print("DEBUG: CASE: 1   (klikniety pierwszy obrazek)")

                        last_number = obrazek.number
                        print("DEBUG:  @@ LAST_NUMBER: " + str(last_number))
                        obrazek.isClicked = False
                        obrazek.obrazekClickedAsFirst = True
                        obrazek.wasClicked = True


            elif case_number == 1:   # przypadek: klikniety zostal juz pierwszy obrazek, teraz klikamy drugi obrazek
                for obrazek in obrazki:
                    obrazek.obrazek_Clicked(pos)
                    if obrazek.isClicked and obrazek.obrazekClickedAsFirst == False:
                        case_number = 2
                        print("DEBUG: CASE: 2    (klikniety drugi obrazek")

                        current_number = obrazek.number
                        print("DEBUG: @@ CURRENT_NUMBER: " + str(current_number))
                        obrazek.wasClicked = True
                        obrazek.isClicked = False


            if case_number == 2:   # przypadek: zostaly klikniete dwa obrazki i rozwazamy czy pasuja
                case_number = 0 #back to default case
                print("DEBUG: CASE: 0     (kliknieto dwa obrazki i sa teraz porownywane")

                if(current_number == last_number):
                    print("!!!WYGRANKO!!!")
                    # # if obrazek.wasClicked == True:
                    # rewers_image = pygame.image.load("rewers_wygranko.jpg")
                    # window.blit(rewers_image, (locationX, locationY))
                    for obrazek in obrazki:
                        if obrazek.obrazek_Clicked(pos):
                            obrazek.rewers()
                    for obrazek in obrazki:
                        obrazek.obrazekClickedAsFirst = False
                        last_number = 100
                        current_number = 101
                else:
                    print("!!!PRZEGRANKO!!!")
                    for obrazek in obrazki:
                        obrazek.obrazekClickedAsFirst = False
                        current_number = 100
                        current_number = 101












# def picture( images , x , y , width , height , angle , horizontal_flip , vertical_flip ):
#
#     images1 = image.load( images ) # loading image
#
#     images2 = transform.scale( images1 , ( width , height ) ) # changing size
#
#     images3 = transform.rotate( images2 , angle ) # changing angle 0 - 360 degree
#
#     images4 = transform.flip( images3 , horizontal_flip , vertical_flip ) # horizontal or vertical flip - true or false
#
#     images4rect = images4.get_rect(  )
#
#     images4rect.x = x # setting x
#
#     images4rect.y = y # setting y
#
#     screen.blit( images4 , images4rect ) # image blit
#
# while true:
#     screen.fill( ( 0 , 0 , 0 ) )
#
#     images = "image.png" # image name
#
#     x = 100 # x-axis
#
#     y = 100 # y-axis
#
#     angle = 0 # 0 - 360
#
#     horizontal_flip = false # true
#
#     vertical_flip = false # true
#
#     width = 200 # width of image
#
#     height = 150 # height of image
#
#     picture( images , x , y , width , height , angle , horizontal_flip , vertical_flip )
