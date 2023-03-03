#!/usr/bin/python3
"""Command interpreter to execute the hbnb console"""
import cmd
from models.base_model import BaseModel
from models.amenity import Amenity
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review
from models.city import City
from models import storage


class HBNBCommand(cmd.Cmd):
    """Hbnb console"""

    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "Amenity": Amenity
    }

    def emptyline(self):
        """Method to cancel last command repetition"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program\n"""
        return True

    def check_class(self, clsname):
        """Validations of class name existency"""
        if clsname == "":
            print("** class name missing **")
            return False
        elif clsname not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return False
        return True

    def check_id(self, clsname, id):
        """Validations of id existency"""
        if id == "":
            print("** instance id missing **")
            return False
        elif clsname + "." + id not in storage.all():
            print("** no instance found **")
            return False
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel\n"""

        """Checks the classname"""
        if not self.check_class(arg):
            return

        """Creates a new instance and saves it"""
        instance = HBNBCommand.classes[arg]()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Prints a specific instance of a class\n"""

        args = arg.split()
        line = []

        """Fill 'line' list with user's arguments"""
        for i in range(2):
            if (len(args) > i):
                line.append(args[i])
                continue
            line.append("")

        """Checks the classname"""
        if not self.check_class(line[0]):
            return

        """Checks the class id"""
        if not self.check_id(line[0], line[1]):
            return

        key = line[0] + "." + line[1]
        print(storage.all()[key])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
