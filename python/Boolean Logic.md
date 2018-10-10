# Boolean Logic
The basic operations:  
* **AND** - the *and* of a set of operands is true if and only if *all* of its operands are true;
* **OR** - the *or* of a set of operands is true if and only if *one or more* of its operands is true.  

## Python Examples
```python
if a == 1 and b == 2:
```
Will execute only if **a** is equal to **1** and **b** is equal to **2**.

```python
if a == 1 or a == 2:
```
Will execute only if **a** is equal to **1** or **2**.

```python
if (a == 1 or a == 2) and b > 3:
```
Will execute only if **a** is equal to **1** or **2** and **b** is greater than **3**. Brackets are important here!

```python
if a != 0:
```
Will execute only if **a** is not equal to **0** (int other words any number expect **0**).
