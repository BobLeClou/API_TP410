from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

with open ("./athlete.json") as f:
    athlete_json = json.load(f)

def athlete_contains(athlete_id, athlete_name, athlete_surname, athlete_json):
    athletes = athlete_json.values()
    results = []

    for athlete_list in athletes:
        for athlete in athlete_list:
            if athlete_id != 0 and str(athlete.get("athlete_id")) != str(athlete_id):
                continue  # Si l'ID est spécifié mais ne correspond pas, passer à l'athlète suivant
            if athlete_name and athlete_name.lower() not in athlete.get("name", "").lower():
                continue  # Si le nom est spécifié mais ne correspond pas, passer à l'athlète suivant
            if athlete_surname and athlete_surname.lower() not in athlete.get("surname", "").lower():
                continue  # Si le nom de famille est spécifié mais ne correspond pas, passer à l'athlète suivant
            results.append(athlete)

    return results

@app.route('/athlete')
@app.route('/athlete/id/<athlete_id>')
@app.route('/athlete/name/<athlete_name>')
@app.route('/athlete/surname/<athlete_surname>')
def athlete(athlete_id=0, athlete_name="", athlete_surname=""):
    result = (athlete_contains(athlete_id, athlete_name, athlete_surname, athlete_json))
    return result

if __name__== "__main__":
    app.run(port=5001)
