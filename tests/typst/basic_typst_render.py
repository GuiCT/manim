from manimlib import *

class ExampleTypst(Scene):
    def construct(self):
        # Create a text object using Typst syntax
        txt = Typ("$ mat(delim:\"[\", 1, 2, 3; 4, 5, 6; 7, 8, 9) $").move_to(UP)
        txt2 = Typ("$ mat(1, 2, 3; 4, 5, 6; 7, 8, 9) $").move_to(UP)

        # Display the text on the screen
        self.play(Write(txt))
        self.play(Transform(txt, txt2))


if __name__ == "__main__":
    s = ExampleTypst()
    s.run()