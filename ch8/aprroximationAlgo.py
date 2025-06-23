states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])
#why we use set
arr = [1, 2, 2, 3, 3, 3]
print(set(arr)) #{1, 2, 3} => no duplicate element
#create hash table (each station covers states)
stations = {
    "kone":set(["id", "nv", "ut"]),
    "ktwo" : set(["wa", "id", "mt"]),
    "kthree" : set(["or", "nv", "ca"]),
    "kfour" : set(["nv", "ut"]),
    "kfive" : set(["ca", "az"])
}
# 最後決定要合作的電台清單
final_stations = set()
#station_for_states => 該電台覆蓋的州
while states_needed:
    best_station = None
    states_covered = set()
    for station, station_for_states in stations.items():
        # intersections 交集 (由此電台覆蓋且還沒被其他電台覆蓋的州組合起來的集合)
        covered = states_needed & station_for_states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    final_stations.add(best_station)
    states_needed-= states_covered # set difference
print(final_stations)