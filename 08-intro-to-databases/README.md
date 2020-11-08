# Jupyter Notebook

## We Do: Launching Jupyter Notebook

Go into the `student` directory of this lesson. Now, let's try to launch Jupyter Notebook.

```zsh
jupyter notebook my-first-notebook.ipynb
```

And it should say something like:

```
pyenv: jupyter: command not found

The `jupyter' command exists in these Python versions:
  anaconda3-2020.02
```

See, currently we are using the latest version of plain-jane Python -- which does not have all of the data science tools installed, so we cannot launch `jupyter notebook` or any other data science tool. 

We *could* install the tools manually with `pip`, but the alternative is to install Anaconda (which comes with everything in the box), which we have already done. All we have to do is access it! This is where **Pyenv** comes in, which you might remember we installed way back when at Installfest.

To run the Anaconda version of Python instead, do the following (Replace the `X`s and `Y`s as appropriate):

```zsh
pyenv local anaconda3-2020.02
```

You will notice that a new file called `.python-version` has been created inside your `student` directory. If you `cat` the contents of this file, it only says `anaconda3-2020.02`.

What this file does is tell the Operating System: "*Hey, when we are inside this directory, use the Anaconda version of Python!*"

This is what **Pyenv** is good for! If you have a project using an older version of Python, for example, you can designate that directory with the older version, and the older version will be automatically used while inside that folder (and its subfolders!).

(If you exit the `student` folder with `cd ..`, you'll see that we revert to using plain Python again.)

Let's get back to Jupyter Notebook. Now, make sure you're back in the `student` folder. If you try to launch Jupyter Notebook again:

```zsh
jupyter notebook my-first-notebook.ipynb
```

_wait..._

It opens in your browser! ... If you're on Mac!

(On Windows, you have to manually copy the URL starting with http://127.0.0.1 into your browser.)

**Note:** Development environments between Mac and Windows differ, and there are different ways to open Jupyter Notebooks (Just like there are many ways to open any given file or program on your computer!), but this is the way we're going to do it... On the Command Line!

## We Do: Code Cells

Let's begin!

* There is already a cell that exists in the new notebook. Inside the cell, write:

   ```python
   print('hello world')
   ```

* Be sure your cursor is inside the cell. Press `Ctrl-Enter`

This is how you run a code cell!

* Create a new cell: Click `+` in the upper left hand corner. Enter:

   ```python
   my_list = [1,2,3]

   for i in my_list:
     print(i)
   ```

* `Ctrl-Enter` to run it.

## We Do: Markdown Cells

Markdown cells allow you to write and format text.

* Make a cell: Click the `+` in the upper left corner
   * You're going to be doing this a lot!

* Change this cell to a markdown cell:
   * Click: `Cell` :arrow_right: `Cell Type` :arrow_right: `Markdown`
  
* Inside the markdown cell, write:

   ```md
   # Hello world
   ```

* Run the cell: `Ctrl-Enter`. Bam! Pretty formatted text.

Here are some of the most commonly used Markdown syntax:

<pre>
# Heading 1

## Heading 2

**Bold**

*Italic*

```python
print('Sample code')
```
</pre>

**Note**: We will not spend much time learning markdown syntax! Instead, take a look at the cheatsheet and links in Additional Resources.

When it comes to markdown,no one spends time memorizing its syntax. Rather, we reference the markdown cheatsheet to remember how to make large headers, bulleted lists, tables, and more. An apt analogy is a mechanic does not spend time memorizing the pantones of cars, but when he/she needs to do a paint job, they will look up the necessary color codes.

## We Do: Closing Down

* **Note**: Jupyter Notebook automatically saves your work as you execute cells. ***BUT***, before you close the notebook, click the :floppy_disk: icon to save your work, just in case!
   * ([What is that funny looking icon anyway?](https://www.distractify.com/p/save-icon-vending-machine))
* Now, close the tab in your browser
* That actually doesn't quit the Notebook program!
* Open your Terminal where we first used the `jupyter notebook` command. You'll see that the process is still running
   * Hit <kbd>⌃ Control</kbd>+<kbd>c</kbd>
   * It should ask `Shutdown this notebook server (y/[n])`? Enter `y`
* That will fully shutdown the Jupyter Notebook program

---

# Why Jupyter Notebooks?

Jupyter Notebook is the preferred integrated development environments (IDEs) of data science.

## Data Science is Both Code and Methodology

As data scientists, the code we write is only half the story. The methodology, or manipulations, that we're applying on that data are -- are the other half. 

Typically these methdologies are far more subjective in contrast to straight software development.

For example: Pretend we're missing many values in our data. Do you fill in missing values with the mean (average) or the median? The code for doing either of these operations is fairly easy, compared to the justifying decision, which should be documented in text cells.

Jupyter Notebooks make it easy to create code cells next to text cells.

## Connect to Remote Computing Resources

While we will not be doing this, but Jupyter Notebooks make it easy to connect to remote computers in datacenters. This is why the Jupyter Notebook is in your browser.

Basically we've created a website for one person: you, running on your computer. After we're done writing the code, we could in swap the brains from your laptop for stronger computers in a datacenter if we need to do more muscular processing. Wow!

---

# Additional Resources

* Markdown Cheatsheet [here](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
* Interactive Markdown Cheatsheet [here](http://markdownlivepreview.com/)
