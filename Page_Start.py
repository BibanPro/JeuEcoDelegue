import pygame
import sys
import time
from Inventaire_Boutique import *

nb_coffre = 1
inventaire_joueur = Inventaire()
boutique = Boutique()

class PagePrincipale:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("son\Jeu_Son.mp3")
        pygame.mixer.music.play(-1)

        # Définition des constantes
        SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 800
        self.screen = pygame.display.set_mode((1200, 800))

        pygame.display.set_caption("Trash Hunters")
        icon = pygame.image.load("image\icon.png")
        pygame.display.set_icon(icon)

        self.clock = pygame.time.Clock()
        self.nb_coffre = nb_coffre
        self.couleur_fond = (0, 0, 0)  # Noir

        self.coffre_image = pygame.image.load("image/coffre.png")
        self.coffre_image = pygame.transform.scale(self.coffre_image, (350, 350))  # Redimensionner l'image si nécessaire
        self.coffre_position = (40, 200)

        self.tune = inventaire_joueur.eco_euros
        self.images = {
            "parametre": pygame.transform.scale(pygame.image.load("image/Paramètres.png"), (124, 124)),
            "casier": pygame.transform.scale(pygame.image.load("image/Cintre.png"), (100, 100)),
            "boutique": pygame.transform.scale(pygame.image.load("image/Boutique.png"), (100, 100)),
            "personnage": pygame.transform.scale(pygame.image.load("image/Personnage.png"), (400, 400)),
            "personnage_2": pygame.transform.scale(pygame.image.load("image/Personnage_2.png"), (400, 400)),
            "jouer": pygame.transform.scale(pygame.image.load("image/bouton-jouer.png"), (200, 200)),
            "valider": pygame.transform.scale(pygame.image.load("image/verifie.png"), (40, 40)),
            "fleche_gauche": pygame.transform.scale(pygame.image.load("image/Suivant2.png"), (50, 50)),
            "fleche_droite": pygame.transform.scale(pygame.image.load("image/Suivant.png"), (50, 50)),
            "piece": pygame.transform.scale(pygame.image.load("image/piece.png"), (50, 50)),
            "button": pygame.transform.scale(pygame.image.load("image/plus.png"), (30, 30))
        }

        self.current_personnage = "personnage"

        self.boutons = {
            "coffre": pygame.Rect(40, 200, 350, 350),
            "parametre": pygame.Rect(10, 10, 124, 124),
            "casier": pygame.Rect(10, SCREEN_HEIGHT - 160, 100, 100),
            "boutique": pygame.Rect(120, SCREEN_HEIGHT - 160, 100, 100),
            "jouer": pygame.Rect(SCREEN_WIDTH - 250, SCREEN_HEIGHT - 250, 200, 200),
            "fleche_gauche": pygame.Rect(SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT - 300, 50, 50),
            "fleche_droite": pygame.Rect(SCREEN_WIDTH // 2 + 125, SCREEN_HEIGHT - 300, 50, 50),
            "saisie": pygame.Rect(SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT - 500, 300, 40),
            "valider": pygame.Rect(SCREEN_WIDTH - 490, SCREEN_HEIGHT - 500, 300, 40),
        }

        self.couleurs = {
            "parametre": self.couleur_fond,
            "boutique": (252, 126, 44),
            "casier": (212, 232, 57),
            "survol": (200, 200, 200),
        }

        self.pseudo_input = ""

        self.gif = pygame.image.load("image/Titre.gif")
        self.gif_rect = self.gif.get_rect(center=(SCREEN_WIDTH // 2, 136))

        # Chargement de l'image "piece.png" et redimensionnement
        self.piece_image = pygame.image.load("image/piece.png")
        self.piece_image = pygame.transform.scale(self.piece_image, (50, 50))
        self.piece_rect = self.piece_image.get_rect()

        # Chargement de l'image "plus.png" pour le bouton
        self.button_image = pygame.image.load("image/plus.png")
        self.button_image = pygame.transform.scale(self.button_image, (30, 30))
        self.button_rect = self.button_image.get_rect()

        # Police de texte
        self.font = pygame.font.Font(None, 30)  # Réduire la taille de la police

        # Création de la zone de texte
        self.text_surface = self.font.render(f"{self.tune}" , True, (0, 0, 0))
        self.text_rect = self.text_surface.get_rect()

        # Positionnement des éléments dans une barre en haut à droite
        self.bar_rect = pygame.Rect(SCREEN_WIDTH - 180, 10, 170, 50)
        self.text_rect.midtop = (self.bar_rect.centerx - 50, self.bar_rect.centery - 10)
        self.piece_rect.midtop = (self.bar_rect.centerx + 10, self.bar_rect.centery - 25)
        self.button_rect.midtop = (self.bar_rect.centerx + 55, self.bar_rect.centery - 15)
        self.images_coffre = [pygame.image.load(f'image/coffre ({i}).jpg') for i in range(1, 33)]

    def ouvrir_parametre(self):
        print("Ouverture des paramètres")

    def ouvrir_casier(self):
        print("Ouverture du casier")

    def ouvrir_boutique(self):
        from Boutique import PageBoutique
        Lance_page4 = PageBoutique()
        Lance_page4.run()

    def open_coffre(self):
        if nb_coffre >= 1:
            self.afficher_pop_up()

    def lancer_jeu(self):
        from Chargement import ChargementGraphique

        Lance_page2 = ChargementGraphique()
        Lance_page2.afficher_chargement(3)

        from Choix_Niveau import PersonnageJeu

        Lance_page3 = PersonnageJeu()
        Lance_page3.run()

    def valider_pseudo(self):
        print(f"Pseudo validé : {self.pseudo_input}")

    def afficher_chargement(self, duree, popup_rect=None):
        debut = time.time()
        indice_image = 0

        while time.time() - debut < duree:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if popup_rect:
                image_actuelle = pygame.transform.scale(self.images.get(indice_image, pygame.Surface((500, 500))), (500, 500))
                rect = image_actuelle.get_rect(center=popup_rect.center)
                self.screen.blit(image_actuelle, rect.topleft)
            else:
                image_actuelle = self.images[indice_image]
                rect = image_actuelle.get_rect(center=self.screen.get_rect().center)
                self.screen.blit(image_actuelle, rect.topleft)

            pygame.display.flip()
            self.clock.tick(15)  # Nombre d'images par seconde

            # Traiter les événements pendant l'animation
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            print(f"Affichage de l'image {indice_image}")
            indice_image = (indice_image + 1) % len(self.images)


    def afficher_pop_up(self):
        popup_width = 800
        popup_height = 600
        popup_rect = pygame.Rect((self.screen.get_width() - popup_width) // 2,
                                 (self.screen.get_height() - popup_height) // 2,
                                 popup_width, popup_height)

        self.afficher_chargement(3, popup_rect)  # Appelez la fonction d'animation avec la durée et la position du pop-up
        return


    def run(self):
        font_size = 72
        font = pygame.font.Font(None, font_size)  # Modifié la taille de la police

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for bouton, rect in self.boutons.items():
                        if rect.collidepoint(event.pos):
                            if bouton == "valider":
                                self.valider_pseudo()
                            elif bouton == "fleche_gauche":
                                self.current_personnage = "personnage"
                            elif bouton == "fleche_droite":
                                self.current_personnage = "personnage_2"
                            elif bouton == "jouer":
                                self.lancer_jeu()
                            elif bouton == "plus":
                                self.ouvrir_boutique()
                            elif bouton == "coffre":
                                self.open_coffre()
                            elif bouton == "saisie":
                                pass
                            else:
                                getattr(self, f"ouvrir_{bouton}")()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.pseudo_input = self.pseudo_input[:-1]
                    elif event.key == pygame.K_RETURN:
                        self.valider_pseudo()
                    else:
                        if len(self.pseudo_input) < 10:
                            self.pseudo_input += event.unicode

            self.screen.fill(self.couleur_fond)

            # Blit the GIF at the top center of the screen
            self.screen.blit(self.gif, self.gif_rect)

            # Affichage du personnage en bas de la page
            self.screen.blit(self.images[self.current_personnage], (self.screen.get_width() // 2 - 200, self.screen.get_height() - 400))

            for bouton, rect in self.boutons.items():
                if bouton != "saisie":
                    pygame.draw.rect(self.screen, self.couleurs.get(bouton, self.couleur_fond),
                                    rect if rect.collidepoint(pygame.mouse.get_pos()) else rect)
                    if bouton in self.images:  # Check if the key exists in the images dictionary
                        self.screen.blit(self.images[bouton], rect.topleft)

            # Affichage de la zone de texte pour le pseudo
            pygame.draw.rect(self.screen, (255, 255, 255), self.boutons["saisie"])  # Zone de texte
            pseudo_text = font.render(f"{self.pseudo_input}", True, (0, 0, 0))  # Pas de préfixe
            self.screen.blit(pseudo_text, (self.screen.get_width() // 2 - pseudo_text.get_width() // 2, self.boutons["saisie"].y + 5))

            # Affichage de la barre en haut à droite
            pygame.draw.rect(self.screen, (255, 255, 255), self.bar_rect)

            self.screen.blit(self.coffre_image, self.coffre_position)


            # Affichage des éléments dans la barre en haut à droite
            self.screen.blit(self.text_surface, self.text_rect)
            self.screen.blit(self.piece_image, self.piece_rect)
            self.screen.blit(self.button_image, self.button_rect)
            self.clock.tick(60)
            pygame.display.flip()

            # Réduire la taille de la police lors de la saisie du pseudo
            if len(self.pseudo_input) > 0:
                font_size = 48
                font = pygame.font.Font(None, font_size)

if __name__ == "__main__":
    page_principale = PagePrincipale()
    page_principale.run()

