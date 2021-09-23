# Exercise 2.27 Summation

Create the method `sum` in the exercise template so that it calculates and returns the sum of the numbers that are given as the parameter using the following structure:

```python
def sum(number1, number2, number3, number4):
    # write your code here
    # remember to include return (at the end)!

def main():
    answer = sum(4, 3, 6, 1)
    print("Sum: " + str(answer))
```

The output of the program:

```plaintext
Sum: 14
```

**NB:** when an exercise describes a method that should _return_ something, this means that the type of the return value must be declared in the method definition, and that the method contains a `return` command that returns the wanted data. The method itself will print nothing (i.e. will not use the command `print`) - that task is left to the method caller, which in this case is the main program.
