## SSO Reflection

### Description
I looked at the all the suggested SSO's, OpenID Connect, OAuth, and uPort. I ended up choosing OAuth.

### Why I chose OAuth
I chose OAuth because they had a very detailed and easy to follow quick-start guide that I could use to attach the SSO to my webpage.

### How far I got
I was able to create the wepage, server, and authentication config files. The server works, and the webpage does load on my http://localhost:3000/ when my server is running (using 'npm run dev' on GitBash to run 'nodemon server.js'). However, the login and logout buttons are still currently locked until I get my updateUI function working.

### Obstacles I encountered
As I mentioned above both my login and logout buttons are locked on my wepage. This is because following the OAuth guide required me to use ESLint (.eslintrc) so the functions they had on their quickstart guide would work, however I'm still running into issues of syntax errors despite this. I'll probably just have to rewrite the code to use more current javascript syntax so that I don't require ESLint.
