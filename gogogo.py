input_from_app = [{"Vegetarian" : 0, "Glutenfrei" : 1, "Hersteller" : 0, "Koscher" : 1},
                  {"Raw": 1, "Tee" : 1, "Eier" : 0, "Kaffee" : 1}]

custom_templ = {'journey':input_from_app, 'is_journey': False, 'requires_journey': True, 'exhibitors': None}
# WORKS - app requires booth path - we return them

input_from_app = [{"Vegetarian" : 0, "Glutenfrei" : 1, "Hersteller" : 0, "Koscher" : 1},
                  {"Raw": 1, "Tee" : 1, "Eier" : 0, "Kaffee" : 1}]

custom_templ = {'journey':input_from_app, 'is_journey': False, 'requires_journey': True, 'exhibitors': None}
# WORKDS - regular response added one item to journey


res = requests.post('https://backend_fairitrail.hopul.net/journey/', json=custom_templ)