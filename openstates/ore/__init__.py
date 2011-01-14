status = dict(
    bills=False,
    bill_versions=False,
    sponsors=False,
    actions=False,
    votes=False,
    legislators=False,
    contributors=['Gabriel J. Perez-Irizarry'],
    notes="Legislator data available for only 2009. Oregon does not hold annual sessions.",
)

metadata = dict(
    name='Oregon',
    abbreviation='or',
    legislature_name='Oregon Legislative Assembly',
    upper_chamber_name='Senate',
    lower_chamber_name='House of Representatives',
    upper_chamber_title='Senator',
    lower_chamber_title='Representative',
    upper_chamber_term=4,
    lower_chamber_term=2,
    terms = [
        {'name': '1995',
         'sessions': ['1995 Regular Session',
                      '1995 Special Session'],
         'start_year': 1995, 'end_year': 1995},
        {'name': '1996 Special Session',
         'sessions': ['1996 Special Session'],
         'start_year': 1996, 'end_year': 1996},
        {'name': '1997',
         'sessions': ['1997 Regular Session'],
         'start_year': 1997, 'end_year': 1997},
        {'name': '1999',
         'sessions': ['1999 Regular Session'],
         'start_year': 1999, 'end_year': 1999},
        {'name': '2001',
         'sessions': ['2001 Regular Session'],
         'start_year': 2001, 'end_year': 2001},
        {'name': '2002 Special Sessions',
         'sessions': ['2002 First Special Session',
                      '2002 Second Special Session'
                      '2002 Third Special Session',
                      '2002 Fourth Special Session',
                      '2002 Fifth Special Session'],
         'start_year': 2002, 'end_year': 2002},
        {'name': '2003',
         'sessions': ['2003 Regular Session'],
         'start_year': 2003, 'end_year': 2003},
        {'name': '2005',
         'sessions': ['2005 Regular Session'],
         'start_year': 2005, 'end_year': 2005},
        {'name': '2007',
         'sessions': ['2007 Regular Session'],
         'start_year': 2007, 'end_year': 2007},
        {'name': '2008 Special Session',
         'sessions': ['2008 Special Session'],
         'start_year': 2008, 'end_year': 2008},
        {'name': '2009',
         'sessions': ['2009 Special Session'],
         'start_year': 2009, 'end_year': 2009},
        {'name': '2010 Special Session',
         'sessions': ['2010 Special Session'],
         'start_year': 2010, 'end_year': 2010},   
         ]                  
)