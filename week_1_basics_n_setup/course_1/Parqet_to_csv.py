import pandas as pd
# need pyarrow
parquet = pd.read_parquet("yellow_tripdata_2021-01.parquet")
parquet.to_csv("yellow_tripdata_2021-01.csv")
