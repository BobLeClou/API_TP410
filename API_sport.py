from flask import Flask, render_template, request, jsonify
import waitress  # pip install waitress : serveur WSGI pour Windows / pour Linux : gunicorn
import json

app = Flask(__name__)

with open ("C:\\Users\\Utilisateur\\Documents\\IUT\\DevCloud\\TP_flask\\sport.json") as f:
    sport_json = json.load(f)

def sport_contains(sport_id, sport_name, sport_category, sport_json):
    sports = sport_json.values()
    results = []

    for sport_list in sports:
        for sport in sport_list:
            if sport_id != 0 and str(sport.get("sport_id")) != str(sport_id):
                continue
            if sport_name and sport_name.lower() not in sport.get("name", "").lower():
                continue 
            if sport_category and sport_category.lower() not in sport.get("category", "").lower():
                continue
            results.append(sport)

    return results

@app.route('/sport')
@app.route('/sport/id/<sport_id>')
@app.route('/sport/name/<sport_name>')
@app.route('/sport/category/<sport_category>')
def sport(sport_id=0, sport_name="", sport_category=""):
    result = sport_contains(sport_id, sport_name, sport_category, sport_json)
    return result

if __name__== "__main__":
    app.run(port=5003)