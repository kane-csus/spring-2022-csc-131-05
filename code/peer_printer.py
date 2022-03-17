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
    darryl_nguyen = Person('Darryl Nguyen', False)
    emrys_poggemann = Person('Emrys Poggemann', True)
    gary_kane = Person('Gary Kane', False)
    nikita_cherepanov = Person('Nikita Cherepanov', True)
    ian_schultz = Person('Ian Schultz', False)
    vaibhav_jain = Person('Vaibhav Jain', False)

    # List of people in our class (alphabetical order by first name)
    peers = [ashley_palencia_wisniewski, darryl_nguyen, emrys_poggemann, gary_kane, nikita_cherepanov, ian_schultz, vaibhav_jain]

    # Print out people in our class
    print("Welcome to learning Git in %s %s!" % (COURSE[0], SEMESTER[0]))
    print("Peers: %s" % peers)

    # Logic to see who likes pineapple pizza (alphabetical order by first name)
    for peer in peers:
        print(f"{peer.name} {'likes' if peer.likes_pineapple_pizza else 'DOES NOT like'} pineapple pizza")

if __name__ == "__main__":
    main()
