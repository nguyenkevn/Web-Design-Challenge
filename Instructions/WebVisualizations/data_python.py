import pandas as pd
#Import CSV into Pandas
data = pd.read_csv("Resources/cities.csv")

#Save to html source: https://stackoverflow.com/questions/14897833/save-pandas-to-html-as-a-file
data.to_html("data.html", index=False)
