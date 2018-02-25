OBJECTIVE

Use OpenAmbit to download the data from the Suunto device.
OpenAmbit stores each activity in a .log file.
I want to read the log file, store the data in a database and then visualize / analyze the data with a webapp.

THE .LOG FILE

The .log file is an xml file.
I did not find any documentation about its structure, therefore I am "guessing" how it works.
For what I can see there are some header information about the activity.
Then a section delimited by <log></log> starts; this section has the detailed data, i.e. the "samples" taken by the device as the activity goes on.
I will have to use these data to have time-dependent measures, not just summarized measures (like average values).

THE UML MODEL

I am working on a UML model first. Then I will start building the Django models from there.

TODOs

- Find and implement a formula to calculate the limits of all heart rate zones.
- Where do I implement the methods to set the "calculated fields of my models"? I think I have to do that in views not in the models.
- Add to the uml model and to the django app the remaining header data (i.e. those I have not included yet).
- Implement security, so that a device owner can see the data related to his device(s) only.
- Add the <log></log> data to the uml model and to the django app.
