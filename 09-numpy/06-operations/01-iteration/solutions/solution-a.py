
result = []

for value in DATA.ravel():
    if value % 2 == 0:
        result.append(value)


#%% Alternative Solution
# for row in DATA:
#     for value in row:
#         if value % 2 == 0:
#             result.append(value)
