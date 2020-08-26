Python Version ```-- 3.8.4```

To check your current python version type in following command in the terminal ```python --version```

Django Version ```3.1```

To check your current version of django type following command
in the terminal ```python -m django --version``` 

Angular version ```10```

Instruction for Collaborators 

*   Create a branch name same as issue name with issue number, For Example, if issue name is "this-is-issue-abcd #8" your branch name should be "this-is-issue-abcd.#8" 
*   Once you done the task commit the changes with most suitable commit message followed by #issue_number
*   Pull the Changes from Origin/Remote Master Branch 
*   Apply the changes and commit & push the changes 
*   Create the pull request after commit & push the changes
*   Link the pull request with relevant issue

Note : Do not try to commit to the master branch, Test well locally before you create the pull request

Recommended IDE Pycharm Professional 

Download Link https://www.jetbrains.com/pycharm/download

Instruction about how to install the Django framework

UNIX/Linux and Mac OS X Installation 

*   Download the latest version of Django http://www.djangoproject.com/download.
*   When you got archive from link above, it will be like Django-x.xx.tar.gz
*   Extract and install it using this command

      ```$ tar xzvf Django-x.xx.tar.gz```
      
      ```$ cd Django-x.xx```
      
      ```$ sudo python setup.py instal```
*   Test your installation by running this command
      ```$ django-admin.py --version``` If it isn't working run this ```$ django-admin --version```
*   If you see the current version of Django printed on the screen, then everything is set

Windows Installation 

*   Download the latest version of Django http://www.djangoproject.com/download.
*   On some version of (windows 7) you may need to ensure the Path system variable has the Path the following ``` C:\Python27\;C:\Python27\Lib\sitepackages\django\bin\```int it, it depending on your Python version.
*   When you got your archive from the link above, Extract and install Django

      ```c:\>cd c:\Django-x.xx ```
*   install Django by running the below command for which you will need administrative privileges in windows shell "cmd"

      ```c:\Django-x.xx>python setup.py install ```
      
*   To test your installation, open a command prompt and type

      ```c:\>django-admin.py --version ``` If you see the current version of Django printed on screen, then everything is set. 
      
*   Or else Launch a "cmd" prompt and type python then:

      ```c:\> python ```
      
      ```>>> import django ```
      
      ```>>> print django.get_version() ```
