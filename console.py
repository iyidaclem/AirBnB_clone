#!/usr/bin/python3
"""
A module that contains our hbnb console
"""

import cmd
import models
from  models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    The HBNB console class
    """

    prompt = "(hbnb) "

    all_models = {"BaseModel": BaseModel}

    def do_quit(self, line):
        """ Simple command to exit the console """
        return True

    def do_EOF(self, line):
        """ EOF exits the console """
        return True

    def do_create(self, line):
        """ Creates a new instance of BaseModel """
        if len(line) == 0:
            print("** class name missing **")
        elif line not in HBNBCommand.all_models:
            print("** class doesn't exist **")
        else:
            new_model = HBNBCommand.all_models[line]()
            new_model.save()
            print(new_model.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance based on the class name and id
        """
        all_classes = models.storage.all()
        if len(line) == 0:
            print("** class name missing **")
        else:
            _line = line.split()
            name = _line[0]
            _id = None
            if len(_line) > 1:
                _id = _line[1]
            if name not in HBNBCommand.all_models:
                print("** class doesn't exist ** (")
            elif _id == None:
                print ("** instance id missing **")
            elif name + "." + _id not in all_classes:
                print("** no instance found **")
            else: 
                print(all_classes[name  + "." + _id].__str__())

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id (save the change into the JSON file)
        """

        all_classes = models.storage.all()
        if len(line) == 0:
            print("** class name missing **")
        else:
            _line = line.split()
            name = _line[0]
            _id = None
            if len(_line) > 1:
                _id = _line[1]
            if name not in HBNBCommand.all_models:
                print("** class doesn't exist ** (")
            elif _id == None:
                print ("** instance id missing **")
            elif name + "." + _id not in all_classes:
                print("** no instance found **")
            else:
                all_objects = models.storage.all()
                del all_objects[name + "." + _id]
                models.storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all instances based or not on the class name. Ex: $ all BaseModel or $ all
        """

        all_objects = models.storage.all()
        if len(line) > 0 and line in HBNBCommand.all_models:
            print([v.__str__() for k, v in all_objects.items() if v.__class__.__name__ == line])
        elif len(line) > 0 and line not in HBNBCommand.all_models:
            print("** class doesn't exist ** ")
        else:
            print([v.__str__() for k, v in all_objects.items()])

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)
        """

        _line = line.split()
        all_classes = models.storage.all()
        if len(line) == 0:
            print("** class name missing **")
        else:
            name = _line[0]
            _id = None
            if len(_line) > 1:
                _id = _line[1]
            if name not in HBNBCommand.all_models:
                print("** class doesn't exist ** ")
            elif _id == None:
                print ("** instance id missing **")
            elif name + "." + _id not in all_classes:
                print("** no instance found **")
            elif len(_line) < 3:
                print("** attribute name missing **")
            elif len(_line) < 4:
                print("** value missing **")
            elif _line[2] == "id" or _line[2] == "created_at" or _line[2] == "updated_at":
                print("Illegal update")
                pass
            else:
                print(type(eval(_line[3])))
                setattr(all_classes[name + "." + _id], _line[2], eval(_line[3]))
                models.storage.save()



if __name__ == '__main__':
    HBNBCommand().cmdloop()
