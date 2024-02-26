#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 23:30:06 2024

@author: apurva
"""
import pandas as pd
import os 
from os.path import isfile,join

from file_reader_writer import file_reader, file_writer

dat_folder_path = './input_files'
csv_folder_path = './output_files'

#Fecth only files from given input directory
try :
    fileNames = [f for f in os.listdir(dat_folder_path) if isfile(join(dat_folder_path,f))]
except FileNotFoundError as e :
    print(f'Path not correct : {e}')
except Exception as e :
        print(f"Error occured : {e}")
        
#Read all input files
final_df = file_reader(fileNames,dat_folder_path)

#Add calculated column gross_salary
final_df['gross_salary'] = final_df['basic_salary'] + final_df['allowances']

#Fetch second highest salary
second_highest_salary = final_df.nlargest(2,['gross_salary']).iloc[1]['gross_salary']

#Calculate average salary
avg_salary = final_df.gross_salary.mean().round(2)

#create summary dataframe to add as a footer
summary =pd.DataFrame({
        'id' : ['Second Highest Salary = ',second_highest_salary],
        'first_name' : ['Average Salary = ', avg_salary]
        })

#concat summary df with main df 
final_df = pd.concat([final_df, summary],sort=False)

#write final result 
file_writer(csv_folder_path, final_df)



