FavTweets
===

Have you ever wondered which tweets your friends are marking as favorite?
Generate an OPML file with RSS feeds from your friends' favorite tweets,
and then import it into your feed reader! Simple like that.


Setup
---

    git clone git://github.com/tiagofernandez/favtweets.git
    easy_install python-twitter (cf. http://code.google.com/p/python-twitter/issues/detail?id=179)
    easy_install oauth2


Usage
---

    make run user=tiagofernandez


OPML Import
---

Google Reader:

* Settings > Reader settings > Import/export
* Choose file (favtweets/build/favtweets_user.opml)
* Upload


Author
---

Tiago Fernandez (2010) | [Twitter][t]

[t]: http://twitter.com/tiagofernandez