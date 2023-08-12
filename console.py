#!/usr/bin/python3
"""module containing the cmd interpreter for project"""
import cmd
from models.base_model import BaseModel
from models.engine import file_storage
from models import storage


class HBNBCommand(cmd.Cmd):
    """derrived class of the inbuilt cmd base class"""
    prompt = "(hbnb) "
    obj_container = storage.all()

    def do_create(self, arg):
        """method that creates instance with uuid"""
        args = arg.split(" ")
        if not args[0]:
            print("** class name missing **")
            
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        else:
            new_model = BaseModel()
            new_model.save()
            print(new_model.id)

    def do_EOF(self, arg):
        """method that sends Ctrl+D signal to 
        quit the interpreter"""
        return True

    def do_quit(self, arg):
        """method to quit command to exit the program"""
        return True

    def do_show(self, arg):
        """method that Prints the string repr of an instance
        based on the class name and id"""
        
        split_args = arg.split()
        if len(split_args) == 0:
            print("** class name missing **")
        elif len(split_args) == 1:
            print("** instance id missing **")
        elif split_args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        else:
            for key in HBNBCommand.obj_container.keys():
                if str(key) == "{}.{}".format(split_args[0], split_args[1]):
                    data_to_show = HBNBCommand.obj_container[key]
                    print(data_to_show)
                    break
                else:
                    print("** no instance found **")
    
    def do_destroy(self, arg):
        """metho that deletes the specified data from the
        data base Usage: <class_name> <id>"""

        split_args = arg.split()
        if len(split_args) == 0:
            print("** class name missing **")
        elif split_args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(split_args) == 1:
            print("** instance id missing **")
        else:
            for key in HBNBCommand.obj_container.keys():
                if str(key) == "{}.{}".format(split_args[0], split_args[1]):
                    del HBNBCommand.obj_container[key]
                    storage.save()
                    break
                else:
                    print("** no instance found **")
                    
    def do_all(self, arg):
        """prints the string representation of all classes
        Usage: all [<class_name>]"""

        line = arg.split()
        obj_list = []

        if len(line) == 1:
            if line[0] in ["BaseModel"]:
                for key, value in HBNBCommand.obj_container.items():
                    if key.startswith(line[0]):
                        obj_list.append(str(value))
            else:
                print("** class doesn't exist **")
                return
        else:
            for value in HBNBCommand.obj_container.values():
                obj_list.append(str(value))

        print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by
        adding or updating attribute"""

        split_args = arg.split()
        if len(split_args) == 0:
            print("** class name missing **")
        elif len(split_args) == 1:
            print("** instance id missing **")
        elif len(split_args) == 2:
            print("** attribute name missing **")
        elif len(split_args) == 3:
            print("** value missing **")
        else:
            for key in HBNBCommand.obj_container.keys():
                if str(key) == "{}.{}".format(split_args[0], split_args[1]):
                    """I couldnt type cast the attribute value to """
                    setattr(HBNBCommand.obj_container[key], split_args[2], split_args[3])
                    storage.save()
                    break
                else:
                    print("** no instance found **")

    def emptyline(self):
        """Don't budge"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
