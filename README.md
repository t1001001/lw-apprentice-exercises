# Apprentice Exercises
This repository contains a list of programming exercises designed for apprentices at **LEONHARD WEISS** specialising in **application development**.

These exercises are made to help apprentices understand core programming concepts and to build proficiency in various programming paradigms and tools.

Each exercise is structured to achieve specific learning outcomes - follow the instructions in the respective folders and refer to the README sections for further clarification.


## 01-interfaces
**Problem:**

In this exercise, you're tasked with implementing an object-oriented design using abstract classes and inheritance. Specifically:
- Create an abstract base class **Geometry** with two abstract methods: **area()** and **perim()**. These methods should be implemented by all concrete subclasses.
- Create the two concrete classes **Rectangle** and **Circle** which both implement the **area()** and **perim()** methods.
- Define a **measure()** function that accepts any **Geometry** object and prints both its area and perimeter.

**Learning Outcome:**

By completing this exercise, you will:
- Understand how to define and work with **abstract classes**.
- Practice **inheritance** by extending an abstract class and implementing its abstract methods.
- Gain experience in using **polymorphism** where different classes share a common interface but have different implementations of methods like area() and perim().
- Develop the ability to design and structure classes around real-world objects with common properties and methods.


## 02-fizzbuzz
**Problem:**

In this exercise, you're tasked with implementing a function that iterates through numbers from 1 to **n** and for each number:
- Print **Fizz** if the number is divisible by 3.
- Print **Buzz** if the number is divisible by 5.
- Print **FizzBuzz** if the number is divisible by both 3 and 5.
- Otherwise, print the number itself.

**Learning Outcome:**

By completing this exercise, you will:
- Practice using loops and conditional statements.
- Develop the ability to manipulate and accumulate results in lists.
- Gain familiarity with handling multiple conditions in a structured manner.


## 03-arena
**Problem:**

In this exercise, you're tasked with implementing a small game in the terminal where two characters are created that fight each other - the game ends end one character is defeated.
- Create the classes **Knight**, **Archer** and **Wizard**. All classes should be subclasses of **Character**.
- The **Character** class has the fields **name**, **health** and **damage** and the methods **attack()** and **is_defeated()**.
- Knights deal double damage to Wizards but take double damage from Archers.
- Archers deal double damage to Knights but take double damage from Wizards.
- Wizards deal double damage to Archers but take double damage from Knights.
- Define a **battle()** function where two characters take turns fighting eachother - the function should end if one character is defeated.

**Learning Outcome:**

By completing this exercise, you will:
- Deepen your understanding in object-oriented programming through the use of **inheritance** and **polymorphism**.
- Learn how different objects interact with each other.
- Learn core principles of software and object-oriented design.


## 04-library
**Problem:**

In this exercise, you're tasked with designing a mini library management system using object-oriented principles. Books have a titel, author, pages and information whether they are checkout out or not. The system will allow the library to:
- Add printed books and e-books as well as checking them in and out.
- Display information about printed books and e-books.
- Compare books based on title and page counts.
- Additionally, printed books have a shelf locations while e-books have a file size.

**Learning Outcome:**

By completing this exercise, you will:
- Practice class inheritance and abstract base classes.
- Implement encapsulation using private and protected members.
- Apply polymorphism and method overriding.
- Overload operators in custom classes.

## Notes

Feel free to explore each exercise, modify the code, and experiment with variations.

The goal is not only to complete each task, but to understand the underlying concepts and principles.