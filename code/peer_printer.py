# Spring 2022 CSC 131-05
# Welcome to Coding using Git! We all must edit this same file.

# Create a Person object under 'Person objects' (starting on line 47).
# Keep the list of persons in alphabetical by first name order. Example:
# john_doe = Person('John Doe', True)
# sam_smith = Person(Sam Smith', False)

# Update peers list (line 50) with your Person object alphabetical order by
# first name. This list will increase as more students make commits.
# Example: peers = [fiz_ban, foo_bar, john_doe]

# Add an if-statement (line 57) to print a message on whether or not you like
# pineapple pizza. Keep the if-statements alphabetical order by first name.
# See my example.

# Run the program and make sure it works!
# You can use a simple online IDE if you don't have a Python3 environment
# Example: https://ideone.com/l/python-3

COURSE = ['CSC 131-05']
SEMESTER = ['Spring 2022']


class Person:
    '''
    This class is the Person class. It represents basic person info.
    Attributes
    ----------
    name : str
        a string for a person's full name (first and last) used to print
    likes_pineapple_pizza : bool
        whether or not this person likes pineapple on pizza
    '''
    # Python constructor to initialize attributes (fields in Java)
    def __init__(self, name: str, likes_pineapple_pizza: bool):
        self.name = name
        self.likes_pineapple_pizza = likes_pineapple_pizza

    # Special Python method used to represent a class's objects as a string
    def __repr__(self):
        return self.name


def main():
    # Person objects (alphabetical order by first name)
    ashley_palencia_wisniewski = Person('Ashley Palencia - Wisniewski', False)
    brandon_symansiv = Person('Brandon Symansiv', True)
    connor_mckibben = Person('Connor McKibben', True)
    darryl_nguyen = Person('Darryl Nguyen', False)
    dat_mai = Person('Dat Mai', False)
    emad_sabir = Person('Emad Sabir', False)
    emrys_poggemann = Person('Emrys Poggemann', True)
    enrique_alcacer = Person('Enrique Alcacer', False)
    gary_kane = Person('Gary Kane', False)
    ian_schultz = Person('Ian Schultz', False)
    jackson_martin = Person('Jackson Martin', True); 
    jasmine_randhawa = Person('Jasmine Randhawa', False)
    james_mcdole = Person('James McDole', True)
    jason_yu = Person('Jason Yu', True)
    jesus_cervantes = Person('Jesus Cervantes', True)
    joseph_doan = Person('Joseph Doan', True)
    juan_mendez = Person('Juan Mendez', False)
    marco_galindo = Person('Marco Galindo', False)
    maria_valencia = Person('Maria Valencia', True)
    miguel_lopez = Person('Miguel Lopez', True)
    niketa_kosyuk = Person('Niketa Kosyuk', True)
    nikita_cherepanov = Person('Nikita Cherepanov', True)
    riley_johnson = Person('Riley Johnson', True)
    rohit_agrawal = Person('Rohit Agrawal', False)
    vaibhav_jain = Person('Vaibhav Jain', False)
    von_mueller = Person('Von Mueller', False)

    # List of people in our class (alphabetical order by first name)

    peers = [ashley_palencia_wisniewski, brandon_symansiv, connor_mckibben, darryl_nguyen, dat_mai, emrys_poggemann, enrique_alcacer, gary_kane, ian_schultz, jackson_martin,jasmine_randhawa, james_mcdole, jason_yu,jesus_cervantes, joseph_doan, juan_mendez, marco_galindo, maria_valencia, miguel_lopez, niketa_kosyuk, nikita_cherepanov, riley_johnson, vaibhav_jain, von_mueller]

    # Print out people in our class
    print("Welcome to learning Git in %s %s!" % (COURSE[0], SEMESTER[0]))
    print("Peers: %s" % peers)

    # Logic to see who likes pineapple pizza (alphabetical order by first name)
    if ashley_palencia_wisniewski.likes_pineapple_pizza:
	print("%s likes pineapple pizza" % ashley_palencia_wisniewski.name)
    else:
	print("%s DOES NOT like pineapple pizza" % ashley_palencia_wisniewski.name)
    if brandon_symansiv.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % brandon_symansiv.name)
    else:
        print("%s DOES NOT like pineapple pizza" % brandon_symansiv.name)
    if connor_mckibben.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % connor_mckibben.name)
    else:
        print("%s DOES NOT like pineapple pizza" % connor_mckibben.name)
    if darryl_nguyen.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % darryl_nguyen.name)
    else:
        print("%s DOES NOT like pineapple pizza" % darryl_nguyen.name)
    if dat_mai.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % dat_mai.name)
    else:
        print("%s DOES NOT like pineapple pizza" % dat_mai.name)
    if emad_sabir.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % emad_sabir.name)
    else:
        print("%s DOES NOT like pineapple pizza" % emad_sabir.name)
    if emrys_poggemann.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % emrys_poggemann.name)
    else:
        print("%s DOES NOT like pineapple pizza" % emrys_poggemann.name)
    if enrique_alcacer.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % enrique_alcacer.name)
    else:
        print("%s DOES NOT like pineapple pizza" % enrique_alcacer.name)
    if gary_kane.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % gary_kane.name)
    else:
        print("%s DOES NOT like pineapple pizza" % gary_kane.name)
    if ian_schultz.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % ian_schultz.name)
    else:
        print("%s DOES NOT like pineapple pizza" % ian_schultz.name)
    if jackson_martin.likes_pineapple_pizza:
            print("%s likes pineapple pizza" % jackson_martin.name)
    else:
        print("%s DOES NOT like pineapple pizza" % jackson_martin.name)
    if jasmine_randhawa.likes_pineapple_pizza:
            print("%s lieks pineapple pizza" % jasmine_randhawa.name)
    else:
        print("%s DOES NOT like pineapple pizza" % jasmine_randhawa.name)
    if james_mcdole.likes_pineapple_pizza:
            print("%s likes pineapple pizza" % james_mcdole.name)
    else:
        print("%s DOES NOT like pineapple pizza" % james_mcdole.name)
    if jason_yu.likes_pineapple_pizza:
            print("%s likes pineapple pizza" % jason_yu.name)
    else:
        print("%s DOES NOT like pineapple pizza" % jason_yu.name)
    if jesus_cervantes.likes_pineapple_pizza:
            print("%s likes pineapple pizza" % jesus_cervantes.name)
    else:
        print("%s DOES NOT like pineapple pizza" % jesus_cervantes.name)
    if joseph_doan.likes_pineapple_pizza:
            print("%s likes pineapple pizza" % joseph_doan.name)
    else:
        print("%s DOES NOT like pineapple pizza" % joseph_doan.name)
    if juan_mendez.likes_pineapple_pizza:
	    print("%s likes pineaplle pizza" % juan_mendez.name)
    else:
	    print("%s DOES NOT like pineapple pizza" % juan_mendez.name)
    if marco_galindo.likes_pineapple_pizza:
	    print("%s likes pineapple pizza" % marco_galindo.name)
    else:
            print("%s DOES NOT like pineapple pizza" % marco_galindo.name)
    if maria_valencia.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % maria_valencia.name)
    else:
        print("%s DOES NOT like pineapple pizza" % maria_valencia.name)
    if miguel_lopez.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % miguel_lopez.name)
    else:
        print("%s DOES NOT like pineapple pizza" % miguel_lopez.name)
    if niketa_kosyuk.likes_pineapple_pizza:
            print("%s likes pineapple pizza" % niketa_kosyuk.name)
    else:
        print("%s DOES NOT like pineapple pizza" % niketa_kosyuk.name)
    if nikita_cherepanov.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % nikita_cherepanov.name)
    else:
        print("%s DOES NOT like pineapple pizza" % maria_valencia.name)
    if riley_johnson.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % riley_johnson.name)
    else:
        print("%s DOES NOT like pineapple pizza" % riley_johnson.name)
    if rohit_agrawal.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % rohit_agrawal.name)
    else:
        print("%s DOES NOT like pineapple pizza" % rohit_agrawal.name)
    if vaibhav_jain.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % vaibhav_jain.name)
    else:
        print("%s DOES NOT like pineapple pizza" % vaibhav_jain.name)
    if von_mueller.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % von_mueller.name)
    else:
        print("%s DOES NOT like pineapple pizza" % von_mueller.name)

if __name__ == "__main__":
    main()
