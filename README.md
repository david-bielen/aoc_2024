<h1>Advent of code 2024</h1>

This repo contains the python code to solve the riddles in the advent of code 2024 series: https://adventofcode.com/2024/

The source code is encrypted and each file represents one riddle (each day consists of two riddles).
To decrypt a file, you need to execute the following:
```
openssl enc -d -aes-256-cbc -in input_file.py -out output_file.py
```
The encryption password is the answer for the riddle the code intends to solve.
