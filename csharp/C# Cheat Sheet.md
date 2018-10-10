# C# Cheat Sheet

## Types
*	`int` – 32-bit integer;
*	`double` – 64-bit floating-point value;
*	`bool` – boolean values true/false;
*	`string` – sequence of zero or more Unicode characters.

You can convert `string` to `int`:
```csharp
int a = int.Parse(“234”);
```

You can mix int and double during calculations. 

## Assignment
Assignment works from right to left. First expression on the right is calculated and then it is saved to variable on the left.

Syntax:
```
<type> <variable> = <expression>;
```

Example:
```csharp
int a = 2;
a = a + 1;
string b = Console.ReadLine();
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
### if - else if - else
Most popular conditional statement. Must always start with `if`. `else if` and `else` are optional. Can have more than one `else if`. `else` should always be last.

Syntax:
```
if(<boolean statement>)
{
}
else if(<boolean statement>)
{
}
else
{
}
```

Example:
```csharp
int a = int.Parse(Console.ReadLine());  

if(a == 0) 
{
    Console.WriteLine("Zero");
}
else if(a > 0)
{
    Console.WriteLine("Larger than zero");
}
else
{
    Console.WriteLine("Less than zero");
}
```

## Loops
### while
The easiest type of loop. Repeats until its condition is `true`. You need to change the condition to `false` inside the loop to exit.

Syntax:
```
while(<boolean statement>)
{
}
```

Example:
```csharp
int a = 1;

while(a <= 5)
{
    Console.WriteLine(a);
    a = a + 1;
}
```
