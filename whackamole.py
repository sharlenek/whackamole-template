import pygame
import random


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:

        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        mole_rect = mole_image.get_rect(topleft=(random.randrange(0, 640 - mole_image.get_width()), random.randrange(0, 512 - mole_image.get_height())))

        clock = pygame.time.Clock()
        running = True
        position = (0, 0)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:

                    print(f"Mouse clicked at {event.pos}")
                    mouse_x , mouse_y = event.pos
                    mouse_x = (mouse_x // 32) * 32
                    mouse_y = (mouse_y // 32) * 32

                    x, y = position

                    if mouse_x == x and mouse_y == y:
                        print("hi")
                        x = (random.randrange(0, 640) // 32) * 32
                        y = (random.randrange(0, 512) // 32) * 32

                        position = x,y



            screen.fill("light green")

            screen.blit(mole_image, mole_image.get_rect(topleft=(position)))
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