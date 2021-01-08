# Level 5

## Puzzle

The Vignere cipher is one of the strongest classical ciphers. Level 5 is a slightly weakened version of it. You'll find the stronger version in Level 6. 

The Vignere cipher is best thought of as a repeated Caesar cipher. Recall the Caesar cipher

```
message : HELLO
key     : 3
cipher  : KHOOR
```

We can also express the `key` as a letter. 

```
message : HELLO
key     : D (3)    /* Here the letter A = 0.
cipher  : KHOOR
```

Now suppose we make a key out of more one that letter,

```
message : HELLO
key     : KEY
cipher  : ?????
```

The Vignere cipher uses a key like this, and repeats it for the length of the message. Then each character in the message is encrypted according to that part of the key.

```
message : HELLOWORLD
key     : KEY

/* Extend the key to the length of the message */

message : HELLOWORLD
key     : KEYKEYKEYK

/* Encrypt each letter in the message by each letter in the key */

message : HELLOWORLD
key     : KEYKEYKEYK
cipher  : RIJVSUYVJN

/* Breaking down the encryption of the first three letters */
A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25

H + K = R   (7  + 10 = 17)
E + E = I   (4  + 4  = 8)
L + Y = J   (11 + 24 = 35 # we 'wrap' around by subtracting 26 # = 35 - 26 = 9)
```

Cracking the Vignere cipher is quite tricky, so for this level I've made the key easy.

## Solving

