import feedparser
import urllib.parse

def lookup(geo):
    """Looks up articles for geo."""

    # check cache for geo
    if geo in lookup.cache:
        return lookup.cache[geo]

    # get feed from Google
    feed = feedparser.parse("http://news.google.com/news?geo={}&output=rss?hl=en-US&gl=US&ceid=US:en".format(urllib.parse.quote(geo, safe="")))

    # cache results
    lookup.cache[geo] = [{"link": item["link"], "title": item["title"]} for item in feed["items"]]

    # return results
    return lookup.cache[geo]

# initialize cache
lookup.cache = {}
