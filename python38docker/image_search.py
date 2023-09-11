# -*- coding: utf-8 -*-

from itertools import islice
from typing import Any, Dict, List
import requests
from constants import ENDPOINT, HEADER


def clean_string_value(value:str):
    try:
        cleaned_value = value.strip().lower()
    except Exception as e:
        print(f"error to strip  {e}, ignoring ... ")
        return ""
    return cleaned_value

def get_url_with(list_source:List[str], params:Dict[str, Any]) -> Dict[int, List[str]] :
    index = 0
    dict_row = {}

    last_string_parameter = ""
    last_content_url_list_str = []
    
    for value in list_source:
        cleaned_value: str = clean_string_value(value=value)
        if last_string_parameter != cleaned_value and cleaned_value != "": 
            params['q'] = clean_string_value
            last_string_parameter = cleaned_value
            dict_response:Dict = get_dic_response(params=params)
            result_value_list_dict:List = dict_response["value"]
            content_url_list_str = [url_image["contentUrl"] for url_image in result_value_list_dict ]
            content_url_list_str = list(islice(content_url_list_str, 5))
            last_content_url_list_str = content_url_list_str
        dict_row[index] = last_content_url_list_str
        index = index + 1 
        
    return dict_row



# Call the API
def get_dic_response(params:Dict) -> Dict  : 
    try:
        response = requests.get(ENDPOINT, headers=HEADER, params=params)
        response.raise_for_status()
    except Exception as ex:
        raise ex
    
    return response.json()
