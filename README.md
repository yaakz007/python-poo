🐍 Python POO

!Python !Rich !Status

A collection of exercises and challenges focused on Object-Oriented Programming (OOP) in Python, organized by increasing complexity — from basic classes to inheritance, abstract classes, polymorphism, and encapsulation.

Why This Repository Exists

Learning OOP through theory alone isn't enough. Here, each concept is turned into working code: a small problem (a remote control, a shipping cost calculator, or a payroll system) solved using classes, with the results displayed in the terminal using the Rich library.

The goal isn't just to "make it work," but to practice code organization: each class has a clear responsibility and is kept separate from the code responsible for displaying the interface.

Concepts Covered
Concept	Where to Find It
Classes, objects, and constructors (__init__)	ex01, ex02, desafios/challange001 to 006
Special methods (__str__)	ex02, desafios/challange003, 004
Class vs. instance attributes	desafios/challange001, desafios/10, ex07
Inheritance and super()	ex04, ex05, ex06
Abstract classes (ABC, @abstractmethod)	ex06, ex07, desafios/challange008, 009, 10
Polymorphism	desafios/challange008, 009, 10, ex07
Encapsulation (_atributo, @property, getters, and setters)	desafios/challange007
Highlights
Remote Control (desafios/challange007.py): Channel and volume are protected, with getters and setters that validate their allowed ranges. The TV's state can only be changed through the power() method, keeping the interface outside the class.
Shipping Cost Calculator (desafios/10): An abstract Transporte class with Moto, Caminhao, and Drone, each implementing calc_frete() according to its own distance rules, demonstrating polymorphism.
Payroll System (ex07): An abstract Funcionario class with FuncionarioHorista and FuncionarioMensalista, each calculating salaries according to its own rules.
Technologies
Layer	Technology
Programming language	Python 3.12+
Terminal interface	Rich (panels and tables)
Standard library	abc, math, os
Project Structure
python-poo/
├── ex01/              # First class, attributes, and methods
├── ex02/              # Constructor, __str__, __dict__
├── ex03/              # ContaBancaria
├── ex04/              # Inheritance (Pessoa, Aluno, Professor, Funcionario)
├── ex05/              # Inheritance, one class per file
├── ex06/              # Abstract class Pessoa
├── ex07/              # Abstract Funcionario (Horista and Mensalista)
├── desafios/
│   ├── challange001–006/  # Cadastro, etiqueta, churrasco, livro, gamer, caneta
│   ├── challange007.py    # Remote control (encapsulation)
│   ├── challange008.py    # Polygons (area and perimeter)
│   ├── challange009.py    # Hot beverages
│   ├── 10/                # Shipping cost calculator
│   └── 11/                # In progress
└── rich/              # Experiments with the Rich library

How to Run

Clone the repository and install the required dependency:

git clone https://github.com/yaakz007/python-poo.git
cd python-poo
pip install rich


Directories containing __main__.py can be executed using their directory paths:

python ex07
python desafios/10


Standalone Python files can be executed directly:

python desafios/challange007.py
python desafios/challange008.py


The desafios/challange007.py remote control exercise uses the following keyboard commands:

Key	Action
@	Turn the TV on or off
+ / -	Increase or decrease the volume
< / >	Change the channel
#	Select a channel
0	Exit the program
Example Output
Shipping Cost Calculator

Command: python desafios/10 (shipping costs for 30 km).

┏━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┓
┃ Distância ┃ Tipo     ┃ Frete               ┃
┡━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━┩
│ 30km      │ Moto     │ R$15.00             │
│ 30km      │ Caminhao │ Raio mínimo de 50km │
│ 30km      │ Drone    │ Raio máximo de 10km │
└───────────┴──────────┴─────────────────────┘

Payroll System

Command: python ex07 (net salary after INSS deductions).

╭─────────────────── Análise de salário ───────────────────╮
│ O salário de Lucas Gabriel é de R$6891.25 e corresponde  │
│ a 4.3 salários mínimos.                                  │
╰──────────────────────────────────────────────────────────╯

Future Improvements
Encapsulate ContaBancaria: The balance is currently public. The next step is to protect it using _saldo, @property, and validation in saque and deposito, following the approach used in the remote control exercise.
Encapsulate Funcionario: salario_bruto and salario are still public, and salario is only available after calling calc_sal().
Improve ex06: Replace abstractclassmethod with abstractmethod and properly implement the estudar() method.
Complete desafios/11: Finish the exercise, as the file is still incomplete.
Add tests: Use pytest to test shipping cost calculations, salary rules, and remote control limits.
Standardize filenames: Correct the spelling of challange to challenge in a future cleanup and document each challenge with a short problem statement.
