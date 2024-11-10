
result = pd.DataFrame([
    ('Mark', 'Watney', 'botanist', ),
    ('Melissa', 'Lewis', 'commander', ),
    ('Rick', 'Martinez', 'pilot', ),
    ('Alex', 'Vogel', 'chemist', ),
    ('Beth', 'Johanssen', 'engineer', ),
    ('Chris', 'Back', 'medic', ),
], columns=['firstname', 'lastname', 'role'])


#%% Alternative Solution
result = pd.DataFrame({
    'firstname': ['Mark', 'Melissa', 'Rick', 'Alex', 'Beth', 'Chris'],
    'lastname': ['Watney', 'Lewis', 'Martinez', 'Vogel', 'Johanssen', 'Back'],
    'role': ['botanist', 'commander', 'pilot', 'chemist', 'engineer', 'medic'],
})



#%% Alternative Solution
# result = pd.DataFrame([
#     {'Crew': 'Prime', 'Role': 'CDR', 'Astronaut': 'Neil Armstrong'},
#     {'Crew': 'Prime', 'Role': 'LMP', 'Astronaut': 'Buzz Aldrin'},
#     {'Crew': 'Prime', 'Role': 'CMP', 'Astronaut': 'Michael Collins'},
#     {'Crew': 'Backup', 'Role': 'CDR', 'Astronaut': 'James Lovell'},
#     {'Crew': 'Backup', 'Role': 'LMP', 'Astronaut': 'William Anders'},
#     {'Crew': 'Backup', 'Role': 'CMP', 'Astronaut': 'Fred Haise'},
# ])
