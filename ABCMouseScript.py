import pandas as pd

df = pd.read_csv('ABCm_orders.csv')

df["apt_suite"] = df["apt_suite"].fillna("")

df = df.drop("date", axis = 'columns')

df = df.drop("phone", axis = 'columns')
  
df["sku"] = ""

item_list = []

def edition(row):
    if row['starter pack edition'] == "ABCmouse Starter Pack - Early Elementary Edition":
        row['sku'] = 53781
    elif row['starter pack edition'] == "ABCmouse Starter Pack - School Readiness Edition":
        row['sku'] = 53783
    elif row['starter pack edition'] == "ABCmouse Starter Pack - Both Editions":

        row['sku'] = 53781
        
        new_entry = row.copy()
        new_entry['starter pack edition'] = ""
        new_entry['sku'] = 53783

        item_list.append(new_entry)
        

df.apply(lambda row: edition(row) , axis = 1)


new_df = pd.DataFrame(item_list)


df = pd.concat([df, new_df])

df = df.sort_values(by = ["name"])

df.to_csv("new_ABCm_orders.csv")



