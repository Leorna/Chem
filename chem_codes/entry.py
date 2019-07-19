import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk
from gi.repository import GLib as glib


class EntryWindow(gtk.Window):
    def __init__(self, widget):
        gtk.Window.__init__(self, title='Composto')
        self.set_size_request(200, 100)
        
        vbox = gtk.Box(orientation=gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)
        
        self.entry = gtk.Entry()
        self.entry.set_text('Digite o nome')
        vbox.pack_start(self.entry, True, True, 0)
        
        hbox = gtk.Box(spacing=6)
        vbox.pack_start(hbox, True, True, 0)
        
        
        self.__add_icon()
        self.__show_entry_window()   
    
    def __add_icon(self):
        icon_name = 'system-search-symbolic'
        self.entry.set_icon_from_icon_name(gtk.EntryIconPosition.PRIMARY, icon_name)

    def __show_entry_window(self):
        self.connect('destroy', gtk.main_quit)
        self.show_all()
        gtk.main()