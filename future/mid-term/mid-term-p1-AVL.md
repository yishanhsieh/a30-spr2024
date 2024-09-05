# 1. Start from an empty AVL tree and show what happens (draw on paper how the tree evolves)

# when you insert the following numbers: 5, 6, 7, 4, 3, 9, 8, 1, 2, 0 (in that order).

```
5
```

```add 6
5
 \
  6
```

```add 7
  6
 / \
5   7
```

```add 4
     6
    / \
   5   7
  /
 4
```

```add 3
     6
    / \
   4   7
  / \
 3   5
```

```add 9
     6
    / \
   4   7
  / \   \
 3   5   9
```

```add 8
      6
    /   \
   4     8
  / \   / \
 3   5  7   9

```

```add 1
      6
    /   \
   4     8
  / \   / \
 3   5  7   9
/
1
```

```add 2
      6
    /    \
   4      8
  / \    / \
 2   5  7   9
/ \
1  3
```

```add 0
       6
    /    \
   2      8
  / \    / \
 1   4  7   9
/   / \
0  3   5
```
