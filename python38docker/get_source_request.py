# -*- coding: utf-8 -*-

from typing import List
from openpyxl import load_workbook
from image_search import get_dic_response


def get_list_source(data_frame, column_name:str) -> List[str]:
    return data_frame[column_name].tolist()
    

