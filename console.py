#!/usr/bin/python3
"""
this module contains the command interpreter
"""

import cmd
from models.base_model import BaseModel
from models.__init__ import storage
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.user import User

classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
           'State': State, 'City': City, 'Amenity': Amenity, 'Review': Review}

class HBNBCommand(cmd.Cmd):
    """
    Class is for a command line interpreter
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Uses quit as a command to exit"""
        exit()

    def do_EOF(self, arg):
        """command for end of file"""
        exit()

    def emptyline(self):
        """empty line"""
        return

    def do_create(self, arg):
        """Creates new instance of BaseModel\n"""
        classes = storage.classes()
        if arg == "" or arg is None:
            print('** class name missing **')
        elif arg in classes.keys():
            obj = classes[arg]()
            obj.save()
            print(obj.id)
        else:
            print("** class doesn't exist **")
    
    def classes(self):
        """Method for importing classes to fix circular import"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        from models import storage

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
            "storage": FileStorage
            }
        return classes

    def do_show(self, *args):
        """Prints string representation of instance\n"""
        classes = storage.classes()
        if args[0] == '' or args[0] is None:
            print("** class name missing **")
            return
        string = args[0]
        arg = string.split(' ')
        if arg[0] not in classes.keys():
            print("** class doesn't exist **")
            return
        if len(arg) == 1:
            print("** instance id missing **")
            return
        string = arg[0] + "." + arg[1]
        all_objs = storage.all()
        if string in all_objs.keys():
            print(all_objs[string])
            return
        print("** no instance found **")

    def do_destroy(self, *args):
        """Deletes an instance based on the class name and id\n"""
        classes = storage.classes()
        if args[0] == '' or args[0] is None:
            print("** class name missing **")
            return
        string = args[0]
        arg = string.split(' ')
        if arg[0] not in classes.keys():
            print("** class doesn't exist **")
            return
        if len(arg) == 1:
            print("** instance id missing **")
            return
        string = arg[0] + "." + arg[1]
        all_objs = storage.all()
        if string in all_objs.keys():
            del all_objs[string]
            storage.save()
            return
        print("** no instance found **")

    def do_all(self, *args):
        """Prints string representation of all\n"""
        classes = storage.classes()
        all_objs = storage.all()
        list_objs = []
        if args[0] == '':
            for k, v in all_objs.items():
                list_objs.append(str(v))
            print(list_objs)
            return
        if args[0] not in classes.keys():
            print("** class doesn't exist **")
            return
        for k, v in all_objs.items():
            if args[0] == type(v).__name__:
                list_objs.append(str(v))
        print(list_objs)

    def do_update(self, *args):
        """Updates an instance based on the class name and id\n"""
        all_objs = storage.all()
        classes = storage.classes()
        if args[0] == '' or args[0] is None:
            print("** class name missing **")
            return
        string = args[0]
        arg = string.split(' ')
        if arg[0] not in classes.keys():
            print("** class doesn't exist **")
            return
        if len(arg) == 1:
            print("** instance id missing **")
            return
        string = arg[0] + "." + arg[1]
        if string not in all_objs.keys():
            print("** no instance found **")
            return
        if len(arg) == 2:
            print("** attribute name missing **")
            return
        if len(arg) == 3:
            print("** value missing **")
            return
        try:
            a = float(arg[3])
            if a.is_integer():
                a = int(a)
        except (TypeError, ValueError):
            if "\"" in arg[3]:
                arg[3] = arg[3].replace("\"", "")
            setattr(all_objs[string], arg[2], str(arg[3]))
            storage.save()
            return
        setattr(all_objs[string], arg[2], a)
        storage.save()

                
if __name__ == '__main__':
    HBNBCommand().cmdloop()
