# Git

## What is Version Control?

![](assets/finalfinalfinal.png)

Source: [The Dog House Diaries](http://thedoghousediaries.com/5964)

Version Control: A system that records changes to a file or set of files, over time.

* It lets you travel back in time. You can restore any past version of your work, so there's no need to be afraid of experimenting with your code and breaking things

## What is Git?

* Industry-standard!
* Git features:
   * It allows sharing your work with collaborators
   * It acts as a backup system
   * It's small and fast
* In Git, each project is called a **repository**, or **repo**
* A repo consists of:
   * All project files and folders (directories)
   * The history of each file
* A project's version history is made up of a series of **commits**
   * Think of them as "snapshots" or "saved games"
* You don't wanna know what came before Git...

Git is used by real programmers and companies *every day* to produce real software. It's large and complicated but very important to learn to be part of the programming world!

![](assets/git.png)

Git is a *huge* topic!

To survive, we're only going to learn the *bare minimum* necessary for us to do the course!

## What is Github?

Git and Github are two different things, but closely related.

Basically, Github is a website where you can store your git repositories. If you've ever used a service like Dropbox or iCloud, it's very similar except instead of storing photos, you're storing code!

The difference is that it doesn't do so automatically like iCloud does with photos. You as the programmer must direct it to do its work, that's because coding requires much more fine-grained control than photos! You need to control the syncing of each code file yourself.

In addition storing code for you online, Github allows you to collaborate on code together. It's kind of like a Programmer Social Network.

## What is Github Enterprise?

### Github - [github.com](https://github.com)

For everybody in the world to use, for free!

### Github Enterprise - [git.generalassemb.ly](https://git.generalassemb.ly)

A private Github just for one particular organization -- In this case, General Assembly. (This is part of how Github makes money!)

We'll be storing our course work, homework assignments, etc. in GA's Github Enterprise.

But... we'll still call it "Github".

# Standard Git Workflow for Our Course

There are different Git workflows depending each company. For our course, we'll use a simplified Git workflow.

Let's practice some Git!

**Important:** *Do not ever place a Git Repo inside another Git Repo!*

## Beginning of a Project

1. **Fork** the homework repo on Github. This puts a copy of it in your account. We call this repo a  **remote repository**.
   
   * Let's try this now. Fork [Homework #0](https://git.generalassemb.ly/PYTHR-june-2020/hw-00-submission-practice)
   * It should now show up in your Github homepage, under the **Repositories** box
   * Click on your copy of the repo

1. Copy to the clipboard the Git Repo URL with the "Clone or download" button (we'll call this the `github url`)
1. **Clone** the repository to your computer so you can start working on it. This copy (or clone) is called a **local repository**.

   ```bash
   git clone <github url>
   ```

## While Working on the Project

As you work on your project, you should occasionally check the status of the repo:

```bash
git status
```

## Making Commits

After you make some changes and you feel like you need to "save your game", you will need to make a **commmit**.

Here's how you make a commit.

### Untracked and Unstaged

<img src="assets/unstaged.png" width="300" />

New files start as **untracked** until you tell Git that they now exist.

First, we use `git status` to examine the status of our repo, and then `git add` to add the changes.

```bash
git status
git add --all
```

If you've made any changes to existing files, they will be considered **unstaged**.

To tell Github about changes to existing files, you execute `git add --all` just like with new files.

### Staged

After **adding**, these changes are now considered to be **staged**.

<img src="assets/staged.png" width="300" />

Staged files are ready to be **committed**!

### Committed

To **commit** changes, we execute:

```bash
git status
git commit -m 'some commit message'
```

<img src="assets/committed.png" width="300" />

This will take a snapshot of the changes in time, and create a "save point".

It's important to add a good commit message, so that your coworkers can understand what your changes are all about!

### Back to Unstaged

Once you've made a commit, the stage is clear again and the repo is back to an **unstaged** status.

<img src="assets/unstaged.png" width="300" />

### Summary

The `git status` step is optional but highly helpful when you're just starting out!

```bash
git status
git add --all
git status
git commit -m 'add a comment'
```

## To View The Past

To display all the commits:

```bash
git log
```

## Syncing with Github

### Pushing

These changes you've been making to the local repository are just that -- on the local repository. If you want to "back up" your changes to the cloud on Github, you have to **push** your code to Github (aka The "origin").

```bash
git push origin master
```

The words `origin master` have to do with the idea of *branches*, which we will not be covering in this course. In the full time course, this topic takes an entire 2-hour lecture to cover!

### Pulling

If other people are working on the same repo, then you also have to occasionally **pull** new stuff they've written:

```bash
git pull
```

Starting next lesson, you'll perform a `git pull` at the beginning of every lesson on this very repository -- so that you can get the latest course materials written by your instructor! (We'll go through that next class.)

# Fundamental Git Concepts

## `clone` vs `init`

You will only ever do one of `git clone` _or_ `git init` - never both.

* If a project already exists on Github and you want a copy on your computer, you use `git clone <github url>`.
* If you're starting a _brand new_ project on your computer, and no files exist yet on Github, you use `git init`.

In this course, we'll **not** be using `git init`.

The only reason you might need git init in this course is if you come up with an amazing project idea during a flight to Hong Kong, and you don't have internet access to be able to create a project on Github, and you just gotta *start your project on your laptop right now!*

## Collaborators

In the real world, most code projects are done in teams.

Github allows you to add collaborators to a repo so that you can invite others to work on the same code. Collaborators can work on the code in a repo, but are not considered an owner of the repo.

To add a collaborator, from the repo page on Github: `Settings` :arrow_right: `Collaborators & teams`

In this course, we'll **not** need to add any collaborators.

Even if you might choose to discuss work with your classmates, you'll be always be working on and handing in assignments in your own repos.

But as you continue on your journey towards becoming a developer, you'll definitely add collaborators to your projects eventually or join another project as a collaborator!

## Forking

What if the project you're interested in working on won't add you as a collaborator? You can **fork** the project!

When you fork someone else's repo, you copy an independent version of that project to *your* account. Even though you may not have been a collaborator in the original project, you can make changes and push to *your fork*!

The fork has the same history as the original repo, but from that point on, the two repos diverge. When you push to your fork, the original repo is unaffected.

To get the forked repo on to your computer, run `git clone <github url>` like you would any other repo. 

In this course, we'll generally be *forking* assignments and working on our *own fork* of the assignment!

Once you've forked a repo, you go into the Standard Git Workflow as described above.

# Homework Submission Procedures

Now, we'll go over the homework submission procedures using Git and Github.

We'll practice with the Submission Practice repo -- notice that it's Homework #0, so this homework won't be officially graded!

---

# Additional Resources

* [Git Tutorial: Setting Up a Git Repository](https://www.atlassian.com/git/tutorials/setting-up-a-repository)
* [Git Tutorial: Saving Changes](https://www.atlassian.com/git/tutorials/saving-changes)
* [Git Tutorial: Inspecting a Repository](https://www.atlassian.com/git/tutorials/inspecting-a-repository)
* [Try Git: A Course on Code School](https://www.codeschool.com/courses/try-git)
* [How to undo the last Git commit?](http://stackoverflow.com/questions/927358/how-to-undo-the-last-git-commit)
* [Git Guide](http://rogerdudler.github.io/git-guide/)
* [Create a Repository on Github](https://help.github.com/articles/create-a-repo)
