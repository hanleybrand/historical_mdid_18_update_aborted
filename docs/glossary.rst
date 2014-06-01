MDID Glossary
=============

.. sectionauthor:: Peter Hanley


.. glossary::

   Records
      The basic atomic item/object.  Sort of synonymous with 'artifact,' except it's more like a referent of the artifact that metadata can cling to (Metadata is attached via fields, with the exception of Title, which is part of the Record (I think))

   Media
      The data base record of a digital media file. Can be pretty much anything, but jpegs have the richest level of support.

   Files
      Actual files on disk.

   Storage
      Both the location on disk where Media is stored, and a container than can have access controls (e.g. You can have "Common" storage that any user can upload to and then "Exclusive" storage that is reserved for your VRC staff

   User
      Intuitively a person, but really it's a username and password combination optionally fleshed out via a first & last name. Also an email address.

   Group
      A collection of  users for the purposes of bulk assigning permissions. Two special (or, extended) groups are "Anonymous" (anyone in the world, even if they haven't logged in) and "Authenticated Users" (anyone who has logged in successfully)

   Collections
      I think technically it's best to think of Collections as "Permission sets" as much as a way to logically group Records - basically you can set a type of access controls for a collection and each Record that is a member of that collection inherits those permissions.  Example: You have two collections, "Common" and "Exclusive."  Records that go into Common can be set to be viewed by all logged in users (Authenticated Users) or even anyone on the web (Anonymous). The Exclusive collection could restrict access to only members of the group called Exclusive (which you would have also created and added the correct users to).  A user can create personal records and share them via that group. You can also use collections to limit search results (i.e. only search records in the Exclusive collection)

   Field
      A key/value pair attached to a record. Keys are easily mutable.  (examples  'title' : 'Nude descending a staircase'  or 'medium' : 'jello'). Can be organized via field sets and metadata standards.

   Field Sets
      An named arbitrary collection of fields. Dublin Core & VRA Core 4 are default.

   Metadata Standard
      Another layer of metadata organization. Adds a prefix to field names.

   Vocabularies
      No idea, to tell you the truth.

   Vocabulary items
      Same, but I think a bunch of these makes up a Vocabulary?

   Flat Pages
      "A flatpage is a simple object with a URL, title and content. Use it for one-off, special-case pages, such as “About” or “Privacy Policy” pages, that you want to store in a database but for which you don’t want to develop a custom Django application."  An optional feature of the django framework, documentation is here: https://docs.djangoproject.com/en/1.2/ref/contrib/flatpages/

   Impersonation
      The ability of an admin user to assume the identity of another user. Very useful for checking problem reports, especially when trying to determine if a problem is your server or the person who is having the problem's computer.  Accessible from the Options page (link on upper right of the page).  I think you can set custom impersonation options (like maybe a VRC Help role that can impersonate specific Faculty members for support purposes?), but I've never done it, because at Temple anyone who would get a custom impersonation role is a sys admin anyway.
