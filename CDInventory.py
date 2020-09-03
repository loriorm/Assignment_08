#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# ormerodl, 2020-Sept-1, add code to process data from file
# ormerodl, 2020-Sept-1, add code to save data to txt file
# ormerodl, 2020-Sept-1, add code to display menu to user
# ormerodl, 2020-Sept-1, add code to allow user to select menu task
# ormerodl, 2020-Sept-1, add code to display inventory in program
# ormerodl, 2020-Sept-2, broke code trying to update for save/load
# ormerodl, 2020-Sept-1, updated to allow for saving of data to text file
# ormerodl, 2020-Sept-1, got 20 continuous AttributeErrors
# ormerodl, 2020-Sept-2, email Dirk & Doug for help
# ormerodl, 2020-Sept-2, call my friend Mike for help
# ormerodl, 2020-Sept-2, define values stmt in CD class
# ormerodl, 2020-Sept-1, update error handling
# ormerodl, 2020-Sept-1, update 
#------------------------------------------#


# -- DATA -- #
strFileName = 'CDInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:
        __str__: print objects
        append: Add objects to list
    """
    # -- Contructors -- #
    def __init__(self,cd_id, cd_ttl, cd_art):
        # -- Attributes -- #
        self.__cd_id = cd_id
        self.__cd_title = cd_ttl
        self.__cd_artist = cd_art

    # -- Properties -- #
    @property
    def cd_id(self):
        return self.__cd_id
    
    @cd_id.setter
    def cd_id(self, value):
        if type(value)== int:
            self.__cd_id = value
        else:
            raise Exception('ID must be an integer')

    @property
    def cd_title(self):
        return self.__cd_title
    
    @cd_title.setter
    def cd_title(self, value):
        if type(value)== str:
            self.__cd_title = value
        else:
            raise Exception('Title must be an string')

    @property
    def cd_artist(self):
        return self.__cd_artist
    
    @cd_artist.setter
    def cd_artist(self, value):
        if type(value)== str:
            self.__cd_artist = value
        else:
            raise Exception('Artist must be an string')


    # -- Methods -- #
    @staticmethod
    def __str__(self):
        return '{}, {}, {}'.format(self.cd_id, self.cd_title, self.cd_artist)

    def values(self):
        return [self.cd_id, self.cd_title, self.cd_artist]

    @staticmethod
    def add_cd(cd_id, cd_title, cd_artist, table):
        appendywendy = CD(int(cd_id), cd_title, cd_artist)
        table.append(appendywendy)


# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    @staticmethod
    def save_inventory(file_name, table):
        """Function to save data from a list of dictionaries to text file

        Writes the data from a 2D list of objects to a text file identified by file_name
         one row in table represents one line in the file.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dicts): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        strRow = ''
        for row in table:
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'

        objFile = open(file_name, 'w')
        objFile.write(strRow)
        objFile.close()
        print('CD Inventory has been saved to "CDInventory.txt"\n')

    @staticmethod
    def load_inventory(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        table.clear()  # this clears existing data and allows to load data from file
        objFile = open(file_name, 'r')
        for line in objFile:
            data = line.strip().split(',')
            data = CD(data[0], data[1], data[2])
            table.append(data)
        objFile.close()
        pass

# -- PRESENTATION (Input/Output) -- #
class IO:
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case string of the users input out of the choices l, a, i, d, s or x

        """
        choice = ''
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table

        """
        print('\n======= The Current Inventory: =======')
        print('ID\tCD Title\t (by: Artist)\n')
        for row in table:
            print('{},\t {}\t (by: {})'.format(*row.values()))
        print('======================================\n')


    @staticmethod
    def user_input():
        """Gets user input for CD Inventory

        Args:
            None.

        Returns:
            strID (string): A numeric string from user input
            strTitle (string): alphanumeric string for CD Title
            StrArtist (string): alphnumeric string for CD Artist

        """
        strID = int(input('Enter ID: ').strip())
        strTitle = input('What is the CD\'s title? ').strip()
        strArtist = input('What is the Artist\'s name? ').strip()
        return strID, strTitle, strArtist

# -- Main Body of Script -- #

# 1. When program starts, read in the currently saved Inventory
try:
    FileIO.load_inventory(strFileName, lstOfCDObjects)

except FileNotFoundError:
    createFile = input('File does not exist, would you like to create it now? [y/n] ')
    if createFile.lower() == 'y':
        with open(strFileName, 'w'):
            pass
        print('File has been created, get down whichya bad self adding data!')

# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

# 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
        try:
            print('WARNING: If you continue, all unsaved data will be lost and the Inventory loaded from file.')
            strYesNo = input('Would you like to continue and load from file? [y/n] ')
            if strYesNo.lower() == 'y':
                print('loading...')
                FileIO.load_inventory(strFileName, lstOfCDObjects)
                IO.show_inventory(lstOfCDObjects)
            else:
                input('canceling... Inventory data NOT loaded. Press [ENTER] to continue to the menu.')
            continue  # start loop back at top.
    #Why is my except not printing when the file is empty?
        except EOFError:
            print('File exists, but there is no data. Please add data using menu option "a"\n')
        continue # start loop back at top

    # 3.3 process add a CD
    elif strChoice == 'a':
        try:
        # TODO update for OOP functionality
            strID, strTitle, strArtist = IO.user_input()
            CD.add_cd(strID, strTitle, strArtist, lstOfCDObjects)
            IO.show_inventory(lstOfCDObjects)
            continue  # start loop back at top.
        except ValueError:
            print('ID must be a positive integer. Please try again.\n')
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.

    # 3.5 process save inventory to file
    elif strChoice == 's':
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            FileIO.save_inventory(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # 3.6 catch-all should not be possible, as user choice gets vetted in IO, but to be safe:
    else:
        print('General Error')

