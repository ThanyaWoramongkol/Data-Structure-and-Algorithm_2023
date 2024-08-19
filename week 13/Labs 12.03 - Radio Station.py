"""Labs 12.03 - Radio Stations"""
from json import loads
def findstations(allplace, num_station, station, used):
    """Use least station to sent all message"""
    for _ in range(num_station):
        station.append(loads(input()))
    while allplace != [] and station != []:
        for sta in station:
            sta.update({"have": 0})
        for check in allplace:
            for num in range(len(station)):
                if check in station[num]["Cities"]:
                    station[num]["have"] += 1
        station = sorted(station, key=lambda x: x["have"], reverse=True)
        if station[0]["have"] != 0:
            for dele in station[0]["Cities"]:
                if dele in allplace:
                    allplace.remove(dele)
            used.append(station[0]["Name"])
        station.pop(0)
    print(sorted(used))
findstations(loads(input()), int(input()), [], [])
