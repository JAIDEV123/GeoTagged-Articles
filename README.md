# GeoTagged-Articles
A web application to pin locations on a map and view articles that are relevant to that location. Implemented using Flask and GMaps API.

![Image of GeoTagged](https://github.com/JAIDEV123/GeoTagged-Articles/blob/master/Screenshot.png)

##Installation

```bash
pip3 install --user -r requirements.txt
```

If there are more dependencies, raise an issue.

##Setup

```bash
python3 application.py
```

Now visit `localhost:5000` to view the web application.

##What goes where:

###Application.py

This serves as the api as well as endpoints for the application. The routes `/articles`, `/search`, and `/update` are called by script.js through ajax requests in order to fetch articles, search for a location and update the map respectively.

###Helpers.py

Google News has a provision to send RSS feeds of news which is what helpers.py does. The function lookup returns the top 5 results for a location.

###Script.js

This is the primary piece of code that drives this application. It renders the map in the `$.{...}` function, configures the application and sets up eventlisteners for clicks, drags, zooms, and more. Using ajax requests, it is able to retrieve data for the search bar, tagged locations and more asynchronously.