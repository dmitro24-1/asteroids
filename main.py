import pygame
from constants import *
from player import *
from asteroids import *
from asteroidfield import *




def main():
    pygame.init()
    dt = 0
    time = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroids.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    ast_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        updatable.update(dt)
        for ast in asteroids:
            if ast.collision_check(player):
                raise SystemExit("Game Over!")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = time.tick(60) / 1000
        



if __name__ == "__main__":
    try:
        main()
    except SystemExit as a:
        print (a)