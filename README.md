# Sage

Live Version: [Sage](https://sage-advice-8dd203911010.herokuapp.com/)

Repository: [GitHub Repo](https://github.com/TammyGirl2015/Sage)

The app is developed by [Tamarie Maenzanise](https://github.com/TammyGirl2015).

## About

Sage advice is a blog app that provides advice, unsolicited as it may be, it is much needed in the world we live in. It offers a kind word to the healing soul and words of experience.

## User Experience Design

The design is simple and the words are made to stand out against a simple backround.

### Strategy

The aim of this app is to provide comfort and words of wisdom to those seeking it. Many a time people don't know where to turn to for words of comfort and Sage Advice is meant to provide such direction in a soothing, heartwarming manner.

### Target Audience

This blog can be read by a few groups:
- Teenagers: This group of people ususally prefer not to turn to their parents for advice (for whatever reason), and wuld rather interact with their peers who will likely not provide wise direction. This is aimed at letting such ones find the advice they need - as though coming from their parents given the soundness of it.
- Young adults: Young adults are often looking for a friend - not just any - a good one who will stick by them. Unfortunately these are had to come by and this site can be a place they can rely on.
- Adults: Adults have usually come to their senses about things (hopefully), and they can attest to some of the words of wisdom found on the site. Not only can they benefit from it but they can contirbute by way of commenting.
- Elderly: These ones are a true osurce of wisdom (can be), and they are key in providing the sound advice and guidance many seek today for one good reason - experience. They do say experience is the best teacher. Their input is most valuable and the site can benefit from their comments and additions by way of review.

### User Stories

| Issue ID    | User Story |
|-------------|-------------|
|[#1] View post list (https://github.com/users/TammyGirl2015/projects/5/views/1?pane=issue&itemId=80645726&issue=TammyGirl2015%7CSage%7C1)| As a site user I can view a list of posts so that I can select one to read |
|[#2] Open a post (https://github.com/users/TammyGirl2015/projects/5/views/1?pane=issue&itemId=80645725&issue=TammyGirl2015%7CSage%7C2)| As a site user I can click on a post so that I can read the full text |
|[#3] View likes (https://github.com/users/TammyGirl2015/projects/5/views/1?pane=issue&itemId=80645723&issue=TammyGirl2015%7CSage%7C3) | As a Site User/ Admin I can view the likes on each post* so that I can see which one is most popular or has gone viral |
|[#4] View comments (https://github.com/users/TaAs a Site User/ Admin I can view the comments on a post so that I can read the comments |
|[#5] Account registration (https://github.com/users/TammyGirl2015/projects/5/views/1?pane=issue&itemId=80645721&issue=TammyGirl2015%7CSage%7C5)| As a site user I can register an account so that I can comment on and like posts |
|[#6] Comment on a post (https://github.com/users/TammyGirl2015/projects/5/views/1?pane=issue&itemId=80645720&issue=TammyGirl2015%7CSage%7C6)| As a site user I can leave comments on a post so that I can be involved in the conversation |
|[#7] Like/ Unlike a post (https://github.com/users/TammyGirl2015/projects/5/views/1?pane=issue&itemId=80645719&issue=TammyGirl2015%7CSage%7C7)| As a site user I can like or unlike posts so that I can interact with the content |
|[#8] Manage posts (https://github.com/users/TammyGirl2015/projects/5/views/1?pane=issue&itemId=80645718&issue=TammyGirl2015%7CSage%7C8)| As a SiteAdmin I can create, read, update and delete posts so that I can manage the blog content that I post |
|[#9] Create drafts (https://github.com/users/TammyGirl2015/projects/5/views/1?pane=issue&itemId=80645717&issue=TammyGirl2015%7CSage%7C9)| As a Site Admin I can create draft posts so that I can finish writing content later if I need to |
|[#10] Approve comments (https://github.com/users/TammyGirl2015/projects/5/views/1?pane=issue&itemId=80645716&issue=TammyGirl2015%7CSage%7C10)| As a Site Admin I can approve or disapprove comment so that filter out objectionable comments |


## Technologies used

- ### Languages:
    
    + [Python 3.12.6] : the primary language used to develop the server-side of the site.
    + [JS] : the primary language used to develop the interactive components of the site.
    + [HTML] : the markup language used in creating the site.
    + [CSS] : the styling language used to style the website.

- ### Frameworks and libraries:

    + [Django]: python framework used to create all the logic.
    + [jQuery]: used to control click events.
    + [jQuery User Interface] : used to create the interactive elements.

- ### Databases:

    + [SQLite] : was used as a development database.
    + [PostgreSQL] : the database used to store all the data.

- ### Other tools:

    + [Git] : the version control system used to manage the code.
    + [Pip3] : the package manager used to install the dependencies.
    + [Gunicorn] : the webserver used to run the website.
    + [Django-allauth] : the authentication library used to create the user accounts.
    + [Django-crispy-forms] : was used to control the rendering behavior of Django forms.
    + [Cloudinary] : the cloud database used to store all the data.
    + [GitHub] : used to host the website's source code.


---


### Imagery

I struggled with adding an image as it defualted back to the placeholder image or gave me an error i was unable to fix. As i started the project i intended to go for functionality first and then look at styling however as i struggled with the functionality i did not have time leftover to configure the imagery as i wished. In the next version of this project, it will ideally have imagery befitting the topic it speaks of, with calm sage green and brown hues that remind one of an elderly person sitting on a porch on a sunny day looking out over fields, sharing their words of wisdom, their sage advice.

### Wireframes

No wireframes available at this time

---


## Information Architecture

### Database

* During the earliest stages of the project, the database was created using SQLite.
* The database was then migrated to PostgreSQL.

## Testing

### Nav Links:

- Home
Intended action: click on it and return to the home page. Test: When clicked on it does take the user to the home page.

- Sage Advice 
Intended action: click on it and return to the home page. Test: When clicked on it does take the user to the home page.

- Register
Intended action: take user to the sign up page. Test: when clicked on it does take the user to the sign up page.

- Login
Intended action: takes the user to the sign in page where they can input their details to login. Test: when clicked on, it takes the user to the sign in page where the user can enter their login details.

- Post
Intended action: when the heading on the post is clicked on, it takes the user to the post page where they can read the full article. Test: all headings on each post takes the user to the intended page.

- Like
Intended action: the user is meant to click on the heart to indicate thet like the article. It is supposed to turn red once clicked on. It is also supposed to lose the red color if clicked on again to remove the like. Also the counter increases by the number of likes. Each user can only add 1 like. Test: the test shows that the heart does reflect red when clicked on and returns to white when clicked on a second time. The counter increases and decreases in numbre by 1 for each user as the heart is clicked on.

- Comment
Intended action: the comment body is meant to be filled in and the submit button clicked to let the comment go into a pending stage for the comment to be approved. Test: The test indicates this does happen as intended.

Forms
- Sign Up/ Register
Intended action: the form has labels for details for the user to input, each field must be filled unless marked optional. When each required field is filled in the user clicks on sign up and the user is created. The user is taken to a page that reflects this. Any wrong input eg into an email field is indicated to be wrong if it is incorrect.
Test: The test proves that the intended actions occur as stated.

- Sign In/Login
Intended action: the form has labels for details for the user to input, each field must be filled unless marked optional. When each required field is filled in the user clicks on sign up and the user is created. The user is taken to a page that reflects this. Any wrong input eg into an email field is indicated to be wrong if it is incorrect.
Test: The test proves that the intended actions occur as stated.

## Deployment

- The app was deploye to Heroku
- The live link is https://8000-tammygirl2015-sage-znmr2ztblji.ws.codeinstitute-ide.net/

## Credits

- [GitHub](https://github.com/) for giving the idea of the project's design.
- [Django](https://www.djangoproject.com/) for the framework.
- [Render](https://render.com/): for the free hosting of the website.
- [Cloudinary] : for the free hosting of the database.
- [BGJar](https://www.bgjar.com/): for the free access to the background images build tool.
- [Font awesome](https://fontawesome.com/): for the free access to icons.
- [Heroku](https://www.heroku.com/): for the free hosting of the website.
- [jQuery](https://jquery.com/): for providing varieties of tools to make standard HTML code look appealing.
- [Favicon Generator. For real.](https://realfavicongenerator.net/): for providing a free platform to generate favicons.
- [Code Institute] : for the walkthrough project which i templated as the basis for my project. 

---

## Acknowledgments

- Kieron/ Student Care/ Code Institute: The student care have been most helpful over the period of this course. I deeply wish to thank them for their understanding and patience.
- I would like to thank my mentor, Julia, for coming onboard at the 11th hour almost literally and adjusting as needed to provide the support, encouragement, enthusiasm, motivation i needed to maybe not excel with this project but in the very least not to give up.


