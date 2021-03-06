import pygame
from random import randint
from math import degrees, atan, tan, sqrt
from json import dump as jsdump
from json import load as jsload

pygame.init()
screen = pygame.display.set_mode((1280, 720))

with open('./bin/config.json') as json_file:
    config_data = jsload(json_file)
    newdata = config_data
# the setting what needs when new game
def default_setup():
    global x
    global y
    global x_2
    global y_2
    global enemy_x
    global enemy_y
    global x_poison
    global y_poison
    global esc
    global xs
    global ys
    global space
    global bullet
    global alive
    global mov_speed
    global xp
    global lvl
    global ab_lvl
    global health
    global y_up
    global x_right
    global ability1
    global ability2
    global ability3
    global ability4
    global on_menu_angle

    x = 480
    y = 270
    x_2 = randint(50, 1100)
    y_2 = randint(50, 650)
    enemy_x = -200
    enemy_y = 500
    x_poison = randint(50, 1100)
    y_poison = randint(50, 650)
    esc = False
    xs = -100
    ys = -100
    space = 0
    bullet = False
    alive = True
    mov_speed = 13
    xp = 110
    lvl = 0 # max lvl 8
    ab_lvl = 0
    health = 24 # max 24
    y_up = 0
    x_right = 0
    ability1 = {"is" : False, "lvl" : 0}
    ability2 = {"is" : False, "lvl" : 0, "plus_speed" : {0 : 0, 1 : 4, 2 : 8}}
    ability3 = {"is" : False, "lvl" : 0, "cd" : {1 : 8, 2 : 4}}
    ability4 = {"is" : False, "lvl" : 0}
    on_menu_angle = 0

# settings
default_setup()

sure_quit = False
go = True
loading = True
logo = False
menu = False
settings_menu = False
show_hitbox = False
b_speed = 20
shot_radius = 400

animation_x = -20
animation_y = 550
menu_spider_rotate = 0
settings_tab = 0
controll_is_set = 0
# full screen
DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.time.delay(3000)
# text
font = pygame.font.SysFont("comicsansms", 20)
level_text = font.render("Level:", True, (0, 255, 0))
hp_text = font.render("Health:", True, (255, 0, 0))
# ability cd
cd_font = pygame.font.SysFont("comicsansms", 40)
# pause menu
backtothegame_text = font.render("Back to the Game", True, (0, 0, 0))
quit_text = font.render("Quit", True, (0, 0, 0))
sure_quit_text = font.render("Are you sure?", True, (0, 0, 0))
cancel_text = font.render("Cancel", True, (0, 0, 0))
settings_text = font.render("Settings", True, (0, 0, 0))
backtomenu_text = font.render("Main Menu", True, (0, 0, 0))
newgame_text = font.render("New Game", True, (0, 0, 0))
savegame_text = font.render("Save Game", True, (0, 0, 0))
loadgame_text = font.render("Load Game", True, (0, 0, 0))
# settings menu
back_text = font.render("Back", True, (0, 0, 0))
controlls_text = font.render("Controlls", True, (0, 0, 0))
sound_text = font.render("Sound", True, (0, 0, 0))
new_settings_tab_text = font.render(" ", True, (0, 0, 0))
new_settings_tab_text2 = font.render(" ", True, (0, 0, 0))

ab1_key_text = font.render("Ability1: " + pygame.key.name(newdata["controlls"]["ab1"]).upper(), True, (0, 0, 0))
ab2_key_text =  font.render("Ability2: " + pygame.key.name(newdata["controlls"]["ab2"]).upper(), True, (0, 0, 0))
space_key_text = font.render("Function: " + pygame.key.name(newdata["controlls"]["space"]).upper(), True, (0, 0, 0))
up_key_text = font.render("Up: " + pygame.key.name(newdata["controlls"]["up"]).upper(), True, (0, 0, 0))
down_key_text = font.render("Down: " + pygame.key.name(newdata["controlls"]["down"]).upper(), True, (0, 0, 0))
left_key_text = font.render("Left: " + pygame.key.name(newdata["controlls"]["left"]).upper(), True, (0, 0, 0))
right_key_text = font.render("Right: " + pygame.key.name(newdata["controlls"]["right"]).upper(), True, (0, 0, 0))

press_key_to_set = font.render("Press a Key to set!", True, (0, 0, 0))
# game over
overfont = pygame.font.SysFont("comicsansms", 80)
game_over_text = overfont.render("Game Over! You Dead.", True, (255, 255, 255))
press_space_text = font.render("Press " + pygame.key.name(newdata["controlls"]["space"]).upper() + " to start a new game!", True, (255, 255, 255))
# descriptions
desc_font = pygame.font.SysFont("comicsansms", 15)
hearth_desc = desc_font.render("You get hp from meat", True, (66, 245, 170))
speed_desc = desc_font.render("When you eat a meat, you have chance to get extra speed for the next 4 seconds", True, (66, 245, 170))
web_desc = desc_font.render("You can shot a web to stun an enemy", True, (66, 245, 170))
poti_desc = desc_font.render("You can buy different potions in the shop", True, (66, 245, 170))
shop_desc = desc_font.render("You can buy different potions here", True, (66, 245, 170))

x_right = 0
y_up = 0
# textures
spider_up = pygame.image.load('./bin/images/spider_up_small.png')
spider_on_menu = pygame.image.load('./bin/images/spider_on_menu.png')
background = pygame.image.load("./bin/images/background.png")
background2 = pygame.image.load("./bin/images/background2.png")
background3 = pygame.image.load("./bin/images/background3.png")
pause_grayImg = pygame .image.load('./bin/images/pause_gray.png')
meatImg = pygame.image.load('./bin/images/meat.png')
poisonImg = pygame.image.load('./bin/images/poison.png')
coinImg = pygame.image.load('./bin/images/coin.png')
upgradeImg = pygame.image.load('./bin/images/upgrade.png')
shot = pygame.image.load("./bin/images/shot2.png")
bulletImg = pygame.image.load("./bin/images/bullet.png")
logoImg = pygame.image.load('./bin/images/logo.png')
any_keyImg = pygame.image.load('./bin/images/any_key.png')
theImg = pygame.image.load('./bin/images/the.png')
flyImg = pygame.image.load('./bin/images/fly.png')
# abilities
hearth_onImg = pygame.image.load('./bin/images/hearth_ability_ready.png')
hearth_offImg = pygame.image.load('./bin/images/hearth_ability_off.png')
speed_onImg = pygame.image.load('./bin/images/speed_ability_ready.png')
speed_offImg = pygame.image.load('./bin/images/speed_ability_off.png')
web_onImg = pygame.image.load('./bin/images/cobweb_ability_ready.png')
web_offImg = pygame.image.load('./bin/images/cobweb_ability_off.png')
poti_offImg = pygame.image.load('./bin/images/potion_ability_off.png')

poti_cyan_onImg = pygame.image.load('./bin/images/potion_cyan_ability_ready.png')
poti_green_onImg = pygame.image.load('./bin/images/potion_green_ability_ready.png')
poti_orange_onImg = pygame.image.load('./bin/images/potion_orange_ability_ready.png')
poti_pink_onImg = pygame.image.load('./bin/images/potion_pink_ability_ready.png')
poti_purple_onImg = pygame.image.load('./bin/images/potion_purple_ability_ready.png')
poti_red_onImg = pygame.image.load('./bin/images/potion_red_ability_ready.png')
poti_yellow_onImg = pygame.image.load('./bin/images/potion_yellow_ability_ready.png')
# configset
def set_config(newdata):
    with open('./bin/config.json', 'w') as outfile:
        jsdump(newdata, outfile)

# rotation
def rot_center(image, angle, blittedRect):
    oldCenter = blittedRect.center
    rotatedSurf = pygame.transform.rotate(image, angle)
    rotRect = rotatedSurf.get_rect()
    rotRect.center = oldCenter
    return(screen.blit(rotatedSurf, rotRect))

def blitRotateCenter(surf, image, topleft, angle):

    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    return surf.blit(rotated_image, new_rect.topleft)
# set character's textures by direction
def character1(x, y, vertical, horisontal, blittedChar):
    if vertical == 0:
        if horisontal == 0 or horisontal == 1:
            character1Img = rot_center(spider_up, 0, blittedChar)
        elif horisontal == -1:
            character1Img = rot_center(spider_up, 180, blittedChar)
    elif vertical == 1:
        if horisontal == 0:
            character1Img = rot_center(spider_up, -90, blittedChar)
        elif horisontal == 1:
            character1Img = rot_center(spider_up, -45, blittedChar)
        elif horisontal == -1:
            character1Img = rot_center(spider_up, -135, blittedChar)
    elif vertical == -1:
        if horisontal == 0:
            character1Img = rot_center(spider_up, 90, blittedChar)
        elif horisontal == 1:
            character1Img = rot_center(spider_up, 45, blittedChar)
        elif horisontal == -1:
            character1Img = rot_center(spider_up, 135, blittedChar)
    return(character1Img)

while go == True:
    # setup
    ab1_key_text = font.render("Ability1: " + pygame.key.name(newdata["controlls"]["ab1"]).upper(), True, (0, 0, 0))
    ab2_key_text =  font.render("Ability2: " + pygame.key.name(newdata["controlls"]["ab2"]).upper(), True, (0, 0, 0))
    space_key_text = font.render("Function: " + pygame.key.name(newdata["controlls"]["space"]).upper(), True, (0, 0, 0))
    up_key_text = font.render("Up: " + pygame.key.name(newdata["controlls"]["up"]).upper(), True, (0, 0, 0))
    down_key_text = font.render("Down: " + pygame.key.name(newdata["controlls"]["down"]).upper(), True, (0, 0, 0))
    left_key_text = font.render("Left: " + pygame.key.name(newdata["controlls"]["left"]).upper(), True, (0, 0, 0))
    right_key_text = font.render("Right: " + pygame.key.name(newdata["controlls"]["right"]).upper(), True, (0, 0, 0))

    press_space_text = font.render("Press " + pygame.key.name(newdata["controlls"]["space"]).upper() + " to start a new game!", True, (255, 255, 255))
    # loading screen
    if loading == True:
        # logo = True
        screen.blit(background, [0, 0])
        if animation_x < 614:
            animation_x += 10
            screen.blit(pygame.transform.rotate(spider_up, -90), [animation_x, animation_y])
        elif animation_y > 334:
            screen.blit(spider_up, [animation_x, animation_y])
            animation_y -= 10
        else:
            logo = True

        if logo == True:
            pygame.draw.rect(screen, (0, 0, 0), (0, 0, 1280, 720))
            screen.blit(theImg, [581, 150])
            screen.blit(logoImg, [287, 260])
            screen.blit(any_keyImg, [377, 500])
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    loading = False
                    menu = True

    # main menu
    elif menu == True:
        blittedSpider_menu = screen.blit(spider_on_menu, [800, 100])
        screen.blit(background2, [0, 0])

        pygame.draw.rect(screen, (0, 106, 255), (180, 100, 350, 500))
        m_newgame = pygame.draw.rect(screen, (120, 120, 120), (267.5, 150, 175, 30))
        m_loadgame = pygame.draw.rect(screen, (120, 120, 120), (267.5, 200, 175, 30))
        m_settings = pygame.draw.rect(screen, (120, 120, 120), (267.5, 250, 175, 30))
        m_exit = pygame.draw.rect(screen, (120, 120, 120), (267.5, 350, 175, 30))

        screen.blit(newgame_text, (314.5, 150))
        screen.blit(loadgame_text, (314.5, 200))
        screen.blit(settings_text, (314.5, 250))
        screen.blit(quit_text, (332.5, 350))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if m_exit.collidepoint(pygame.mouse.get_pos()):
                    go = False
                elif m_settings.collidepoint(pygame.mouse.get_pos()):
                    settings_menu = True
                    menu = False
                    from_game = False
                    newdata = config_data
                elif m_newgame.collidepoint(pygame.mouse.get_pos()):
                    menu = False
                    default_setup()
                    continue
                elif m_loadgame.collidepoint(pygame.mouse.get_pos()):
                    pass

                elif m_spider.collidepoint(pygame.mouse.get_pos()):
                    pygame.time.delay(250)
                    if menu_spider_rotate == 0:
                        menu_spider_rotate = 1
                    else:
                        menu_spider_rotate = 0
        # spider animation (spider going around)
        if menu_spider_rotate == 0:
            if on_menu_angle > -359:
                on_menu_angle -= 3
            else:
                on_menu_angle = 0
            m_spider = rot_center(spider_on_menu, on_menu_angle, blittedSpider_menu)
        else:
            if on_menu_angle > -359:
                on_menu_angle += 3
            else:
                on_menu_angle = 0
            m_spider = rot_center(pygame.transform.flip(spider_on_menu, 1, 0), on_menu_angle, blittedSpider_menu)

    # settings
    elif settings_menu == True:
        # main tab
        if settings_tab == 0:
            screen.blit(pause_grayImg, [0, 0])
            pygame.draw.rect(screen, (65, 65, 65), (465, 110, 350, 500))

            controlls = pygame.draw.rect(screen, (220, 220, 220), (550, 150, 175, 30))
            sound = pygame.draw.rect(screen, (220, 220, 220), (550, 200, 175, 30))
            new_settings_tab = pygame.draw.rect(screen, (220, 220, 220), (550, 250, 175, 30))
            new_settings_tab2 = pygame.draw.rect(screen, (220, 220, 220), (550, 300, 175, 30))
            back = pygame.draw.rect(screen, (220, 220, 220), (550, 400, 175, 30))

            screen.blit(controlls_text, (600, 150))
            screen.blit(sound_text, (610, 200))
            screen.blit(new_settings_tab_text, (597, 250))
            screen.blit(new_settings_tab_text2, (597, 300))
            screen.blit(back_text, (615, 400))

            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        if from_game == False:
                            menu = True
                        settings_menu = False
                        set_config(newdata)
                if event.type == pygame.MOUSEBUTTONUP:
                    if controlls.collidepoint(pygame.mouse.get_pos()):
                        settings_tab = 1
                    elif sound.collidepoint(pygame.mouse.get_pos()):
                        settings_tab = 2
                    elif new_settings_tab.collidepoint(pygame.mouse.get_pos()):
                        pass
                    elif new_settings_tab.collidepoint(pygame.mouse.get_pos()):
                        pass
                    elif back.collidepoint(pygame.mouse.get_pos()):
                        if from_game == False:
                            menu = True
                        settings_menu = False
                        set_config(newdata)
        # controlls tab
        elif settings_tab == 1:
            screen.blit(pause_grayImg, [0, 0])
            pygame.draw.rect(screen, (65, 65, 65), (465, 110, 350, 500))

            ab1_key_set = pygame.draw.rect(screen, (220, 220, 220), (475, 150, 330, 30))
            ab2_key_set = pygame.draw.rect(screen, (220, 220, 220), (475, 200, 330, 30))
            space_key_set = pygame.draw.rect(screen, (220, 220, 220), (475, 250, 330, 30))
            up_key_set = pygame.draw.rect(screen, (220, 220, 220), (475, 300, 330, 30))
            down_key_set = pygame.draw.rect(screen, (220, 220, 220), (475, 350, 330, 30))
            left_key_set = pygame.draw.rect(screen, (220, 220, 220), (475, 400, 330, 30))
            right_key_set = pygame.draw.rect(screen, (220, 220, 220), (475, 450, 330, 30))

            back = pygame.draw.rect(screen, (220, 220, 220), (550, 550, 175, 30))

            if controll_is_set == 1:
                screen.blit(press_key_to_set, (485, 150))
            else:
                screen.blit(ab1_key_text, (485, 150))
            if controll_is_set == 2:
                screen.blit(press_key_to_set, (485, 200))
            else:
                screen.blit(ab2_key_text, (485, 200))
            if controll_is_set == 3:
                screen.blit(press_key_to_set, (485, 250))
            else:
                screen.blit(space_key_text, (485, 250))
            if controll_is_set == 4:
                screen.blit(press_key_to_set, (485, 300))
            else:
                screen.blit(up_key_text, (485, 300))
            if controll_is_set == 5:
                screen.blit(press_key_to_set, (485, 350))
            else:
                screen.blit(down_key_text, (485, 350))
            if controll_is_set == 6:
                screen.blit(press_key_to_set, (485, 400))
            else:
                screen.blit(left_key_text, (485, 400))
            if controll_is_set == 7:
                screen.blit(press_key_to_set, (485, 450))
            else:
                screen.blit(right_key_text, (485, 450))

            screen.blit(back_text, (615, 550))

            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        settings_tab = 0
                        controll_is_set = 0

                if controll_is_set == 1:
                    if event.type == pygame.KEYDOWN:
                        newdata["controlls"]["ab1"] = event.key
                        controll_is_set = 0
                elif controll_is_set == 2:
                    if event.type == pygame.KEYDOWN:
                        newdata["controlls"]["ab2"] = event.key
                        controll_is_set = 0
                elif controll_is_set == 3:
                    if event.type == pygame.KEYDOWN:
                        newdata["controlls"]["space"] = event.key
                        controll_is_set = 0
                elif controll_is_set == 4:
                    if event.type == pygame.KEYDOWN:
                        newdata["controlls"]["up"] = event.key
                        controll_is_set = 0
                elif controll_is_set == 5:
                    if event.type == pygame.KEYDOWN:
                        newdata["controlls"]["down"] = event.key
                        controll_is_set = 0
                elif controll_is_set == 6:
                    if event.type == pygame.KEYDOWN:
                        newdata["controlls"]["left"] = event.key
                        controll_is_set = 0
                elif controll_is_set == 7:
                    if event.type == pygame.KEYDOWN:
                        newdata["controlls"]["right"] = event.key
                        controll_is_set = 0

                # else:
                if event.type == pygame.MOUSEBUTTONUP:
                    if back.collidepoint(pygame.mouse.get_pos()):
                        settings_tab = 0
                        controll_is_set = 0
                    elif ab1_key_set.collidepoint(pygame.mouse.get_pos()):
                        if controll_is_set == 1:
                            controll_is_set = 0
                        else:
                            controll_is_set = 1
                    elif ab2_key_set.collidepoint(pygame.mouse.get_pos()):
                        if controll_is_set == 2:
                            controll_is_set = 0
                        else:
                            controll_is_set = 2
                    elif space_key_set.collidepoint(pygame.mouse.get_pos()):
                        if controll_is_set == 3:
                            controll_is_set = 0
                        else:
                            controll_is_set = 3
                    elif up_key_set.collidepoint(pygame.mouse.get_pos()):
                        if controll_is_set == 4:
                            controll_is_set = 0
                        else:
                            controll_is_set = 4
                    elif down_key_set.collidepoint(pygame.mouse.get_pos()):
                        if controll_is_set == 5:
                            controll_is_set = 0
                        else:
                            controll_is_set = 5
                    elif left_key_set.collidepoint(pygame.mouse.get_pos()):
                        if controll_is_set == 6:
                            controll_is_set = 0
                        else:
                            controll_is_set = 6
                    elif right_key_set.collidepoint(pygame.mouse.get_pos()):
                        if controll_is_set == 7:
                            controll_is_set = 0
                        else:
                            controll_is_set = 7

        # sound tab
        elif settings_tab == 2:
            screen.blit(pause_grayImg, [0, 0])
            pygame.draw.rect(screen, (65, 65, 65), (465, 110, 350, 500))

            #
            back = pygame.draw.rect(screen, (220, 220, 220), (550, 400, 175, 30))

            #
            screen.blit(back_text, (615, 400))

            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        settings_tab = 0

                if event.type == pygame.MOUSEBUTTONUP:
                    if back.collidepoint(pygame.mouse.get_pos()):
                        settings_tab = 0
        # new_settings_tab
        elif settings_tab == 3:
            settings_tab = 0
        # new_settings_tab2
        elif settings_tab == 4:
            settings_tab = 0
    # the game
    else:
        nowtime = pygame.time.get_ticks()
        if esc == False:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        esc = True
                        continue
            if alive:
                # controlling
                pressed = pygame.key.get_pressed()
                if pressed[newdata["controlls"]["up"]] or pressed[newdata["controlls"]["down"]] or pressed[newdata["controlls"]["left"]] or pressed[newdata["controlls"]["right"]]:
                    x_right = 0
                    y_up = 0
                if pressed[newdata["controlls"]["up"]]:
                    y -= mov_speed
                    y_up = 1
                elif pressed[newdata["controlls"]["down"]]:
                    y += mov_speed
                    y_up = -1
                if pressed[newdata["controlls"]["left"]]:
                    x -= mov_speed
                    x_right = -1
                elif pressed[newdata["controlls"]["right"]]:
                    x += mov_speed
                    x_right = 1

                if ability3["is"]:
                    if space == 0:
                        if pressed[newdata["controlls"]["ab1"]]:
                            space = 1

                    elif space == 1:
                        if pressed[newdata["controlls"]["ab1"]] == False:
                            space = 2
                            ab3_again = (pygame.time.get_ticks()) + (ability3["cd"][ability3["lvl"]] * 1000)
                            ability3["is"] = False
                else:
                    if ability3["lvl"] >= 1:
                        if ab3_again <= pygame.time.get_ticks():
                            ability3["is"] = True

                #tp if it runs out of the map
                if y < 70:
                    y += 680
                if y >= 710:
                    y -= 680
                if x <= -20:
                    x += 1280
                if x >= 1280:
                    x -= 1280

                blittedChar = screen.blit(spider_up, [x, y])
                blittedRect = screen.blit(shot, [x-104, y-100])

                if show_hitbox:
                    shotHitbox = pygame.draw.circle(screen, [0, 0, 0], [int(xs), int(ys)], shot_radius)
                    show_hitbox = False
                screen.blit(background, [0, 0])
                # generate characters
                meat = screen.blit(meatImg, (x_2, y_2))
                poison = screen.blit(poisonImg, (x_poison, y_poison))

                # shot aroow
                if space == 1:
                    mp = pygame.mouse.get_pos()
                    a = x+26 - mp[0]
                    b = y+26 - mp[1]
                    if b == 0:
                        b = 1

                    rotate_deg = degrees(atan(a/b))
                    if b < 0:
                        if rotate_deg < 0:
                            rotate_deg += 180
                        elif rotate_deg > 0:
                            rotate_deg -= 180

                        if rotate_deg == -0.0:
                            rotate_deg = 180
                    nyil = rot_center(shot, rotate_deg, blittedRect)

                elif space == 2:

                    bullet = True
                    xs = x +21
                    ys = y +21
                    space = 3
                    show_hitbox = True

                elif space == 3:

                    if xs < -100 or xs > 1380:
                        xs = -100
                        bullet = False
                    if ys < -100 or ys > 820:
                        ys = -100
                        bullet = False
                    if bullet_object.colliderect(shotHitbox) == False:
                        xs = -100
                        ys = -100
                        bullet = False

                    if bullet == True:
                        if a < 0:
                            a = a*(-1)
                        if b < 0:
                            b = b*(-1)
                        ba = 1000
                        aa = ba * (a/b)
                        aa -= aa % 1
                        root = sqrt((b_speed**2) / (ba**2 + aa**2))
                        ar = root * aa
                        br = root * ba

                        if rotate_deg < 0:
                            rd2 = rotate_deg * (-1)
                        else:
                            rd2 = rotate_deg

                        if rd2 < 90:
                            ys -= br
                        else:
                            ys += br

                        if rotate_deg > 0:
                            xs -= ar
                        else:
                            xs += ar
                    else:
                        space = 0

                bullet_object = screen.blit(bulletImg, [xs, ys])

                character = character1(x, y, x_right, y_up, blittedChar)

                # calculation
                if lvl == 7:
                    meatxp = 6
                else:
                    meatxp = 24 / (lvl + 1)

                # enemy
                enemy_a = enemy_x - x
                enemy_b = enemy_y - y
                if enemy_b == 0:
                    enemy_b = 1

                enemy_rotate_deg = degrees(atan(enemy_a/enemy_b))
                if enemy_b < 0:
                    if enemy_rotate_deg < 0:
                        enemy_rotate_deg += 180
                    elif enemy_rotate_deg > 0:
                        enemy_rotate_deg -= 180

                    if enemy_rotate_deg == -0.0:
                        enemy_rotate_deg = 180

                enemy_obj = blitRotateCenter(screen, flyImg, (enemy_x, enemy_y), enemy_rotate_deg)
                # enemy movement
                if enemy_a < 0:
                    enemy_a = enemy_a*(-1)
                if enemy_b < 0:
                    enemy_b = enemy_b*(-1)
                enemy_ba = 1000
                enemy_aa = enemy_ba * (enemy_a/enemy_b)
                enemy_aa -= enemy_aa % 1

                enemy_speed = 0
                if lvl > 0:
                    if lvl > 8:
                        enemy_speed = 20
                    else:
                        enemy_speed = 10

                root = sqrt((enemy_speed**2) / (enemy_ba**2 + enemy_aa**2))
                enemy_ar = root * enemy_aa
                enemy_br = root * enemy_ba

                if enemy_rotate_deg < 0:
                    enemy_rd2 = enemy_rotate_deg * (-1)
                else:
                    enemy_rd2 = enemy_rotate_deg

                if enemy_rd2 < 90:
                    enemy_y -= enemy_br
                else:
                    enemy_y += enemy_br

                if enemy_rotate_deg > 0:
                    enemy_x -= enemy_ar
                else:
                    enemy_x += enemy_ar
                # enemy actions
                if character.colliderect(enemy_obj):
                    health -= 12
                    enemy_x = -200
                    enemy_y = 500

                if bullet_object.colliderect(enemy_obj):
                    enemy_x = -200
                    enemy_y = 500
                    enemy_xp = meatxp + 2
                    xp += enemy_xp
                    xs = -200
                    ys = -200

                # meat pickup
                if character.colliderect(meat):
                    x_2 = randint(50, 1100)
                    y_2 = randint(50, 650)
                    xp += meatxp

                    if ability1["lvl"] == 1:
                        health += 3
                    elif ability1["lvl"] == 2:
                        health += 6

                    if ability2["is"]:
                        plus_speed_chance = randint(1, ((ability2["lvl"] * 4) / (ability2["lvl"] ** 2)))
                        if plus_speed_chance == 1:
                            mov_speed += ability2["plus_speed"][ability2["lvl"]]
                            prev_speed = ability2["plus_speed"][ability2["lvl"]]
                            ab2_again = (pygame.time.get_ticks() + 4000)
                            ability2["is"] = False

                if ability2["is"] == False:
                    if ability2["lvl"] >= 1:
                        if ab2_again <= pygame.time.get_ticks():
                            ability2["is"] = True
                            mov_speed -= prev_speed

                if health > 24:
                    health = 24
                if xp >= 120:
                    lvl += 1
                    xp = 0
                if health <= 0:
                    alive = False
                    continue
                level_num = font.render(str(lvl), True, (0, 255, 0))
                lvl_ind = (xp * 2) + 180

                if character.colliderect(poison):
                            x_poison = randint(50, 1100)
                            y_poison = randint(50, 650)
                            health -= 8

                if health >= 0:
                    h_cor = (health * 10) + 180
                if health < 0:
                    h_cor = 180
                # calculations
                if lvl > ab_lvl:
                    stay = True

                # hotbar
                pygame.draw.rect(screen, (110, 110, 100), (0, 0, 1280, 50))
                # level indication
                screen.blit(level_text, (100, -5))
                screen.blit(level_num, (160, -5))
                pygame.draw.line(screen, (0, 0, 255), (178, 11), (422, 11), 13)
                pygame.draw.line(screen, (0, 255, 0), (180, 11), (lvl_ind, 11), 8)
                # hp indication
                screen.blit(hp_text, (100, 14))
                pygame.draw.line(screen, (0, 0, 255), (178, 30), (422, 30), 13)
                pygame.draw.line(screen, (255, 0, 0), (180, 30), (h_cor, 30), 8)

                # ability upgrades
                if lvl > ab_lvl:
                    # show lvl up buttons
                    if ability1["lvl"] < 2:
                        up_1 = screen.blit(upgradeImg, (454.5, 45))
                    else:
                        up_1 = screen.blit(upgradeImg, (-100, -100))
                    if ability2["lvl"] < 2:
                        up_2 = screen.blit(upgradeImg, (498.5, 45))
                    else:
                        up_2 = screen.blit(upgradeImg, (-100, -100))
                    if ability3["lvl"] < 2:
                        up_3 = screen.blit(upgradeImg, (542.5, 45))
                    else:
                        up_3 = screen.blit(upgradeImg, (-100, -100))
                    if ability4["lvl"] < 2:
                        up_4 = screen.blit(upgradeImg, (586.5, 45))
                    else:
                        up_4 = screen.blit(upgradeImg, (-100, -100))

                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONUP:
                            if up_1.collidepoint(pygame.mouse.get_pos()):
                                ability1["lvl"] += 1
                                ab_lvl += 1
                                if ability1["lvl"] == 1:
                                    hearth_desc = desc_font.render("Lvl: (" + str(ability1["lvl"]) + ") You get (3) hp from meat", True, (66, 245, 170))
                                else:
                                    hearth_desc = desc_font.render("Lvl: (" + str(ability1["lvl"]) + ") You get (6) hp from meat", True, (66, 245, 170))
                                ability1["is"] = True
                            elif up_2.collidepoint(pygame.mouse.get_pos()):
                                ability2["lvl"] += 1
                                ab_lvl += 1
                                if ability2["lvl"] == 1:
                                    speed_desc = desc_font.render("Lvl: (" + str(ability2["lvl"]) + ") When you eat a meat, you have (25%) chance to get extra speed for the next 4 seconds", True, (66, 245, 170))
                                else:
                                    speed_desc = desc_font.render("Lvl: (" + str(ability2["lvl"]) + ") When you eat a meat, you have (50%) chance to get extra speed for the next 4 seconds", True, (66, 245, 170))
                                ability2["is"] = True
                            elif up_3.collidepoint(pygame.mouse.get_pos()):
                                ability3["lvl"] += 1
                                ab_lvl += 1
                                web_desc = desc_font.render("Lvl: (" + str(ability3["lvl"]) + ") You can shot a web to stun an enemy", True, (66, 245, 170))
                                ability3["is"] = True
                            elif up_4.collidepoint(pygame.mouse.get_pos()):
                                ability4["lvl"] += 1
                                ab_lvl += 1
                                poti_desc = desc_font.render("Lvl: (" + str(ability4["lvl"]) + ") You can buy different potions in the shop", True, (66, 245, 170))
                                ability4["is"] = True

                # abilities
                hearth = pygame.draw.rect(screen, (0, 0, 255), (448, 5, 36, 36))
                if ability1["is"]:
                    screen.blit(hearth_onImg, (450, 7)) # you get hp from meat
                else:
                    screen.blit(hearth_offImg, (450, 7))

                speed = pygame.draw.rect(screen, (0, 0, 255), (492, 5, 36, 36))
                if ability2["is"]:
                    screen.blit(speed_onImg, (494, 7)) # if you eat a meat, you have 25/50% chance to get extra speed for 4 seconds
                else:
                    screen.blit(speed_offImg, (494, 7))
                    if ability2["lvl"] >= 1:
                        if ab2_again > pygame.time.get_ticks():
                            cd2now = int((ab2_again - pygame.time.get_ticks()) / 1000) + 1
                            ab2_cd_text = cd_font.render(str(cd2now), True, (0, 0, 0))
                            screen.blit(ab2_cd_text, (498, -5))

                web = pygame.draw.rect(screen, (0, 0, 255), (536, 5, 36, 36))
                if ability3["is"]:
                    if bullet == False:
                        screen.blit(web_onImg, (538, 7)) # you can shot a web to stun an enemy
                    else:
                        screen.blit(web_offImg, (538, 7))
                else:
                    screen.blit(web_offImg, (538, 7))
                    if ability3["lvl"] >= 1:
                        if ab3_again > pygame.time.get_ticks():
                            cd3now = int((ab3_again - pygame.time.get_ticks()) / 1000) + 1
                            ab3_cd_text = cd_font.render(str(cd3now), True, (0, 0, 0))
                            screen.blit(ab3_cd_text, (542, -5))

                poti = pygame.draw.rect(screen, (0, 0, 255), (580, 5, 36, 36))
                if ability4["is"]:
                    screen.blit(poti_offImg, (582, 7)) # you can buy potions
                else:
                    screen.blit(poti_offImg, (582, 7))
                # shop icon
                pygame.draw.rect(screen, (0, 0, 255), (620, 7, 18, 18))
                shop = screen.blit(coinImg, (620, 7)) # you can buy potions
                pos_all = pygame.mouse.get_pos()
                pos_set = [pos_all[0] + 12, pos_all[1]]
                # description
                if hearth.collidepoint(pygame.mouse.get_pos()):
                    screen.blit(hearth_desc, pos_set)
                elif speed.collidepoint(pygame.mouse.get_pos()):
                    screen.blit(speed_desc, pos_set)
                elif web.collidepoint(pygame.mouse.get_pos()):
                    screen.blit(web_desc, pos_set)
                elif poti.collidepoint(pygame.mouse.get_pos()):
                    screen.blit(poti_desc, pos_set)
                elif shop.collidepoint(pygame.mouse.get_pos()):
                    screen.blit(shop_desc, pos_set)

            # game over screen
            else:

                screen.blit(background, [0, 0])
                meat = screen.blit(meatImg, (x_2, y_2))
                poison = screen.blit(poisonImg, (x_poison, y_poison))
                character = character1(x, y, x_right, y_up, blittedChar)

                screen.blit(game_over_text, (250, 150))
                screen.blit(press_space_text, (500, 300))

                pressed = pygame.key.get_pressed()
                if pressed[newdata["controlls"]["space"]]:

                    default_setup()

                    continue
        # pause menu
        else:
            if sure_quit == False:
                screen.blit(pause_grayImg, [0, 0])
                pygame.draw.rect(screen, (65, 65, 65), (465, 110, 350, 500))
                bttg = pygame.draw.rect(screen, (220, 220, 220), (550, 150, 175, 30))
                settings = pygame.draw.rect(screen, (220, 220, 220), (550, 200, 175, 30))
                newgame = pygame.draw.rect(screen, (220, 220, 220), (550, 250, 175, 30))
                savegame = pygame.draw.rect(screen, (220, 220, 220), (550, 300, 175, 30))
                backtomenu = pygame.draw.rect(screen, (220, 220, 220), (550, 350, 175, 30))
                exit = pygame.draw.rect(screen, (220, 220, 220), (550, 450, 175, 30))

                screen.blit(backtothegame_text, (555, 150))
                screen.blit(settings_text, (597, 200))
                screen.blit(newgame_text, (597, 250))
                screen.blit(savegame_text, (595, 300))
                screen.blit(backtomenu_text, (597, 350))
                screen.blit(quit_text, (615, 450))

                for event in pygame.event.get():

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            esc = False
                    if event.type == pygame.MOUSEBUTTONUP:
                        if exit.collidepoint(pygame.mouse.get_pos()):
                            sure_quit = True
                        elif bttg.collidepoint(pygame.mouse.get_pos()):
                            esc = False
                        elif settings.collidepoint(pygame.mouse.get_pos()):
                            settings_menu = True
                            from_game = True
                            newdata = config_data
                        elif savegame.collidepoint(pygame.mouse.get_pos()):
                            pass
                        elif backtomenu.collidepoint(pygame.mouse.get_pos()):
                            menu = True
                        elif newgame.collidepoint(pygame.mouse.get_pos()):
                            default_setup()
                            continue
            else:
                screen.blit(pause_grayImg, [0, 0])
                pygame.draw.rect(screen, (65, 65, 65), (465, 310, 350, 200))

                cancel = pygame.draw.rect(screen, (220, 220, 220), (550, 400, 175, 30))
                exit = pygame.draw.rect(screen, (220, 220, 220), (550, 450, 175, 30))

                screen.blit(sure_quit_text, (578, 350))
                screen.blit(cancel_text, (606, 400))
                screen.blit(quit_text, (615, 450))

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            sure_quit = False
                    if event.type == pygame.MOUSEBUTTONUP:
                        if exit.collidepoint(pygame.mouse.get_pos()):
                            go = False
                        elif cancel.collidepoint(pygame.mouse.get_pos()):
                            sure_quit = False

    pygame.display.flip()
    pygame.time.Clock().tick(60)
