# Level One

### Puzzle

Cracking Caesar's cipher was pretty easy. Just shift left by 3. But what if you don't know how many characters it's been shifted by? 

The puzzle,

```
NZHLCODOTPXLYJETXPDMPQZCPESPTCOPLESDESPGLWTLYEYPGPCELDEPZQOPLESMFEZYNPZQLWWESPHZYOPCDESLETJPESLGPSPLCOTEDPPXDEZXPXZDEDECLYRPESLEXPYDSZFWOQPLCDPPTYRESLEOPLESLYPNPDDLCJPYOHTWWNZXPHSPYTEHTWWNZXPS
```

has been shifted by `n` characters. What was the original text?



## Solving

From this puzzle onwards, I've included some functions to help you out in `tools/helper.py`. 

#### Helpers

You can use `helper.write_line_to_file()` to write some text out to a file in case you want to look at it later.  
```
# Example usage
my_string = 'Hello World'
helper.write_line_to_file(my_string)
```
When you call this function, the string you pass as a parameter will be written to `scratchpad.txt`








