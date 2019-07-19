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
        
        checkbutton = gtk.CheckButton('Click me!')
        stack.add_titled(checkbutton, 'check', 'Check Button')
        
        label = gtk.Label()
        label.set_markup('<big>A fancy label</big>')
        stack.add_titled(label, 'label', 'A label')
        
        stack_switcher = gtk.StackSwitcher()
        stack_switcher.set_stack(stack)
        vbox.pack_start(stack_switcher, True, True, 0)
        vbox.pack_start(stack, True, True, 0)
        
        
win = StackWindow()
win.connect('destroy', gtk.main_quit)
win.show_all()
gtk.main()

        