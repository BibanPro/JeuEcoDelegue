class Boutique:
    def __init__(self):
        # Liste de tuples représentant les skins disponibles à l'achat (nom, rareté)
        self.skins_disponibles = [
            ("Ekko", 1),
            ("Greta Thunberg", 1),
            ("Groot", 2),
            ("Aquaman", 2),
            ("Neytiri", 3),
            ("Pomona Chourave", 3),
            ("Hashirama", 3),
            ("Wall-e", 3),
            ("Mr Beast", 3),
            ("Wonder woman", 3),
            # Ajoutez d'autres skins avec leurs caractéristiques au besoin
        ]

        # Dictionnaire des valeurs en éco-euros pour chaque rareté
        self.valeurs_raretes = {1: 100, 2: 200, 3: 299}

    def afficher_skins_disponibles(self, inventaire):
        """Affiche les skins disponibles à l'achat, en excluant ceux déjà possédés."""
        for skin in self.skins_disponibles:
            nom, rarete = skin
            prix = self.valeurs_raretes[rarete]
            if skin not in inventaire.recuperer_skins_possedes():
                print(f"{nom} - Rareté {rarete} - Prix : {prix} eco-euros")

    def acheter_skin(self, inventaire, skin_a_acheter):
        """Permet au joueur d'acheter un skin et l'ajoute à son inventaire."""
        skin_nom, skin_rarete = skin_a_acheter
        skin_trouve = next((skin for skin in self.skins_disponibles if skin[0] == skin_nom and skin[1] == skin_rarete), None)

        if skin_trouve and skin_a_acheter not in inventaire.recuperer_skins_possedes():
            prix = self.valeurs_raretes[skin_rarete]
            if inventaire.eco_euros >= prix:
                inventaire.eco_euros -= prix
                inventaire.ajouter_skin(skin_a_acheter)
                print(f"Vous avez acheté le skin {skin_nom} de rareté {skin_rarete} pour {prix} eco-euros.")
                print(inventaire.eco_euros)
            else:
                print(f"Vous n'avez pas assez d'argent pour acheter le skin {skin_nom}.")
        else:
            print("Le skin n'est pas disponible à l'achat ou vous le possédez déjà.")


class Inventaire:
    def __init__(self):
        self.skins_possedes = [("Ekko", 1)]
        self.eco_euros = 500  # Ajout de l'attribut eco_euros

    def ajouter_skin(self, skin):
        """Ajoute un skin à l'inventaire."""
        self.skins_possedes.append(skin)

    def recuperer_skins_possedes(self):
        """Renvoie la liste des skins possédés par le joueur."""
        return self.skins_possedes

# Exemple d'utilisation
inventaire_joueur = Inventaire()
boutique = Boutique()
##
##print("Skins disponibles à l'achat :")
##boutique.afficher_skins_disponibles(inventaire_joueur)

##print("\nAchat d'un skin :")
##boutique.acheter_skin(inventaire_joueur, boutique.skin_disponibles[i])
##
print("\nInventaire du joueur :")
for skin in inventaire_joueur.recuperer_skins_possedes():
    print(skin)

##print(f"{inventaire_joueur.eco_euros}")

import random

class CaseOpening:
    def __init__(self, inventaire, boutique):
        self.inventaire = inventaire
        self.boutique = boutique

    def recuperer_skins_utilises(self):
        """Renvoie la liste des skins déjà possédés par le joueur."""
        return self.inventaire.recuperer_skins_possedes()

    def ouvrir_case(self):
        """Effectue le tirage aléatoire en fonction des taux de drop et renvoie le skin gagné."""
        # Récupère les pourcentages de drop pour chaque rareté
        pourcentages_rarete = self.boutique.pourcentages_rarete

        raretes_cumulees = 0
        rareté_gagnante = None
        rarete_trouvee = False

        # S'assure que la somme des pourcentages est égale à 100
        total_pourcentages = sum(pourcentages_rarete.values())
        pourcentages_rarete = {rarete: pourcentage / total_pourcentages * 100 for rarete, pourcentage in pourcentages_rarete.items()}
        print(pourcentages_rarete)

        # Génère un nombre aléatoire entre 1 et 100
        random_value_rarete = random.randint(1, 100)
        print(random_value_rarete)

        # Trouve la rareté gagnante en fonction du nombre aléatoire
        for rarete, pourcentage in pourcentages_rarete.items():
            raretes_cumulees += pourcentage
            if not rarete_trouvee and random_value_rarete <= raretes_cumulees:
                rarete_gagnante = rarete
                rarete_trouvee = True

        print(rarete_gagnante)


        if rarete_gagnante:
            # Filtrer les skins disponibles uniquement pour la rareté gagnante
            skins_rarete_gagnante = [(skin, rarete) for skin, rarete in self.boutique.skins_disponibles if rarete == rarete_gagnante]


            # Filtrer les skins disponibles uniquement pour la rareté gagnante
            skins_rarete_gagnante = [(skin, rarete) for skin, rarete in self.boutique.skins_disponibles if rarete == rarete_gagnante]

            # Génère un nombre aléatoire entre 0 et le nombre de skins dans la rareté gagnante - 1
            random_value_skin = random.randint(0, len(skins_rarete_gagnante) - 1)

            # Trouve le skin gagnant en fonction du nombre aléatoire
            skin_gagnant = skins_rarete_gagnante[random_value_skin]

            if skin_gagnant:
                skin, rarete = skin_gagnant
                if skin_gagnant in self.recuperer_skins_utilises():
                    # Si le joueur a déjà le skin, gagne 50 % de son prix en éco-euros
                    prix_original = self.boutique.valeurs_raretes[rarete]
                    gain_eco_euros = prix_original // 2
                    self.inventaire.eco_euros += gain_eco_euros
                    return f"Vous avez gagné le skin {skin} de rareté {rarete}! Vous avez déjà ce skin, vous gagnez {gain_eco_euros} eco-euros."
                else:
                    self.inventaire.ajouter_skin(skin_gagnant)
                    # Si le joueur n'a pas déjà le skin, affiche le message standard de gain
                    return f"Vous avez gagné le skin {skin} de rareté {rarete}!"
        # Si aucune rareté gagnante, cela ne devrait pas se produire normalement
        return "Aucun skin gagné cette fois-ci."



# Modifie les pourcentages de drop pour chaque rareté
boutique.pourcentages_rarete = {
    1: 70,
    2: 20,
    3: 10
}


##case_opening = CaseOpening(inventaire_joueur, boutique)
##
##print("\nOuverture d'une case :")
##print(case_opening.ouvrir_case())
##print(f"\nArgent restant : {inventaire_joueur.eco_euros} eco-euros.")
##for skin in inventaire_joueur.recuperer_skins_possedes():
##    print(skin)
