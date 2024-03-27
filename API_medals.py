from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

with open ("./medal.json") as f:
    medal_json = json.load(f)

def medal_contains(medal_id, color, year, medal_json):
    medals = medal_json.values()
    results = []

    for medal_list in medals:
        for medal in medal_list:
            if medal_id != 0 and str(medal.get("medal_id")) != str(medal_id):
                continue
            if color and color.lower() not in medal.get("color", "").lower():
                continue
            if year != 0 and str(medal.get("year")) != str(year):
                continue
            results.append(medal)

    return results

@app.route('/medal')
@app.route('/medal/id/<medal_id>')
@app.route('/medal/color/<medal_color>')
@app.route('/medal/year/<year>')
def medal(medal_id=0, medal_color="", year=0):
    result = medal_contains(medal_id, medal_color, year, medal_json)
    return result
   
if __name__== "__main__":
    app.run(port=5002)
