# Problem #1

## Task

Find the sum of all multiples of 3 or 5 below 1000.

## Solution

In range from `r1` to `r2` with step `step` take each number, check if number is multiples of 3 (`a`) or 5 (`b`) and add to `sum`. Print `sum`.

## Handle change with ease

In order to handle change well the following things were introduced:

* Variables `r1`, `r2` and `step` - use to redefine range borders and step;
* `dividers` - list of dividers (in this task we use `a` and `b` and values `3` and `5`, but can we change them or/and add more values);
* `find_sum()` and `check_division()` are two functions, each is with single responsibility.

## Result

233168