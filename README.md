# AirBnB Clone

## About

This project provides a command-line interpreter or as we like to call it the `Console` for managing instances of different classes.the interpreter implements operations like (Create, Read, Update, Delete) on instances/objects of various classes. It also includes a base class or creating instances with UUIDs and serialization and deserialization functionality.

## Quirks and features
The following provide the several operations performed by the command line interpreter:

* objects creation
* serialisation of python objects
* Persisting created objects into files
* deserialisation of json strings
* Retrieving objects from files
* Manipulating retrieved objects
* Updating stored objects
* Destroying an object


# Concepts

* Python packages and modules
* packaage and module importation
* object oriented programming concepts
* datetime module
* uuid module
* serialisation to json format
* deserialisation from json foromat to python object
* unittesting
* args & kwargs
* cmd interpreter

## Installation

* Clone this repository to your local machine.
* Navigate to the project directory.

## Usage

* To run the the command interpreter interratively run the following command in your terminal:

`python console.py`

or

`./console.py`

* To run the the command interpreter in non interactive mode run the following command in your terminal:

`echo "help" | ./console.py`


## example
(if you see this then you know you did it right)

```$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
create  help add  change  quit```


## Testing
to run the unit tests of the instant program run:

$ python -m unittest discover tests
