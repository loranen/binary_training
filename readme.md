# Binary training game

## Arguments

| Argument  | Explanation |
| -----    | ----- |
| ``Level``   | How many bits are used in the questions (default 4) |
| ``training``     | Infinite training mode answer 'q' to quit |
| ``game``   | Game of 5 questions. Points per questions formula: <br>points = 100 points - 100 points/20sec*answer_time    |

## Example usage:

```cmd
Selected Level: 4 (Max decimal 15)

1. What is decimal and binary of 0x3 (dec,bin): 3,11
Correct answer! 75.20 points earned
2. What is binary and hex of 7 (bin,hex): 111,7
Correct answer! 57.51 points earned
3. What is decimal and binary of 0x1 (dec,bin): 1,1
Correct answer! 87.97 points earned
4. What is decimal and binary of 0x5 (dec,bin): 5,101
Correct answer! 69.61 points earned
5. What is decimal and hex of 1011 (dec,hex): 11,b
Correct answer! 67.96 points earned

Game score:  358.25
Avg correct: 100 %
Avg time:    5.67 sec
```