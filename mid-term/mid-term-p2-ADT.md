# 2. Starting from an empty Heap ADT show what happens (draw on paper how the tree evolves)

# when you insert the following numbers: 5, 6, 7, 4, 3, 9, 8, 1, 2, 0 (in that order).

Min Heap

```
5
```

```add 6
  5
 /
6
```

```add 7
  5
 / \
6   7
```

```add 4

    4
   / \
  5   7
 /
6
```

```add 3
    3
   / \
  4   7
 / \
6   5
```

```add 9
     3
   /    \
  4      7
 / \    /
6   5  9
```

```add 8
     3
   /    \
  4      7
 / \    / \
6   5  9   8
```

```add 1
       1
     /    \
    3      7
   / \    / \
  4   5  9   8
 /
6
```

```add 2
       1
     /    \
    2      7
   / \    / \
  3   5  9   8
 / \
6   4
```

```add 0

        0
      /    \
     1      7
   /   \    / \
  3     2  9   8
 / \   /
6   4  5
```
