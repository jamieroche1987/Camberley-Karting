# Testing

## Unit Testing

Automated unit tests have been written and used, they can all be found in the following locations:
 - karting > test_forms.py
 - karting > test_views.py
 - home > test_views.py

 The following command will run the tests: <br>
 `python3 manage.py test`



### TestBookingForm

The following tests have been written for the BookingForm class:
- test_the_form_works: Test the setup and basic functionality of the form.
- test_date_of_booking_is_required: Test that the date of booking is a required field.
- test_date_cannot_be_in_past: Test that the date of booking cannot be in the past.
- test_service_name_is_required: Test that the service name is a required field.
- test_start_time_is_required: Test that the start time is a required field.
- test_start_time_cannot_be_in_the_past: Test that the start time cannot be in the past.
- test_fields_are_explicit_in_form_meta_class: Test that form fields are explicitly defined in the Meta class.


### TestBookingSearchForm

The following tests have been written for the BookingSearchForm class.
- test_return_all_future_bookings: Test returning all future race day bookings.
- test_search_by_username: Test searching bookings by username.
- test_search_by_date: Test searching bookings by date.



### TestBookingsListView

The following tests have been written for the BookingsListView view.
- test_redirect_to_login_if_not_logged_in: Test redirection to login if not logged in.
- test_if_admin_gets_all__future_bookings: Test if admin gets all future race day  bookings.
- test_user_is_shown_their_future_bookings: Test if the user is shown their future race day bookings.



### TestPastBookingsView

The following tests have been written for the PastBookingsView view.
- test_redirect_to_login_if_not_logged_in: Test redirection to login if not logged in.
- test_only_past_bookings_shown: Test only past bookings are shown.


### EmailTest

The following tests have been written for the email functionality.
- test_send_email_confirmation: Test sending email confirmation.



### TestCreateBookingView

The following tests have been written for the CreateBookingView view.
- test_load_booking_form: Test loading the booking form.
- test_user_must_be_logged_in: Test that the user must be logged in.


### TestUpdateBookingView

The following tests have been written for the UpdateBookingView view.
- test_load_booking_form: Test loading the booking form.
- test_user_must_be_booking_owner: Test that the user must be the booking owner.
- test_user_must_be_logged_in: Test that the user must be logged in.



### TestBookingDetailView

The following tests have been written for the BookingDetailView view.
- test_load_booking_detail: Test loading the booking detail.
- test_user_must_be_booking_owner: Test that the user must be the booking owner.
- test_user_must_be_logged_in: Test that the user must be logged in.

### TestBookingDeleteView

The following tests have been written for the BookingDeleteView view.
- test_user_cant_delete_another_users_booking: Test that the user can't delete another user's booking.
- test_user_can_delete_their_own_booking: Test that the user can delete their own booking.
- test_admin_can_delete_bookings: Test that the admin can delete bookings.


### TestConfirmBookingView

The following tests have been written for the ConfirmBookingView view.
- test_admin_can_confirm_booking: Test that the admin can confirm a booking.
- test_users_cant_confirm_bookings: Test that regular users can't confirm bookings.


## Manual Testing

### User Story: Favicon

Description:
- A favicon has been added to the website, and it should appear on every page of the site. This will help users identify the website easily from the browser.

Steps:
- View the tab in different browsers:
    - Chrome
    - Firefox
    - Safari

Expected:
- Favicon is displayed

Actual:
- As expected

### User Story: Deployed site

Description:
- The user can view the deployed site.

Steps:
1. Go to [the deployed site](https://camberleykarting-609b5eae883e.herokuapp.com/)
2. View the site

Expected:
- Site loads without errors

Actual:
- As expected


### User Story: List of Karting packages

Description:
- The user can view a list of all the karting packages offered by the karting company

Steps:
1. Go to the landing page
2. Navigate to the 'Karting Packages' section
3. Click on one of the karting Packages

Expected:
- A list of karting packages is displayed
- Clicking on a service will display a modal with more information including:
    - Service name
    - Cost
    - Link to book a karting package


Actual:
- As expected



### User Story: 403 page

Description:
- A user will see a custom 403 page when they try to access a forbidden page

Steps:
1. A logged-in-user should navigate to a booking that is not theirs

Expected:
- Custom 403 page is displayed

Actual:
- As expected


### User Story: 404 page

Description:
- A user will see a custom 404 page when they try to access a page that is not part of the site

Steps:
1. A user should add some random letter to the end of the url

Expected:
- Custom 404 page is displayed

Actual:
- As expected


### User Story: View past bookings

Description:
- A user can view their past bookings

Steps:
- From the My Account page click on the 'past race days' button
- View all past race day bookings

Expected:
- All past bookings are displayed including:
    - Date
    - Package name
    - Time
    - Message icon (if a message is attached to the booking)
- If more than 25 bookings have been made page pagination will be on display
    - Next >>
    - << Prev

Actual:
- As expected

### User Story: View Past Bookings for Admin User

Description:
- An admin user can view all past bookings

Steps:
1. Go to the My Account page
2. Click 'Past Bookings'
3. View all the past bookings

Expected:
- All bookings are in the past and include:
    - Date
    - Service name
    - Time
    - User
    - Message (if a message is attached to the booking)
- If more than 25 bookings have been made page pagination will be on display
    - Next >>
    - << Prev


### User Story: Navbar

Description:
- A navbar is on display to the user across all pages

Steps:
1. View all pages
2. Check navbar is on display
3. Check links work

Expected:
- Navbar is always on display
- Camberley Karting takes you to the landing page
- About takes you to the about section on the landing page
- Karting Packages takes you to the karting serrvices provided section on the landing page
- Contact takes you to the contact section on the landing page
- Book a Race day takes you to: 
    - the booking form if logged in
    - the login page if not logged in, then the booking form
- Register takes you to the signup page
- Login takes you to the login page
- My account takes logged in users to their account home page
- Logout takes logged in users to the logout page

Actual:
- As expected

### User Story: Footer

Description:
- A footer is on display to the user across all pages

Steps:
1. View all pages
2. Check footer is on display

Expected:
- Footer is always on display
- The links all work:
    - Facebook takes the user to the facebook page in a new window
    - Instagram takes the user to instagram in a new window
    - Github takes the user to the GitHub new window

Actual:
- As expected

### User Story: Create user account

Description:
- A user can sign up by accessing the sign-up form and entering their details.

Steps:
1. Go to the register page
2. Enter the requested details
3. Click Sign Up

Expected: 

- Email should be optional, but if entered a confirmation email should be received by the user
- A username should be unique
- A password should comply with the regulations
- Send to account home upon successful sign-up

Actual:
- As expected, error messages displayed when incorrect or invalid data entered, confirmation email received and redirected to account home.



### User Story: Admin can search by username

Description:
- Admin users can search upcoming bookings by username

Steps:
1. On the account home page in the search bookings section type a username (or part of a username)
2. Click 'search'

Expected:
- The bookings for the user(s) with the entered username will be displayed
- If no bookings are found 'No upcoming bookings' will be displayed

Actual:
- As expected

[Back to Top](#testing)


### User Story: Confirm bookings

Description:
- An admin can confirm a booking for a user

Steps:
1. Click on a booking card with a confirmation status of 'Not yet confirmed' from the admin account home
2. Click 'Confirm Booking'

Expected:
- The admin will be redirected to account home
- A success message will be displayed
- The booking status changes to 'Booking Confirmed'
- A confirmation email will be send to the user (if an email address is associated with the account)

Actual:
- As expected

[Back to Top](#testing)

## Accessibility

[Wave Accessibility](https://wave.webaim.org/) tool was used throughout development and for final testing of the deployed website to check for any aid accessibility testing.

![Wave Testing]()

Testing was focused to ensure the following criteria were met:

- All forms have associated labels or aria-labels so that this is read out on a screen reader to users who tab to form inputs
- Color contrasts meet a minimum ratio as specified in [WCAG 2.1 Contrast Guidelines](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html)
- Heading levels are not missed or skipped to ensure the importance of content is relayed correctly to the end user
- All not textual content had alternative text or titles so descriptions are read out to screen readers
- HTML page lang attribute has been set
- Aria properties have been implemented correctly
- WCAG 2.1 Coding best practices being followed

[Back to Top](#testing)

## Validator Testing

All pages were run through the [w3 HTML Validator](https://validator.w3.org/).

The Django templating language would not allow the files to be pasted into the validator and as some of the pages were restricted due to login or admin access I used the Chrome DevTools to copy the HTML content and paste that into the validator.

![HTML Validator]()

All pages were run through the [Code Institute Pylint](https://pep8ci.herokuapp.com/) validator to ensure all code was pep8 compliant.

![PEP8]()

JavaScript code was run through [JSHINT](https://jshint.com) javascript validator.

![JS validator]()


## Lighthouse Reports
All lighthouse reports for all pages came back with a score of at least , you can see the full reports below.

Landing Page<br>
![Lighthouse Landing Page]()

Account Home<br>
![Lighthouse Account Home]()

Booking Detail<br>
![Lighthouse Booking Detail]()

Booking Form<br>
![Lighthouse Booking Form]()

Logout<br>
![Lighthouse Logout]()

Sign Up<br>
![Lighthouse Sign Up]()

Log In<br>
![Lighthouse Log In]()


## Responsiveness

All pages were tested to ensure responsiveness on screen sizes from 320px and upwards as defined in WCAG 2.1 Reflow criteria for responsive design on Chrome, Firefox and Safari.

Steps to test:

- Open browser and navigate to [Camberley Karting](https://camberleykarting-609b5eae883e.herokuapp.com/)
- Open the developer tools (right click and inspect)
- Set to responsive and decrease width to 320px
- Click and drag the responsive window slowly to maximum width

Expected:

Website is responsive on all screen sizes and no images are pixelated or stretched. No horizontal scroll is present. No elements overlap.

Actual:

Website behaved as expected.

## Browser Compatibility

The following browsers were used to test the site:
- Google Chrome
- Firefox
- Safari
