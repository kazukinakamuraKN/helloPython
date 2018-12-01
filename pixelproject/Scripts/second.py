import pyxel

class App(object):
  def __init__(self, x, y, caption, fps):
    print(f"App(x = {x}, y = {y}, caption = {caption}, fps = {fps})")
    self.pix = [[0,0],[0,0]]
    self.changeUseBox = 0
    pyxel.init(x,y, caption = caption, fps = fps)
    pyxel.run(self.update, self.draw)

  def update(self):
    if pyxel.btnp(pyxel.KEY_SPACE):
      self.changeUseBox += 1
      if len(self.pix) <= self.changeUseBox:
        self.changeUseBox = 0
    if pyxel.btnp(pyxel.KEY_UP):
      self.pix[self.changeUseBox][1] = (self.pix[self.changeUseBox][1] - 1) % (pyxel.height)
    if pyxel.btnp(pyxel.KEY_DOWN):
      self.pix[self.changeUseBox][1] = (self.pix[self.changeUseBox][1] + 1) % (pyxel.height)
    if pyxel.btnp(pyxel.KEY_LEFT):
      self.pix[self.changeUseBox][0] = (self.pix[self.changeUseBox][0] - 1) % (pyxel.width)
    if pyxel.btnp(pyxel.KEY_RIGHT):
      self.pix[self.changeUseBox][0] = (self.pix[self.changeUseBox][0] + 1) % (pyxel.width)
    if pyxel.btnp(pyxel.KEY_Q):
      pyxel.quit()
    print('Im updating')

  def draw(self):
    pyxel.cls(0)
    pyxel.pix(self.pix[0][0], self.pix[0][1], 1)
    pyxel.pix(self.pix[1][0], self.pix[1][1], 5)
    print('Im drawing')

App( 10, 10,"Moving pixel", 8)