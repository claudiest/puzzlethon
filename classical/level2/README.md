# Level Two

## Puzzle

The Spartans had their own encryption method, different from how the Romans did it. They would take a long string of characters, and wrap them around a stick.

From Wikipedia,

"
Suppose the rod allows one to write four letters around in a circle and five letters down the side of it. The plaintext could be, "I am hurt very badly help". To encrypt, one simply writes across the leather

```
_____________________________________________________________
       |   |   |   |   |   |  |
       | I | a | m | h | u |  |
     __| r | t | v | e | r |__|
    |  | y | b | a | d | l |
    |  | y | h | e | l | p |
    |  |   |   |   |   |   |
_____________________________________________________________
```
so the ciphertext becomes, "Iryyatbhmvaehedlurlp"
"



The example above is where the rod has a diameter of `4` characters. The puzzle in `puzzle.txt` has been encrypted with a rod with a diameter of `n` characters.




## Solving

### `solve()`

Write your code within the `solve()` function. The puzzle has been automatically read in for you, and saved as `puzzletext`
```python
def solve():
    puzzletext = read_puzzle()

    # Your code goes here! #
    
    return plaintext # Save your answer in this variable

```

### Helpers

#### `helper.write_line_to_file()`

You can use `helper.write_line_to_file()` to write some text out to a file in case you want to look at it later.

```python
# Example usage
my_string = 'Hello Level 4'
helper.write_line_to_file(my_string)
```

When you call this function, the string you pass as a parameter will be written to `scratchpad.txt`

#### `helper.print_puzzle_stats()`

You can use `helper.print_puzzle_stats()` to get some useful information about the puzzle.

```python
# Usage
puzzletext = read_puzzle()
helper.print_puzzle_stats(puzzletext)
```



### Python Note

In python it's common to see loops like, 
```
for x in xs:
	# do something with x
```

But the `encrypt()` function uses loops like,
```
for i in range(0, len(xs)):
	#  do something with xs[i]
```

*Hint: why might the encryption function be concerned with the length of a list*