Pandas pipeline.
===================
Data processing with the Pandas library.</br>
Get raw CSV file and processing with Pandas.
Used Faker and Pandas.
## Preparation
Random data generated (first and last name)
and saved to a raw CSV file with the default name "input.csv".
Create data:
```shell
 python create_data.py
```
## Run app
```shell
 python main.py
```

## Processing
1. Read this file.
2. Filtered duplicates.
3. Sorted all records by Surname.
4. Filtered out all records with a last name starting with the letter 'S'.
## Save data
After processing, the data is saved to a CSV file with the default name "output.csv".
