# -*- coding: utf-8 -*-

from typing import Dict, List
import pandas as pd

from constants import BASE_NAME_NEW_COLUMN, COLUMN_START_WRITE, ROW_START_WRITE


def write_data_in_xlsx(row_start:int = ROW_START_WRITE,
                       column_start:int=COLUMN_START_WRITE,
                       data_frame:pd.DataFrame=None,
                       file_path:str="",
                       sheet_name:str= "",
                       dict_list_value:Dict[int, List[str]]=[]):
    
    if data_frame is None:
        raise Exception("DataFrame is required")
    if file_path == "":
        raise Exception("file_path is required")
    if sheet_name == "":
        raise Exception("sheet_name is required")
    
    for row, list_str in dict_list_value.items():
        # Edit the cell value
      
        for index, item in enumerate(list_str):
            try:
                data_frame.iat[row_start+row, column_start+index] = item
            except:
                data_frame[f'{BASE_NAME_NEW_COLUMN} {index+1}'] = item



    # Save the modified DataFrame back to the same Excel file, on the specified sheet
    with pd.ExcelWriter(file_path, engine='openpyxl', mode='a',if_sheet_exists='overlay') as writer:
        data_frame.to_excel(writer, sheet_name=sheet_name, index=False)
    print("\nFile updated successfully.") 