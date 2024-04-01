import pygame
import sys
import time

class PersonnageJeu:
    def __init__(self):
        # Initialisation de Pygame
        pygame.init()
        pygame.display.set_caption("Trash Hunters")
        icon = pygame.image.load("image\icon.png")
        pygame.display.set_icon(icon)
        pygame.mixer.music.load("son\Jeu_Son.mp3")
        pygame.mixer.music.play(-1)

        # Définition des couleurs
        self.BLANC = (255, 255, 255)
        self.NOIR = (0, 0, 0)

        # Paramètres de la fenêtre
        self.largeur_fenetre = 1200
        self.hauteur_fenetre = 800

        # Paramètres du personnage
        self.taille_personnage = 50
        self.x_personnage = (self.largeur_fenetre - self.taille_personnage) // 2
        self.y_personnage = self.hauteur_fenetre - self.taille_personnage - 200

        # Paramètres des points au sol
        self.points_sol = [(20, self.hauteur_fenetre - 250),(295, self.hauteur_fenetre - 250), (570, self.hauteur_fenetre - 250), (845, self.hauteur_fenetre - 250), (1110, self.hauteur_fenetre - 250)]
        self.rayon_detection = 50

        # Paramètres de déplacement du personnage
        self.vitesse_personnage = 6

        # Chargement des images pour l'animation
        self.animation_images_left = [pygame.image.load(f"image/image_left_{i}.png") for i in range(1, 11)]
        self.animation_images_right = [pygame.image.load(f"image/image_right_{i}.png") for i in range(1, 11)]
        self.image_base = pygame.image.load("image/image_base.png")

        # Redimensionnement des images du personnage
        self.animation_images_left = [pygame.transform.scale(img, (self.taille_personnage, self.taille_personnage)) for img in self.animation_images_left]
        self.animation_images_right = [pygame.transform.scale(img, (self.taille_personnage, self.taille_personnage)) for img in self.animation_images_right]
        self.image_base = pygame.transform.scale(self.image_base, (self.taille_personnage, self.taille_personnage))

        # Initialisation de l'index d'image
        self.image_index = 0

        # Création de la fenêtre
        self.fenetre = pygame.display.set_mode((self.largeur_fenetre, self.hauteur_fenetre))
        pygame.display.set_caption("Personnage en Vue du Dessus")

        # Chargement de l'image pour le bouton
        self.bouton_image = pygame.image.load("image/annuler.png")
        self.bouton_image = pygame.transform.scale(self.bouton_image, (50, 50))
        self.bouton_rect = self.bouton_image.get_rect(topleft=(10, 10))

    # Fonction appelée lorsque le joueur appuie sur Entrée
    def action_entree(self):
        print("Fonction appelée !")

    # Fonction appelée lorsque le bouton est cliqué
    def action_bouton(self):
        pygame.quit()
        from Page_Start import PagePrincipale
        page_principale = PagePrincipale()
        page_principale.run()

    def run(self):
        # Boucle principale
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    # Vérifier si le personnage est à proximité d'un point
                    for point in self.points_sol:
                        distance = pygame.math.Vector2(point[0] - self.x_personnage, point[1] - self.y_personnage).length()
                        if distance < self.rayon_detection:
                            self.action_entree()

                # Gestion du clic de souris
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Clic gauche
                        if self.bouton_rect.collidepoint(event.pos):
                            self.action_bouton()

            # Gestion des touches
            touches = pygame.key.get_pressed()
            if touches[pygame.K_LEFT] and self.x_personnage > 0:
                self.x_personnage -= self.vitesse_personnage
                self.image_index = (self.image_index + 1) % len(self.animation_images_left)
            elif touches[pygame.K_RIGHT] and self.x_personnage < self.largeur_fenetre - self.taille_personnage:
                self.x_personnage += self.vitesse_personnage
                self.image_index = (self.image_index + 1) % len(self.animation_images_right)

            # Dessin de la scène
            self.fenetre.fill(self.NOIR)

            # Dessin du personnage avec l'image d'animation
            if touches[pygame.K_LEFT]:
                self.fenetre.blit(self.animation_images_left[self.image_index], (self.x_personnage, self.y_personnage))
            elif touches[pygame.K_RIGHT]:
                self.fenetre.blit(self.animation_images_right[self.image_index], (self.x_personnage, self.y_personnage))
            else:
                # Si le personnage ne bouge pas, afficher l'image de base
                self.fenetre.blit(self.image_base, (self.x_personnage, self.y_personnage))

            # Dessin des points au sol
            for point in self.points_sol:
                pygame.draw.circle(self.fenetre, self.BLANC, point, 5)

            # Dessin du bouton en haut à gauche
            self.fenetre.blit(self.bouton_image, self.bouton_rect.topleft)
            pygame.display.flip()

            # Limite de la fréquence d'images pour augmenter la vitesse
            pygame.time.Clock().tick(70)  # Ajustez la valeur pour changer la vitesse de l'animation