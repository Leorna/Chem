import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk
from winconfig import Window


w = Window()


class ChemWindow(gtk.Window):
    """A class that represents the window of the Chem program"""

    def __init__(self):
        gtk.Window.__init__(self, title='Chem')

        #adding a grid
        self.grid = gtk.Grid()
        self.add(self.grid)

        #-----------------creating and attaching buttons------------------#
        self.carbon_buttons = [gtk.Button(label=str(value) + 'C') for value in range(1, 11)]
        self.__attach_carbon_buttons()

        self.connections_buttons = [
            gtk.Button(label='Simples'),
            gtk.Button(label='Dupla'),
            gtk.Button(label='Tripla'),
            gtk.Button(label='Duas Duplas'),
        ]
        self.__attach_connections_buttons()

        self.of_buttons = [
            gtk.Button(label='Hidrocarboneto'),
            gtk.Button(label='Álcool'),
            gtk.Button(label='Eter'),
            gtk.Button(label='Aldeido'),
        ]
        self.__organic_functions_buttons()

    def __attach_carbon_buttons(self):
        """Adds the buttons of quantity of carbons"""
        self.grid.attach(self.carbon_buttons[0], 1, 30, 3, 3)
        #attach(object, x_pos, y_pos, width, height)

        for i in range(len(self.carbon_buttons)-1):
            #adding the button in i+1 position under the button in i position
            self.grid.attach_next_to(self.carbon_buttons[i+1], self.carbon_buttons[i], gtk.PositionType.BOTTOM, 3, 3)
            #attach_next_to(obj1, obj2, position, width, height)

    def __attach_connections_buttons(self):
        """Adds the buttons of type of connections"""
        self.grid.attach(self.connections_buttons[0], w.width / 2, 3, 1, 1)
        #attach(object, x_pos, y_pos, width, height)

        for i in range(len(self.connections_buttons)-1):
            #adding the button in i+1 position to the right of the button in i position
            self.grid.attach_next_to(self.connections_buttons[i+1], self.connections_buttons[i], gtk.PositionType.RIGHT, 1, 1)
            #attach_next_to(obj1, obj2, position, width, height)

    def __organic_functions_buttons(self):
        """Adds the buttons of the organic functions"""
        self.grid.attach(self.of_buttons[0], w.width+100, 30, 5, 5)
        #attach(object, x_pos, y_pos, width, height)

        for i in range(len(self.of_buttons)-1):
            #adding the button in i+1 position under the button in i position
            self.grid.attach_next_to(self.of_buttons[i+1], self.of_buttons[i], gtk.PositionType.BOTTOM, 5, 5)
            #attach_next_to(obj1, obj2, position, width, height)

    def show_chem_window(self):
        """Shows the window"""
        #destroys the window if the user closes it
        self.connect('destroy', gtk.main_quit)
        self.show_all()
        gtk.main()