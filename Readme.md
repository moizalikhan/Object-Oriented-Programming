# Object-Oriented Programming Concepts

## OOP Basics

A class is a blueprint for creating objects. Classes are a layer of abstraction over constructor functions.

Objects are instances of a class.

Note: We can chain methods on an object but we must return the object every time on method.

## Core OOP Principles

### Abstraction

Allows us to hide complex implementation details while exposing only the necessary parts of an object.

Examples: Classes, Constructor, Prototypes, Closures

#### Abstract Classes

- Blueprint for creating objects that cannot be instantiated on its own
- Serves as a template for other classes
- Contains methods that subclasses must implement
- Provides default implementations
- Classes extend only one abstract class (inheritance)

#### Interfaces

- A contract specifying methods a class must implement
- Don't provide default implementations
- Contains abstract methods
- Can implement multiple interfaces (multiple inheritance)
- Can have public(readonly), static, or final fields

#### Methods Types

- Abstract methods: Does not have an implementation body, must be implemented by subclasses
- Concrete methods: Implemented methods

### Encapsulation

Data hiding to control access to object properties. Keeping data and methods private inside the class that are not accessible outside of class.

#### Field Types

- Public fields: Declared outside/inside constructor, present on each instance, not part of prototype
- Public methods: Functions accessible from instances, not in constructor, part of prototype
- Private fields: Declared with #, not in constructor, can assign values
- Private methods: Functions declared with #, must be declared in class body

Notes:

- Getters and setters can be public or private
- Both static and instance variables can be public and private
- Public methods typically interact with private fields/methods

Example: Closures

### Inheritance

Allows a new class to be based on an existing class. The new class inherits properties and methods from the existing class.

Features:

- Hierarchical classification of classes
- Method overriding (polymorphism)
- Uses "extends" keyword
- Examples: prototype chain, Object.create()

#### Super()

- Used within class to call parent methods/constructors
- Must be called before using 'this' in subclass constructor
- Ensures proper initialization of inheritance chain

### Polymorphism

Methods can take different forms based on the calling object.

Types:

1. Sub-type (inheritance based)
2. Parametric Polymorphism
3. Duck Typing (Behavioral)

#### Method Types

- Static methods: Belong to class itself, not instances
- Static variables: Shared among all class instances
- Virtual Functions: Methods in base class overrideable in derived class

## Function Comparison

| Aspect       | Normal Function       | Constructor Function     |
| ------------ | --------------------- | ------------------------ |
| Purpose      | Tasks/calculations    | Creates objects          |
| Invocation   | greet()               | new Person()             |
| Return Value | Explicit              | New object automatically |
| this Binding | Global/calling object | New instance             |
| Naming       | camelCase             | PascalCase               |

## SOLID Principles

### Single Responsibility (S)

Class should have only one reason to change
Example: UserClass, SendEmailClass

### Open/Closed (O)

Open for extension, closed for modification
Example: Calculator, CircleArea, TriangleArea

### Liskov Substitution (L)

Subclass objects should be replaceable for superclass objects

### Interface Segregation (I)

Clients shouldn't depend on unused interfaces
Example: Work(), eat()

### Dependency Inversion (D)

High-level modules should depend on abstractions, not low-level modules

## Design Patterns

### Types

- Creational: Object creation
- Structural: Object/class structure
- Behavioral: Object responsibilities

### Common Patterns

#### Singleton

- Single instance with global access
- Private constructor
- Static creation method

#### Factory

- Superclass creates objects
- Subclasses alter object types
- Decoupled creation code

#### Strategy

- Interchangeable algorithms
- Runtime flexibility

#### Observer

- One-to-many object relationships
- Notification system
