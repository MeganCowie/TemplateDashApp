# Heroku Deployment instructions. 

LORD. I don't know why this is so challenging for me. I've done this 2-3 times already and each time I have wasted 4-5 hours going in circles. So, here are instructions for what worked for me this time. Hopefully they will also work next time. These steps presume that I already have the app on Github, Git installed on my computer, and the heroku cli installed as well.  
https://devcenter.heroku.com/articles/getting-started-with-python#set-up

1. Make sure to have the correct files. These include:
    - requirements.txt (within Atom, you can generate a requirements.txt file with the python-requirements package). This package will not include gunicorn, so you must append "gunicorn" to the file manually. 
    -  Procfile (web: gunicorn app:server) and Procfile.windows (web: python manage.py runserver 0.0.0.0:5000) for running the application on a server or locally on Windows
    -  runtime.txt which states the python version that should be used (python-3.9.5)
    -  manage.py (I don't quite understand what this does but I think to do with selecting the server. I just copy/pasted it from an example...)
    -  .gitignore 

2.  Navigate to C:\Program Files\Git and open the application git-cmd.exe. For reasons I don't yet understand, this thing does not work through the command prompt or Powershell. Also don't even bother trying it through the website interface / connect through Github. I've never been able to figure out why, but it never works. 

3. Login to heroku CLI: <br>
      $ heroku login
      
4. Navigate to the folder where the app is stored. 

5. Create an empty app on Heroku: <br>
      $ heroku create
      
6. Deploy the code: <br>
      $ git push heroku main

7. Run and open the app: <br>
      $ heroku ps:scale web=1<br>
      $ heroku open
      
8. Within the website interface, it's easy to rename the deployed app and find the link. 


I don't know why this has been so challenging. This is exactly the instructions on their website. I guess knowing exactly what files to include and not understanding why it didn't work on the command prompt or Powershell were my main slowdowns. Oh also knowing to add guinicorn manually is a bit sneaky, since neither Pip nor the Atom package seem to find it. 
