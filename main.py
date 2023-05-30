from flask import Flask, render_template, request, make_response
import sqlite3, json
 
# FLASK SETTINGS + INIT
HOST_NAME = "localhost"
HOST_PORT = 80
DBFILE = "./data/community_center_data.db"
app = Flask(__name__)

# GET ALL ITEMS FROM DATABASE 
def getitems(filter = "all"):
  conn = sqlite3.connect(DBFILE)
  cursor = conn.cursor()
  match filter:
    case 'all': cursor.execute("SELECT * FROM `community_center`"),
    case 'checked': cursor.execute("SELECT * FROM `community_center` WHERE checked = 'true' "),
    case 'unchecked': cursor.execute("SELECT * FROM `community_center` WHERE checked = 'false' OR checked = '0' "),
    case 'spring': cursor.execute("SELECT * FROM `community_center` WHERE category = 'spring' "),
    case 'summer': cursor.execute("SELECT * FROM `community_center` WHERE category = 'summer' "),
    case 'fall': cursor.execute("SELECT * FROM `community_center` WHERE category = 'fall' "),
    case 'winter': cursor.execute("SELECT * FROM `community_center` WHERE category = 'winter' "),
    case 'other': cursor.execute("SELECT * FROM `community_center` WHERE category = 'other' "),
    case other: cursor.execute("SELECT * FROM `community_center`")
  results = cursor.fetchall()
  conn.close()
  return results

# DEFAULT ROUTE
@app.route("/", methods=['GET', 'POST'])
def index():
  if request.method == 'GET':
    items = getitems()
    return render_template("table.html", item = items)
  else: #POST
    if request.form.get('filter') != None:
      items = getitems(request.form.get('filter'))
      return render_template("table.html", item = items)
    print(request.form.get('filter'))
    data = request.json
    conn = sqlite3.connect(DBFILE)
    cursor = conn.cursor()
    item_name = data["item_name"]
    if data["item_checked"]:
      cursor.execute(f"UPDATE `community_center` SET checked = 'true' WHERE name = '{item_name}'")
      conn.commit()
    else:
      cursor.execute(f"UPDATE `community_center` SET checked = 'false' WHERE name = '{item_name}'")
      conn.commit()
    conn.close()
    return 'Received !' # response to your request.

# START
if __name__ == "__main__":
  app.run(HOST_NAME, HOST_PORT)
