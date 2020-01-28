import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN:
                    print(event.key)
                    print(pygame.key.name(event.key).upper())

        pygame.display.flip()


"""
space
w
a
s
d
# q ---> later
# e ---> later
"""
