🐍 Python OOP

!Python !Rich !Status

A collection of Python exercises and challenges focused on Object-Oriented Programming (OOP), progressing from basic classes to inheritance, abstraction, polymorphism, and encapsulation.

📌 About This Repository

Learning OOP through theory alone isn't enough. This repository turns concepts into working code through small, practical projects, including:

A TV remote control.
A shipping cost calculator.
A payroll system.
Exercises involving inheritance and abstract classes.

The output is displayed in the terminal using Rich.

The main goal is to practice not only how to make code work, but also how to organize it properly, giving each class a clear responsibility and keeping business logic separate from the user interface.

📚 Concepts Covered
Concept	Examples
Classes, objects, and constructors (__init__)	ex01, ex02, desafios/challange001–006
Special methods (__str__)	ex02, desafios/challange003–004
Class and instance attributes	desafios/challange001, desafios/10, ex07
Inheritance and super()	ex04, ex05, ex06
Abstract classes (ABC, @abstractmethod)	ex06, ex07, desafios/challange008–010
Polymorphism	desafios/challange008–010, ex07
Encapsulation (@property, getters, and setters)	desafios/challange007
✨ Highlights
🎮 Remote Control

Location: desafios/challange007.py

Encapsulated channel and volume attributes.
Getters and setters with input validation.
TV state controlled through the power() method.
User interface logic separated from the class.
🚚 Shipping Cost Calculator

Location: desafios/10

Abstract base class: Transporte.
Subclasses: Moto, Caminhao, and Drone.
Each subclass implements calc_frete() according to its own distance rules.
Demonstrates polymorphism and abstraction.
💰 Payroll System

Location: ex07

Abstract base class: Funcionario.
Subclasses: FuncionarioHorista and FuncionarioMensalista.
Each subclass implements its own salary calculation.
🛠️ Technologies
Technology	Purpose
Python 3.12+	Programming language
Rich	Terminal panels and tables
abc	Abstract base classes
math	Mathematical operations
os	Operating system utilities
📂 Project Structure
python-poo/
├── ex01/                   # Classes, attributes, and methods
├── ex02/                   # Constructors, __str__, and __dict__
├── ex03/                   # Bank account
├── ex04/                   # Inheritance
├── ex05/                   # Inheritance, one class per file
├── ex06/                   # Abstract Person class
├── ex07/                   # Payroll system
├── desafios/
│   ├── challange001–006/   # Basic OOP exercises
│   ├── challange007.py     # Remote control and encapsulation
│   ├── challange008.py     # Polygons: area and perimeter
│   ├── challange009.py     # Hot beverages
│   ├── 10/                 # Shipping cost calculator
│   └── 11/                 # Work in progress
└── rich/                   # Rich library experiments

🚀 Getting Started
1. Clone the repository
git clone https://github.com/yaakz007/python-poo.git
cd python-poo

2. Install the dependency
pip install rich

3. Run an exercise

Directories containing __main__.py can be executed directly:

python ex07
python desafios/10


Standalone Python files can be executed individually:

python desafios/challange007.py
python desafios/challange008.py

Remote Control Commands

When running challange007.py, use the following keyboard commands:

Key	Action
@	Turn the TV on or off
+ / -	Increase or decrease the volume
< / >	Change the channel
#	Select a channel
0	Exit the program
📸 Example Output
Shipping Cost Calculator

Command: python desafios/10

Example for a distance of 30 km:

┏━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┓
┃ Distance  ┃ Type     ┃ Shipping Cost       ┃
┡━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━┩
│ 30km      │ Moto     │ R$15.00             │
│ 30km      │ Caminhao │ Minimum range: 50km │
│ 30km      │ Drone    │ Maximum range: 10km │
└───────────┴──────────┴─────────────────────┘

Payroll System

Command: python ex07

╭─────────────────── Salary Analysis ──────────────────────╮
│ Lucas Gabriel's salary is R$6891.25, equivalent to 4.3  │
│ minimum wages.                                            │
╰───────────────────────────────────────────────────────────╯

🗺️ Roadmap
Encapsulate the bank account balance using _saldo, @property, and validation for withdrawals and deposits.
Improve encapsulation in Funcionario, including salario_bruto and salario.
Replace abstractclassmethod with abstractmethod in ex06 and implement estudar().
Complete the exercise in desafios/11.
Add automated tests with pytest for shipping costs, salary calculations, and remote control limits.
Rename files containing the misspelling challange to challenge.
Add a short problem description to each challenge.

This repository is part of my journey to improve my Python skills and build a solid understanding of Object-Oriented Programming.
