import pygame
from time import sleep
import emoji
print("{:=^70}".format("Bem-Vindo Ao Mini Jukebox"))
print("""
Escolha os Artistas ou bandas abaixo para tocar uma música:

(1) The Beatles
(2) Pink Floyd
(3) Tiny Tim
(4) Nirvana
(5) The Who
(6) Paul McCartiney

""")
opUser = int(input("Digite um número da lista: "))
if opUser == 0 or opUser > 6:
    print("Numeração inválida!")
else:
    print(emoji.emojize("Processando...:hourglass_flowing_sand:", use_aliases=True))
    sleep(4)
    print("Divita-se com esse som!")
    if opUser == 1:      
        pygame.init()
        pygame.mixer.music.load("sound/The End.ogg")
        pygame.mixer.music.play()
        print(emoji.emojize("Reproduzindo The Beatles :guitar: :guitar: :violin: :drum:", use_aliases=True))
        sleep(200)
        pygame.event.wait()

    elif opUser == 2:      
        pygame.init()
        pygame.mixer.music.load("sound/Eclips.ogg")
        pygame.mixer.music.play()
        print(emoji.emojize("Reporduzindo Pink Floyd :pig2: :factory: :hammer:", use_aliases=True))
        sleep(200)
        pygame.event.wait()
    elif opUser == 3:
        pygame.init()
        pygame.mixer.music.load("sound/Livi.ogg")
        pygame.mixer.music.play()
        print(emoji.emojize("Reproduzindo Tiny Tim :violin: :tophat: :microphone:", use_aliases=True))
        sleep(200)
        pygame.event.wait()
    elif opUser == 4:
        pygame.init()
        pygame.mixer.music.load("sound/About A Gir.ogg")
        pygame.mixer.music.play()
        print(emoji.emojize("Reporduzindo Nirvana :guitar: :guitar: :drum: :microphone:", use_aliases=True))
        sleep(200)
        pygame.event.wait()      
    elif opUser == 5:
        pygame.init()
        pygame.mixer.music.load("sound/Boris The Spide.ogg")
        pygame.mixer.music.play()
        print(emoji.emojize("Reproduzindo The Who :spider: :guitar: :microphone:", use_aliases=True))
        sleep(200)
        pygame.event.wait()
    else:
        pygame.init()
        pygame.mixer.music.load("sound/Smile Away.ogg")
        pygame.mixer.music.play()
        print(emoji.emojize("Reproduzindo Paul McCartiney :musical_score: :violin: :guitar: :drum: :musical_keyboard:", use_aliases=True))
        sleep(200)
        pygame.event.wait()

