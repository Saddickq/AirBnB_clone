#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.engine import file_storage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

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
        args = arg.split(" ")
        if not args[0]:
            print("** class name missing **")
        elif not isinstance(args[0], BaseModel):
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            
            
    
    def emptyline(self):
        pass
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
