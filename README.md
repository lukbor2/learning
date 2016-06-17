learning
========

I would like to use this repository to store the projects I use for learning so I can access them from different development environments.

From Cloud9
===========

	For existing files:

	git commit -a -m "A message here"
	git push

	For new files

	git add folder/filename
	git commit -a -m "A message here"
	git push
	
	example
	
	git add ./EloquentJavaScript/eloquentJS_1401.html
	git add ./EloquentJavaScript/js/http.js
	
	NOTE: for a reason I don't know, when my workspace was re-activated, the project from GitHub was not working properly anymore.
	I could see the main folder (learning) but nothing below it. So I deleted the workspace and cloned it again. After taking these
	steps it worked again.

From Eclipse
============

	Right click the project
	Select Team and then Commit
	In one of the windows which follow select the master branch and
	use the option "force commit"
	Then click on the button "Commit and Push"

	
Error Message
=============

	When one repository has non-committed changes and I commit and push changes from other repositories,
	(for example I don't commit from Eclipse, but I commit and push from Cloud9) then an error might happen
	
	git  error: The following untracked working tree files would be overwritten by merge
	
	In this case look at the file(s) in the error message and use the command
	
	git clean -f <directory or file> 
	
	to remove those files. After that git pull should work.
