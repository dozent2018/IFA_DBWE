# find_overlap findet in einer csv-Datei überlappende Daten

import ics
from pprint import pprint

def same_day(event1 : dict, event2 : dict) -> bool:
    """ Are two events starting on the same day? """
    if (event1['start'].date() == event2['start'].date() or
        event1['start'].date() == event2['end'].date() or
        event1['end'].date() == event2['start'].date() ) :
        return True
    return False

def same_place(event1, event2) -> bool:
    """ Are the two events happening at the same place? """
    if event1['loc_code'] == event2['loc_code'] :
        return True
    return False

def get_place_by_title_col(title_string):
    """ Try to guess place from event title """
    loc_code = 'UNKNOWN'
    for loc_hint in locations.keys():
        if loc_hint in title_string:
            loc_code = locations[loc_hint]
    return loc_code

def get_place_by_desc(place_desc):
    """ Try to guess place from event description """
    loc_code = 'UNKNOWN'
    for loc_hint in locations.keys():
        if loc_hint in place_desc:
            loc_code = locations[loc_hint]
    return loc_code

def get_place_by_place_col(place_col):
    pass


# Global variables
line_no = 0
# place field is not reliable, so use -3, -8 and -9 class name in the "Ereignistitel"
# column to identify locations BE, ZH or SG
locations = { 'BE' : 'BE', 'Bern' : 'BE', 'SG' : 'SG'q, 'St. Gallen' : 'SG', 
               'Zürich' : 'ZH', 'ZH' : 'ZH', 'Altstetten' : 'ZH', 
               '-3' : 'BE', '-8' : 'ZH', '-9' : 'SG'}
event = {}
prev_event = {}
events = []

# estimated travel times in minutes between locations
travel_times = { ('BE', 'ZH' ) : 100,  
                 ('BE', 'SG' ) : 150, 
                 ('ZH', 'BE' ) : 100,
                 ('ZH', 'SG') : 100 ,
                 ('SG', 'BE') : 150 ,
                 ('SG', 'ZH') : 100 }

with open( 'daten.csv', 'r', encoding = 'utf-8-sig' ) as in_file :
    reader_obj = csv.reader(in_file, dialect = 'excel', delimiter = ';')
    for line in reader_obj:
        # create single event dict from each line
        event['start'] = datetime.strptime(line[0] + ' ' + line [1], '%d.%m.%y %H:%M')
        event['end'] = datetime.strptime(line[0] + ' ' + line [2], '%d.%m.%y %H:%M')
        event['title'] = line[3]
        event['loc_code'] = get_place_by_title_col(line[3])
        event['loc_desc'] = line[4]
        event['duration'] = line[5]
        # add event to list. Important to create a new event object with copy()
        events.append(event.copy())


prev_event = {'start' : datetime(1971, 1, 1, 1, 1),
              'end' : datetime(1971, 1, 1, 1, 1),
              'title' : '',
              'loc_code' : '',
              'loc_desc' : '',
              'duration' : 0
}

for event in events :
    # only events which start or end on the same day are checked
    if same_day(event, prev_event) :
        # events may overlap, regardless of place
        latest_start = max(event['start'], prev_event['start'])
        earliest_end = min(event['end'], prev_event['end'])
        delta = (earliest_end - latest_start).total_seconds()
        if delta > 0 :
            print('Überlappung: ', delta/60, ' Minuten')
            print(prev_event['start'], ' - ', prev_event['end'], ' : ', prev_event['title'])
            print(event['start'], ' - ', event['end'], ' : ', event['title'])
            print()
        elif (not same_place(event, prev_event) and event['loc_code'] !='UNKNOWN' 
        and prev_event['loc_code'] != 'UNKNOWN') :
            travel_time = travel_times[ prev_event['loc_code'], event['loc_code'] ]
            start_travel = event['start'] - timedelta(minutes=travel_time)
            delta = (prev_event['end'] - start_travel).total_seconds()
            if delta > 0 :
                print(prev_event['start'], ' - ', prev_event['end'], ' : ', prev_event['title'])
                print(event['start'], ' - ', event['end'], ' : ', event['title'])
                print('Conflict: No way to travel on time !')
                print()
    prev_event = event
