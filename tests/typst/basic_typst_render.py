from manimlib import *

class ExampleTypst(Scene):
    def construct(self):
        # Create a text object using Typst syntax
        txt = Typ(
            "$ mat(delim:\"[\", 1, 2; 3, 4; 5, 6) $").move_to(UP)
        txt2 = Typ("$ mat(1, 2; 3, 4; 5, 6) $").move_to(UP)

        # Display the text on the screen
        write_anim = Write(txt)
        self.play(write_anim)
        transform_anim = Transform(txt, txt2)
        self.play(transform_anim)


class TexControl(Scene):
    def construct(self):
        frame_counter = Integer(0).to_corner(UR)

        def frame_counter_updater(mobj): return mobj.set_value(
            int(self.time * self.camera.fps))
        frame_counter.add_updater(frame_counter_updater)

        self.add(frame_counter)
        # Create a text object using Tex syntax, to compare behavior
        txt = Tex(
            r"\begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}").move_to(UP)
        txt2 = Tex(
            r"\begin{pmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{pmatrix}").move_to(UP)

        # Display the text on the screen
        write_anim = Write(txt)
        self.play(write_anim)
        transform_anim = Transform(txt, txt2)
        self.play(transform_anim)


if __name__ == "__main__":
    s = ExampleTypst(
        file_writer_config={
            "write_to_movie": True,
            "file_name": "basic_typst_render",
        }
    )
    s.run()
    t = TexControl(
        file_writer_config={
            "write_to_movie": True,
            "file_name": "tex_control_render",
        }
    )
    t.run()
