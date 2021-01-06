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

The example above is where the rod has a diameter of 4 characters. The puzzle in `puzzle.txt` has been encrypted with a rod with a diameter of `n` characters.




## Solving

### Helpers

You can use `helper.print_puzzle_stats()` to get some useful information about the puzzle.
```
# Usage
puzzletext = read_puzzle()
helper.print_puzzle_stats(puzzletext)
```



### Programming

In python it's common to see loops like, 
```
for x in xs:
	# do something to x
```

But the `encrypt()` function uses loops like,
```
for i in range(0, len(xs)):
	#  do something to xs[i]
```

*Hint: why is the length of the list, `xs`, important?*