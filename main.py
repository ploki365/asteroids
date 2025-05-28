import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    asteroids = pygame.sprite.Group()

    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)

    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)

        for asteroid in asteroids:
            if player.is_colliding(asteroid):
                print("Game Over!")
                sys.exit(0)

        for asteroid in asteroids:
            for bullet in shots:
                if asteroid.is_colliding(bullet):
                    bullet.kill()
                    asteroid.split()
                    

        screen.fill("black")

        for p in drawable:
            p.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()