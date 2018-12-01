import pyxel

class App(object):
  def __init__(self,x , y, caption, fps):
    print(f"App(x = {x}, y = {y}, caption = {caption}, fps = {fps})")
    self.pix_x = int(x / 2)
    self.pix_y = int(y / 2) - 50
    pyxel.init(x,y, caption = caption,fps = fps)
    pyxel.run(self.update, self.draw)

  def update(self):
    self.pix_y += 20
    if (self.pix_y >= 160):
      self.pix_y = 0
      self.pix_x += 20
      if (self.pix_x >= 160):
        self.pix_x = 0
    print('Im updating')
    print(self.pix_y)

  def draw(self):
    pyxel.cls(0)
    pyxel.pix(self.pix_x, self.pix_y, 15)
    print('Im drawing')

App(160,160,"Moving pixel",5)
