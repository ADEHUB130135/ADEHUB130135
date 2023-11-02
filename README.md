import pygame
import random

pygame.init()

genislik = 1350
yukseklik = 750
goruntu_yuzeyi = pygame.display.set_mode((genislik, yukseklik))

FPS = 30
saat = pygame.time.Clock()
class Oyuncu(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("hair.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = genislik // 2
        self.rect.bottom = yukseklik

        self.can = 5
        self.jokerler = 2
        self.hiz = 8

    def update(self):
        tuslar = pygame.key.get_pressed()
        if tuslar[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.hiz
        if tuslar[pygame.K_RIGHT] and self.rect.right < genislik:
            self.rect.x += self.hiz
        if tuslar[pygame.K_UP] and self.rect.top > 100:
            self.rect.y -= self.hiz
        if tuslar[pygame.K_DOWN] and self.rect.bottom < yukseklik - 100:
            self.rect.y += self.hiz

    def joker(self):
        if self.jokerler > 0:
            self.jokerler -= 1
            self.rect.bottom = yukseklik

    def yenileme(self):
        self.rect.centerx = genislik // 2
        self.rect.bottom = yukseklik


class Canavar(pygame.sprite.Sprite):
    def __init__(self, x, y, image, canavar_tipi):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.type = canavar_tipi

        self.dx = random.choice([-1, 1])
        self.dy = random.choice([-1, 1])
        self.hiz = random.randint(1, 5)

    def update(self):
        self.rect.x += self.dx * self.hiz
        self.rect.y += self.dy * self.hiz

        if self.rect.left <= 0 or self.rect.right >= genislik:
            self.dx = -1 * self.dx
        if self.rect.top <= 100 or self.rect.bottom >= yukseklik - 100:
            self.dy = -1 * self.dy
class Oyuncu(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("hair.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = genislik // 2
        self.rect.bottom = yukseklik

        self.can = 5
        self.jokerler = 2
        self.hiz = 8

    def update(self):
        tuslar = pygame.key.get_pressed()
        if tuslar[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.hiz
        if tuslar[pygame.K_RIGHT] and self.rect.right < genislik:
            self.rect.x += self.hiz
        if tuslar[pygame.K_UP] and self.rect.top > 100:
            self.rect.y -= self.hiz
        if tuslar[pygame.K_DOWN] and self.rect.bottom < yukseklik - 100:
            self.rect.y += self.hiz

    def joker(self):
        if self.jokerler > 0:
            self.jokerler -= 1
            self.rect.bottom = yukseklik

    def yenileme(self):
        self.rect.centerx = genislik // 2
        self.rect.bottom = yukseklik


class Canavar(pygame.sprite.Sprite):
    def __init__(self, x, y, image, canavar_tipi):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.type = canavar_tipi

        self.dx = random.choice([-1, 1])
        self.dy = random.choice([-1, 1])
        self.hiz = random.randint(1, 5)

    def update(self):
        self.rect.x += self.dx * self.hiz
        self.rect.y += self.dy * self.hiz

        if self.rect.left <= 0 or self.rect.right >= genislik:
            self.dx = -1 * self.dx
        if self.rect.top <= 100 or self.rect.bottom >= yukseklik - 100:
            self.dy = -1 * self.dy
oyuncu_grubum = pygame.sprite.Group()
oyuncum = Oyuncu()
oyuncu_grubum.add(oyuncum)

canavar_grubum = pygame.sprite.Group()

oyunum = Oyun(oyuncum, canavar_grubum)
oyunum.yeni_round_baslama()

durum = True
while durum:
    for etkinik in pygame.event.get():
        if etkinik.type == pygame.QUIT:
            durum = False
        if etkinik.type == pygame.KEYDOWN:
            if etkinik.key == pygame.K_SPACE:
                oyuncum.joker()

    goruntu_yuzeyi.fill((0, 0, 50))

    oyuncu_grubum.update()
    oyuncu_grubum.draw(goruntu_yuzeyi)

    canavar_grubum.update()
    canavar_grubum.draw(goruntu_yuzeyi)

    oyunum.update()
    oyunum.cizmek()

    pygame.display.update()
    saat.tick(FPS)

pygame.quit()
