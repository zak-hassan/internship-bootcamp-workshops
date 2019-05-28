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

mhild will add stuff

I'll re-factor the code to be even worse :)

## Profiling Code

zak will add stuff

## Bots

frido will add stuff

## Optimizing ML Code

prasanth

## Create a PR

* create a PR to the original Repo
* ask for a review by a peer
