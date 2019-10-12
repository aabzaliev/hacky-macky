import pandas as pd
import json
import ast
import itertools


def input_word(in_text, not_in_text, previous_output, list_of_exhibitors):
    list_of_exhibitors_in = list_of_exhibitors[
        list_of_exhibitors.apply(lambda x: set(x).isdisjoint(set(in_text)) == False)]

    list_of_exhibitors_filtered = list_of_exhibitors_in[
        list_of_exhibitors_in.apply(lambda x: set(x).isdisjoint(set(not_in_text)))]

    if(len(list_of_exhibitors_filtered) == 0):
        return ''

    list_of_terms = list_of_exhibitors_filtered.apply(pd.Series).stack().reset_index(drop=True)

    list_of_terms = list_of_terms.value_counts() / len(list_of_exhibitors_filtered)

    indices_to_return = [i for i in list_of_terms.index if i not in (previous_output + in_text)]

    return list_of_terms[indices_to_return].head(1).index[0]


def get_exhibitor_list(input_from_app, df, list_of_exhibitors):
    in_text = [k for d in input_from_app for k, v in d.items() if v == 1]
    not_in_text = [k for d in input_from_app for k, v in d.items() if v == 0]

    temp1 = list_of_exhibitors.apply(lambda x: set(x).isdisjoint(set(in_text)) == False)

    indices1 = list(set(temp1[temp1].index))
    temp2 = list_of_exhibitors[indices1].apply(lambda x: set(x).isdisjoint(set(not_in_text)))
    indices = set(temp2[temp2].index)

    list_of_exhibitors_filtered = df.loc[indices]

    return list_of_exhibitors_filtered


def orchestrate(input_from_app, list_of_exhibitors, df):
    in_text = [k for d in input_from_app for k, v in d.items() if v == 1]
    not_in_text = [k for d in input_from_app for k, v in d.items() if v == 0]

    current_exhibitor_list = get_exhibitor_list(input_from_app, df, list_of_exhibitors)
    if(len(current_exhibitor_list) <= 10):
        output_exhibitor_list = get_exhibitor_list(input_from_app[:-1], df, list_of_exhibitors)
        return output_exhibitor_list

    res1 = input_word(in_text, not_in_text, [''], list_of_exhibitors)
    res2 = input_word(in_text, not_in_text, [res1], list_of_exhibitors)
    res3 = input_word(in_text, not_in_text, [res1, res2], list_of_exhibitors)
    res4 = input_word(in_text, not_in_text, [res1, res2, res3], list_of_exhibitors)

    if((res1 == '') | (res2 == '') |(res3 == '') |(res4 == '')):
        return current_exhibitor_list

    output_dict = {res1: None, res2: None, res3: None, res4: None}

    output = input_from_app + [output_dict]

    return output

