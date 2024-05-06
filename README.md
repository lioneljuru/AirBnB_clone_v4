# AirBnB-clone web-dynamic
we touched on almost everything
nd solved the following tasks:
0. Last clone!
mandatory
A new codebase again? Yes!

For this project you will fork this codebase:

Update the repository name to AirBnB_clone_v4
Update the README.md:
Add yourself as an author of the project
Add new information about your new contribution
Make it better!
If you’re the owner of this codebase, create a new repository called AirBnB_clone_v4 and copy over all files from AirBnB_clone_v3
If you didn’t install Flasgger from the previous project, it’s time! sudo pip3 install flasgger

1. Cash only
Write a script that starts a Flask web application:

Based on web_flask, copy: web_flask/static, web_flask/templates/100-hbnb.html, web_flask/__init__.py and web_flask/100-hbnb.py into the web_dynamic folder
Rename 100-hbnb.py to 0-hbnb.py
Rename 100-hbnb.html to 0-hbnb.html
Update 0-hbnb.py to replace the existing route to /0-hbnb/
If 100-hbnb.html is not present, use 8-hbnb.html instead

2. Select some Amenities to be comfortable!
mandatory
For the moment the filters section is static, let’s make it dynamic!

Replace the route 0-hbnb with 1-hbnb in the file 1-hbnb.py (based on 0-hbnb.py)

Create a new template 1-hbnb.html (based on 0-hbnb.html) and update it:

Import JQuery in the <head> tag
Import the JavaScript static/scripts/1-hbnb.js in the <head> tag
In 1-hbnb.html and the following HTML files, add this variable cache_id as query string to the above <script> tag
Add a <input type="checkbox"> tag to the li tag of each amenity
The new checkbox must be at 10px on the left of the Amenity name
Add to the input tags of each amenity (<li> tag) the attribute data-id=":amenity_id" => this will allow us to retrieve the Amenity ID from the DOM
Add to the input tags of each amenity (<li> tag) the attribute data-name=":amenity_name" => this will allow us to retrieve the Amenity name from the DOM
Write a JavaScript script (static/scripts/1-hbnb.js):

Your script must be executed only when DOM is loaded
You must use JQuery
Listen for changes on each input checkbox tag:
if the checkbox is checked, you must store the Amenity ID in a variable (dictionary or list)
if the checkbox is unchecked, you must remove the Amenity ID from the variable
update the h4 tag inside the div Amenities with the list of Amenities checked



# Authors
* JURU Jean Lionel(lioneljuru@gmail.com)
