from pygame import mixer
mixer.init()
mixer.music.load('recaida.mp3')
mixer.music.play()
mixer.event.wait()