# -*- coding: utf-8 -*-

from typing import Dict, List
from constants import COLUMN_READ_SOURCE, FILE_PATH, PARAMS, SHEET_NAME
from get_source_request import get_list_source
from image_search import get_url_with
from load_data_frame_xlsx import load_data_frame
import pandas as pd

from write_xlsx_file import write_data_in_xlsx


def main():
    print("Loadind Data Frame File...")
    data_frame:pd.DataFrame = load_data_frame(file_path=FILE_PATH, sheet_name=SHEET_NAME)
    print("Getting List Source...")
    list_source:List[str] = get_list_source(data_frame, column_name=COLUMN_READ_SOURCE)
    print("Getting URLs Images...")
    dict_list_urls:Dict[int, List[str]] = get_url_with(list_source, params=PARAMS)
    print("Writing URLs Images...")
    write_data_in_xlsx(data_frame=data_frame, file_path=FILE_PATH, sheet_name=SHEET_NAME, dict_list_value=dict_list_urls)
    print("All Done !")
if __name__ == "__main__":
    main()