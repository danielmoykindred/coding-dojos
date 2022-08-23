# Eight Queens

## Kata
The kata is based on the classic chess rules. You must put eight chess queens on an 8x8 chessboard such that none of them are able to capture any othe rusing the standard chess queen's moves.

## Step 1
Use TDD to build a program that finds all solutions.

## Tree traversal
* Rewrite a new program to use a Depth-first walk
* Rewrite a new program to use a Breadth-first walk
* Compare performances and lisibility

## Output
* An 8x8 board
* A `1` represents a Queen
* A blank space represents an empty square

## Example Solution
```
+---+---+---+---+---+---+---+---+
|   |   |   |   |   | 1 |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   | 1 |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   | 1 |   |
+---+---+---+---+---+---+---+---+
| 1 |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   | 1 |
+---+---+---+---+---+---+---+---+
|   | 1 |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   |   |   | 1 |   |   |   |
+---+---+---+---+---+---+---+---+
|   |   | 1 |   |   |   |   |   |
+---+---+---+---+---+---+---+---+

00000100
00010000
00000010
10000000
00000001
01000000
00001000
00100000
```

[Coding Dojo Link](https://codingdojo.org/kata/eight-queens/)