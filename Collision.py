import pygame
import random

FPS = 60
SIZE = 30
WIDTH = 1080
HEIGHT = 920


class Object:
    def __init__(self, x, y, x_velocity, y_velocity):
        self.x = x
        self.y = y
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity


class GameView:

    def __init__(self):
        self._objects = []

    def add_object(self, x, y):
        self._objects.append(Object(x, y, random.randint(-5, 5), random.randint(-5, 5)))

    def recoordinate(self):
        for i in self._objects:
            if i.x <= 0 or i.x >= WIDTH - SIZE:
                i.x_velocity = -1 * i.x_velocity
                i.y_velocity = -1 * i.y_velocity
            if i.y <= 0 or i.y >= HEIGHT - SIZE:
                i.x_velocity = -1 * i.x_velocity
                i.y_velocity = -1 * i.y_velocity
            i.x += i.x_velocity
            i.y += i.y_velocity

    def draw(self, screen):
        for i in self._objects:
            pygame.draw.rect(screen, (255, 255, 255), (i.x, i.y, SIZE, SIZE))


class GameWindow:

    def __init__(self):
        # pygame init
        pygame.init()

        # Window
        self._width = WIDTH
        self._height = HEIGHT
        self._title = "Collision"
        self._screen = pygame.display.set_mode([self._width, self._height])
        pygame.display.set_caption(self._title)

        self._view = GameView()

    def mainloop(self):
        finished = False
        clock = pygame.time.Clock()
        while not finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    self._view.add_object(x - SIZE/2, y - SIZE/2)
            self._screen.fill((0, 0, 0))
            self._view.draw(self._screen)
            self._view.recoordinate()
            pygame.display.flip()
            clock.tick(FPS)


def main():
    window = GameWindow()
    window.mainloop()
    print("Stop")


if __name__ == "__main__":
    main()
