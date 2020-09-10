# Assignment: Object-Oriented Programming - Inheritance... and File I/O

In this assignment, you'll practice:

* Inheritance
* Reinforcing OOP Basics:
   * Classes and instantiating objects/instances
   * Instance variables
   * Instance methods
* Using modules
* Reading documentation
* Scripting
* File I/O
* Using dictionaries
* Reinforcing fundamentals:
   * Lists and iteration

This assignment can be challenging! Feel free to collaborate with other students on this assignment, but you should still hand in your own assignment.

## Deliverables & Submitting

You know what you're doing by now! **Fork**/**Clone**/**Commit**/**Push**/**Submit** :grin:

---

# Exercise 1: Solar System

Let's explore our Solar System using Inheritance!

For this exercise, some starter code is already in the file named `exercise1.py`. Take a look at it now and familiarize yourself with the layout of the starter code.

Your job is to use your knowledge of **inheritance** and **instance methods** to fill in all of the `???` areas of the code and make the program actually run.

**Note**: Do **not** add any new functions or methods! Just fill out the `???`s.

Let's start with the basics:

* A **Celestial Body** is a naturally occurring physical entity like a Star, Planet, or a Moon
* A [Planetary System](https://en.wikipedia.org/wiki/Planetary_system), like our own [Solar System](https://en.wikipedia.org/wiki/Solar_System), can contain several of these celestial bodies

We can model the different kinds of celestial bodies as follows:

1. Each `Body`, no matter which kind (star, planet, or moon) has to keep track of two pieces of information -- Its `name` and `mass`
   * The `name` of a `Body` should be a string
   * The `mass` of a `Body` should be an integer
   * **Hint:** Use **instance variables** to keep track of these!
   * Your job is to implement the `__init__` method of the `Body` class
1. Each `Star` (which is a kind of `Body`), has an additional piece of information to keep track of: Its [`type`](https://study.com/academy/lesson/types-of-stars-by-size-color-and-life-cycle.html)
   * The `type` of a `Star` should be a string
   * **Hint:** Stars also have `name`s and a `mass`! But you need to use inheritance to keep track of a Star's name and mass. Remember that a `Star` is a `Body`!
   * Your job is to:
      * Use Inheritance to deal with the `name` and `mass` of Stars,
      * Implement the rest of the `__init__` method of the `Star` class
1. Next, each `Planet` is also a kind of `Body`
   * Planets, in addition to having a `name` and `mass`, also has a `day_length` and a `year_length`
   * The `day_length` should be a integer and it represents the number of hours in a day (For example: `24` for the Earth)
   * The `year_length` should also be an integer and it represents the number of days in a year (For example: `365` for the Earth)
   * Your job is to:
      * Use Inheritance again to deal with the `name` and `mass` of Planets,
      * Implement the rest of the `__init__` method of the `Planet` class
1. Finally, each `Moon` is also a kind of `Body`
   * Moons, in addition to having a `name` and `mass`, also has a `month_length` and a `orbit_planet`
   * The `month_length` should be a integer and it represents the number of days in a month (For example: `30` for the Earth's moon - Luna)
   * The `orbit_planet` should be an *instance of the planet* that the moon orbits around!
      * For example, Luna orbits the Earth
      * **Hint:** This means the Earth must exist before its moon can be created!
   * Your job is to:
      * Use Inheritance again to deal with the `name` and `mass` of Moons,
      * Implement the rest of the `__init__` method of the `Moon` class

Next, we can model our Solar System with a top-level class, let's call it `System`, which can contain as many celestial bodies as needed. Most of this class has already been written for you except for a few `???`s you need to fill out.

* A `System` starts with no bodies inside of it
* Fill out the parameter list of the `__init__` method of the `System` class
* A `System` has the ability to `add` bodies to itself
   * Fill out the `???`s in the `add` method of `System`, to accept some new `body`
   * As you can see, the new `body` is added to the System's already existing collection of bodies via `append`.
* Finally, a `System` can report on the `total_mass` of all the celestial bodies inside the system.
   * The return value of the `total_mass` method is the sum of all the masses of the bodies inside the system
   * The only thing you need to do in the `total_mass` method is to fill out the parameter list
* **Note**: A `System` is **not** a `Body`! Instead, it *contains* bodies.

Finally, implement the missing parts of the `main` function:
   * Instantiate a `sun`, an `earth`, and a `luna`
      * For the `sun`, Use the name `'Sun'`, mass of `200`, and `type` of `'G-Type'`
      * For the `earth`, Use the name `'Earth'`, mass of `150`, `day_length` of `24`, and `year_length` of `365`
      * For `luna`, Use the name `'Luna'`, mass of `100`, `month_length` of `30`, and an `orbit_planet` of ... what do you think?
   * Instantiate a `solar_system`
      * Add the three bodies you've already instantiated to the solar system

**Note**: **Do not** add any new functions or methods, and **do not** modify the rest of the `main()` function. Just fill out the `???`s.

### Expected Output

Assuming that you have implemented everything correctly, this is the expected output when you run `exercise1.py`:

```
Earth
Sun
Luna
450
```

---

# Exercise 2: TPS Report

Your boss, Bill, asks you to come in on Saturday to finish your TPS report.

You promise to finish the report, but as Bill walks away, you smile knowing you have a trick up your sleeve: scripting!

You plan on quickly writing up a bit of code to finish the report, all without spending a minute of your Saturday!

You know of a Python module called [`csv`](https://docs.python.org/3/library/csv.html) that can be used to read and write `csv` files. CSV stands for "Comma-Separated Values" and is a file type commonly used for spreadsheets.

You can check out the [`csv` docs](https://docs.python.org/3/library/csv.html) for examples of how this module works.

We'll be using [`DictWriter`](https://docs.python.org/3/library/csv.html#csv.DictWriter), which can output dictionaries to rows in a CSV file.

## `DictWriter` Example

```python
import csv

# This line opens or creates a `names.csv` file
with open('names.csv', 'w', newline='') as csvfile:

  # These are the header row values at the top
  # It should be a List!
  fieldnames = ['first_name', 'last_name']

  # This opens the `DictWriter`. Notice that we pass in the list of fieldnames
  writer = csv.DictWriter(csvfile, fieldnames)

  # Write out the header row (this only needs to be done once!)
  writer.writeheader()

  # Write as many rows as you want!
  writer.writerow({ 'first_name': 'Baked', 'last_name': 'Beans' })
  writer.writerow({ 'first_name': 'Lovely', 'last_name': 'Spam' })
  writer.writerow({ 'first_name': 'Wonderful', 'last_name': 'Spam' })
```

### Output of `DictWriter` Example

If you run the previous example, you'll end up with a `names.csv` file that looks like this when you open it in a text editor:

```
first_name,last_name
Baked,Beans
Lovely,Spam
Wonderful,Spam
```

This `csv` file represents a spreadsheet that looks like this:

| first_name | last_name |
| --- | --- |
| Baked | Beans |
| Lovely | Spam |
| Wonderful | Spam |

If you double click the `names.csv` file that is generated, it will open in whatever spreadsheet program you have on your computer. On a Mac, this is probably *Numbers*. On Windows, this is probably *Microsoft Excel*. If you don't have a spreadsheet program on your computer, you can upload the file to Google Sheets and view it there.

## Your Job!

Now that you have a good idea how to wrangle a `csv` file, let's think about what you'd like to do with this newfound power.

You have a list of dictionaries called `employees`, which contains information about each employee including `first_name`, `last_name`, `hire_date`, `job_title`, and `performance_review`.

Open a new file called `tps_report.csv`, and write a loop to write out every employee in the `employees` dictionary to `tps_report.csv`.

* **Hint 1:** Think about where you can retrieve the report field names from, without having to write them all out
   
* **Hint 2:** Instead of writing `writer.writerow` many times (as in the example earlier), try looping through the `employees` list

### (Spoiler Alert)

<details>
<summary>Hint 1</summary>
For the <code>fieldnames</code> of the TPS report, think about how you can retrieve the report field names, without having to write them all out by hand! (It's not a big deal if you have to write it out by hand.)
</details>

<details>
<summary>Hint 2</summary>
Expanding on Hint 1, recall that you can get the keys of a dictionary with the <code>keys()</code> method, the result which then must be converted to a list (you know how to convert between different data types!)
</details>

<details>
<summary>Hint 3</summary>
Instead of writing <code>writer.writerow</code> many times (as in the example earlier), try looping through the <code>employees</code> list
</details>

### Starter Code

The starter code is inside the file called `exercise2.py`.

Write your code where indicated in the `main()` function!

### Expected Output

**After** you write and run your program, the `tps_report.csv` file should contain:

```
first_name,last_name,job_title,hire_date,performance_review
Bill,Lumbergh,Vice President,1985,excellent
Michael,Bolton,Programmer,1995,poor
Peter,Gibbons,Programmer,1989,poor
Samir,Nagheenanajar,Programmer,1974,fair
Milton,Waddams,Collator,1974,does he even work here?
Bob,Porter,Consultant,1999,excellent
Bob,Slydell,Consultant,1999,excellent
```

If you open up that file in a spreadsheet program (like Excel or Numbers), it should look something like:

| first_name | last_name | job_title | hire_date | performance_review |
| --- | --- | --- | --- | --- |
| Bill | Lumbergh | Vice President | 1985 | excellent |
| Michael | Bolton | Programmer | 1995 | poor |
| Peter | Gibbons | Programmer | 1989 | poor |
| Samir | Nagheenanajar | Programmer | 1974 | fair |
| Milton | Waddams | Collator | 1974 | does he even work here? |
| Bob | Porter | Consultant | 1999 | excellent |
| Bob | Slydell | Consultant | 1999 | excellent |

---

# Exercise 3 (STRETCH): Have You Seen My Stapler?

Now we have generated a TPS report... but it isn't finished. There are still a couple of things left to do!

You notice that the performance review of you and your friends are pretty bad... so let's change your performance reviews in the system. :smiling_imp:

Copy your `exercise2.py` file into `exercise3.py` file and make your changes in the new file.

1. Add a field called `review_finished` to each employee
   * The value for every row should be `yes`
   * **Hint 1**: You figure you can just add this field to each dictionary when you loop through each employee
   * **Hint 2**: Don't forget to update the headers in the report!
1. Change everyone's `performance_review` to `excellent`... 
   * Unless it's your boss Bill Lumbergh or someone with the `job_title` of `Consultant`. In that case, make their `performance_review` value `poor`. (Hehehe)
1. Re-generate the TPS Report and make sure your new program does the job

**Hint**: Don't forget that you can always write a function if your code starts getting too long!

### Expected Output

**After** you write and run your program, the `tps_report.csv` file should contain:

```
first_name,last_name,job_title,hire_date,performance_review,review_finished
Bill,Lumbergh,Vice President,1985,poor,yes
Michael,Bolton,Programmer,1995,excellent,yes
Peter,Gibbons,Programmer,1989,excellent,yes
Samir,Nagheenanajar,Programmer,1974,excellent,yes
Milton,Waddams,Collator,1974,excellent,yes
Bob,Porter,Consultant,1999,poor,yes
Bob,Slydell,Consultant,1999,poor,yes
```

If you open up that file in a spreadsheet program (like Excel or Numbers), it should look something like:

| first_name | last_name | job_title | hire_date | performance_review | review_finished |
| --- | --- | --- | --- | --- | --- |
| Bill | Lumbergh | Vice President | 1985 | poor | yes |
| Michael | Bolton | Programmer | 1995 | excellent | yes |
| Peter | Gibbons | Programmer | 1989 | excellent | yes |
| Samir | Nagheenanajar | Programmer | 1974 | excellent | yes |
| Milton | Waddams | Collator | 1974 | excellent | yes |
| Bob | Porter | Consultant | 1999 | poor | yes |
| Bob | Slydell | Consultant | 1999 | poor | yes |

---

# Look at You, Being a Boss!

What do you call a snake that's 3.14 meters long?

![](https://media.giphy.com/media/3owyoUHuSSqDMEzVRu/giphy.gif)

A `Pi-Thon`! :grin: