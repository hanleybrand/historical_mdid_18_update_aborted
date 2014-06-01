Fields, Fieldsets and Metadata Standards
========================================

Field sets are a way to group individual fields in the UI

Example:

Take a collection with a specific set of metadata to be implemented in  MDID

Collection name: Teaching Images
Metadata fields:  Title, Creator, Period, Style, Medium (etc)


The below steps don’t really need to be done in order as far as I can tell — it’s just a little easier to do it in this order

Step 1 Metadata Standards:

mdid3.server.edu/admin > Data > Metadata Standards  click +Add
Form values:  Teaching Images, teaching_images, ti

This will give the Teaching Images fields a prefix so they’ll show up in the admin views like ti.title

Step 2 Field Sets:
mdid3.server.edu/admin > Data > Field Sets  click +Add
Form Values: Teaching Images, teaching_images, (blank) — I’m not sure what the effect of setting an owner is,
I click “standard” but similarly I’m not sure what effect it has

Step 3 Fields
mdid3.server.edu/admin > Data > Fields  click +Add
Form values: Title, title, (blank), Standard: Teaching Images, (—————)

for Equivalent, it’s important to set equivalents to the dc standards where you can. It’s especially important with name of work/title fields because Record pages in mdid display the dc.title field, but there’s no reason not to map the other equivalents

Example - on my test server the Field ti.title could map to Equivalents dc.title, aah.title, vra.title


Rinse and repeat for the rest of the fields.