def study_schedule(permanence_period, target_time):
    counter = 0

    try:
        for period in permanence_period:
            if period[0] <= target_time <= period[1]:
                counter += 1
    except Exception:
        return None

    return counter


# def study_schedule(permanence_period, target_time):
#     counter = 0

#     if not target_time:
#         return None

#     for period in permanence_period:
#         if (isinstance(period[0], str) or
#                 isinstance(period[1], str) or
#                 period[0] is None or period[1] is None):
#             return None
#         elif period[0] <= target_time <= period[1]:
#             counter += 1

#     return counter
