import pyxel

pyxel.init(160,160,caption='hello Pyxel')

def update():
	print("Updating values and objects")
	
def draw():
	print("What to draw on the screen!")
	pyxel.cls(0)
	pyxel.pix(80,80,11)
	
pyxel.run(update,draw)