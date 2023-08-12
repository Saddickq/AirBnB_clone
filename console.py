#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.engine import file_storage
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    obj_container = storage.all()

    def do_create(self, arg):
        """Create user with uuid"""
        args = arg.split(" ")
        if not args[0]:
            print("** class name missing **")
            
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        else:
            new_model = BaseModel()
            new_model.save()
            print(new_model.id)

    def do_all(self, value):
        """Prints the reloaded deserialised info"""
        print(self.load())

    def do_EOF(self, arg):
        """sends an Eof  signal to quit the interpreter"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_show(self, arg):
        class_name, id = arg.split()
        if not class_name:
            print("** class name missing **")
        elif not class_name in ["BaseModel"]:
            print("** class doesn't exist **")
        elif not id:
            print("** instance id missing **")
        else:
            for key in HBNBCommand.obj_container.keys():
                if str(key) == "{}.{}".format(class_name, id):
                    data_to_show = HBNBCommand.obj_container[key]
                    print(data_to_show)
                    break
                else:
                    print("** no instance found **")

    def emptyline(self):
        pass
    
    def do_destroy(self, arg):
        """Deletes the specified data from the data base"""
        
        class_name, id = arg.split()
        if not class_name:
            print("** class name missing **")
        elif class_name not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif not id:
            print("** instance id missing **")
        else:
            for key in HBNBCommand.obj_container.keys():
                if str(key) == "{}.{}".format(class_name, id):
                    del HBNBCommand.obj_container[key]
                    storage.save()
                    break
                else:
                    print("** no instance found **")
                    
    def do_all(self, arg):
        """prints the string representation of all classes"""
        line = arg.split()
        if not line[0] or line[0] in ["BaseModel"]:
            obj_list = []
            for value in HBNBCommand.obj_container.values():
                obj_list.append(str(value))
            print(obj_list)
        else:
            print("** class doesn't exist **")
    
    def do_update(self, arg):
        """update <class name> <id> <attribute name> "<attribute value>\""""
        class_name, id, attr_name, attr_value = arg.split()
        if not class_name:
            print("** class name missing **")
        elif not id:
            print("** instance id missing **")
        elif not attr_name:
            print("** attribute name missing **")
        elif not attr_value:
            print("** value missing **")
        else:
            for key in HBNBCommand.obj_container.keys():
                if str(key) == "{}.{}".format(class_name, id):
                    """I couldnt type cast the attribute value to """
                    setattr(HBNBCommand.obj_container[key], attr_name, attr_value)
                    storage.save()
                    break
                else:
                    print("** no instance found **")
                
            

if __name__ == '__main__':
    HBNBCommand().cmdloop()
