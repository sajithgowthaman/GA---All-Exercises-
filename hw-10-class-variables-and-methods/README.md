# Assignment: Object-Oriented Programming - Class Variables and Methods

In this assignment, you'll practice:

* Defining classes and instantiating objects/instances
* Defining and using instance variables
* Defining and calling instance methods
* Defining and using class variables
* Defining and calling class methods
* Reinforcing:
   * `if/else` statements
   * Lists and iteration

This assignment can be challenging! Feel free to collaborate with other students on this assignment, but you should still hand in your own assignment.

## Deliverables and Submitting

You know what you're doing by now! :grin:

---

# Exercise 1: Bank Account

Some starter code is already in the file named `exercise1.py`.

Complete the rest of the program!

*Do not modify any of the code in the `main()` function. Only modify the parts of the program indicated by `???`.*

1. Fill in the rest of the `BankAccount` class.
1. Add a **class variable** called `interest_rate` that is a **float** representing the interest rate for all the accounts in the bank
   * `interest_rate` is a class variable because it is used across all of the accounts in the bank!
1. Add another **class variable** called `accounts` that starts as an empty list
   * This will eventually store the collection of all the accounts in the bank
1. Add an `__init__` **instance method** that sets the bank account's `balance` to zero
   * The `balance` is stored in an instance variable because the value needs to be different from account to account
   * `__init__` should also add the account that is being initialized to the `accounts` class variable so that the bank can keep track of it
1. Add an **instance method** called `deposit` that accepts a number as an argument and adds that amount to that account's balance
   * `deposit` needs to be an instance method because it pertains to a *single, specific* account.
1. Add an **instance method** called `withdraw` that accepts a number as an argument and subtracts that amount from the account's balance
   * Why is `withdraw` an instance method, not a class method?
   * What should happen if you try to withdraw more money than you have?
1. Add a **class method** called `total_funds` that returns the sum of all balances across all accounts in the `accounts` class variable
   * `total_funds` needs to be a class method because it *does not* pertain to any *single, specific* account
1. Add a **class method** called `add_interest` that iterates through all accounts, and increases their balances according to the `interest_rate` in effect for all accounts
   * `add_interest` needs to be a class method because it operates on _all_ bank accounts, not a _single, specific_ account.

### Example output

When you run the `exercise1.py` program after completing the `BankAccount` class,assuming that you have set the `interest_rate` to `0.01`, you should get the following output:

```
0
0
200
1000
1200
202.0
1010.0
1212.0
152.0
1162.0
```

---

# Exercise 2: Vampire Infestation

There's a vampire infestation! But that doesn't mean we don't have time to practice using class variables and methods.

Some starter code is already in the file named `exercise2.py`.

Complete the rest of the program!

*Do not modify any of the code in the `main()` function. Only modify the parts of the program indicated by `???`.*

Now that you've had some experience using class variables and methods it's time to test your knowledge of _when_ to use them.

Your task is to write a `Vampire` class that stores a list of vampires (a `coven`, if you will).

Every vampire has a `name`, `age`, an `in_coffin` boolean, and a `drank_blood_today` boolean.

Every day at sunset the vampires leave their coffins in search of blood. If they don't drink blood and get back to their coffins before sunrise, they die.

Your `Vampire` class should have the following methods:

* `__init__`, which initializes a new vampire, assigns values for each of its attributes, and adds it to the coven
* `drink_blood`, which sets a vampire's `drank_blood_today` boolean to true
* `sunset`, which sets `drank_blood_today` and `in_coffin` to false for the entire coven, as they go out in search of blood
* `go_home`, which sets a vampire's `in_coffin` boolean to true
* `sunrise`, which removes from the coven any vampires who are out of their coffins or who haven't drank any blood in the last day

It's up to you to determine whether each method should be an instance method or a class method.

You'll also have to decide what instance and class variables you need.

If you're not sure whether a method should be an instance method or a class method, starting to write the body of the method may help you figure it out based on what data you need access to.

If you're still uncertain, don't be afraid to ask an instructor for help during office hours.

Good luck!

**Big Hint**: For the `sunrise` method, you'll have to iterate through a list. Be extremely careful: [Thou Shalt Not Modify A List During Iteration](https://unspecified.wordpress.com/2009/02/12/thou-shalt-not-modify-a-list-during-iteration/)! 

Instead, as the author of the article suggests, "You could construct a new list during iteration rather than mutating the existing one. (For example, rather than removing all the elements which satisfy a condition, insert into a new list all the elements which don’t)."

### Example output

When you run the `exercise2.py` program after completing the `Vampire` class, you should get the following output:

```
Coven at the beginning:
Riley
Alice
Jasper
Renesmee
Marcus
Zafrina
Demetri
Coven at the end:
Riley
Renesmee
```

---

# Parting Thought: Bank Accounts and Vampires

You're done! But here's a parting thought:

Isn't it strange how, in most vampire fiction, vampires are lavishly wealthy, often living in expensive homes and wearing fine clothing?

![](https://media.giphy.com/media/Quauv5GIn3WR9OY7RS/source.gif)
