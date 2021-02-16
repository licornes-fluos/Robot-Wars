# Robot-Wars
projet de nsi 2020-2021

Robot Wars (nom temporaire?)
 - jeu en 2D top-down à 2 joueurs sur le même clavier (WASD/ZQSD et flèches directionnelles ou personnalisé)
 - 2 robots contrôlés par chaque joueur se battent jusqu'à ce que l'un perde
 - système d'attaques et de défenses dans le sens vers lequel le robot regarde


## Projet de base
 - Déterminer une carte 2D top-down (grille)
 - Programmer les touches pour bouger x2
 - Faire apparaître les personnages
 - Touche pour attaque de bases (bombe) x2 (où la bombe va quand on la pose, combien de dégâts, force de la bombe -1 case dans tous les sens-)
 - Vie du perso et dégâts de la bombe

## Répartition des rôles
 - Aline: s'occupe de prgrammer la carte
 - Rachel: s'occupe des personnages
 - Vazgen: s'occupe du temps de vie et dégâts
 - Yuko: s'occupe des attaques
 
## Needed to run:
 - latest main file (**main5.0.py**)
 - assets folder

## Difficultés
 ### passé
 - problèmes de touches (claviers qwerty, azerty)
 - mise en place des attentes esthétiques
 - débugger le mouvement main 4
 - fusionner les versions main 3 et 4
 
 ### présent
 - faire fonctionner les modules
 - developper les premières mécaniques de jeu
 - faire apparaitre du texte dans le jeu pour changer les touches (au lieu du shell)
 - trouver un moyen d'adapter la fenêtre selon la résolution de l'écran (sinon elle peut être trop grande)
 
 ### futur
 - jouer et s'assurer que le gameplay est amusant/jouable
 
 ## Aspects techniques
 Nous avons basé notre programme sur la librairie pygame, mais nous avons aussi utilisé la librairie time. Pour ce qui est de la construction du code, on a un code principal qui s'appelle 'main' (avec . et un nombre selon l'avancement et les options du jeu). A partir de là, nous avons créé un module pour les sprites qui s'appelle 'sprite' et nous voulons en créer d'autres pour les différentes parties du programme (comme les bombes et la barre de vie par exemple). Il y a un fichier, 'assets', qui contient les fonds d'écrans du jeu et les images dont nous avons besoin.

### barre_vie appartient à Vazgen
