## "Wikipedia" Style Website for practice in the Python-Django Framework 

### About the project

This project uses Python by means of the Django framework to set the foundations for the basics of a Wikipedia-style webpage.
The features of this page (as can be seen by downloading and executing the code) can be seen in the following youtube video made by me. Each feaure is 
linked to in the following timestamp. ADter each feature, i have given a justification as to why i decided upon it.
https://www.youtube.com/watch?v=9eJZMsDpwjs&t=4s

Timestamps:
1. Entry page: https://youtu.be/9eJZMsDpwjs?t=3
2. Typing /TITLE brings user to page named TITLE: https://youtu.be/9eJZMsDpwjs?t=10 - _this was an important feature for me as it got me into the habit of being able to link url addresses to specific webpages if they exist.
3. if TITLE in 2 doesnt exist, user sees error message: https://youtu.be/9eJZMsDpwjs - _standard feature of any website, if a user visits a page that doesn't exist, they will be sent to an "error" page, where the user can click on other links so their overall experience on the website is not disrupted._
4. Links on index page and sends user to that page: https://youtu.be/9eJZMsDpwjs?t=20
5. Search: typing in page title into search sends user to that page: https://youtu.be/9eJZMsDpwjs?t=31 -  _this is a crucial feature of any website. An issue i had when attempting this was forgetting that the search program was case-sensitive. Pages that i thought should have been showing in search just weren't, but once i realised that it was actually working, i could disable the case-sensitive aspect accordingly to give a better user experience.
6. Typing substring of search title, gives list of pages that include that substring: https://youtu.be/9eJZMsDpwjs?t=34 - _Another crucial part of a website, searching not only for the whole word title of a given page, but also substrings of that title. This makes the website more user friendly, and realistic._
7. Create new entry page: https://youtu.be/9eJZMsDpwjs?t=60 - _This puts the user in charge of the growth of the website. They can enter a new page entry into various forms and a new page is created, which can then be accessed using "search" above. A problem i had when trying to complete this was being able to convert the newly created page into the Markdown Language format, after only being written in regular type. However, i found that there was a built in django function for this. Given "#" indicates a "heading" in Markdown, i had to write the code such that the title of the page was given both a "#" character as well as a new line afterwards, to distinguish between it and the main body of the page's text. _
8. Trying to create page that already exists gives error message: -_Trying to compsensate for any mistake made on behalf of the user._
https://youtu.be/9eJZMsDpwjs?t=80
9. Edit page and save changes: https://youtu.be/9eJZMsDpwjs?t=107 - _An important feauture, to make the website fully editable and dynamic, just like the regular wikipedia_
10. Random page generator: https://youtu.be/9eJZMsDpwjs?t=114
