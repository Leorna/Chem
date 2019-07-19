import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk
from buttons import Buttons
from shapes import Shapes


class ChemWindow(gtk.Window):
    """A class that represents the window of the Chem program"""

    def __init__(self):
        gtk.Window.__init__(self, title='Chem')
        
        #adding a box
        box = gtk.Box()
        self.add(box)
        
        #packing drawing area to the box
        darea = Shapes()
        box.pack_start(darea, True, True, 0)
        
        #packing grid to the box
        grid = gtk.Grid()
        box.pack_end(grid, True, True, 0)
        
        #attaching buttons to grid
        buttons = Buttons()
        
        buttons._attach_carbon_buttons(grid)
        buttons._attach_connections_buttons(grid)
        buttons._attach_organic_functions_buttons(grid)
        buttons._attach_search_button(grid)
        
        #adding event
        buttons._connect_search_button()
        buttons._connect_connections_buttons(darea.draw)
        
    def show_chem_window(self):
        """Shows the window"""
        #destroys the window if the user closes it
        self.connect('destroy', gtk.main_quit)
        self.show_all()
        gtk.main()