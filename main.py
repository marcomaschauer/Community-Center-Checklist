from flask import Flask, render_template, request, make_response
import sqlite3
 
# FLASK SETTINGS + INIT
HOST_NAME = "localhost"
HOST_PORT = 80
DBFILE = "./data/community_center_data.db"
app = Flask(__name__)

# GET ALL ITEMS FROM DATABASE 
def getitems():
  conn = sqlite3.connect(DBFILE)
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM `community_center`")
  results = cursor.fetchall()
  conn.close()
  return results

# SHOW ITEMS IN TABLE
@app.route("/")
def index():
  items = getitems()
  # RENDER HTML PAGE
  return render_template("table.html", item = items)
 
# START
if __name__ == "__main__":
  app.run(HOST_NAME, HOST_PORT)
