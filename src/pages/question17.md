- info
    - Lv.1
    - Binary Tree

# Robot-cat Maintenance Day

## Problem Description
Licat decided to create a robot called 'Robot-Cat', a delegate version of Licat's Fish Inc. to operate the giant company. So, Robot-Cat was born! Licat assigned a unique identification number to Robot-Cat to make it easy to manage Robot-Cat. Then, Robot-Cats flew all over Weniv World.

And on the day of Robot-Cat maintenance, the Robot-Cats returned to the company, but there were also some Robot-Cats that couldn't return because they were too far away. For the Robot-Cats that need maintenance among those who did not attend the maintenance, an alarm should be sent.


Write a function solution that returns the identification number of the Robot-Cat that needs an alarm to be sent based on the identification numbers of the Robot-Cats that attended and those that need maintenance.

---

## Constraints

- 1 ≤ the number of Robot-Cats that attended ≤ 1000 
- 1 ≤ the number of Robot-Cats that need maintenance ≤ 1000 
- The identification numbers of the Robot-Cats are not duplicated. 
- Sort the result in ascending order. This problem should be solved using a binary tree.

---

## Examples

| Input                                  | Output  |
| ------------------------------------ | ------- |
| [[2, 4, 1, 7, 9, 8, 12], [2, 4, 8, 3, 6]] | [3, 6] |
| [[3, 6, 9, 1, 8, 7], [3, 8]] | [] |
| [[102, 21, 38, 52, 219, 63, 1, 9, 35], [36, 9, 95, 32, 7, 52, 102]] | [7, 32, 36, 95] |

---

## Explanation for Examples

- The identification numbers for the Robot-Cats that attended, and the identification numbers for the Robot-Cats that need maintenance, are given. 
- Determine the identification number of the Robot-Cats that require an alarm. Sort in ascending order. 
- If there are no Robot-Cats that require an alarm, return an empty list.