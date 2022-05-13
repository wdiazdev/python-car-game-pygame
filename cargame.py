from turtle import left
import pygame
from pygame.locals import *
import random

size = width, height = (800, 800)
road_w = int(width/1.6)
roadmark_w = int(width/80)
right_lane = width/2 - road_w/4
left_lane = width/2 + road_w/4
speed = 1

pygame.init()
running = True
# Set window size
screen = pygame.display.set_mode(size)
# Set Title
pygame.display.set_caption("Furious Car Game")
# Set background color
screen.fill((116, 165, 77))

# Apply changes
pygame.display.update()

# User car image
user_car = pygame.image.load("red car.png")
usercar_location = user_car.get_rect()
usercar_location.center = (right_lane, height * 0.8)
# Enemy car
enemy_car = pygame.image.load("enemy car.png")
enemy_car_location = enemy_car.get_rect()
enemy_car_location.center = (left_lane, height * 0.2)

counter = 0
# Game loop
while running:
    counter += 1
    if counter == 5000:
        speed += 0.15
        counter = 0
        print("Level up", speed)

    # Enemy vehicle animation
    # Enemy vehicle one pixel down
    enemy_car_location[1] += speed
    # For enemy vehicle to keep moving down
    if enemy_car_location[1] > height:
        # Random enemy vehicle movement
        if random.randint(0,1) == 0:
            enemy_car_location.center = right_lane, -200
        else:
            enemy_car_location.center = left_lane, -200
    # End game condition
    if usercar_location[0] == enemy_car_location[0] and enemy_car_location[1] > usercar_location[1] -250:
        print("GAME OVER")
        break

    # Event listeners
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            #  Left turn
            if event.key in [K_a, K_LEFT]:
                usercar_location = usercar_location.move([-int(road_w/2), 0])
            # Right turn    
            if event.key in [K_d, K_RIGHT]:
                usercar_location = usercar_location.move([int(road_w/2), 0])

    # Draw Road
    pygame.draw.rect(screen, (44, 47, 51), (width/2 - road_w/2, 0, road_w, height))
    # Draw roadmark
    pygame.draw.rect(screen, (255, 240, 60), (width/2 - roadmark_w/2, 0, roadmark_w, height))
    # Roda lines - white
    pygame.draw.rect(screen, (255, 255, 255), (width/2 - road_w/2 + roadmark_w * 2, 0, roadmark_w, height))
    pygame.draw.rect(screen, (255, 255, 255), (width/2 + road_w/2 - roadmark_w * 3, 0, roadmark_w, height))

    screen.blit(user_car, usercar_location)
    screen.blit(enemy_car, enemy_car_location)
    pygame.display.update()


pygame.quit()