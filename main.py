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
@app.route("/", methods=['GET', 'POST'])
def index():
  if request.method == 'GET':
    items = getitems()
    return render_template("table.html", item = items)
  else:
    data = request.form.getlist('checkbox')
    for item in data:
      conn = sqlite3.connect(DBFILE)
      cursor = conn.cursor()
      cursor.execute(f"UPDATE `community_center` SET checked = 'true' WHERE name = '{item}'")
      conn.commit()
      conn.close()
      items = getitems()
    return render_template("table.html", item = items)
 
# START
if __name__ == "__main__":
  app.run(HOST_NAME, HOST_PORT)
