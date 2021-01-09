# Level 6

## Puzzle

Congratulations on making it to the end! This one will be tough. 

This puzzle is the same as level 5, with one key difference (pun intended). This time, you don't know the length of the key.

The file, `puzzle.txt` has been encrypted in this way. You have to decrypt it!

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