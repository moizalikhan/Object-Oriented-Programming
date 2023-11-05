## Java Notes

* In functional programming not modifying the data as much and it also has first class functions
* Code + data = object
* Classes --- named groups of properties and functions
* Compile time--means converting language to machine codes--0s and 1s
* In statically type languages type checking is done at compile time
  * int a = 10
  * a = 'moiz'--gives an error
  * a -- reference variable in stack and 10 is the object in heap
  * more than one reference variable can point to same object 
  * if any one of the reference variable change the object then it is changed for every reference variable
  * in java there's only pass by reference value
  * an object without the reference variable will be deleted by garbage collector 

### Java Architecture:
* java code in .java file(source code)
* java compiler compiles the file into byte code(.class)(binary format that consists of constants, references and numeric codes)
* and byte code is run by JVM
* byte code --> interpreter --> binary because of this Java is platform independence
* JVM is platform Dependent
* JDK--> Java Development kit
    * JDK: JRE-->Java Runtime Environment + Developer Tools
      *  JRE: JVM-->Java Virtual Machine + Library Classes
        * JVM: JIT--> Just In Time Compiler
* JDK: a package and environment
  * JRE --> only environment and other and JVM
    * Class loader load all classes needed to execute the program
    * JVM sends bytecode to bytecode verifier to check the format of code
  * JavaC(compiler)
  * Jar --> archiver
  * Java Docs -->docs generator
  * interpreter / loader
* Run time image
* 

