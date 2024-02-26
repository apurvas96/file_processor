#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 23:30:06 2024

@author: apurva
"""
import pandas as pd
from os.path import join




def file_reader(file_list,dat_folder_path) :
    df_list = []

    try :
        for file in file_list :
            try :
                
                with open(join(dat_folder_path,file), 'rb') as in_csv :
                    df = pd.read_csv(in_csv,delimiter='\t')    
                    df_list.append(df)
            except UnicodeDecodeError:
                try :
                    with open(join(dat_folder_path,file), 'rb') as in_csv :
                        df = pd.read_csv(in_csv)    
                        df_list.append(df)
                except Exception as e :
                    print(f"Could not read file {file} because of error: {e}")
            except Exception as e :
                print(f"Could not read file {file} because of error: {e}")
                
        big_df = pd.concat(df_list, ignore_index=True)
        
        big_df = big_df.drop_duplicates()
        return big_df
    except Exception as e :
        print(f"Could not read file {file} because of error: {e}")

def file_writer(csv_folder_path, df):
    try :
        with open(join(csv_folder_path,'results.csv') , 'w') as out_csv :
            df.to_csv(out_csv, index=False)
        print(f'Result stored in {csv_folder_path}')
    
    except Exception as e :
            print(f"Could not write file because of error: {e}")

