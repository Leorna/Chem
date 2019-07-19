import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk
from winconfig import WindowSettings
from entry import EntryWindow


w = WindowSettings()


class Buttons:
    """A class with all buttons of the application"""
    
    def __init__(self):
        #-----------------creating and attaching buttons------------------#
        self.carbon_buttons = [gtk.Button(label=str(value)+'C') for value in range(1, 11)]

        self.connections_buttons = [
            gtk.Button(label='Simples'),
            gtk.Button(label='Dupla'),
            gtk.Button(label='Tripla'),
            gtk.Button(label='Duas Duplas'),
        ]

        self.of_buttons = [
            gtk.Button(label='Hidrocarboneto'),
            gtk.Button(label='Álcool'),
            gtk.Button(label='Eter'),
            gtk.Button(label='Aldeido'),
        ]
        
        self.search_button = gtk.Button(label='Composto')

    def _attach_carbon_buttons(self, grid):
        """Adds the buttons of quantity of carbons"""
        grid.attach(self.carbon_buttons[0], 1, 30, 3, 3)
        #attach(object, x_pos, y_pos, width, height)

        for i in range(len(self.carbon_buttons)-1):
            #adding the button in i+1 position under the button in i position
            grid.attach_next_to(self.carbon_buttons[i+1], self.carbon_buttons[i], gtk.PositionType.BOTTOM, 3, 3)
            #attach_next_to(obj1, obj2, position, width, height)

    def _attach_connections_buttons(self, grid):
        """Adds the buttons of type of connections"""
        grid.attach(self.connections_buttons[0], w.width / 2, 3, 1, 1)
        #attach(object, x_pos, y_pos, width, height)

        for i in range(len(self.connections_buttons)-1):
            #adding the button in i+1 position to the right of the button in i position
            grid.attach_next_to(self.connections_buttons[i+1], self.connections_buttons[i], gtk.PositionType.RIGHT, 1, 1)
            #attach_next_to(obj1, obj2, position, width, height)

    def _attach_organic_functions_buttons(self, grid):
        """Adds the buttons of the organic functions"""
        grid.attach(self.of_buttons[0], w.width+100, 30, 5, 5)
        #attach(object, x_pos, y_pos, width, height)

        for i in range(len(self.of_buttons)-1):
            #adding the button in i+1 position under the button in i position
            grid.attach_next_to(self.of_buttons[i+1], self.of_buttons[i], gtk.PositionType.BOTTOM, 5, 5)
            #attach_next_to(obj1, obj2, position, width, height)
            
    def _attach_search_button(self, grid):
        """Adds the search button"""
        grid.attach(self.search_button, 0, 0, 5, 5)
        
    def _connect_search_button(self):
        """Connects the EntryWindow constructor to the clicked event"""
        self.search_button.connect('clicked', EntryWindow)
        
    def _connect_connections_buttons(self, callback):
        """Connects the connections buttons to the drawing area"""
        self.connections_buttons[0].connect('clicked', callback)
