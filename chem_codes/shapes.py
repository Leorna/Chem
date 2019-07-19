import cairo
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk as gtk

SIZE = 30


class Shapes(gtk.DrawingArea):
    def __init__(self):
        gtk.DrawingArea.__init__(self)

    def __triangle(self, ctx):
        ctx.move_to(SIZE, 0)
        ctx.rel_line_to(SIZE, 2 * SIZE)
        ctx.rel_line_to(-2 * SIZE, 0)
        ctx.close_path()

    def __square(self, ctx):
        ctx.move_to(0, 0)
        ctx.rel_line_to(2 * SIZE, 0)
        ctx.rel_line_to(0, 2 * SIZE)
        ctx.rel_line_to(-2 * SIZE, 0)
        ctx.close_path()

    def __draw_shapes(self, ctx, x, y, fill):
        ctx.save()
        
        ctx.new_path()
        ctx.translate(3 * SIZE, 0)
        self.__square(ctx)
        if fill:
            ctx.fill()
        else:
            ctx.stroke()

        ctx.new_path()
        ctx.translate(3 * SIZE, 0)
        self.__triangle(ctx)
        if fill:
            ctx.fill()
        else:
            ctx.stroke()

        ctx.restore()

    def __stroke_shapes(self, ctx, x, y):
        self.__draw_shapes(ctx, x, y, False)

    def __draw(self, da, ctx):
        ctx.set_source_rgb(0, 0, 0)

        ctx.set_line_width(SIZE / 4)
        ctx.set_tolerance(0.1)

        ctx.set_line_join(cairo.LINE_JOIN_ROUND)
        
        self.__stroke_shapes(ctx, 0, 0)

        ctx.set_dash([], 0)
        self.__stroke_shapes(ctx, 0, 3 * SIZE)
        
    def draw(self, widget):
        self.connect('draw', self.__draw)
        
        

# def main():
#     win = Gtk.Window()
#     win.connect('destroy', lambda w: Gtk.main_quit())
#     win.set_default_size(450, 550)

#     drawingarea = Gtk.DrawingArea()
#     win.add(drawingarea)
#     drawingarea.connect('draw', draw)

#     win.show_all()
#     Gtk.main()
