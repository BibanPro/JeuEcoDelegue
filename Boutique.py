import pygame
import sys
from Inventaire_Boutique import *

inventaire_joueur = Inventaire()
boutique = Boutique()

class PageBoutique:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
##        pygame.mixer.music.load("son\Jeu_Son.mp3")
##        pygame.mixer.music.play(-1)

        # Définition des constantes
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 1200, 800

        self.ecran = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Boutique")
        icon = pygame.image.load("image\icon.png")
        pygame.display.set_icon(icon)

        self.bouton_achat = pygame.image.load("image/achat.png")  # Remplacez le chemin par votre image de bouton
        self.bouton_rect = self.bouton_achat.get_rect()
        self.clock = pygame.time.Clock()

        self.couleur_fond = (0, 0, 0)  # Noir

        # Liste des skins avec leurs prix
        self.skins = [
            {"nom": "Ekko", "prix": 00},
            {"nom": "Greta Thunberg", "prix": 100},
            {"nom": "Groot", "prix": 200},
            {"nom": "Aquaman", "prix": 200},
            {"nom": "Neytiri", "prix": 299},
            {"nom": "Pomona Chourave", "prix": 299},
            {"nom": "Hashirama", "prix": 299},
            {"nom": "Wall-e", "prix": 299, "rarete": 3},
            {"nom": "Mr Beast", "prix": 299},
            {"nom": "Wonder woman", "prix": 299},
            # Ajoutez autant de skins que nécessaire
        ]
        self.tune = inventaire_joueur.eco_euros
        self.scroll_position = 0
        self.scroll_speed = 20
        self.selected_skin = None

        self.police = pygame.font.Font(None, 36)
        # Chargement de l'image pour le bouton
        self.bouton_image = pygame.image.load("image/annuler.png")
        self.bouton_image = pygame.transform.scale(self.bouton_image, (50, 50))
        self.bouton_rect = self.bouton_image.get_rect(topright=(600, 600))
        # Dessin du bouton en haut à gauche
        self.ecran.blit(self.bouton_image, self.bouton_rect.topright)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.check_buttons_click(event.pos)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.scroll_position += self.scroll_speed
            elif keys[pygame.K_DOWN]:
                self.scroll_position -= self.scroll_speed

            self.ecran.fill(self.couleur_fond)

            self.draw_skins()

            pygame.display.flip()
            self.clock.tick(60)  # Ajustez la fréquence d'images au besoin

        pygame.quit()
        sys.exit()

    def draw_skins(self):
        max_visible_skins = 7
        total_skins = len(self.skins)

        # Calculer la position maximale et minimale de défilement
        max_scroll_position = 0
        min_scroll_position = -(total_skins - max_visible_skins) * 100

        # Limiter la position de défilement
        self.scroll_position = max(min(self.scroll_position, max_scroll_position), min_scroll_position)

        for i in range(total_skins):
            y = i * 100 + self.scroll_position

            # Vérifier si le skin est visible à l'écran
            if -100 <= y <= self.SCREEN_HEIGHT:
                skin = self.skins[i]

                # Utiliser des rectangles avec des bords arrondis pour le skin
                rect_skin = pygame.Rect(50, y, 700, 80)
                pygame.draw.rect(self.ecran, (200, 200, 200), rect_skin, border_radius=10)

                texte_nom = self.police.render(skin["nom"], True, (0, 0, 0))
                self.ecran.blit(texte_nom, (100, y + 20))

                texte_prix = self.police.render(f"Prix: {skin['prix']} coins", True, (0, 0, 0))
                self.ecran.blit(texte_prix, (500, y + 20))

                # Dessiner le bouton "Acheter"
                self.bouton_rect.topleft = (700, y + 20)
                self.ecran.blit(self.bouton_achat, self.bouton_rect)

                # Si un skin est sélectionné, dessiner une bordure autour de celui-ci
                if self.selected_skin == i:
                    pygame.draw.rect(self.ecran, (255, 0, 0), rect_skin, 3, border_radius=10)

        # Dessiner le gros bouton à droite
        gros_bouton_rect = pygame.Rect(800, 300, 200, 100)
        pygame.draw.rect(self.ecran, (255, 20, 147), gros_bouton_rect, border_radius=10)  # Couleur verte
        texte_gros_bouton = self.police.render("Acheter vie", True, (255, 255, 255))
        self.ecran.blit(texte_gros_bouton, (820, 330))

    def check_buttons_click(self, mouse_pos):
        # Vérifier la collision avec le bouton "Acheter tout"
        gros_bouton_rect = pygame.Rect(800, 300, 200, 100)
        if gros_bouton_rect.collidepoint(mouse_pos):
            self.acheter_tout()
            return

        # Vérifier la collision avec le bouton d'achat de skin
        for i, skin in enumerate(self.skins):
            y = i * 100 + self.scroll_position
            rect_skin = pygame.Rect(50, y, 700, 80)
            if rect_skin.collidepoint(mouse_pos):
                self.selected_skin = i
                self.acheter_skin(i)
                return

    def acheter_tout(self):
        page_achat_vie = PageAchatVie(self.ecran, self.clock)
        page_achat_vie.run()

    def acheter_skin(self, index):
        boutique.acheter_skin(inventaire_joueur, boutique.skins_disponibles[index]) # Utilisez le nom du skin et la rareté associée

class LabelAchatVie:
    def __init__(self, ecran, police, label_principal):
        self.ecran = ecran
        self.police = police
        self.label_principal = label_principal
        self.texte1 = ""
        self.texte2 = ""
        self.texte3 = ""
        self.temps_affichage = 0
        self.temps_affichage_max = 5  # Durée d'affichage en secondes

    def afficher_message(self, message1, message2, message3):
        self.texte1 = message1
        self.texte2 = message2
        self.texte3 = message3
        self.temps_affichage = time.time()

inventaire_joueur = Inventaire()
boutique = Boutique()







































import pygame
from pygame.locals import QUIT

class PageAchatVie:
    def __init__(self, ecran, clock):
        self.ecran = ecran
        self.clock = clock
        self.couleur_fond = (0, 0, 0)
        self.bouton_achat = pygame.image.load("image/Coeur.png")
        self.bouton_achat = pygame.transform.scale(self.bouton_achat, (200, 200))
        self.bouton_rect_gauche = pygame.Rect(100, 300, 200, 200)
        self.bouton_rect_droite = pygame.Rect(900, 300, 200, 200)
        self.police = pygame.font.Font(None, 36)
        self.couleur_gauche = (255, 0, 0)
        self.couleur_droite = (0, 0, 255)
        self.clic_gauche = False
        self.clic_droite = False
        self.prix_vie = 50
        self.nombre_vies = 3
        self.bouton_image = pygame.image.load("image/annuler.png")
        self.bouton_image = pygame.transform.scale(self.bouton_image, (50, 50))
        self.bouton_rect_annuler = self.bouton_image.get_rect(topleft=(10, 10))

    def action_annuler(self):
        pygame.quit()
        from Page_Start import PagePrincipale
        page_principale = PagePrincipale()
        page_principale.run()

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.bouton_rect_gauche.collidepoint(event.pos) and not self.clic_gauche:
                            self.clic_gauche = True
                            self.couleur_gauche = (0, 255, 0)
                            self.acheter_vie_1()
                        elif self.bouton_rect_droite.collidepoint(event.pos) and not self.clic_droite:
                            self.clic_droite = True
                            self.couleur_droite = (0, 255, 0)
                            self.acheter_vie()
                        elif self.bouton_rect_annuler.collidepoint(event.pos):
                            self.action_annuler()

            self.ecran.fill(self.couleur_fond)

            pygame.draw.rect(self.ecran, self.couleur_gauche, self.bouton_rect_gauche)
            pygame.draw.rect(self.ecran, self.couleur_droite, self.bouton_rect_droite)
            self.ecran.blit(self.bouton_achat, self.bouton_rect_gauche)
            self.ecran.blit(self.bouton_achat, self.bouton_rect_droite)
            self.ecran.blit(self.bouton_image, self.bouton_rect_annuler.topleft)

            texte_prix = self.police.render(f"Prix: 20 HP {self.prix_vie} coins", True, (255, 255, 255))
            texte_vies = self.police.render(f"Prix: Full HP 200", True, (255, 255, 255))
            self.ecran.blit(texte_prix, (100, 550))
            self.ecran.blit(texte_vies, (900, 550))

            pygame.display.flip()
            self.clock.tick(60)

    def acheter_vie(self):
        print("Vous gagnez 100hp(1vie)")

    def acheter_vie_1(self):
        print("Vous gagnez 20hp")

if __name__ == "__main__":
    page_boutique = PageBoutique()
    page_boutique.run()

