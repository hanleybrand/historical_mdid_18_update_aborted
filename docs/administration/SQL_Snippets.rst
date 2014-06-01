.. sectionauthor:: Peter Hanley
.. publishdate:: 2014-04-25
.. summary:: A small collection of SQL code an administrator can run against the database
.. highlight:: sql

.. index::
   single: administration
   single: sql
   single: database

SQL Snippets
============


Although an MDID3 system administrator will ultimately be better
served by becoming familiar with python/django and interacting with MDID3 via shell\_plus, it is
possible (and sometimes more convenient) to query the MDID database with SQL. Here are some sample queries to
help discovery of the MDID schema.


Alphabetical list of collections
--------------------------------


.. code-block:: sql

    SELECT
        data_collection.id,
        data_collection.title,
        data_collection.name,
        data_collection.owner_id,
        data_collection.hidden,
        data_collection.description,
        data_collection.agreement,
    FROM
        data_collection
    ORDER BY data_collection.title ASC


Getting the database id of a specific user by username
------------------------------------------------------

.. code-block:: sql

    SELECT id, username
    FROM `rooibos`.`auth_user`
    WHERE auth_user.username = 'llux'


How many presentations does that user have?
-------------------------------------------

.. code-block:: sql

    SELECT
        COUNT(presentation_presentation.id)
    FROM
        presentation_presentation
    WHERE
        presentation_presentation.owner_id = 60

-----------

getting information about records
---------------------------------

If searching for information in your individual records, you might try something like:

.. code-block:: sql

    SELECT
        id, created, modified, name, owner_id
    FROM
        data_record
    WHERE
        data_record.id = 41588

This gets some information about a record, but it will be missing the
metadata, here's the output:

.. raw:: html

   <table class="table table-bordered">
   <tbody class="table-striped table-hover">
   <tr>
   <td>id</td>
   <td>created</td>
   <td>modified/td>
   <td>name</td>
   <td>owner_id</td>
   </tr>
   <tr>
   <td>41588</td>
   <td>2007-10-04 13:32:23<td>
   2010-10-20 09:15:58</td>
   <td>r-6165371</td>
   <td>60</td>
   </tr>
   </tbody>
   </table>

--------------

If you want detailed information, maybe it's unsurprising that some
JOINs are necessary:

.. code-block:: sql

    SELECT
        data_record.id,
        data_record.name,
        data_fieldvalue.label,
        data_fieldvalue.value
    FROM
        rooibos.data_record
            INNER JOIN
        rooibos.data_fieldvalue ON data_fieldvalue.record_id = data_record.id
    WHERE
        data_record.id = 41588

.. raw:: html

   <table class="table table-bordered">
   <tbody class="table-striped table-hover">
    <col>
    <col>
    <col>
    <col>

    <tr>
     <td>41588</td>
     <td>r-6165371</td>
     <td>Date</td>
     <td>1964</td>
    </tr>
    <tr>
     <td>41588</td>
     <td>r-6165371</td>
     <td>Description</td>
     <td>mixed material assemblage</td>
    </tr>
    <tr>
     <td>41588</td>
     <td>r-6165371</td>
     <td>Creator</td>
     <td>Kienholz, Edward</td>
    </tr>
    <tr>
     <td>41588</td>
     <td>r-6165371</td>
     <td>Title</td>
     <td>Back Seat Dodge, '38</td>
    </tr>
    </tbody>
   </table>



