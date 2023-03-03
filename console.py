#!/usr/bin/python3
"""Command interpreter to execute the hbnb console"""
import cmd
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import shlex


class HBNBCommand(cmd.Cmd):
    """Hbnb console"""

    prompt = "(hbnb) "
    classes = {
        "Amenity": Amenity,
        "BaseModel": BaseModel,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State,
        "User": User
    }

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program\n"""
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

        line = self.command_line(arg, 2)

        """Checks the classname"""
        if not self.check_class(line[0]):
            return

        """Checks the class id"""
        if not self.check_id(line[0], line[1]):
            return

        key = line[0] + "." + line[1]
        print(storage.all()[key])

    def do_all(self, arg):
        """Prints all the instances of a specific class\n"""

        instances_list = []

        if arg == "":
            for value in storage.all().values():
                instances_list.append(str(value))
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        else:
            for key in storage.all().keys():
                if arg in key:
                    instances_list.append(str(storage.all()[key]))

        print(instances_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and the id\n"""

        line = self.command_line(arg, 4)

        """Checks the class name"""
        if not self.check_class(line[0]):
            return

        """Checks the class id"""
        if not self.check_id(line[0], line[1]):
            return

        """Checks the class attributes and its value"""
        if not self.check_attr(line[2], line[3]):
            return

        value = line[3]
        if value.isnumeric():
            value = int(value)

        key = line[0] + "." + line[1]
        setattr(storage.all()[key], line[2], value)
        storage.save()

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id\n"""

        line = self.command_line(arg, 2)

        """Checks the classname"""
        if not self.check_class(line[0]):
            return

        """Checks the class id"""
        if not self.check_id(line[0], line[1]):
            return

        key = line[0] + "." + line[1]
        del storage.all()[key]
        storage.save()

    def emptyline(self):
        """Method to cancel last command repetition"""
        pass

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

    def check_attr(self, attr, value):
        """Checks the class attributes and its value"""
        if attr == "":
            print("** attribute name missing **")
            return False
        elif value == "":
            print("** value missing **")
            return False
        return True

    def command_line(self, arg, num_args):
        """Fill 'line' list with user's arguments"""

        args = shlex.split(arg)
        line = []

        for i in range(num_args):
            if (len(args) > i):
                line.append(args[i])
                continue
            line.append("")

        return line


if __name__ == '__main__':
    HBNBCommand().cmdloop()
