import random
import pygame
from pygame.locals import *

def on_grid_random():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x //10 * 10, y//10 * 10)

def collision(c1 , c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

#criação do Display
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake')

#posição inicial da cobra
snake = [(200, 200), (210,200), (220,200)]
#Matriz que irá definir o formado e o tamanho da cobra
snake_skin = pygame.Surface((10,10))
snake_skin.fill((255, 255,  255))#RGB da cor branca para a cobra

apple_pos = on_grid_random() #matrz de posição inicial da maça
apple = pygame.Surface((10,10))#matriz que define a maçã
apple.fill((255, 0, 0))#RGB vermelho da maça

my_direction = LEFT

clock = pygame.time.Clock()

#laço infinito
while True:
    clock.tick(20)
    #condição para fechar o game
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            
        #analise de entrada para os comandos
        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_LEFT:
                my_direction = LEFT
            if event.key == K_RIGHT:
                my_direction = RIGHT

    if collision(snake[0], apple_pos): #colisão entre a cobra e a maça
        apple_pos = on_grid_random() #cria uma nova posição aleatoria para a maça
        snake.append((0,0)) #adiciona um novo quadrado (matriz) para a cobra

    for i in range(len(snake) - 1, 0, -1): #toma a posição da calda anterior
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

    #MECANICA DE MOVIMENTAÇÃO DA CABEÇA DA COBRA
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] -10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1] )
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])


    screen.fill((0,0,0))
    screen.blit(apple, apple_pos )
    for pos in snake:
        screen.blit(snake_skin, pos)

    pygame.display.update()