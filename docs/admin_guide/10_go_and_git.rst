Working with git
================




Get a github account, make a repo - or at least make issues
-----------------------------------------------------------

Do it! If you keep settings\_local.pt in your .gitignore file you won't
push sensitive info to the internet - and it makes asking questions
about your code easier, because you can link specifically to the file
that's causing problems.

ALSO - having a github account will enable participation in community
wikis, etc.

| ALSO - if you find an issue with mdid3, it's probably best to file it
here, at least when you're sure what's causing the problem:
| `https://github.com/cit-jmu/rooibos/issues <https://github.com/cit-jmu/rooibos/issues>`__

AND ALSO - Consider doing a git tutorial. It's a neat system in and of
itself that has number of potential uses (even if you're not a developer
at all - it's kind of like a free command line driven version of that
Apple time machine, minus the fancy zooming things)

-  `http://try.github.com/levels/1/challenges/1 <http://try.github.com/levels/1/challenges/1>`__
-  `http://blip.tv/scott-chacon/git-talk-4113729 <http://blip.tv/scott-chacon/git-talk-4113729>`__
-  `http://www.codeschool.com/courses/git-real <http://www.codeschool.com/courses/git-real>`__
   (requires subscription to codeschool)

a bunch of tutorials and resources are collected here: \*
`http://sixrevisions.com/resources/git-tutorials-beginners/ <http://sixrevisions.com/resources/git-tutorials-beginners/>`__

--------------

Getting to it
-------------

Branching is best
-----------------

It's best if you keep your server on it's own branch - this gives you
the ability to switch to the canonical experimental branch, update,
merge & confirm there are not problems after updating and then re-merge
experimental with your own custom branch. This may seem like an extra
step, but it's worth keeping your own modifications segmented away from
the official repos.

Important note
--------------

    Always run ``python manage.py syncdb`` and then restart your
    webserver after pulling an update from github - some changes can
    cause hard-to-notice through extremely bizarre behaviors if the
    database is not synced - even data loss (or at least data mangling)
    is possible. So just do it.

How to set this up
~~~~~~~~~~~~~~~~~~

After you've successfully installed, create a branch before making
changes (I'm calling it 'ourSite' below). This can also be done directly
after a successful fetch/merge from upstream (upstream is the standard
name for a git repo that you've cloned, i.e. that you can not push to -
in our collective case, upstream would be
git://github.com/cit-jmu/rooibos.git ):

::

    git branch create ourSite
    git checkout ourSite
    git branch
       master
       experimental
     * ourSite

Then do your customizations and commit the changes -

::

    git -am commit "commit message"

Updating is Easyish
-------------------

When some new changes strike your fancy, fetch from upstream

::

    git fetch upstream
      remote: Counting objects: 67, done.
      remote: Compressing objects: 100% (20/20), done.
      remote: Total 44 (delta 33), reused 34 (delta 23)
      Unpacking objects: 100% (44/44), done.
      From git://github.com/cit-jmu/rooibos
        a79c65e..6e3b630  experimental -> upstream/experimental
        bd553f8..580e79a  jmu-production -> upstream/jmu-production

(You could also do 'git pull', but that auto-merges with... well,
exactly. It automerges. In my opinion, when I could explain it without
looking it up, I'll use git pull. In the meantime, I'll use 'git fetch'
which gets the changes but keeps them in secret .gitland until I merge
them somewhere explicitly.)

So then, I want to patch my local experimental branch, which I keep in
sync and unchanged from the cit-jmu repo:

::

    git checkout experimental
      Switched to branch 'experimental'
    git status
      # On branch experimental
      nothing to commit (working directory clean)
    git merge upstream/experimental
      Updating a79c65e..6e3b630
      Fast-forward
       rooibos/data/models.py              |   10 +++++-----
       rooibos/legacy/views.py             |    9 ++++++++-
       rooibos/solr/templates/browse.html  |   10 ++++++++++
       rooibos/solr/templates/results.html |   12 +++++++++---
       rooibos/solr/views.py               |    6 +++++-
       rooibos/urls.py                     |    4 ++++
       6 files changed, 41 insertions(+), 10 deletions(-)

Now, I switch back to my local customizations and then merge in the new
changes

::

    git checkout ourSite
       Switched to branch 'ourSite'
    git merge experimental
      Merge made by recursive.
       rooibos/data/models.py              |   10 +++++-----
       rooibos/legacy/views.py             |    9 ++++++++-
       rooibos/solr/templates/browse.html  |   10 ++++++++++
       rooibos/solr/templates/results.html |   12 +++++++++---
       rooibos/solr/views.py               |    6 +++++-
       rooibos/urls.py                     |    4 ++++
       6 files changed, 41 insertions(+), 10 deletions(-)

Now, if there's no conflicts the output on your second merge will look
like the first.

If there are conflicts, read this:
`http://genomewiki.ucsc.edu/index.php/Resolving\_merge\_conflicts\_in\_Git <http://genomewiki.ucsc.edu/index.php/Resolving_merge_conflicts_in_Git>`__

Lastly, you'll almost always need to ``python manage.py syncdb`` ad then
restart web services - either via ``sudo apachectl restart`` or
``iisreset`` depending.

And hopefully, you've successfully updated!
