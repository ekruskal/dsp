# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > 

    ls will list all the files and folders in your current directory.

    mv [file name] [destination] will move a file in your current directory to the destination. mv [old file name] [new file name] will rename the file.
    
    cd [subdirectory] will change your location to a subfolder. cd .. will change your location to the parent of your current directory.
    
    rm [file] will remove the file in your current directory.
    
    cp [file or directory] [destination] will copy a file or directory to the given destination.
    
    less [file] will print the contents of a file in a new window with paging.
    
    [command] > [file] will take the output from the command and write it to the file on the right.
    
    [command] >> [file] will take the output from the command and append it to the file on the right.
    
    a* is the set of all elements of your directory starting with a, *a is the set of all elements of your directory ending in a, a*.* is the set of all elements in your directory containing a.
    
    grep [string] [files] searches the files for the given string.
    
    man [command] will give you the name and description of the command and all accessible optionswhile performing the command.

---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

> > 

    ls will list the contents of your current directory excluding those that begin with ".".

    ls -a will list all the contents of your current directory including those that begin with ".".

    ls -l will list the contents of your current directory using a long listing pattern, meaning it will list them vertically
    and will provide additional information, such as size and creation date.

    ls -lh will perform the same operation as ls -l, except it will display the size in a human readable format.

    Now let's say I wanted to list the contents of my directories using a long listing pattern but I wanted to include files
    that began with ".". Then I would combine the flags -l and -a like so:  
        $ls -l -a
    Similarly if I wanted that same list but with human readable file sizes, I would use:
        $ls -lh -a



---


---

What does `xargs` do? Give an example of how to use it.

> > xargs is used to build and execute command lines from standard input.


> > So for example, let's say I had a text file temp.txt. Written in this textfile are the words newfile1, newfile2, newfile3
    on seperate lines. Now suppose I wanted to use the command line to take the contents of temp.txt, and create new text files
    newfile1.txt, newfile2.txt, and newfile3.txt. The first thing I would try would be 
    
    $cat temp.txt | touch
    
> > But this pops up an error, because touch can only take in a file name, not standard input. So instead I would have to use 
    
    $cat temp.txt | xargs touch 
    
> > This would get me the desired results.

---

