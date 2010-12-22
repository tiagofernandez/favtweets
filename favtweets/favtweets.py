import os, sys, twitter
from string import Template

def main():
  user = sys.argv[1]
  friends_ids = get_friends_ids(user)
  opml = generate_opml(user, friends_ids)
  write_opml_file(opml, user)

def get_friends_ids(user):
  api = twitter.Api(
    consumer_key='qeRmw4vYmKONVpUY078pg',
    consumer_secret='ejHsXwbPvybMgC57g9juL9kXmS5yVC3Lf35rzO1TRs',
    access_token_key='16024857-wOlq0sDBSxkd5d58Fh2LDmLvf7bRNWUqNtRSwlvGP',
    access_token_secret='KGEPCNZZtqV0vBDKZj8DbY6a9RwjOEsTK3oXz3zO4')

  friends = api.GetFriends(user)
  return { f.id : f.name for f in friends }

def generate_opml(user, friends_ids):

  outline_template = '      <outline title="%s" type="rss" xmlUrl="http://twitter.com/favorites/%s.rss"/>'
  outlines = [outline_template % (name, id) for id, name in friends_ids.items()]

  opml_template = Template("""<?xml version="1.0" encoding="UTF-8"?>
  <opml version="1.0">
    <head>
      <title>$user's favorite tweets</title>
    </head>
    <body>
      <outline title="Favorite Tweets">
  $outlines
      </outline>
    </body>
  </opml>""")

  opml = opml_template.substitute({
    'outlines' : '\n'.join(outlines),
    'user' : user})
  
  return opml.encode('utf-8', 'ignore')

def write_opml_file(opml, user):
  outdir = 'build'

  if not os.path.exists(outdir):
    os.makedirs(outdir)

  outfile = open('%s/favtweets_%s.opml' % (outdir, user), 'w')
  outfile.write(opml)
  outfile.close()

#--------------------------
if __name__ == "__main__":
  if len(sys.argv) > 1:
    main()
  else:
    print 'Please provide an username.'