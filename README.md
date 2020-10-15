# The Command Line and Code Editor

<!--
## Your Operating System

* MacOS or Linux are preferred by many developers because they have full-featured UNIX-style command-line interfaces
* Getting to know your keyboard shortcuts will help you be more productive
   * Switching Windows
      * MacOS: <kbd>Command</kbd>+<kbd>Tab</kbd>
      * Windows: <kbd>Win</kbd>+<kbd>Tab</kbd>
      * Linux: <kbd>Alt</kbd>+<kbd>Tab</kbd>
      * Hold down shift to reverse direction
   * Switching Tabs in Chrome
      * All OSes: <kbd>Ctrl</kbd>+<kbd>Tab</kbd>
      * Hold down shift to reverse direction
-->

## The Terminal

* What is the Command Line Terminal?
   * What is `bash`? What is `zsh`?
   * (Allows you to be a *computer whisperer*)

   ![](https://media.giphy.com/media/MBrKW6dKfO9Jm/giphy-downsized.gif)

* Common Commands:
   * `exit`
   * `ls` (:star:)
   * `cd` (:star:)
      * You can `cd` into subfolders with `cd a/b/c`
   * `pwd` (:star:)
   * `clear`
   * `mkdir`
   * `rmdir`
   * `touch` (:star:)
      * Let's create some files: `a1.txt`, `a2.txt`, `b2.txt`
   * `mv`
      * `mv a*.txt`
   * `rm`
   * `rm -r` :fire: **Dangerous!** :fire:
   * `rm -rf` :fire::fire: **SUPER Dangerous!** :fire::fire:
      * You can easily [delete your whole company](https://itsfoss.com/accidentally-deletes-company-wrong-command/) with this command!
* Directories
   * `.` refers to current directory
   * `..` refers to parent directory
   * `/` refers to the top-level directory of entire computer/file system
* Tab autocompletion
* Up arrow repeats previous commands
* <kbd>^Control</kbd>+<kbd>c</kbd> is a general "exit hatch" for most "bad situations"

### `sudo` :fire::fire::fire: **UBER Dangerous!** :fire::fire::fire:

Sometimes you may see instructions refering to `sudo some_command`, where the word `sudo` was put in front of a command.

`sudo` stands for "Super User Do" and it means *"I'm the owner of the computer, override any protections that may have been put in place, and do that command anyway"*.

The problem is that these protections may have been put in place for good reason!

In general, until you have learned much more about the command line: 

> **Do not ever put `sudo` in front of your command**! It can seriously mess up your computer, sometimes irreparably, and always painfully.

## The Code Editor

### Running the Editor from the Command Line

This is how to open the editor from the command line.

1. Navigate to the directory you wish to work from with a series of `cd` commands.

1. To open the *current directory*, run:

   `code .`

### Integrated Terminal

VS Code has a great *Integrated Terminal* feature, which helps reduce the amount of window switching we have to do.

First, you have to already have a project folder open. That is, you've already run, via the command line: `code .`.

Then, the way you open up the Integrated Terminal is different depending on your OS.

**Protip:** The **backtick** <kbd>`</kbd> key should be underneath the <kbd>Escape</kbd> key.

### Windows

<kbd>⌃Control</kbd>+<kbd>Shift</kbd>+<kbd>`</kbd>

### MacOS

<kbd>⌃Control</kbd>+<kbd>`</kbd>

---

# Additional Resources

* [Useful keyboard shortcuts for Terminal](https://github.com/0nn0/terminal-mac-cheatsheet/wiki/Terminal-Cheatsheet-for-Mac-(-basics-))
* [CheatSheet App for MacOS](http://www.cheatsheetapp.com/CheatSheet/)
* [Spectacle](https://www.spectacleapp.com/)
* [Linux Unity Keyboard Shortcuts](https://askubuntu.com/a/28087)
* [Reference to Unix Commands](http://www.cs.tau.ac.il/~roded/courses/soft1-b05/unix1.htm)
* [Dive more into Unix](http://matt.might.net/articles/basic-unix/)
