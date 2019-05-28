# Workshop: Development and Coding Standards

## Fork and clone

As always you should first *fork* https://github.com/AICoE/workshop-coding-best-practices into your github account.
Click on the `Fork` button in the upper right corner.

Then *clone* your fork to your local machine. 

**REPLACE <my_account_name> with your account name**

`git clone git@github.com:<my_account_name>/workshop-coding-best-practices.git`

If the above fails, make sure you have setup git correctly, for help see: https://help.github.com/en/articles/testing-your-ssh-connection

Now you can `cd workshop-coding-best-practices` into your fork.

## Installation and execution the model code

To manage python requirements we're using [Pipenv](https://github.com/pypa/pipenv#installation). On Fedora you should be
good with running `sudo dnf install pipenv`.

TODO: check if this works and if the interns have rhel CSB?!

Now install all requirements with `pipenv install` and enter a shell with the correct python settings: `pipenv shell`
If some dependencies are missing when you run your code, you might be in another shell without the correct settings.
Again, run `pipenv shell` in this directory or always execute your code with `pipenv run python model.py`

Then you can run the code via `python model.py`

## Clean Code

You'll go through 5 steps of refactoring to make the code a little bit better to understand and read.
This is important, because not only you will need to understand your code one month ahead, but also your peers.
So [Clean Code](https://www.oreilly.com/library/view/clean-code/9780136083238/) is a book and a [Google Search Term](http://lmgtfy.com/?q=clean+code) 
you should remember.

### Naming Convention

> When you write Python code, you have to name a lot of things: variables, functions, classes, packages, and so on. Choosing sensible names will save you time and energy later. You’ll be able to figure out, from the name, what a certain variable, function, or class represents. You’ll also avoid using inappropriate names that might result in errors that are difficult to debug.

[PEP8 Naming Conventions](https://realpython.com/python-pep8/#naming-conventions).

[Solution](https://github.com/AICoE/workshop-coding-best-practices/commit/db01c83b35a37452586c774fd34144ca675ade23)

### Meaningful names

> This is what makes code self-documenting. When you read over your old code, you shouldn’t have to look over every little comment and run every small piece of code to figure out what it all does!
> The code should roughly read like plain English. This is especially true for variable names, classes, and functions. Those three items should always have names that are self-explanatory. Rather than use a default name like “x” for example, call it “width” or “distance” or whatever the variable is supposed to represent in “read-world” terms. Coding in “real-world” terms will help make your code read in that way

[Choosing Names](https://medium.com/@george.seif94/these-5-clean-code-tips-will-dramatically-improve-your-productivity-b20c152783b)

[Solution](https://github.com/AICoE/workshop-coding-best-practices/commit/ac522375c622b2cfdcd064f43d737b89b29b7921)

### Single Responsibility

> One method should be responsible only for one action. If your method does two or three different things at a time then you should consider splitting the functionality of this method into other methods.
> Such method is easier to understand, scale and reuse in other methods.

[10 Tips To Keep Your Code Clean](https://medium.com/oril/10-tips-to-keep-your-code-more-clean-2fa9aafea1cf#d065)

[Solution](https://github.com/AICoE/workshop-coding-best-practices/commit/90fc03ab3437099d68fd544ab76be58d474010f6)

### Keep it DRY

> The DRY principle, formulated by Any Hunt and Dave Thomas in The Pragmatic Programmer, is the use of functions, classes and instances to allow you to avoid retyping code that has already been written once. This fundamental principle allows developers to avoid duplication to produce much cleaner code compared to the programmer who uses unnecessary repetition. Optimizing the code is what often separates a great coder from an average one.

[Don’t Repeat Yourself (DRY)](https://www.codingdojo.com/blog/clean-code-techniques)

[Solution](https://github.com/AICoE/workshop-coding-best-practices/commit/129f0910586a205f36a025586d8e4d4ba746b229)

### Comments

> 1. Always try to explain yourself in code.
> 2. Don't be redundant.
> 3. Don't add obvious noise.

[Comments Rules by Uncle Bob](https://gist.github.com/wojteklu/73c6914cc446146b8b533c0988cf8d29#comments-rules)

[Solution](https://github.com/AICoE/workshop-coding-best-practices/commit/0127ea96ae8bd193c433b09672579fb39417e4d8)


## Profiling Code

zak will add stuff

## Bots

frido will add stuff

## ML Code

### Running the ML Code
`python model.py`

### Understand Data

#### Data preview and dimentions

`print(dataset.shape)`

`print(dataset.dtypes)`

`print(dataset.head(15))`

#### Descriptive Statistics

`print(dataset.describe())`

#### Correlation

`print(dataset.corr(method='pearson'))`

#### Model accuracy

`from sklearn import metrics`

`print(metrics.mean_absolute_error(yPrediction, yTest))`


## Create a PR

* create a PR to the original Repo
* ask for a review by a peer
