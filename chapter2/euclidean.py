# 欧氏距离计算
def euclidean(rating1, rating2):
    distance = 0
    for key in rating1:
        if key in rating2:
            distance += abs(rating1[key] - rating2[key])**2
    distance = distance**0.5
    return distance