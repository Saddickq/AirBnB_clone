import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_create(self, value):
        """Create user with uuid"""
        self.value = value

    def do_all(self, value):
        """Prints the reloaded deserialised info"""
        print(self.load())

    def do_EOF(self, arg):
        """sends an Eof  signal to quit the interpreter"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()
