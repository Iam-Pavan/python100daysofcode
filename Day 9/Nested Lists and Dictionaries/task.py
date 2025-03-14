travel_log = {
    "France": {
        'num_times_visited': 8,
        'cities_visited': ["Paris", "Lille", "Dijon"]
    },
    "Germany": ["Stuttgart", "Berlin"],
}
print(travel_log["France"]['cities_visited'][0])
nested_list = ['a','b',['c','d']]
print(nested_list[2])
tm = {
    5: 8,
    1:2,
    8:8
}
mt = {}
for keys in tm:
    value = tm[keys]
    mt[keys] = value
print(mt)

li = [4,5,6,7,6]
db = []
for va in li:
    db.append(va)
    if va == 6:
        a = db.index(6)
        db[a] = 8
print(db)
