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
    darryl_nguyen = Person('Darryl Nguyen', False)
    emrys_poggemann = Person('Emrys Poggemann', True)
    gary_kane = Person('Gary Kane', False)
    ian_schultz = Person('Ian Schultz', False)
    jasmine_randhawa = Person('Jasmine Randhawa', False)
    jason_yu = Person('Jason Yu', True)
    jesus_cervantes = Person('Jesus Cervantes', True)
    joseph_doan = Person('Joseph Doan', True)
    nikita_cherepanov = Person('Nikita Cherepanov', True)
    riley_johnson = Person('Riley Johnson', True)
    vaibhav_jain = Person('Vaibhav Jain', False)

    # List of people in our class (alphabetical order by first name)
    peers = [ashley_palencia_wisniewski, brandon_symansiv, darryl_nguyen, emrys_poggemann, gary_kane, ian_schultz,jasmine_randhawa,jesus_cervantes, joseph_doan, nikita_cherepanov, riley_johnson, vaibhav_jain]

    # Print out people in our class
    print("Welcome to learning Git in %s %s!" % (COURSE[0], SEMESTER[0]))
    print("Peers: %s" % peers)

    # Logic to see who likes pineapple pizza (alphabetical order by first name)
    if emrys_poggemann.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % emrys_poggemann.name)
    else:
        print("%s DOES NOT like pineapple pizza" % emrys_poggemann.name)

    if gary_kane.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % gary_kane.name)
    else:
        print("%s DOES NOT like pineapple pizza" % gary_kane.name)
    if ian_schultz.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % ian_schultz.name)
    else:
        print("%s DOES NOT like pineapple pizza" % ian_schultz.name)
    if jasmine_randhawa.likes_pineapple_pizza:
            print("%s lieks pineapple pizza" % jasmine_randhawa.name)
    else: 
        print("%s DOES NOT like pineapple pizza" % jasmine_randhawa.name)
    if jason_yu.likes_pineapple_pizza:
            print("%s likes pineapple pizza" % jason_yu.name)
    else: 
        print("%s DOES NOT like pineapple pizza" % jason_yu.name)
    if joseph_doan.likes_pineapple_pizza:
            print("%s likes pineapple pizza" % joseph_doan.name)
    else: 
        print("%s DOES NOT like pineapple pizza" % jasmine_randhawa.name)
    if vaibhav_jain.likes_pineapple_pizza:
        print("%s likes pineapple pizza" % vaibhav_jain.name)
    else:
        print("%s DOES NOT like pineapple pizza" % vaibhav_jain.name)

if __name__ == "__main__":
    main()
