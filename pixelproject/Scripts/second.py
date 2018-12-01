import pyxel

class App(object):
  def __init__(self, x, y, caption, fps):
    print(f"App(x = {x}, y = {y}, caption = {caption}, fps = {fps})")
    self.pix_x = [0,0]
    self.pix_y = [0,0]
    self.changeUseBox = 0
    pyxel.init(x,y, caption = caption, fps = fps)
    pyxel.run(self.update, self.draw)

  def update(self):
    if pyxel.btnp(pyxel.KEY_SPACE):
      if self.changeUseBox:
        self.changeUseBox = 0
      else:
        self.changeUseBox = 1
    if pyxel.btnp(pyxel.KEY_UP):
      self.pix_y[self.changeUseBox] = (self.pix_y[self.changeUseBox] - 1) % (pyxel.height)
    if pyxel.btnp(pyxel.KEY_DOWN):
      self.pix_y[self.changeUseBox] = (self.pix_y[self.changeUseBox] + 1) % (pyxel.height)
    if pyxel.btnp(pyxel.KEY_LEFT):
      self.pix_x[self.changeUseBox] = (self.pix_x[self.changeUseBox] - 1) % (pyxel.width)
    if pyxel.btnp(pyxel.KEY_RIGHT):
      self.pix_x[self.changeUseBox] = (self.pix_x[self.changeUseBox] + 1) % (pyxel.width)
    if pyxel.btnp(pyxel.KEY_Q):
      pyxel.quit()
    print('Im updating')

  def draw(self):
    pyxel.cls(0)
    pyxel.pix(self.pix_x[0], self.pix_y[0], 1)
    pyxel.pix(self.pix_x[1], self.pix_y[1], 5)
    print('Im drawing')

App( 10, 10,"Moving pixel", 5)