# https://microbit-micropython.readthedocs.io/en/latest/tutorials/music.html

import music

""" music.set_tempo(ticks=100, bpm=10000) """
			
""" for i in range(50):
	for y in range(20):
		music.play(["C4:4", "E4:8"])
	for z in range(20):
		music.play(["B4:4", "D4:8"]) 
"""
music.play(music.NYAN)

""" tune = ["C4:4", "D4:4", "E4:4", "C4:4", "C4:4", "D4:4", "E4:4", "C4:4",
        "E4:4", "F4:4", "G4:8", "E4:4", "F4:4", "G4:8"]

music.play(tune) """

""" for i in range(50):
    for freq in range(880, 1760, 16):
        music.pitch(freq, 6)
    for freq in range(1760, 880, -16):
        music.pitch(freq, 6) """