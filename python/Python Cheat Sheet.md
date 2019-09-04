# Python Cheat Sheet

## Syntax

Python uses new lines to complete a command, as opposed to other programming languages which often use semicolons or parentheses.

Python relies on indentation, using whitespace, to define scope; such as the scope of loops, functions and classes. Other programming languages often use curly-brackets for this purpose.

## Comments

You often might want to add some explanations to the code which should not be interpreted as actual code. To do that `#` is used. Everything to the right of the `#` is ignored by python interpreter.

```python
# this line is just a comment
print("Hi") # will print 'Hi' to console and ignore everything after that
```

## Types

*	`int` – whole number;
*	`float` – floating-point number;
*	`bool` – boolean values true/false;
*	`str` – sequence of zero or more Unicode characters.

You can convert between types:
```python
a = int("234") # converts string "234" to int and saves the value to 'a' variable
b = float("2.9") # converts string "2.9" to float and saves the value to 'b' variable
c = int(3.4) # converts float 3.4 to int, and saves the value (which will be 3) to 'c' variable
```

## Assignment

Assignment works from right to left. First expression on the right is calculated and then it is saved to variable on the left.

Syntax:
```
<variable> = <expression>
```

Example:
```python
a = 2; # saves value 2 to varibale 'a'
a = a + 1; # takes current 'a' value which is 2, adds 2 and 1 and saves 3 to variable 'a'
b = input("Enter a value: ") # reads string value from console and saves it to variable 'b'
c = a + int(b) # takes 'a' value which is 3, converts 'b' to int and saves the sum to variable 'c'
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
    # loop
    # body
```

Example:
```python
a = 1

while a <= 5:
    print(a)
    a = a + 1
```

## Functions
Function is a way of grouping the code. To use a method you need first to **define** a method and then **call** it.

Syntax:
```
def  <function name>(<parameter>, ...):
    # function
    # body
```

Example:
```python
def sum(a, b):
    return a + b

s = sum(2, 4)
print(s)
```
