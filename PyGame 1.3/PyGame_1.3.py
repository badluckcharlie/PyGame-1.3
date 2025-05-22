import pygame
import sys


pygame.init()

WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ülesanne 1.3 ")

taust = pygame.image.load("background.png")
gundam = pygame.image.load("rx.png")

gundam = pygame.transform.scale(gundam, (300, 500)) 

font = pygame.font.SysFont("Arial", 24, bold=True)

valge = (255, 255, 255)
must = (0, 0, 0)

def joonista_jutumull(ekraan, x, y, laius, korgus, tekst):

    pygame.draw.rect(ekraan, (255, 255, 255), (x, y, laius, korgus))
    pygame.draw.rect(ekraan, (0, 0, 0), (x, y, laius, korgus), 2)

    tekst_pilt = font.render(tekst, True, (0, 0, 0))
    ekraan.blit(tekst_pilt, (x + 10, y + 10))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(taust, (0, 0))
    screen.blit(gundam, (50, 50))

    joonista_jutumull(screen, 270, 50, 280, 60, "I am Gundam RX-78")

    pygame.display.flip()
