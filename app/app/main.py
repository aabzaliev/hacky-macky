from flask import Flask
import pandas as pd
import json

app = Flask(__name__)
with open('/data/Export_en.json') as json_file:
    df = json.load(json_file)

df = pd.DataFrame(df["Export"]["Exhibitors"])
app.df = df
df['Productgroups_list'] = df['Productgroups'].str.strip(' ').str.replace(" ","").str.split(',')
app.list_of_exhibitors = df['Productgroups_list'].dropna().apply(lambda x : list(set(x)))

from .core import app_setup

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
