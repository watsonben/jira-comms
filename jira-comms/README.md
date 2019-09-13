# Creating comms of things that were completed in the past week
Steps:
* Run a JQL filter to obtain tickets for a given project that were moved into Done in the last week (you can find a pre-saved version of this under "Done this week" in JIRA)
* From the filter results, export these as a full csv (with all columns)
* Either put this file in the same directory as the python script, or in ~/Downloads, and the alias script will find it.
* Run python create-comms.py (or, if you have the alias script from my .bashrc file, simply run 'comms')
* Copy and paste the script output into a message as the release notes.
