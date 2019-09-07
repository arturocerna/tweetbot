import tweepy
import mysql.connector
def setUpAPI():
  """
	Simple function that creates tweepy api object
  """
  CONSUMER_KEY = [ ENTER CONSUMER KEY ]
  CONSUMER_SECRET = [ ENTER SECRET KEY ]

  ACCESS_KEY = [ ENTER ACCESS KEY ]
  ACCESS_SECRET = [ ENTER SECRET KEY ]

  auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
  auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

  api = tweepy.API(auth)
  print('the authorization worked!')
  return api

def retrieveQuote():
  """
      function that retrieves and formats quote from sql server
  """
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="quotes",
    auth_plugin="mysql_native_password"
  )
  mycursor = mydb.cursor()

  sql = "SELECT * FROM inspire WHERE been_used = 0 ORDER BY RAND() LIMIT 1"
  
  # the cursor is the way in which you execute sql code
  mycursor.execute(sql)

  # to get the results of the query, we store it in myresult
  myresult = mycursor.fetchall()

  # this returns a tuple of the first entry of my results, where each entry is a column
  row = myresult[0]
  
  update = "UPDATE inspire SET been_used = 1 WHERE id = " + str(row[0])

  mycursor.execute(update)

  quote = row[2] + "\n\n" + row[1]
  return quote
  
