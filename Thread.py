from threading import Thread
import affichage
from son import*

sound=Thread(target=musique).start()
window=Thread(target=affichage_grille).start()

