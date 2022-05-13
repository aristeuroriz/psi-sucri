import sgs

CDI = 12
INCC = 192  #  National Index of Building Costs
df = sgs.dataframe([CDI, INCC], start='02/01/2018', end='31/12/2018')

print(sgs.metadata(df))
print('-----------------------')
print(df.head(20))

# codigos = []

# for x in range(10):
#   CDI_CODE = x + 1
#   results = sgs.search_ts(CDI_CODE, language = "pt")
#   if results:
#       print(results[0])
#       codigos.append([results[0]["code"], results[0]["name"]])
  
# print("----------------------------")
# print(codigos)
# print("----------------------------")