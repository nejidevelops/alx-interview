0x01. Lockboxes
===============

This repo is included in Specializations - Web Stack programming ― Back-end Course of Holberton School. We will cover the `Lockboxes` for interview folder.

![Logo](https://www.howtogeek.com/wp-content/uploads/2021/05/laptop-with-terminal-big.png?height=200p&trim=2,2,2,50)

Tasks
-----

### 0\. Lockboxes

You have `n` number of locked boxes in front of you. Each box is numbered sequentially from `0` to `n - 1` and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

*   Prototype: `def canUnlockAll(boxes)`
*   `boxes` is a list of lists
*   A key with the same number as a box opens that box
*   You can assume all keys will be positive integers
    *   There can be keys that do not have boxes
*   The first box `boxes[0]` is unlocked
*   Return `True` if all boxes can be opened, else return `False`

    carrie@ubuntu:~/0x01-lockboxes$ cat main_0.py
    #!/usr/bin/python3
    
    canUnlockAll = __import__('0-lockboxes').canUnlockAll
    
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))
    
    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))
    
    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))
    
    carrie@ubuntu:~/0x01-lockboxes$
    

    carrie@ubuntu:~/0x01-lockboxes$ ./main_0.py
    True
    True
    False
    carrie@ubuntu:~/0x01-lockboxes$
    


## Acknowledgments :mega: 

### **`Holberton School`** (*providing guidance*)
This program was written as part of the curriculum for Holberton School.
Holberton School is a campus-based full-stack software engineering program
that prepares students for careers in the tech industry using project-based
peer learning. For more information, visit [this link](https://www.holbertonschool.com/).
<p align="center">
	<img src="https://assets.website-files.com/6105315644a26f77912a1ada/610540e8b4cd6969794fe673_Holberton_School_logo-04-04.svg" alt="This is a secret;)">
</p>
