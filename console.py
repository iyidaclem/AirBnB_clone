#!/usr/bin/python3
"""
A module that contains our hbnb console
"""

import cmd
import subprocess
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    The HBNB console class
    """

    prompt = "(hbnb) "

    all_models = {"BaseModel": BaseModel, "User": User, "Place": Place,
                  "State": State, "City": City, "Amenity": Amenity,
                  "Review": Review}

    user_commands = ["all"]

    def do_quit(self, line):
        """ Simple command to exit the console """
        return True

    def do_EOF(self, line):
        """ EOF exits the console """
        return True

    def do_shell(self, line):
        """ Used to run default shell command """
        try:
            result = subprocess.run(line, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE, shell=True,
                                    check=True)
            print(result.stdout.decode().strip())
        except subprocess.CalledProcessError as e:
            print(e.stderr.decode().strip())

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
        Prints the string representation of an
        instance based on the class name and id
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
                print("** class doesn't exist ** ")
            elif _id is None:
                print("** instance id missing **")
            elif name + "." + _id not in all_classes:
                print("** no instance found **")
            else:
                print(all_classes[name + "." + _id].__str__())

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name
        and id (save the change into the JSON file)
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
                print("** class doesn't exist **")
            elif _id is None:
                print("** instance id missing **")
            elif name + "." + _id not in all_classes:
                print("** no instance found **")
            else:
                all_objects = models.storage.all()
                del all_objects[name + "." + _id]
                models.storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name. Ex: $ all BaseModel or $ all
        """

        all_objects = models.storage.all()
        if len(line) > 0 and line in HBNBCommand.all_models:
            print([v.__str__() for k, v in
                  all_objects.items() if
                  v.__class__.__name__ == line])
        elif len(line) > 0 and line not in HBNBCommand.all_models:
            print("** class doesn't exist ** ")
        else:
            print([v.__str__() for k, v in all_objects.items()])
    
    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)
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
            elif _id is None:
                print("** instance id missing **")
            elif name + "." + _id not in all_classes:
                print("** no instance found **")
            elif len(_line) < 3:
                print("** attribute name missing **")
            elif len(_line) < 4:
                print("** value missing **")
            elif (_line[2] == "id" or _line[2] == "created_at"
                  or _line[2] == "updated_at"):
                print("Illegal update")
                pass
            else:
                val = None
                if _line[3].isnumeric():
                    val = eval(_line[3])
                elif _line[3][0] == "\"" or _line[3][0] == "\'":
                    val = eval(_line[3])
                else:
                    val = _line[3]
                setattr(all_classes[name + "." + _id], _line[2], val)
                models.storage.save()

    def default(self, line):
        """ Handles default command entered by the user """
        _cmd = line.split(".")
        cls_name = ""
        comd = ""
        _arg = ""

        if len(_cmd) == 2:
            if _cmd[0] in HBNBCommand.all_models:
                cls_name = _cmd[0]
                if _cmd[1][-1] != ")" or "(" not in _cmd[1]:
                    return False
                _split = _cmd[1].split("(")
                if _split[0] in HBNBCommand.user_commands:
                    comd = _split[0]
                    if len(_split[1]) > 1:
                        # _arg = _split[2][0:-1]
                        match comd:
                            case "count":
                                total_inst = leni(self.do_show(cls_name))
                        print(total_inst)
                    else:
                        self.do_all(cls_name)
                else:
                    print("** command not found **")
            else:
                print("** class doesn't exist **")
        else:
            print("*** Unknown syntax:", line)
        return False

    def _time(self):
        print("This is current time")

    def do_mytime(self, line):
        self._time()    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
