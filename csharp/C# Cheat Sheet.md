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
<type> <variable name> = <expression>;
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
    <loop body>
}
```

Example:
```csharp
int i = 1;

while(i <= 5)
{
    Console.WriteLine(i);
    i = i + 1;
}
```

### for
Loop that allows you to execute a specific number of times.
Syntax:
```
for(<init>; <condition>; increment)
{
    <loop body>
}
```


Example:
```csharp
for(int i = 0; i < 5; i = i + 1)
{
    Console.WriteLine(i);
}
```

## Methods
Method is a way of grouping the code. C# is an object oriented language, so each method should belong to some class.
Each C# program has at least one class with method named `Main`.

To use a method you need first to **define** a method and then **call** it.

Syntax:
```
<access specifier> <return type> <method name>(<type> <parameter name>, ...) 
{
   <method body>
}
```

Example:
```csharp
public static void Main(string[] args)
{
    int sum = Sum(2, 3);
    Console.WriteLine(sum);
}

public int Sum(int a, int b)
{
    return a + b;
}
```
