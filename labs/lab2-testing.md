---
title: "Lab 2: Assertions, Exceptions, and Tesing"
author: "Ahmed Eldeeb"
date: "2023-08-21"
format:
  pdf:
    documentclass: article
    margin-left: 30mm
    margin-right: 30mm
    toc: true
  html:
    theme: cosmo
    css: ../styles.css
    toc: true
    code-copy: true
    code-block-background: true
---

## Exercies

1- Create a function that takes in a string and return a string where the space separated words (or tokens) are the same as the input string but sorted according to a specific ordering. The ordering should be determined by the second argument to the function. The ordering is could be specified as (1) alphabetic according to the words (2) alphabetic according to the key produced by sorting the letters of the original word, or (3) numerically.

2- Build a test suite using pytest to test that your function works as intended. Add at least 8 test cases with justification for each.

3- Make sure you have assertions to check for invalid input types and combinations.

4- Make your function throw an exception for invalid input combinations.

5- Write a loop that calls your funciton on a variety of inputs including invalid inputs.

6- Handle the thown exception in the loop and print something appropriate in that case.


