import gi
import cairo
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()

    def onButtonPressed(self, button):
        print("Hello World!")

SIZE = 70
def triangle(ctx):
    ctx.move_to(SIZE, 0)
    ctx.rel_line_to(SIZE, 2 * SIZE)
    ctx.rel_line_to(-2 * SIZE, 0)
    ctx.close_path()
def square(ctx):
    ctx.move_to(0, 0)
    ctx.rel_line_to(2 * SIZE, 0)
    ctx.rel_line_to(0, 2 * SIZE)
    ctx.rel_line_to(-2 * SIZE, 0)
    ctx.close_path()


def bowtie(ctx):
    ctx.move_to(0, 0)
    ctx.rel_line_to(2 * SIZE, 2 * SIZE)
    ctx.rel_line_to(-2 * SIZE, 0)
    ctx.rel_line_to(2 * SIZE, -2 * SIZE)
    ctx.close_path()
def inf(ctx):
    ctx.move_to(0, SIZE)
    ctx.rel_curve_to(0, SIZE, SIZE, SIZE, 2 * SIZE, 0)
    ctx.rel_curve_to(SIZE, -SIZE, 2 * SIZE, -SIZE, 2 * SIZE, 0)
    ctx.rel_curve_to(0, SIZE, -SIZE, SIZE, - 2 * SIZE, 0)
    ctx.rel_curve_to(-SIZE, -SIZE, - 2 * SIZE, -SIZE, - 2 * SIZE, 0)
    ctx.close_path()
def draw_shapes(ctx, x, y, fill):
    ctx.save()
    ctx.new_path()
    ctx.translate(x + SIZE, y + SIZE)
    bowtie(ctx)
    if fill:
        ctx.fill()
    else:
        ctx.stroke()

    ctx.new_path()
    ctx.translate(3 * SIZE, 0)
    square(ctx)
    if fill:
        ctx.fill()
    else:
        ctx.stroke()

    ctx.new_path()
    ctx.translate(3 * SIZE, 0)
    triangle(ctx)
    if fill:
        ctx.fill()
    else:
        ctx.stroke()

    ctx.new_path()
    ctx.translate(3 * SIZE, 0)
    inf(ctx)
    if fill:
        ctx.fill()
    else:
        ctx.stroke()
    ctx.restore()


def fill_shapes(ctx, x, y):
    draw_shapes(ctx, x, y, True)


def stroke_shapes(ctx, x, y):
    draw_shapes(ctx, x, y, False)


def draw(da, ctx):
    ctx.set_source_rgb(255, 0, 0)
    ctx.set_line_width(SIZE / 4)
    ctx.set_tolerance(0.1)
    stroke_shapes(ctx, 0, 0)
    
    
def draw_all(widget):
    builder = Gtk.Builder()
    builder.add_from_file("wesley/doc.glade")
    builder.connect_signals(Handler())
    window = builder.get_object("window")
    drawing_area = builder.get_object("drawingArea")
    drawing_area.connect('draw', draw)

# window.show_all()

# Gtk.main()