{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 1. Exercise Webmining"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    a=256
    b=256
    a*b
    
    "### Use Python as a calculator to compute 256 times 256"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Put the strings \"Hello\" and \"World!\" in two variables. Concatenate both Strings and print them"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Create a list that contains the 4 strings \"alpha\", \"beta\", \"gamma\", and \"delta\". Add \"epsilon\" to the end of this list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Create a sublist with the first three elements of this list\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Write a Python program to construct the following pattern using for loops"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Write a function that takes 3 input parameters and returns product of these values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Write a Python function that takes an int as a parameter and checks if the number is prime or not."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Use your function to create a list that contains all primes from 2 to 100"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Write a function that simulates dice rolls (6-sided dices)\n",
    "- Write a function that has the number of dice rolls as the input parameter\n",
    "- The output is a map with the counts how often each result of a roll (1-6) occurred\n",
    "- You can use the randomint() function from the random package"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Combine two dictionaries by adding values for common keys.\n",
    "d1 = {'a': 100, 'b': 200, 'c':300}\n",
    "\n",
    "d2 = {'a': 300, 'b': 200, 'd':400}\n",
    "\n",
    "Sample output: {'a': 400, 'b': 400, 'd': 400, 'c': 300}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Create a list of lists. Then, write a list comprehension that creates a list with the lengths of each (sub)list in the primary list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Exceptions\n",
    "\n",
    "Write your own function *my_division* that gets two variables a and b and returns a divided by b. Catch the ZeroDivisionError that occurs if b equals 0 and return 1 in this case.\n",
    "\n",
    "How could the same behavior be achieved without catching an exception?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### File handling\n",
    "\n",
    "Write a function that gets a letter and the path to a (text-)file on your harddrive as input parameters and computes a list as its output. The list should contain one number for each line. The i-th line shows, how often the given letter occurs in line number i."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Change please!\n",
    "In our currency, we have coins with certain values, e.g., (200,100,50,20,10,5,2,1) cents. Write a function that computes the different options to pay a certain amount X with the given set of coins."
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "Example:\n",
    "pay_options (10, [200,100,50,20,10,5,2,1])\n",
    "[[10],\n",
    " [5, 5],\n",
    " [5, 2, 2, 1],\n",
    " [5, 2, 1, 1, 1],\n",
    " [5, 1, 1, 1, 1, 1],\n",
    " [2, 2, 2, 2, 2],\n",
    " [2, 2, 2, 2, 1, 1],\n",
    " [2, 2, 2, 1, 1, 1, 1],\n",
    " [2, 2, 1, 1, 1, 1, 1, 1],\n",
    " [2, 1, 1, 1, 1, 1, 1, 1, 1],\n",
    " [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Numpy"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Create a numpy arrays with 20 rows and 10 columns, all values set to zero"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Create an array with the same shape containing all natural numbers 0-199"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Create a 4-dimensional array and set all values to a random integer smaller than 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### What is the mean of all values contained in this array?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Select a sub-array containing the middle two rows of the middle two columns from that array"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Given a numpy array, return a new numpy array the contains only the elements that are greater than 100"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
