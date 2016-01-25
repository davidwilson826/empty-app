from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)

thinline = LineStyle(1, black)
rectangle = RectangleAsset(50, 20, thinline, blue)
ellipse = EllipseAsset(50, 30, thinline, blue)
polygon = PolygonAsset([(250, 85), (250, 115), (350, 115), (350, 85)], thinline, red)

Sprite(rectangle)
Sprite(rectangle, (200, 50))
Sprite(rectangle, (225, 50))
Sprite(ellipse, (300, 100))
Sprite(polygon)

myapp = App()
myapp.run()
