def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    if not target_time:
        return
    count_students = 0
    for e1, e2 in permanence_period:
        if not isinstance(e1, int) or not isinstance(e2, int):
            return
        # if permanence[0] is None or permanence[1] is None:
        #     return
        if int(e1) <= target_time <= int(e2):
            count_students += 1
    return count_students


if __name__ == '__main__':
    permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
    target_time = 2
    result = study_schedule(permanence_period, target_time)
    print(result)
