import pygame
import random


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:

        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))

        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.pos == mole_image.get_rect():
                        x = random.randrange(0, 640)
                        y = random.randrange(0, 512)
                        screen.blit(mole_image, mole_image.get_rect(topleft=(x, y)))
                        pygame.display.flip()

            screen.fill("light green")
            screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))
            for i in range (0, 512, 32):
                pygame.draw.line(screen, "black", (0, i), (640, i))
            for j in range(0, 640, 32):
                pygame.draw.line(screen, "black", (j, 0), (j, 512))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
