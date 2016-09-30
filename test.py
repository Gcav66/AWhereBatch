# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 07:42:59 2016

@author: gus
"""
import pandas as pd
import numpy as np
import csv
from make_call import create_and_make_call
from return_results import return_single_result_basic, return_results_file, return_results_detail

#Small run - two locations
#success = create_and_make_call("..\\Sofia_Data\\4 Countries\\to_run\\BF_2010_anonymized_problem.csv", 2000, 2011, 396)
#single = return_single_result_basic('60685', 'old')

#Large Run - Entire File
"""
success = create_and_make_call("..\\Sofia_Data\\4 Countries\\to_run\\BF_2010_anonymized.csv", 2000, 2011, 396)
success = create_and_make_call("..\\Sofia_Data\\4 Countries\\to_run\\BF_2003_anonymized.csv", 1993, 2004, 396)
success = create_and_make_call("..\\Sofia_Data\\4 Countries\\to_run\\BF_1999_anonymized.csv", 1989, 2000, 396)
success = create_and_make_call("..\\Sofia_Data\\4 Countries\\to_run\\BF_1993_anonymized.csv", 1983, 1994, 396)
success = create_and_make_call("..\\Sofia_Data\\4 Countries\\to_run\\BG_2011_anonymized.csv", 2001, 2012, 396)
success = create_and_make_call("..\\Sofia_Data\\4 Countries\\to_run\\BG_2007_anonymized.csv", 1997, 2008, 396)
success = create_and_make_call("..\\Sofia_Data\\4 Countries\\to_run\\BG_2004_anonymized.csv", 1994, 2005, 396)
success = create_and_make_call("..\\Sofia_Data\\4 Countries\\to_run\\BG_1999_anonymized.csv", 1989, 2000, 396)
success = create_and_make_call("..\\Sofia_Data\\4 Countries\\to_run\\ET_2010_anonymized.csv", 2000, 2011, 396)
success = create_and_make_call("..\\Sofia_Data\\4 Countries\\to_run\\ET_2005_anonymized.csv", 1995, 2006, 396)
success = create_and_make_call("..\\Sofia_Data\\4 Countries\\to_run\\ET_2000_anonymized.csv", 1990, 2001, 396)
success = create_and_make_call("..\\Sofia_Data\\4 Countries\\to_run\\NG_2008_anonymized.csv", 1998, 2009, 396)
success = create_and_make_call("..\\Sofia_Data\\4 Countries\\to_run\\NG_2003_anonymized.csv", 1993, 2004, 396)
success = create_and_make_call("..\\Sofia_Data\\4 Countries\\to_run\\NG_1990_anonymized.csv", 1980, 1991, 396)
success = create_and_make_call("..\\Sofia_Data\\4 Countries\\to_run\\NG_2013_anonymized.csv", 2003, 2014, 396)
"""

#out_data = return_results_file("C:\\Users\\gus\\workspace\\awhere\\Sofia_Data\\4 Countries\\to_run\\BF_2010_anonymized.csv_out.csv", "BF_2010_out_results_old_v2.csv")
"""
out_data = return_results_detail("C:\\Users\\gus\\workspace\\awhere\\Sofia_Data\\4 Countries\\to_run\\BF_2010_anonymized.csv_out.csv", "BF_2010_out_results_old_v2.csv")

out_data = return_results_detail("C:\\Users\\gus\\workspace\\awhere\\Sofia_Data\\4 Countries\\to_run\\BF_2003_anonymized.csv_out.csv", "BF_2003_out_results_old_v2.csv")
out_data = return_results_detail("C:\\Users\\gus\\workspace\\awhere\\Sofia_Data\\4 Countries\\to_run\\BF_1999_anonymized.csv_out.csv", "BF_1999_out_results_old_v2.csv")
out_data = return_results_detail("C:\\Users\\gus\\workspace\\awhere\\Sofia_Data\\4 Countries\\to_run\\BF_1993_anonymized.csv_out.csv", "BF_1993_out_results_old_v2.csv")
out_data = return_results_detail("C:\\Users\\gus\\workspace\\awhere\\Sofia_Data\\4 Countries\\to_run\\BG_2011_anonymized.csv_out.csv", "BG_2011_out_results_old_v2.csv")

out_data = return_results_detail("C:\\Users\\gus\\workspace\\awhere\\Sofia_Data\\4 Countries\\to_run\\BG_2007_anonymized.csv_out.csv", "BG_2007_out_results_old_v2.csv")

out_data = return_results_detail("C:\\Users\\gus\\workspace\\awhere\\Sofia_Data\\4 Countries\\to_run\\BG_2004_anonymized.csv_out.csv", "BG_2004_out_results_old_v2.csv")
out_data = return_results_detail("C:\\Users\\gus\\workspace\\awhere\\Sofia_Data\\4 Countries\\to_run\\BG_1999_anonymized.csv_out.csv", "BG_1999_out_results_old_v2.csv")
out_data = return_results_detail("C:\\Users\\gus\\workspace\\awhere\\Sofia_Data\\4 Countries\\to_run\\ET_2010_anonymized.csv_out.csv", "ET_2010_out_results_old_v2.csv")
out_data = return_results_detail("C:\\Users\\gus\\workspace\\awhere\\Sofia_Data\\4 Countries\\to_run\\ET_2005_anonymized.csv_out.csv", "ET_2005_out_results_old_v2.csv")

out_data = return_results_detail("C:\\Users\\gus\\workspace\\awhere\\Sofia_Data\\4 Countries\\to_run\\ET_2000_anonymized.csv_out.csv", "ET_2000_out_results_old_v2.csv")
out_data = return_results_detail("C:\\Users\\gus\\workspace\\awhere\\Sofia_Data\\4 Countries\\to_run\\NG_2008_anonymized.csv_out.csv", "NG_2008_out_results_old_v2.csv")

out_data = return_results_detail("C:\\Users\\gus\\workspace\\awhere\\Sofia_Data\\4 Countries\\to_run\\NG_2003_anonymized.csv_out.csv", "NG_2003_out_results_old_v2.csv")
out_data = return_results_detail("C:\\Users\\gus\\workspace\\awhere\\Sofia_Data\\4 Countries\\to_run\\NG_1990_anonymized.csv_out.csv", "NG_1990_out_results_old_v2.csv")
out_data = return_results_detail("C:\\Users\\gus\\workspace\\awhere\\Sofia_Data\\4 Countries\\to_run\\NG_2013_anonymized.csv_out.csv", "NG_2013_out_results_old_v2.csv")
"""


#Run NG 2013 again
#out_data = return_results_detail("C:\\Users\\gus\\workspace\\awhere\\Sofia_Data\\4 Countries\\to_run\\NG_1990_anonymized.csv_out.csv", "NG_1990_out_results_old_v2.csv")

"""
df = pd.read_csv("details_NG_2013_out_results_old_v2.csv")
df.drop_duplicates(inplace=True)
df_grp = df.groupby('id')

monthly_averages = df_grp.aggregate({"wind_avg":np.mean, "precipitation": np.mean, 
                                  "humid_max":np.mean, "humid_min":np.mean,
                                  "temp_max": np.mean, "temp_min": np.mean})
"""
