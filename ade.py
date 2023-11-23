import pygame
import time

pygame.init()

genislik = 1300
yukseklik = 700
goruntu_yuzeyi = pygame.display.set_mode((genislik, yukseklik))


class Karakter(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path):
        super().__init__()

        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.hiz = 5


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



class Canavar(pygame.sprite.Sprite):
    def __init__(self, x, y, hiz):
        super().__init__()
        self.image = pygame.image.load("monster (1).png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.hiz = hiz

    def takip_et(self, hedef):
        dx = hedef.rect.centerx - self.rect.centerx
        dy = hedef.rect.centery - self.rect.centery
        uzaklik = (dx**2 + dy**2)**0.5
        if uzaklik != 0:
            self.rect.x += self.hiz * (dx / uzaklik)
            self.rect.y += self.hiz * (dy / uzaklik)

    def update(self):
        pass


karakter = Karakter(genislik - 50, yukseklik - 50, "eb_karakter.jpg")
canavar = Canavar(0, 0, 2)
durum = True
saat = pygame.time.Clock()

while durum:
    for etkinik in pygame.event.get():
        if etkinik.type == pygame.QUIT:
            durum = False

    karakter.update()
    canavar.update()
    canavar.takip_et(karakter)
    goruntu_yuzeyi.fill((0, 0, 0))
    goruntu_yuzeyi.blit(karakter.image, karakter.rect)
    goruntu_yuzeyi.blit(canavar.image, canavar.rect)

    if pygame.sprite.spritecollideany(karakter, [canavar]):
        print("Yenildin!")
        durum = False

    pygame.display.update()
    saat.tick(60)

pygame.quit()

