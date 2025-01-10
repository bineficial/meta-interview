"""
datelist = {
    "android": [1,0,1,0,1,0,1],
    "ios": [0,0,0,1,0,1,1],
    "web": [0,0,0,0,0,0,0]
}
metric = {
    "overall": ["ios", "android", "web"],
    "mobile": ["ios", "web"]
}

output = {
    "overall": 6
    "mobile": 3
}
"""

datelist = {
    "android": [1, 0, 1, 0, 1, 0, 1],
    "ios": [0, 0, 0, 1, 0, 1, 1],
    "web": [0, 0, 0, 0, 0, 0, 0],
}
metrics = {"overall": ["ios", "android", "web"], "mobile": ["ios", "web"]}


def get_active_on_date(data, date_i):
    total = 0
    for row in data:
        total += row[date_i]
    return total


def total_active(datelist, metrics):
    data = {}
    for metric, source in metrics.items():
        data[metric] = [datelist[s] for s in source]

    output = {}
    for metric, data_set in data.items():
        for i in range(len(data_set[0])):
            active_count = get_active_on_date(data_set, i)

            if active_count >= 1:
                output[metric] = output.get(metric, 0) + 1

    return output


print(total_active(datelist, metrics))
