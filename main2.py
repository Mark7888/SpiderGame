import pygame
import random
from math import degrees, atan, tan, sqrt
from pkgutil import get_data as pkg_get_data

pygame.init()
screen = pygame.display.set_mode((1280, 720))
# settings
x = 480
y = 270
x_2 = random.randint(50, 1100)
y_2 = random.randint(50, 650)
x_poison = random.randint(50, 1100)
y_poison = random.randint(50, 650)
xs = -100
ys = -100
go = True
loading = True
logo = False
menu = False
settings_menu = False
esc = False
alive = True
mov_speed = 13
xp = 110
lvl = 0 # max lvl 8
ab_lvl = 0
health = 24 # max 24
ability1 = {"is" : False, "lvl" : 0}
ability2 = {"is" : False, "lvl" : 0}
ability3 = {"is" : False, "lvl" : 0}
ability4 = {"is" : False, "lvl" : 0, "id" : 0}
space = 0
bullet = False
b_speed = 20

animation_x = -20
animation_y = 550
on_menu_angle = 0
menu_spider_rotate = 0

# full screen
DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.time.delay(3000)
# text
font = pygame.font.SysFont("comicsansms", 20)
level_text = font.render("Level:", True, (0, 255, 0))
hp_text = font.render("Health:", True, (255, 0, 0))
# ability cd
cd_font = pygame.font.SysFont("comicsansms", 35)
ab1_cd_text = cd_font.render("3", True, (0, 255, 0))
# pause menu
backtothegame_text = font.render("Back to the Game", True, (0, 0, 0))
quit_text = font.render("Quit", True, (0, 0, 0))
settings_text = font.render("Settings", True, (0, 0, 0))
backtomenu_text = font.render("Main Menu", True, (0, 0, 0))
newgame_text = font.render("New Game", True, (0, 0, 0))
# game over
overfont = pygame.font.SysFont("comicsansms", 80)
game_over_text = overfont.render("Game Over! You Dead.", True, (255, 255, 255))
press_space_text = font.render("Press SPACE to start a new game!", True, (255, 255, 255))
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
spider_up = pkg_get_data('images', 'spider_up_small.png')
spider_on_menu = pkg_get_data('images', 'spider_on_menu.png')
background = pkg_get_data('images', "background.png")
background2 = pkg_get_data('images', "background2.png")
background3 = pkg_get_data('images', "background3.png")
pause_grayImg = pkg_get_data('images', 'pause_gray.png')
meatImg = pkg_get_data('images', 'meat.png')
poisonImg = pkg_get_data('images', 'poison.png')
coinImg = pkg_get_data('images', 'coin.png')
upgradeImg = pkg_get_data('images', 'upgrade.png')
shot = pkg_get_data('images', "shot2.png")
bulletImg = pkg_get_data('images', "bullet.png")
logoImg = pkg_get_data('images', 'logo.png')
any_keyImg = pkg_get_data('images', 'any_key.png')
# abilities
hearth_onImg = pkg_get_data('images', 'hearth_ability_ready.png')
hearth_offImg = pkg_get_data('images', 'hearth_ability_off.png')
speed_onImg = pkg_get_data('images', 'speed_ability_ready.png')
speed_offImg = pkg_get_data('images', 'speed_ability_off.png')
web_onImg = pkg_get_data('images', 'cobweb_ability_ready.png')
web_offImg = pkg_get_data('images', 'cobweb_ability_off.png')
poti_offImg = pkg_get_data('images', 'potion_ability_off.png')

poti_cyan_onImg = pkg_get_data('images', 'potion_cyan_ability_ready.png')
poti_green_onImg = pkg_get_data('images', 'potion_green_ability_ready.png')
poti_orange_onImg = pkg_get_data('images', 'potion_orange_ability_ready.png')
poti_pink_onImg = pkg_get_data('images', 'potion_pink_ability_ready.png')
poti_purple_onImg = pkg_get_data('images', 'potion_purple_ability_ready.png')
poti_red_onImg = pkg_get_data('images', 'potion_red_ability_ready.png')
poti_yellow_onImg = pkg_get_data('images', 'potion_yellow_ability_ready.png')


# rotation
def rot_center(image, angle, blittedRect):
    oldCenter = blittedRect.center
    rotatedSurf = pygame.transform.rotate(image, angle)
    rotRect = rotatedSurf.get_rect()
    rotRect.center = oldCenter
    return(screen.blit(rotatedSurf, rotRect))

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
    if loading == True:
        logo = True
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
            screen.blit(logoImg, [287, 260])
            screen.blit(any_keyImg, [377, 500])
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    loading = False
                    menu = True

    elif menu == True:
        blittedSpider_menu = screen.blit(spider_on_menu, [800, 100])
        screen.blit(background2, [0, 0])

        pygame.draw.rect(screen, (0, 106, 255), (180, 100, 350, 500))
        m_newgame = pygame.draw.rect(screen, (120, 120, 120), (267.5, 150, 175, 30))
        m_settings = pygame.draw.rect(screen, (120, 120, 120), (267.5, 200, 175, 30))
        m_exit = pygame.draw.rect(screen, (120, 120, 120), (267.5, 300, 175, 30))

        screen.blit(newgame_text, (314.5, 150))
        screen.blit(settings_text, (314.5, 200))
        screen.blit(quit_text, (332.5, 300))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if m_exit.collidepoint(pygame.mouse.get_pos()):
                    go = False
                elif m_settings.collidepoint(pygame.mouse.get_pos()):
                    settings_menu = True
                elif m_newgame.collidepoint(pygame.mouse.get_pos()):
                    menu = False
                    x = 480
                    y = 270
                    x_2 = random.randint(50, 1100)
                    y_2 = random.randint(50, 650)
                    x_poison = random.randint(50, 1100)
                    y_poison = random.randint(50, 650)
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
                    ability2 = {"is" : False, "lvl" : 0}
                    ability3 = {"is" : False, "lvl" : 0}
                    ability4 = {"is" : False, "lvl" : 0}
                    on_menu_angle = 0
                    continue

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


    elif settings_menu == True:
        settings_menu = False

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
                if pressed[pygame.K_UP] or pressed[pygame.K_DOWN] or pressed[pygame.K_LEFT] or pressed[pygame.K_RIGHT] or pressed[pygame.K_w] or pressed[pygame.K_s] or pressed[pygame.K_a] or pressed[pygame.K_d]:
                    x_right = 0
                    y_up = 0
                if pressed[pygame.K_UP] or pressed[pygame.K_w]:
                    y -= mov_speed
                    y_up = 1
                elif pressed[pygame.K_DOWN] or pressed[pygame.K_s]:
                    y += mov_speed
                    y_up = -1
                if pressed[pygame.K_LEFT] or pressed[pygame.K_a]:
                    x -= mov_speed
                    x_right = -1
                elif pressed[pygame.K_RIGHT] or pressed[pygame.K_d]:
                    x += mov_speed
                    x_right = 1

                if space == 0:
                    if pressed[pygame.K_SPACE]:
                        space = 1

                elif space == 1:
                    if pressed[pygame.K_SPACE] == False:
                        space = 2

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

                elif space == 3:

                    if xs < -100 or xs > 1380:
                        xs = -100
                        bullet = False
                    if ys < -100 or ys > 820:
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

                screen.blit(bulletImg, [xs, ys])

                character = character1(x, y, x_right, y_up, blittedChar)
                # calculation
                if lvl == 7:
                    meatxp = 6
                else:
                    meatxp = 24 / (lvl + 1)
                # meat pickup
                if character.colliderect(meat):
                            x_2 = random.randint(50, 1100)
                            y_2 = random.randint(50, 650)
                            xp += meatxp
                            if ability1["lvl"] == 1:
                                health += 3
                            elif ability1["lvl"] == 2:
                                health += 6

                            if ability2["lvl"] == 1:
                                flash_chance = random.randint(1, 4)
                                if flash_chance == 1:
                                    mov_speed += 4
                            elif ability2["lvl"] == 2:
                                flash_chance = random.randint(1, 2)
                                if flash_chance == 1:
                                    mov_speed += 4

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
                            x_poison = random.randint(50, 1100)
                            y_poison = random.randint(50, 650)
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
                    if ability2["lvl"] < 2:
                        up_2 = screen.blit(upgradeImg, (498.5, 45))
                    if ability3["lvl"] < 2:
                        up_3 = screen.blit(upgradeImg, (542.5, 45))
                    if ability4["lvl"] < 2:
                        up_4 = screen.blit(upgradeImg, (586.5, 45))

                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONUP:
                            if up_1.collidepoint(pygame.mouse.get_pos()):
                                ability1["lvl"] +=1
                                ab_lvl += 1
                                if ability1["lvl"] == 1:
                                    hearth_desc = desc_font.render("Lvl: (" + str(ability1["lvl"]) + ") You get (3) hp from meat", True, (66, 245, 170))
                                else:
                                    hearth_desc = desc_font.render("Lvl: (" + str(ability1["lvl"]) + ") You get (6) hp from meat", True, (66, 245, 170))
                                ability1["is"] = True
                            elif up_2.collidepoint(pygame.mouse.get_pos()):
                                ability2["lvl"] +=1
                                ab_lvl += 1
                                if ability2["lvl"] == 1:
                                    speed_desc = desc_font.render("Lvl: (" + str(ability2["lvl"]) + ") When you eat a meat, you have (25%) chance to get extra speed for the next 4 seconds", True, (66, 245, 170))
                                else:
                                    speed_desc = desc_font.render("Lvl: (" + str(ability2["lvl"]) + ") When you eat a meat, you have (50%) chance to get extra speed for the next 4 seconds", True, (66, 245, 170))
                                ability2["is"] = True
                            elif up_3.collidepoint(pygame.mouse.get_pos()):
                                ability3["lvl"] +=1
                                ab_lvl += 1
                                web_desc = desc_font.render("Lvl: (" + str(ability3["lvl"]) + ") You can shot a web to stun an enemy", True, (66, 245, 170))
                                ability3["is"] = True
                            elif up_4.collidepoint(pygame.mouse.get_pos()):
                                ability4["lvl"] +=1
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

                web = pygame.draw.rect(screen, (0, 0, 255), (536, 5, 36, 36))
                if ability3["is"]:
                    screen.blit(web_onImg, (538, 7)) # you can shot a web to stun an enemy
                else:
                    screen.blit(web_offImg, (538, 7))

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
                # print ability_cd
                # screen.blit(ab1_cd_text, (457, -2))

            # game over screen
            else:

                screen.blit(background, [0, 0])
                meat = screen.blit(meatImg, (x_2, y_2))
                poison = screen.blit(poisonImg, (x_poison, y_poison))
                character = character1(x, y, x_right, y_up, blittedChar)

                screen.blit(game_over_text, (250, 150))
                screen.blit(press_space_text, (500, 300))

                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_SPACE]:
                    x = 480
                    y = 270
                    x_2 = random.randint(50, 1100)
                    y_2 = random.randint(50, 650)
                    x_poison = random.randint(50, 1100)
                    y_poison = random.randint(50, 650)
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
                    ability2 = {"is" : False, "lvl" : 0}
                    ability3 = {"is" : False, "lvl" : 0}
                    ability4 = {"is" : False, "lvl" : 0}
                    on_menu_angle = 0
                    continue
        # pause menu
        else:

            screen.blit(pause_grayImg, [0, 0])
            pygame.draw.rect(screen, (65, 65, 65), (465, 110, 350, 500))
            bttg = pygame.draw.rect(screen, (220, 220, 220), (550, 150, 175, 30))
            settings = pygame.draw.rect(screen, (220, 220, 220), (550, 200, 175, 30))
            newgame = pygame.draw.rect(screen, (220, 220, 220), (550, 250, 175, 30))
            backtomenu = pygame.draw.rect(screen, (220, 220, 220), (550, 300, 175, 30))
            exit = pygame.draw.rect(screen, (220, 220, 220), (550, 400, 175, 30))

            screen.blit(backtothegame_text, (555, 150))
            screen.blit(settings_text, (597, 200))
            screen.blit(newgame_text, (597, 250))
            screen.blit(backtomenu_text, (597, 300))
            screen.blit(quit_text, (615, 400))

            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        esc = False

                if event.type == pygame.MOUSEBUTTONUP:
                    if exit.collidepoint(pygame.mouse.get_pos()):
                        go = False
                    elif bttg.collidepoint(pygame.mouse.get_pos()):
                        esc = False
                    elif settings.collidepoint(pygame.mouse.get_pos()):
                        settings_menu = True
                    elif backtomenu.collidepoint(pygame.mouse.get_pos()):
                        menu = True
                    elif newgame.collidepoint(pygame.mouse.get_pos()):
                        x = 480
                        y = 270
                        x_2 = random.randint(50, 1100)
                        y_2 = random.randint(50, 650)
                        x_poison = random.randint(50, 1100)
                        y_poison = random.randint(50, 650)
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
                        ability2 = {"is" : False, "lvl" : 0}
                        ability3 = {"is" : False, "lvl" : 0}
                        ability4 = {"is" : False, "lvl" : 0}
                        on_menu_angle = 0
                        continue

    pygame.display.flip()
    pygame.time.Clock().tick(60)
