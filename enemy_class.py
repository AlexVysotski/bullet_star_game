import pygame
import random

import bullet_hero


class Enemy(pygame.sprite.Sprite):

    def __init__(self, h, w):
        super().__init__()
        self.h, self.w = h, w
        # загружаем картинку
        self.image = pygame.image.load(f'image/png-transparent-cute-monster.png')  # импортируе картику
        self.image = pygame.transform.rotozoom(self.image, 1, 0.07)
        # создаём кардинаты
        self.rect = self.image.get_rect()
        # задаём расположение врагов в случайном месте
        self.rect.centery = random.randint(0, 300)
        self.rect.centerx = random.randint(0, 800)
        # задём скорость врагам ( 2 варинаты только в низ или вниз + в бок)
        self.speedy = 2
        self.speedx = 1

    def update(self):
        self.move()



    def move(self):

        if self.rect.bottom > self.h:  # если низ коробля , ниже границы экрана
            self.kill()
        if self.rect.right > self.w:
            self.speedx = -1
        if self.rect.left < 0:
            self.speedx = 1

        self.rect.y += self.speedy
        self.rect.x += self.speedx
