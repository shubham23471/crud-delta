# create dummy data for testing 
import pandas as pd
from deltalake.writer import write_deltalake
import os 


data_path = "./data/"
df = pd.DataFrame({"x": [1, 2, 3]})
# df.to_csv(data_path + 'sample.csv')
write_deltalake(data_path + "table1", df)

