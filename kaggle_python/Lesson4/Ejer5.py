def fashionably_late(arrivals, name):
    l=len(arrivals)//2
    return name in arrivals[-l:-1]

party_attendees = ['Laura', 'Fiona', 'Ben', 'May', 'Brenda', 'Luis', 'Carlos']
print(fashionably_late(party_attendees,"Laura"))
print(fashionably_late(party_attendees,"Brenda"))