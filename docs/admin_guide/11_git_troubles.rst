Git Troubles
============

So git is really easy and won't give me any problems?
-----------------------------------------------------

Well, probably not. At least not all of the time. In the spirit of
honesty, and lending a dose of reality to the above instructions:

It is sometimes not-quite-as-simple as I described above, but I've never
had a problem that googling "what git said" didn't get me out of. The
one place where I have had continuous minor trouble is the .gitignore
file, which is a file that tells git what files to ignore. Basically if
you edit it, it will always conflict with

An example, which I edited out of the instructions from when I went to
apply the new files but which shows what working with git is often like,
at least for me:

Double-click to edit this gadget

-  **
-  **
-  **

::

    $ git checkout experimental
    Switched to branch 'experimental'

    $ git status
    # On branch experimental
    # Untracked files:
    #   (use "git add <file>..." to include in what will be committed)
    #
    #
    rooibos/mdid2.xml
    #
    rooibos/mdid2migrateOut.txt
    #
    rooibos/nohup_solr
    #
    rooibos/settings_local-ldapTunic.py
    #
    solr/nohup_solr
    nothing added to commit but untracked files present (use "git add" to track)

    $ nano .gitignore

so I added files above to .gitignore

::

    $ git status
    # On branch experimental
    # Changes not staged for commit:
    #   (use "git add <file>..." to update what will be committed)
    #   (use "git checkout -- <file>..." to discard changes in working directory)
    #
    #
    modified:   .gitignore
    #
    no changes added to commit (use "git add" and/or "git commit -a")

[sigh - I decide it's easy enough to fix my .gitignore file later]

::

    $ git update-index --assume-unchanged .gitignore

[btw - neat command, let's you essentially lie to git, or make git lie
to itself about a file... but it's dangerous, so I only use it for
gitignore]

::

    $ git status
    # On branch experimental
    nothing to commit (working directory clean)

    $ git merge upstream/experimental
    Updating a79c65e..6e3b630
    [blah blah]
     6 files changed, 41 insertions(+), 10 deletions(-)

    $ git checkout templeCustom
    error: Your local changes to the following files would be overwritten by checkout:
    .gitignore
    Please, commit your changes or stash them before you can switch branches.
    Aborting

[huh, uh oh ... ok, if that's the way you want to play it ... ]

::

    $ git stash 
    No local changes to save

[hmmmmm]

::

    $ git status
    # On branch experimental
    nothing to commit (working directory clean)

    $ git checkout templeCustom
    error: Your local changes to the following files would be overwritten by checkout:
    .gitignore
    Please, commit your changes or stash them before you can switch branches.
    Aborting
    $ git commit -am "committing changes to .gitignore"
    # On branch experimental
    nothing to commit (working directory clean)

::

    [oh boy]

::

    $ git update-index --assume-unchanged .gitignore

[maybe that will work]

::

    $ git checkout templeCustom
    error: Your local changes to the following files would be overwritten by checkout:
    .gitignore
    Please, commit your changes or stash them before you can switch branches.
    Aborting

[nope]

::

    $ git stash .gitignore

| [nope]
| [huh]
| [it occurs to me that the problem is the .gitignore in templeCustom
(from before I updated) will overwrite what I have ignored and thus
can't add. bleh. Ok, I guess I'll be double fixing .gitignore at some
point.]

::

    $ git checkout templeCustom -- .gitignore

[another neat bit: double dash filename after the checkout command will
checkout a single file form another branch, overwriting what you have]

::

    $ git checkout templeCustom
    Switched to branch 'templeCustom'

[ah, there we go]

::

    $ git merge experimental
    Merge made by recursive.

[the rest went smoothly, which was nice]

Double-click to edit this gadget
