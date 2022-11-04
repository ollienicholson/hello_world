import pandas as pd
# from docx import Documenta
from report_example import focus_area_population_narrative

# doc = Document()
df = pd.read_excel('fapopexample.xlsx')

# df = pd.read_sql()

print(df.head(5))

# Sum up Population Count Column = focus area pop
# Sum Age 0 to 4 Column = childrenpop
# Sum Centre Capacity Column = capacity
# Sum Occupancy Column = Occupancy

# store everything in a variable and above and then pass to a column

# Sum the rows of DataFrame
fapop = df["PopulationCount"].sum()
childrenpop = df["Age0to4"].sum()
capacity = df["CentresCapacity"].sum()
occupancy = df["CentresOccupancy"].sum()

x = focus_area_population_narrative(fapop, childrenpop, capacity, occupancy)


# doc.add_paragraph(x)
# doc.save('output.docx')
