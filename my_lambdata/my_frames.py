

# my_lambdata/my_frames.py

import pandas

def add_state_names(my_df):
    """
    Add a column of state names to a dataframe that already has the abbrevs
    Param my_df pandas.DataFrame should have a column of "abbrev"
    Return a copy of the DataFrame with a new column called "name"
    """
    #names_map = {"CT": "Conn", "CO": "Colorado", "CA": "Cali"}
    names_map = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
    } # http://code.activestate.com/recipes/577305-python-dictionary-of-us-states-and-territories/
    #breakpoint() # python 3.7 or later, otherwise use pdb module
    new_df = my_df.copy()
    new_df["name"] = my_df["abbrev"].map(names_map) # see: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html
    return new_df

df = pandas.DataFrame({"abbrev": ["CT", "CO", "CA", "TX"]})
mutated_df = add_state_names(df) # desired invocation
print(mutated_df.head())

df2 = pandas.DataFrame({"abbrev": ["AZ", "DC", "CO", "MI", "WI"]})
mutated_df2 = add_state_names(df2) # desired invocation
print(mutated_df2.head())
