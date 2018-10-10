# Boolean Logic
The basic operations:  
* **AND** - the *and* of a set of operands is true if and only if *all* of its operands are true;
* **OR** - the *or* of a set of operands is true if and only if *one or more* of its operands is true.  

## C# Examples
```csharp
if(a == 1 && b == 2)
```
Will execute only if **a** is equal to **1** and **b** is equal to **2**.

```csharp
if(a == 1 || a == 2)
```
Will execute only if **a** is equal to **1** or **2**.

```csharp
if((a == 1 || a == 2) && b > 3)
```
Will execute only if **a** is equal to **1** or **2** and **b** is greater than **3**. Brackets are important here!

```csharp
if(a != 0)
```
Will execute only if **a** is not equal to **0** (int other words any number expect **0**).
