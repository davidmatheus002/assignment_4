import pandas as pd
import biogeme.database as db
import biogeme.biogeme as bio

df = pd.read_csv('raw/Data.csv', sep=';')
database = db.Database('assignment4', df)
globals().update(database.variables)



# Get the final names of the files
print(f" HTML file : { results.data.htmlFileName }")
print(f" Pickle file : { results.data.pickleFileName }")

# EOF
