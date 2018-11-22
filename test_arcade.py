import arcade

def test_open_an_arcade_window():
   window = arcade.open_window(800, 800, "CGoL")
   assert window == arcade.open_window(800, 800, "CGoL")