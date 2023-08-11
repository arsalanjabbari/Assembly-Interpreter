## Assembly-Interpreter

The Assembly Interpreter is a project that aims to interpret and execute assembly language programs defined in a specific format. This interpreter reads input from a text file containing a sequence of assembly instructions and their corresponding operands. Each instruction is represented by a unique code, and the interpreter processes these codes to simulate the execution of the assembly program.

### Table of Contents
- [Introduction](#introduction)
- [Project Overview](#project-overview)
- [Features](#features)
- [Getting Started](#getting-started)
- [Conclusion](#conclusion)

### Introduction
The Assembly Interpreter project provides a tool to translate and execute assembly language programs. Assembly language is a low-level programming language that is closely related to the architecture of a computer's central processing unit (CPU). It uses mnemonic codes to represent machine instructions, making it more human-readable compared to machine code.

The input for the Assembly Interpreter is a plain text file following a specific format. Each line in the file represents an assembly instruction and its operands. The interpreter reads the instructions, processes them sequentially, and simulates the execution of the program. The provided sample program, factorial.txt, calculates the factorial of a given number.
### Project Overview
The Assembly Interpreter project is organized into a well-defined structure to facilitate easy navigation and understanding. Here's an overview of the key components you'll find in this repository:
```
assembly-interpreter/
├── main.py                 # The main interpreter script
├── factorial.txt           # Sample assembly program: factorial calculation
├── find_max.txt            # Additional example assembly program
├── sum_0_to_n.txt          # Additional example assembly program
├── README.md               # Project documentation
```

### Features
1. **Error Handling**: The program performs three levels of error handling to validate the instructions provided in the input file. It checks for the format and validity of different types of instructions.

2. **Instruction Execution**: The script contains implementations for different assembly-like commands such as BRU, RWD, LDA, STO, SUB, BMI, MPY, ADD, WWD, and HLT. These commands are executed based on the provided input instructions.

### Getting Started
To run this project, follow these steps:
1. Clone the Repository: Start by cloning this repository to your local machine.

2. Input File: Create a text file containing your assembly program, similar to the factorial.txt sample provided.

3. Run the Interpreter: Execute the Assembly Interpreter, providing the path to your assembly program text file as an argument.

4. Execution: The interpreter will process each line of the input file, simulating the execution of the assembly program. It will display the output and final result of the program, if applicable.


   ```bash
   python main.py
   ```

### Conclusion
The Assembly Interpreter project offers an educational and practical insight into the workings of assembly language programming. By reading and simulating assembly programs, users can deepen their understanding of low-level computer architecture and program execution. This project serves as a valuable tool for students, educators, and anyone interested in learning about the fundamental concepts of programming and computer systems.
