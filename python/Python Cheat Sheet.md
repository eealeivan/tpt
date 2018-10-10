# Python Cheat Sheet

## Syntax

Python uses new lines to complete a command, as opposed to other programming languages which often use semicolons or parentheses.

Python relies on indentation, using whitespace, to define scope; such as the scope of loops, functions and classes. Other programming languages often use curly-brackets for this purpose.

## Types

*	`int` – whole number;
*	`float` – floating-point number;
*	`bool` – boolean values true/false;
*	`str` – sequence of zero or more Unicode characters.

You can convert between types:
```python
a = int("234") # converts string "234" to int
b = float("2.9") # converts string "2.9" to float
c = int(3.4) # converts float 3.4 to int, c will be 3
```

## Assignment

Assignment works from right to left. First expression on the right is calculated and then it is saved to variable on the left.

Syntax:
```
<variable> = <expression>
```

Example:
```python
a = 2;
a = a + 1;
b = input("Enter a value: ")
c = a + int(b) # b is str
```

## Comparison Operators 

*	`<` – less than;
*	`>` – greater than;
*	`<=` – less than or equal to;
*	`>=` – greater than or equal to;
*	`==` – equal to;
*	`!=` – not equal to.

All comparison operators return `bool` result.

## Conditional Statements

### if - elif - else

Must always start with `if`. `elif` and `else` are optional. Can have more than one `elif`. `else` should always be last.

Syntax:
```
if <boolean statement>:
    # code
elif <boolean statement>:
    # code
else:
    # code
```

Example:
```python
a = int(input())  

if a == 0: 
    print("Zero")
elif a > 0:
    print("Larger than zero")
else:
    print("Less than zero")
```


## Loops
### while
The easiest type of loop. Repeats until its condition is `true`. You need to change the condition to `false` inside the loop to exit.

Syntax:
```
while <boolean statement>:
    #code
```

Example:
```python
a = 1

while a <= 5:
    print(a)
    a = a + 1
```

