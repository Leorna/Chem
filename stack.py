import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk


class StackWindow(gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self, title='Stack Demo')
        self.set_border_width(10)

        vbox = gtk.Box(orientation=gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        stack = gtk.Stack()
        stack.set_transition_type(gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration(1000)

        