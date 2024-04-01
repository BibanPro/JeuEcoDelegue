import pygame
import sys
import time

class ChestOpening:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Trash Hunters")
        icon = pygame.image.load("image/icon.png")
        pygame.display.set_icon(icon)

        self.images = [pygame.image.load(f'image/coffre ({i}).jpg') for i in range(1, 33)]

        # Référence à la classe PersonnageJeu

    def afficher_chargement(self, duree, popup_rect):
        debut = time.time()
        indice_image = 0

        while time.time() - debut < duree:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill((1, 17, 53))  # Fond bleu (vous pouvez changer la couleur)
            image_actuelle = pygame.transform.scale(self.images[indice_image], (500, 500))
            rect = image_actuelle.get_rect(center=popup_rect.center)
            self.screen.blit(image_actuelle, rect.topleft)

            pygame.display.flip()
            self.clock.tick(15)  # Nombre d'images par seconde (vous pouvez ajuster)

            indice_image = (indice_image + 1) % len(self.images)

    def afficher_pop_up(self):
        popup_width = 800
        popup_height = 600
        popup_rect = pygame.Rect((self.screen.get_width() - popup_width) // 2,
                                 (self.screen.get_height() - popup_height) // 2,
                                 popup_width, popup_height)

        self.afficher_chargement(5, popup_rect)  # Appelez la fonction d'animation avec la durée et la position du pop-up
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    chest_opening = ChestOpening()
    chest_opening.afficher_pop_up()




