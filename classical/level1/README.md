# Level One

### Puzzle

Cracking Caesar's cipher was pretty easy. Just shift left by 3. But what if you don't know how many characters it's been shifted by? 

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



From this puzzle onwards, I've included some functions to help you out in `tools/helper.py`. 

### Helpers

#### `helper.write_line_to_file()`

You can use `helper.write_line_to_file()` to write some text out to a file in case you want to look at it later.

```python
# Example usage
my_string = 'Hello Level 4'
helper.write_line_to_file(my_string)
```

When you call this function, the string you pass as a parameter will be written to `scratchpad.txt`



## Extension

See `Extension.md`!






