# Créé par Alicia Canovas-Andri, le 06/12/2023 en Python 3.7
import pygame
import sys
import time

class ChargementGraphique:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Trash Hunters")
        icon = pygame.image.load("image/icon.png")
        pygame.display.set_icon(icon)

        self.images = [pygame.image.load(f'image/chargement_{i}.png') for i in range(1, 17)]

        # Charger l'image pour le bouton
        self.bouton_image = pygame.image.load("image/annuler.png")
        self.bouton_image = pygame.transform.scale(self.bouton_image, (70, 70))
        self.bouton_rect = self.bouton_image.get_rect(topleft=(10, 10))

        # Référence à la classe PersonnageJeu
        self.personnage_jeu = None

    def afficher_chargement(self, duree):
        debut = time.time()
        indice_image = 0

        while time.time() - debut < duree:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill((1, 17, 53))  # Fond bleu (vous pouvez changer la couleur)
            image_actuelle = self.images[indice_image]
            rect = image_actuelle.get_rect(center=self.screen.get_rect().center)
            self.screen.blit(image_actuelle, rect.topleft)

            # Dessiner le bouton
            self.screen.blit(self.bouton_image, self.bouton_rect.topleft)

            pygame.display.flip()
            self.clock.tick(20)  # Nombre d'images par seconde (vous pouvez ajuster)

            indice_image = (indice_image + 1) % len(self.images)

            # Détecter le clic sur le bouton
            if pygame.mouse.get_pressed()[0]:
                if self.bouton_rect.collidepoint(pygame.mouse.get_pos()):
                    self.lancer_personnage_jeu()

        pygame.quit()  # Fermer la fenêtre Pygame


    def lancer_personnage_jeu(self):
        pygame.quit()
        from Page_Start import PagePrincipale
        page_principale = PagePrincipale()
        page_principale.run()