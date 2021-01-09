# Level 4



## Puzzle

Slow down, you crazy child! You've beaten my Caesar Cipher and you've beaten my Substitution Cipher but can you beat them both at once? 

This time, the encryption scheme has two phases. First, the characters are shifted along in a similar manner to `level2/`

Then the shifted characters are passed through a substitution table, like in `level3/`

The message in `puzzle.txt` has been encrypted in this way.  You've got to decrypt it!



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

You can use `helper.print_puzzle_stats()` to display some interesting statistics about the puzzle.

```python
# Example usage
puzzletext = read_puzzle()
helper.print_puzzle_stats(puzzletext)
```

When you call this function, the stats will be printed to the screen.

#### `helper.SubstitutionTable()`

One of the parameters to the `encrypt()` function is a python `dict`. The helper provides a custom version of the standard `dict` equipped with some functions you may find useful. 
```python
# Example usage
substitution_table = helper.SubstitutionTable()

# print the table
substitution_table.print_table()

# read in a mapping to the substitution table
my_mapping_file = 'guess.txt'
substitution_table.read_in_table(my_mapping_file)
```



*Hint: The more things change, the more they stay the same...*