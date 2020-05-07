## Reflection

### What I have currently working
- The JSON Editor is currently working, however right now I have it set to just edit two files.
- My amazonaws server is currently hosting both the webpages correctly, and contains all my files that I've created to run the program.
- I have the authentication portion of my SSO working, where it checks the clientId with the SSO domain to see if the user has logged in successfuly atleast once.

### What's not working
- Right now the login/logout buttons arn't updating when the user has been authenticated, instead they are both just always locked. (When the user logs in successfuly the login button locks, and logout button unlocks, and vice-versa)
- The editor currently works only for json files (which is why I'm just calling it the JSON Editor), _ideally_ the app would allow for the manipulation of different types of files, especially xml and txt files as well.

### What I hope to have functioning
- I want to have the user type in credentials and have it check with another authorization list. Right now the login button just lets any user click it and it remembers the user so they dont need to re-'login' when they return to the page.
- For the JSON editor I want the user to be able to select from multiple files, rather than just the two I have available.
- What I would like for the app (but am unsure if I can accomplish) is for there to be different levels of authorization, so it checks the login credentials and logs the user in as a certain level, which will determine what files they have access to manipulate.

### References
- I used this page as reference to create an editor for json files, (For mine however it would be more dynamic and able to select from a list of files, read them in , and then present them. https://www.jqueryscript.net/tags.php?/JSON%20Editor/
- I used the AUTH0 guide to help set up a SSO server https://auth0.com/docs/quickstart/spa/vanillajs
