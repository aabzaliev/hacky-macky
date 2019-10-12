from flask import jsonify
import random
import pandas as pd
from ..utils import senseless_print
from flask import request
from ...main import app
from ...core.database import users
import json
from flask import current_app
from ...core.proposer import *
import copy
random.seed(42)
input_from_app = [{"Vegetarian" : 0, "Glutenfrei" : 1, "Hersteller" : 0, "Koscher" : 1},
 {"Raw": 1, "Tee" : 1, "Eier" : 0, "Kaffee" : 1},  {"Raw": 1, "Tee" : 1, "Eier" : 0, "Kaffee" : 1}]

@app.route('/journey/', methods = ['POST'])
def user():
    random.seed(42)
    current_state = request.get_json()
    journey_list = copy.deepcopy(current_state['journey'])

    if current_state['requires_journey']:

        exhibitors_list = get_exhibitor_list(journey_list, current_app.df, current_app.list_of_exhibitors)

        new_state = current_state
        new_state['journey'] = journey_list
        new_state['is_journey'] = True
        new_state['exhibitors'] = exhibitors_list.sample(10, random_state=42).to_json(orient='records')
        return jsonify(new_state)
    else:
        app_out = orchestrate(journey_list, current_app.list_of_exhibitors, current_app.df)
        # TODO: change the orient
        if isinstance(app_out, list):
            # app out contains the dict + new_config
            new_state = current_state #update the state
            new_state['journey'] = app_out
            return jsonify(new_state)

        elif isinstance(app_out, pd.DataFrame):
            new_state = current_state
            new_state['journey'] = journey_list
            new_state['is_journey'] = True
            new_state['exhibitors'] = app_out.sample(10, random_state=42).to_json(orient='records')
            return jsonify(new_state)
        else:
            raise TypeError("The return from orchestrator was wrong!")