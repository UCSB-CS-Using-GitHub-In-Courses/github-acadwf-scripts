github-acadwf-scripts
=====================

This repo containts scripts for github academic workflow, developed at UC Santa Barbara.  Team Leader: Phill Conrad.  Further Acknowledgements and list of authors/contributors at the bottom of this README.

Overview
========

The main workflow that is currently supported is:

* For each assignment, for each student (or pair, or team):
** Set up a private repo where that student (or pair, or team) has push/pull access to the repo, as does the instructional staff (Instructor, TAs, Graders), but no other student (or pair, or team) in the course does.    The repo can be pre-populated with "starting point" materials provided by the instructor.

The repos can be set up "just in time"---you don't have to set them all up at the beginning of the course.


Getting Started
===============

(1) Before anything else, create an organization for your course.

You do that by visiting:

https://github.com/edu

and clicking on "I'm a teacher or student organization".

Indicate how many students you expect to have, and how many
repositories each student or pair will need (i.e. how many assignments
you expect to have for each student or pair.)

Note: John Britton of github strongly encourages "one repo per
project" rather than "one repo per course (with subdirectories in that
repo for assignments.)".  His advice: Don't think of repos as a
"scarce resource" that needs to be conserved---github is happy to
contribute as many repos as you need for academic use.   

So my suggestion is to overestimate by 10 to 20 percent, and then if/when you
exhaust 80% of your private repos, ask for more.    

2) Create a form similar to the one shown here---I suggest doing this
using Google Drive (I have a sample script that grabs the data from
the form) to collect github ids from your students and tie those back
to "real names" and student ids.

https://docs.google.com/forms/d/1icypz0MC67pUn9ZiXZV6tMCR6_P8Ejy2jBEZCuO_8Yg/viewform

3) Ask your students to create their github account and fill out the
form as soon as you can reach them---preferably before the quarter
starts.

Here's the text I used in Spring 2013 for CMPSC 56 at UC Santa Barbara:

```
Welcome to CMPSC56!

CMPSC56 is one of my favorite courses to teach, because, like CMPSC48,
it is where we take you from "toy programming"---where you are coding
just for the sake of learning how to code---towards "software
development" as it is practiced in industry.

As part of that process, we will be using a version control tool
called "git", and a cloud-based repository service called "github.com"
throughout the course.

Therefore it is important for you to CREATE A GitHub.com ACCOUNT ASAP!
It will save us SO much time if you can do this NOW, and it will only
take 5 or 10 minutes at most.  So, please take two steps.  BOTH are
important:

(1) Please visit http://github.com and create an account. (If you
    already have one, that's great--skip this step.)

(2) Visit the following page and let us know what your github.com
    username is.

http://bit.ly/cs56-s12-githubform

That's it!

If you want, there is a third optional step: you can go to the
folllowing link, and spend fifteen minutes to learn a little bit about
git.  You'll be assigned this as "homework" during your first week of
the quarter, so if you don't do it now, you'll have to do it later
anyway.  Why not get it out of the way?

Got 15 minutes and want to learn git? 
  http://try.github.com/levels/1/challenges/1

```


(4)  The next step is where you clone the repository that contains the scripts for working with github.   You should this step and the ones the follow on a machine that has Python 3, and the bash shell---I've made it work on both Linux and Mac.     

First, I like to create a directory called ~/github, and then I always
cd into that directory before I do "git clone <url>"---that way, I
know that all my github repos are organized under that directory.
That's optional though--how you organize your disk space is entirely up to you.

In whatever directory where you want the repo clone to live, do this:

git clone https://github.com/UCSB-CS-Using-GitHub-In-Courses/github-acadwf-scripts.git

That should clone the repository that contains the scripts.  There is one more thing to do though---the repo contains a "sub-repository" for PyGithub---that's like a "symbolic link" or a "pointer" to a separate repo for the software that the scripts are based on.  The next step makes sure that subdirectory gets populated with the latest version of that software:

(5) To populate the PyGithub subdirectory, do this:

git submodule init
git submodule update

That should populate the PyGithub subdirectory with contents.

(6) Create a directory structure for your starting point files 

NOTE: The Spring 2013 version of the software stored these in the same repo with the scripts.   In Fall 2013, I'm modifying the 
scripts so that the location of these is determined by an environment variable.   That should make it easier to use the 
scripts for multiple courses.

Create a directory for your starting point files.    I suggest making this a github repo also---public or private, inside the organization, or not---it doesn't matter.    The important thing is that you have a top level directory, for example:

* ~/courses/CS1/CS1_F13_Labs 

and that under that, you have subdirectories with this naming convention:

* ~/courses/CS1/CS1_F13_Labs/lab00_startingPoint
* ~/courses/CS1/CS1_F13_Labs/lab01_startingPoint
* ~/courses/CS1/CS1_F13_Labs/lab02_startingPoint
* etc.

The prefix "lab00", "lab01", "lab02", etc. can be anything you like---use whatever naming convention makes sense for your course.  The important thing, for convenience sake, is that you add the _startingPoint suffix to each of these, and store them in the same place.

Note that if the top level directory (e.g. CS1_F13_Labs in this example) is a github repo, only THAT directory will have git plumbing (i.e., the .git subdirectory) stored in it.    That's important, because we don't want to confuse git when our script copies files from that directory into each of the student private repos in a later step.

(2) Into lab00_startingPoint, Put the files you want every student to have in their lab00 repo when they first clone it.

(3) Setup an environment variable called GHAW_START_PT (GHAW=github academic workflow) that points to this starting point directory, e.g. in bash:

export GHAW_START_PT=~/courses/CS1/CS1_F13_Labs

The scripts will look in that directory for the subdirectory XXX_startingPoint (where XXX is the name of your assignment).




Acknowledgements
================


These scripts were developed by Phill Conrad at UC Santa Barbara.

Assistance was provided by:

* the instructional staff of CS56 from Spring 2013: Scott Bishop, Aaron Dodon, Leif Dreizler, Jasen Hall, Alex Hamstra, Carina Rammelkamp, 

* Christine Alvarado at UC San Diego, and her instructional support
  staff for CSE100 F13, especially Arden Liao, who helped to test the
  scripts and work flows, and provide valuable suggestions on how they
  could be improved.