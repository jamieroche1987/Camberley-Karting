<h1 align=center>Portfolio Project 4</h1>

<h1 align=center>Welcome to Camberley Karting</h1>

## FINAL DESIGN

#

[Here is a link to the final project]()

#

## User Experience

### User Stories


## Overview

The site was created using Django and has full CRUD functionality and an intuitive UI to make the process of booking a Go Karting race event.
The user is notified of any change to their account or booking with an alert box and email notification where necessary.
The user can see their past race day bookings and is notified when the booking has been confirmed by the karting company itself..
The admin users have extra functionality, being able to search race bookings by date and username.

#

### 1. Strategy

<hr>

To create a website with good UI and UX to promote Camberley Karting where potential customers can login, book and update a race day experience. 



- Project Setup
  - Create the initial Django application
  - Set file structure in accordance with Django common practices
  - Define and create the Database Models
  - Link custom CSS & JavaScript as well as Bootstrap
  - Create a base.html file for the other template to use
  - Link Google Fonts for custom fonts
- UX
  - Include a Favicon logo
  - Install Whitenoise to link up the custom styles
  - View a list of services and cost
  - Style the default allauth pages
  - Create a Homepage
  - Include a contact section
  - Include 403, 500 & 404 pages
  - Allow users and admins to view past race day bookings
  - Display alerts and messages to the user
- Navigation
  - Have a Navbar that is the same across all the pages
  - Have a Footer that is the same across all the pages
- CRUD
  - View upcoming race daybookings
  - Book a race day event
  - Delete a race day booking
  - Enhanced Admin CRUD capabilities
  - Update a race day booking
- Authentication
  - Add user emails
  - Create User Account
  - Setup allauth
  - Allow users and admins to login
  - Send the users email notification when their race day bookings are made, updated, deleted or confirmed
- Validation
  - Include validation in the booking form to make sure bookings are valid and the time is not already taken
- Administration
  - Allow admins to search for date of booking and user
  - Allow users to update their account details including email and password
  - Let admins confirm the race day bookings
- Deployment
  - Cloudinary
  - ElephantSQL
  - Heroku
  - Set Debug to False
- Testing
  - Unit Tests
  - Manual Testing
- Documentation
  - Readme


### 2. Scope



**Agile Methodology**

This project was developed using the Agile methodology.<br>
All epics and user stories implementation progress was registered using [GitHub](https://github.com/). As the user stories were accomplished, they were moved in the GitHub Kanban board from **ToDo**, to **In Progress**, **Done** and **Not Implemented** lists.
The board can be viewed [here](https://github.com/users/jamieroche1987/projects/10)

**Simple and Intuitive UX**
<br>


- Create a responsive navigation menu.
- Create a footer with social links.
- Include an arena location and opening times.
- Ensure that the user is visually notified of all changed to their account, eg race day booking confirmations.
- Ensure that the user keeps their orientation throughout their website experience.

**Relevant Content**<br>

- Make sure all the available Race Day services are listed on the site.
- Display the address of the karting arena so users can find it.
- Only allow users to book available time slots.

**Responsiveness**<br>

- Create a responsive website that works on every device and screen size.<br><br>

### 3. Structure

### 4. Skeleton

- Wireframes created with Balsamiq. <br>

* Colours

**Font Selection**

## Existing Features

### **Navbar**

### **Custom 404 Page not found**

### **Custom 500 Internal server error**

### **Custom 403 Forbidden page**

#

## Future Features

#

## Languages Used

<

## Frameworks, Libraries & Programs Used

## Testing and Code validation

## Deployment

Camberley Karting is deployed using Heroku

<details>
<summary>Heroku Deployment steps: </summary>

 1. Ensure all dependencies are listed within the requirements.txt file

 Within the terminal in Gitpod type `pip3 --local freeze > requirements.txt`, and a list with all requirements will be created to be read by Heroku.

 2. Setting up Heroku

- NB Due to security issues connecting github directly to heroku (at the time this project was deployed),
    first you must log into your heroku account via the terminal in gitpod (more info on this further down).

    2.1 Next, navigate to the [Heroku](https://www.heroku.com/) website

    2.2 Login to Heroku

    2.3 Click on `New` (top right) and Create a new app

    2.4 Choose a project name and set your location

    2.5. Navigate to the `Resources` tab

    2.6. In the `Add ons` section, search for Heroku Postgres and select it on the list
  - A pop up will appear, select, 'Hobby Dev' and click `Submit order form`

    2.7.1. Next, You would usually navigate to the `deploy` tab;
  - Click on connect to Github
  - Search for the repository named Camberley Karting
  - And connect heroku to Github.
    2.7.2. But, as mentioned above this is not possible for the time being.
  - So instead, In order to connect gitpod to heroku type:
    - `$ heroku login -i`
    - Then enter your heroku credentials,
    - Now you are logged into heroku in Gitpod
    - Once all code is commited and pushed to Github, simply push code from Gitpod to heroku using the command:
    - Heroku will start the build process, this can be viewed under the `Activity` tab
    - Once the build process has completed, navigate to `Open App`
    - The app should now be ready to view

    2.8. Navigate to the settings tab

    2.9.  Click on Config Vars, and add Cloudinary, Database URL (from Heroku-Postgres) and Secret key

</details>

<details>
<summary>Forking the GitHub Repository </summary>

- By forking the GitHub Repository, you will be able to make a copy of the original repository on your own GitHub account, allowing you to view and/or make changes without affecting the original repository by using the following steps:

  - Log in to your own GitHub and locate the GitHub Repository you wish to fork
  - At the top of the Repository (not top of page), just above the "Settings" button on the menu, locate the "Fork" button.
  - You should now have a copy of the original repository in your GitHub account

- Making a Local Clone

  - Log in to your own GitHub and locate the GitHub Repository
  - Under the repository name, click "Clone or download"
  - To clone the repository using HTTPS, under "Clone with HTTPS", copy the link
  - Open Git Bash
  - Change the current working directory to the location where you want the cloned directory to be made
  - Type git clone, and then paste the URL you copied in Step 3

 $ git clone <https://github.com/jamieroche1987/Camberley-Karting>

Press Enter. Your local clone will be created

</details>


## Credits and references

### Images

-

## Acknowledgements
