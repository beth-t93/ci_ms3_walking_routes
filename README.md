![images](docs/images/amiresponsive.png)

[View the deployed site here](https://walking-routes.herokuapp.com/)

## Table of Contents

- [Project Goals](#project-goals)
- [User Experience](#user-experience)
    - [User Goals](#user-goals)
    - [Target Audience](#target-audience)
    - [User Stories](#user-stories)
    - [User Requirments and Expectations](user-requirements-and-expectations)
    - [Scope](#scope)
    - [Structure](#structure)
- [Design Choices](#design-choices)
    - [Colours](#colours)
    - [Fonts/Typography](#fonts-typography)
    - [Imagery](#imagery)
- [Wireframes](#wireframes)
- [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks, Librabries and Other Tools](#frameworks-libraries-and-other-tools)
- [Features](#features)
- [Future Features](#future-features)
- [Validation and Testing](#vlaidation-and-testing)
    - [HTML Validation](#html-validation)
    - [CSS Validation](#css-validation)
    - [Acessibility](#accessibility)
    - [Performance](#performance)
    - [Testing on Other Devices](#testing-on-other-devices)
    - [Testing of User Stories](#testing-of-user-stories)
- [Bugs](#bugs)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgements](Acknowledgements)


## Project Goals
The aim of this project is to create a site which enables people to share their favourite walking routes around North Wales. Users will be able to add, edit and delete the routes. 

## User Experience
### User Goals
- An easy to use site
- Add routes quickly and easily
- Find out about new routes
- Keep up to date with any changes to routes on the site.


### Target Audience
- Walkers
- General public interested in getting out walking more
- Dog walkers
- People that are new to the area and would like to find out about walks locally

### User Stories
#### Visitor Goals
1. As a visitor I want the site to be easy and simple to use.
2. As a visitor I want the site to be colourful and eye-catching, as well as be easy to read.
3. As a visitor I would like to be able to add information about new routes easily
4. As a visitor I would like to find out about new routes in my area
5. As a visitor I would like to be able to update routes I have already added to the site
6. As a visitor I would like to be able to delete routes I have previously added to the site
7. As a visitor I would like to be able to see an image from the route

#### Site Owner Goals
8. As a site owner I want the site to be easy to use.
9. As a site owner I want users to be able to view, add, edit and delete routes on the site.
10. As a site owner I want the purpose of the site to be clear to each user.

### User Requirements and Expectations
#### Requirements
- Easy to navigate
- Appealing design
- The user will be able to log in to add a route
- Only the user that added the route origianlly will be able to edit or delete it
- All users will be able to view the routes on the site.

#### Expectations
- Buttons take you to the page they say they will
- The add route form will successfully add a route to the database
- The edit form will successfully edit a route from the database
- The delete button will successfully delete a route from the database
- The user will receive feedback from the site when ading or editing a route and logging off
- Users are able to create an account so they can start adding routes


## Scope
Based on the above information, features to be included in the design include:
- An easy to navigate homepage with an obvious path to other pages
- A profile page that is only accessbile to individual users when they log in
- An add route form which will only be visibale to users when they log in
- Easily log in and logout of the site with the relevant buttons in the navigation bar
- Favicon to help users identify the site in any tabs

## Structure
A responsive site consisitng of 6 pages and two custom error pages. 3 of the pages are only visible when a user creates a profile.

The site will be easy to use across all devices.

## Design Choices
The style of the site will be simple and minimal so it remains easy to navigate and allows people to add and edit routes easily.

### Colours
The colour scheme for this site is meant to be bright and eye catching to the user, however there should still be enough contrast between the colours used so that the site remains easy to read and navigate for longer periods of time.

![images](docs/images/ms3colours.jpg)

I have chosen a colour scheme that is bright and eye-catching to the user, but it still allows the images added to routes by the user to stand out from the page.
### Fonts/Typography
To ensure the website is easily readable while also keeping to the simple and minimal design, the font I have used is Oswald, taken from the Google Fonts library, with sans-serif being the fallback font should either of the selected fonts be unavailable. 

## Skeleton

## Surface

### Wireframes
- [Index - desktop](docs/wireframes/index-web.pdf)
- [Index - mobile and tablet](docs/wireframes/index-mobile.pdf)
- [Login - desktop](docs/wireframes/login-web.pdf)
- [Login - mobile and tablet](docs/wireframes/login-mobile.pdf)
- [Register - desktop](docs/wireframes/register-web.pdf)
- [Register - mobile and tablet](docs/wireframes/register-mobile.pdf)
- [Profile - desktop](docs/wireframes/profile-web.pdf)
- [Profile - mobile and tablet](docs/wireframes/profile-mobile.pdf)
- [Add and Edit Route - desktop](docs/wireframes/add-edit-web.pdf)
- [Add and Edit Route - mobile and tablet](docs/wireframes/add-edit-mobile.pdf)

## Technologies Used

### Languages
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries and Other Tools
1. [Affinity Designer](https://affinity.serif.com/en-gb/designer/) was used to create the colour swatch.
2. [Git](https://git-scm.com/) was used within VS Code for version control to push code to GitHub.
3. [Github](https://github.com/) was used as a remote repository to store code.
4. [Am I Responsive](http://ami.responsivedesign.is/) was used to create the mockup you see at the start of this README.md file
5. [Coolors](https://coolors.co/) was used to help put together the colour scheme used throughout the site.
6. [Visual Studio Code](https://visualstudio.microsoft.com/) is the IDE I used to develop the project.
7. [Balsamiq](https://balsamiq.com/) was used to create the wireframes for the site
8. [Font Awesome](https://fontawesome.com/) was used for the icons throughout the site.
9. [Google Fonts](https://fonts.google.com/) Oswald was the font used throughout the site.
10 [Bootstrap](https://getbootstrap.com/) used to create layout and responsive elements.


## Features
#### Feature 1 - Homepage
The homepage is made up of:
1. The navigation bar
2. The hero image and text
3. The cards containing information about the routes
##### 1. Navigation
![images](docs/features/feature-nav.png)
- This is the first thing you see when you get to the site so I decided this needed to be easy to read to allow the user to successfully navigate through the site.
- As I wanted to keep the logo simple I used text only, in a bold, striking font.
- The navigation links are relevant and change depending on if the user is logged in or not.
###### User stories covered by this feautre:
1. As a visitor I want the site to be easy and simple to use.
2. As a visitor I want the site to be colourful and eye-catching, as well as be easy to read.
3. As a visitor I would like to be able to add information about new routes easily
8. As a site owner I want the site to be easy to use.

##### 2. Hero Text and Image
![images](docs/features/feature-heroimage.png)
- This feature clearly tells the user what the site is about.
- The text is legible and easy to read due to the shadow added to the image.
###### User stories covered by this feautre:
1. As a visitor I want the site to be easy and simple to use.
2. As a visitor I want the site to be colourful and eye-catching, as well as be easy to read.
10. As a site owner I want the purpose of the site to be clear to each user.

##### 3. Cards containing information about the route
![images](docs/features/feature-cards.png)
- This is where all the information added by users will be displayed.
- The design means key information, such as the start and end point are clear and easy to find.
###### User stories covered by this feautre:
2. As a visitor I want the site to be colourful and eye-catching, as well as be easy to read.
4. As a visitor I would like to find out about new routes in my area
7. As a visitor I would like to be able to see an image from the route
9. As a site owner I want users to be able to view, add, edit and delete routes on the site.


#### Feature 2 - Login Page
- This page contains a simple form allowing users to log in to the site.
-There is also a link directing users who do not have an acount to register

##### Login Form
![images](docs/features/feature-login.png)
- This lets the user easily login to their account.

###### User stories covered by this feautre:
1. As a visitor I want the site to be easy and simple to use.


#### Feature 3 - Register Page
- This page contains a simple form allowing users to register.
- There is also a link directing users who already have an account to login.

##### Register Form
![images](docs/features/feature-register.png)
- This lets the user register an account.

###### User stories covered by this feautre:
1. As a visitor I want the site to be easy and simple to use.


#### Feature 4 - Add a Route Page
- This page contains a simple form allowing users to add a route to the site.

##### Add Route Form
![images](docs/features/feature-add-form.png)
- This lets the easily add a route with all the relevant information to the site.

###### User stories covered by this feautre:
1. As a visitor I want the site to be easy and simple to use.
3. As a visitor I would like to be able to add information about new routes easily
9. As a site owner I want users to be able to view, add, edit and delete routes on the site.


#### Feature 5 - Edit a Route Page
- This page contains a simple form allowing users to edit and exisiting route.

##### Edit Route Form
![images](docs/features/feature-edit-form.png)
- This lets the easily edit a route they have already added to the site.
- The form is pre-populated with the routes exisiting information.

###### User stories covered by this feautre:
1. As a visitor I want the site to be easy and simple to use.
5. As a visitor I would like to be able to update routes I have already added to the site
9. As a site owner I want users to be able to view, add, edit and delete routes on the site.


#### Feature 6 - Profile Page
- This page contains a breif introduction, informing the user they are on their profile page.
- The page also displays all the routes that the user has added, with the addidition of edit and delete buttons on each card.

##### Introduction
![images](docs/features/feature-profile-intro.png)
- This lets the user know where they are on the site quickly and easily. It also tells the user what they can do on this page.

###### User stories covered by this feautre:
1. As a visitor I want the site to be easy and simple to use.
10. As a site owner I want the purpose of the site to be clear to each user.

##### Routes
![images](docs/features/feature-profile-cards.png)
- This allows the user to see the routes they have added with all the details easy to see and read through.

###### User stories covered by this feautre:
1. As a visitor I want the site to be easy and simple to use.
2. As a visitor I want the site to be colourful and eye-catching, as well as be easy to read.
7. As a visitor I would like to be able to see an image from the route

##### Edit and Delete Buttons
![images]( docs/features/feature-profile-edit-delete.png)
- This allows the user to edit or delete a route from their profile.
- This feature is only accessible if the user is logged in.
- Users can only edit and delete routes they have added themselves.

###### User stories covered by this feautre:
1. As a visitor I want the site to be easy and simple to use.
5. As a visitor I would like to be able to update routes I have already added to the site
6. As a visitor I would like to be able to delete routes I have previously added to the site
9. As a site owner I want users to be able to view, add, edit and delete routes on the site.


## Future Features
In the future I would add the ability to map out each route so users can easily follow a specific route, that is then supported by the instructions given in the route description.

I would also add a feature where users could comment on eachothers routes, creating a community feel on the site.

The area covered would also expand, as the routes on the site are currently all in North Wales.

## Information Architecture
### Data Storage
#### User Information
    | Title | Key in database | Form Validation | Data Type |
    | ------- | ------ | --------------- | -------- |
    | Account Id | _id | No validation | ObjectId |
    | Username | name | Text | string |
    | Password | password | Text | string |

### Route information 
    | Title | Key in database | Form Validation | Data Type |
    | ------- | ------ | --------------- | -------- |
    | Trail Id | _id | No validation | ObjectId |
    | Image url | image_url | url | string |
    | Route Name | trail_name | Text | string |
    | Terrain | terrain | Text | string |
    | Start Point | start | Text | string |
    | End Point | end | Text | string |
    | Description | description | Text Area | string |
    | Added by | created_by | Text | string |

## Validation and Testing

### HTML Validation
I used the [W3C Markup Validation Service](https://validator.w3.org/) to validate the HTML of the website. All pages passed with 0 errors and 0 warnings.

- [Index](docs/validation/html/index.png)
- [Login](docs/validation/html/login.png)
- [Add a route](docs/validation/html/login.png)
### CSS Validation
I used the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) to validate the CSS of the website.

- [CSS](docs/validation/css/css.png)

### Python Validation
I used [PEP8 online](http://pep8online.com/) and [Extends Class](https://extendsclass.com/python-tester.html) to vaildate the Python of the site

- [PEP8](docs/validation/python/PEP8.png)
- [Extends Class](docs/validation/python/Python-Syntax.png) - Shows 0 syntax errors

### Performance
I used [Google Lighthouse](https://developers.google.com/web/tools/lighthouse) to measure the performance and speed of my website.

- [Index](docs/validation/lighthouse/lighthouse-index.png)
- [Profile](docs/validation/lighthouse/lighthouse-profile.png)

### Testing on other devices

#### Devices tested:
- iPhone 12 Pro
- Samsung Galaxy s20+
- iPad Pro 11"
- 21.5" iMac
- Asus Chromebook Flip C434TA

#### Browser Testing
- Chrome
- Brave (Chromium)
- Safari

#### Tests Performed
- All buttons take you to the part of the site they say they will
- Be able to succesfully register an account
- Be able to easily log in and log out of the account
- Add a route with all fields storing information in the database correctly
- Use the edit button to successfully update a route
- Use the delete button to successfully delete a route

#### Results
All devices passed the tests

### Testing User Stories

1. As a visitor I want the site to be easy and simple to use.
    
    | Feature | Action | Expected Result | Actual Result |
    | ------- | ------ | --------------- | ------------- |
    | Simple, easy to use design | User is able to navigate to all parts of the site | User is able to successfully complete the quiz easily | Works as expected |

2. As a visitor I want the site to be colourful and eye-catching, as well as be easy to read.
    
    | Feature | Action | Expected Result | Actual Result |
    | ------- | ------ | --------------- | ------------- |
    | Bright colour scheme that is also still legible | All colours used on the site are bright and colourful, but still allow good legibility | Users find the site eye-catching and have no issues with the sites ease of use | Works as expected |

3. As a visitor I would like to be able to add information about new routes easily

    | Feature | Action | Expected Result | Actual Result |
    | ------- | ------ | --------------- | ------------- |
    | After login the navigation bar contains an add button | User presses the add button | To be taken to the add routes form | Works as expected |

4. As a visitor I would like to find out about new routes in my area

    | Feature | Action | Expected Result | Actual Result |
    | ------- | ------ | --------------- | ------------- |
    |  Start/End Point on information cards | The user can easily see an address of where the route starts and ends | User is able to see which routes are local to them | Works as expected |

5. As a visitor I would like to be able to update routes I have already added to the site

    | Feature | Action | Expected Result | Actual Result |
    | ------- | ------ | --------------- | ------------- |
    | On the profile page each route has an edit button | click edit to be taken to the edit route form | To be taken to the edit form which is prepoulated with the routes information | Works as expected |

6. As a visitor I would like to be able to delete routes I have previously added to the site

    | Feature | Action | Expected Result | Actual Result |
    | ------- | ------ | --------------- | ------------- |
    | On the profile page each card has a delete button | Click the delete button | The route is deleted from the site and database | Works as expected |

7. As a visitor I would like to be able to see an image from the route

    | Feature | Action | Expected Result | Actual Result |
    | ------- | ------ | --------------- | ------------- |
    | Ablility to add image via URL to each route | The user is able to see the image on each card | The user can easily see an image with each route |  Works as expected|

8. As a site owner I want the site to be easy to use.

    | Feature | Action | Expected Result | Actual Result |
    | ------- | ------ | --------------- | ------------- |
    | Simple page design | Easily see which button you need to press to progress through the site | The user can easily navigate the site | Works as expected |


9. As a site owner I want users to be able to view, add, edit and delete routes on the site.

    | Feature | Action | Expected Result | Actual Result |
    | ------- | ------ | --------------- | ------------- |
    | The homepage and the user profile display the routes | Users can easily see the routes on the site | Users can easily see routes on the site | Works as expected |
    | ------- | ------ | --------------- | ------------- |
    | The eidt and delete buttons on each route on the profile page | Users can easily navigate to edit or delte their routes | Users are able to successfully edit or delete routes | Works as expected |

10. As a site owner I want the purpose of the site to be clear to each user.

    | Feature | Action | Expected Result | Actual Result |
    | ------- | ------ | --------------- | ------------- |
    | Hero Text, page headings and flashes | Each page is clearly labelled with headings or messages telling the user where they are or what action they have just completed | Users can easily see where they are up to on the site | Works as expected |

## Bugs
- Bug : Data storing as null in the database when added through the site
- Fix: update inputs with names

- Bug: Edit and delete buttons being displayed outside the card
- Fix: Edit the structure of the divs on the page

- Bug: SSL error causing communication errors with the database
- Fix: Reinstall and update python

- Bug: URl errors with specific id's
- Fix: Restrucuture python routes ensuring all names are different


## Deployment
### Github Pages
This site is deployed using GitHub pages, this was the process:
1. Log in and selected my MS2 repository
2. Go to settings in the repository
3. Go to 'Pages" in the menu
4. Click 'source'
5. Change to dropdown menu from 'none' to 'main'
6. Click the link to the deployed site once the page has reloaded

### Forking this Repository
1. Find the repository on GitHub
2. Click the 'Fork' button on the top right of the page
3. You will now have a copy of the repository on your Github account

### Cloning this Repository
1. Find the repository on Github
2. Click on 'Code'
3. To clone using HTTPS - copy the url
4. Open Git and go to the directory you want to become the cloned directory
5. In the terminal type 'git clone' and the url
6. Press enter for the clone to be created.

### Create the Flask Application
1. Install Flask - type in terminal:
``` pip3 install Flask ```
2. Now we need to create a few new files. First, our Python file that will be the foundation of our application. You can name it something else, in this case, I used app.py, so type in the terminal:
```touch app.py```
3. Next, we will be storing some sensitive data, and we need to hide them using environment variables. You can use the terminal or just create a new file. I used the terminal, so type in the terminal:
```touch .env```
4. That file should never be pushed to GitHub, so we need to be able to ignore it somehow, so type in the terminal:
```touch .gitignore```
5. Double check in the gitignore file that you see ".env" and "pycache/"
6. Go to the env.py file and add the following:
```import os```
```os.environ["PORT"] = "5000"```
```os.environ["SECRET_KEY"] = "YOUR_SECRET_KEY"```
```os.environ["DEBUG"] = "True"```
```os.environ["MONGO_URI"] = "YOUR_MONGODB_URI"```
```os.environ["MONGO_DBNAME"]= "DATABASE_NAME" ```
7. Go to app.py file and import the following:
```import os```
```from flask import (Flask, render_template, redirect, request,```
```url_for, session, flash)```
```from flask_pymongo import PyMongo```
```from bson.objectid import ObjectId```
```from werkzeug.security import generate_password_hash, check_password_hash```
```from os import environ, path```
```from dotenv import load_dotenv```
```from pathlib import Path```
8. Create an instance of Flask
```app = Flask(__name__)```
9. To test your application, tell your app how and where to run your application. Set your IP and PORT environment variables in the hidden .env file. Make sure to update this to debug=False before the actual deployment of your project.
```if __name__ == "__main__":````
```app.run(host=os.environ.get("IP"),```
```port=int(os.environ.get("PORT")),```
```debug=True)```
10. You can now run your application, type in the terminal:
```python3 app.py```

### Deploying to Heroku
1. In the workspace terminal, run pip3 freeze --local > requirements.txt to collect any dependencies.
2. Run python app.py > Procfile to create a Procfile required for Heroku deployment.
3. Go to the Heroku website. Register for an account and click on "Create a new app".
4. Setup a Heroku app within the Heroku dashboard - Type in the app name and select region the click on create app.
5. In Heroku, in your app, click on "GitHub" to connect to your repository. Type in the repository name as on GitHub. Click on "Connect".
6. Search for your repo (or sign in and connect GitHub account) and select this.
7. In the 'settings tab, click 'Reveal Config Vars' and input your environment variable from your local build in the key/value inputs.
8. Then click "Hide Config Vars" in Heroku.
9. In Heroku, select 'Automatic Deploys' to automatically rebuild the app when a new Git commit is pushed.
10. Once the initial build is complete, click 'Open App' in the top right of the screen to view the application.

## Credits
### Content and Media
- The Hero image came from Avonne Stalling on [Pexels](https://www.pexels.com/photo/brown-and-gray-mountains-near-body-of-water-under-white-cloudy-sky-4538764/) 
- All other images on the site are taken by me
- The text on the site was written by me, using local knowledge for the routes

### Code
- [Stack Overflow](https://stackoverflow.com/questions/53500221/css-hero-image-height-issue) to fix bug with hero image not displaying properly
- [Bootstrap](https://getbootstrap.com/) adapted code for forms, navigation, buttons, cards

## Acknowledgements
- To my mentor, Richard Wells for supporting me in completing this project.
- To my partner for assistance in testing.