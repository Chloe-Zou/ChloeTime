import pygame
from pygame.locals import KEYDOWN, K_l
import time

global counter
bowl = pygame.image.load('images/bowl.png')
def scale_image(image, factor):
  return pygame.transform.scale(image, (image.get_width() * factor, image.get_height() * factor))
bowl = scale_image(bowl, 8)

def timey(screen):
    pygame.init()
    window = pygame.display.set_mode((400, 300))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 100)
    counter = 10
    text = font.render(str(counter), True, ('#ADD8E6'))

    timer_event = pygame.USEREVENT+1
    pygame.time.set_timer(timer_event, 1000)

    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == timer_event:
                counter -= 1
                text = font.render(str(counter), True, ('#ADD8E6'))
                if counter == 0:
                    pygame.time.set_timer(timer_event, 0)
            if event.type == KEYDOWN and event.key == K_l and counter == 0:
                time.sleep(0.3)
                screen.blit(bowl, (90, 70))
                pygame.display.update()
                print("Onion: Good job! You have finished cooking the onion stew")
                run = False
                return run
                

        window.fill(('#000000'))
        text_rect = text.get_rect(center = window.get_rect().center)
        window.blit(text, text_rect)
        pygame.display.flip()
