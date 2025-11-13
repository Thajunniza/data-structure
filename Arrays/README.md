# Arrays

## What is Array
- Array is a linear way of organising data by holding multiple values of same datatype under one variable.
- the elements of the array is accessed through index which is the position.
- Elements don’t have to be accessed sequentially; that is, if I need the 10th element of an array, I can access it directly without having to read the 9 elements stored in the array before it.
- abstract datatype.

## How memeory is organized
- think memory as a stack of shelfes holding removable drawers.
- drawers are the variables to hold the data which can be of different sizes based on the data or data type it hold.
- size of the memory determines how many varaiable it can hold.

## When we use Array
- when you need to store, iterate over, or manipulate a collection of values of (roughly) the same type without knowing much about how the individual values are correlated.

## Array charac
- Arrays are allocated in memory as a single, uninterrupted block of memory with sequential locations, which is both memory and time efficient.
- that means elements of an array located in contegious.
- Arrays are restricted to storing data of the same type. This restriction also stems from the need for optimization because it allows the same memory to be allocated for each element in the array and the compiler/interpreter to quickly know the memory address of each element.


## Array Type based on muttable:
1. Static Array - where the size of the array is fixed and should be defined while declaration.
2. Dynamic Array - where the size is not mandate to define at the time of declaration.

## array Type based Dimension
1. One-Dimensional Array (1D) - a simple linear list of elements.declared with single index.
one row mul columns.
arr = [1, 2, 3, 4, 5]
Access with one index → arr[2].
2.Two-Dimensional array (2D) - array of arrays - like a matrix(rows & columns).
declared with double index.
combination of 1 dimensional array
arr_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
Access → arr_2d[row][col]
Example: arr_2d[1][2] → 6
3.Multi-Dimensional Array (3D, 4D, …)
an array within arrays within arrays.
think of cubes, tensors in AI.
arr_3d = [
    [
        [1, 2], [3, 4]
    ],
    [
        [5, 6], [7, 8]
    ]
]

Access → arr_3d[x][y][z]
4. Jagged Array (Irregular Array)
arrays of different lengths inside.
jagged = [
    [1, 2, 3],
    [4, 5],
    [6]
]
Each row has a different size.



## 📝 Topics
- 📊 [Arrays](./Arrays/)


## 📺 YouTube Playlists
- [William Fiset's Data Structure Playlist](https://www.youtube.com/playlist?list=PLDV1Zeh2NRsB6SWUrDFW2RmDotAfPbeHu)
