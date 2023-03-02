#!/usr/bin/python3
"""Command interpreter to execute the hbnb console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Hbnb console"""

    prompt = "(hbnb) "

    def emptyline(self):
        """Method to cancel last command repetition"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        print('Thank you for using Turtle')
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program\n"""
        print('Thank you for using Turtle')
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
