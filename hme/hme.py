from datetime import datetime, timedelta

from test_cases import SAMPLE_INPUT_OUTPUTS


def get_next_n_slots(week_config, current_time, n=10):
    """
    :param week_config: a list of list containing all available slots for each weekday
    :param current_time: python datetime object after when new slots are to be fetched
    :returns: a python list containing datetime string of next n available slots
    """
    next_n_slots = []
    first = True
    new_time = current_time
    slots_allowed = False

    if not any(week_config):
        # if week_config is empty, return empty result
        return next_n_slots

    while n > 0:
        if first:
            # start finding slots from current day of run
            weekday = current_time.weekday()
            first = False
        else:
            # iterate through all weekdays
            weekday = 0

        for days in week_config[weekday:]:
            # checking for all slots of that day
            for each_slot in days:
                # runs as long as we want slots
                if n > 0:
                    if not slots_allowed:
                        # finding first available slot
                        s_hour, s_minute = map(
                            int, each_slot['start_time'].split(":"))
                        start_time_obj = new_time.replace(hour=s_hour, minute=s_minute)
                        if start_time_obj >= current_time:
                            # once we have got first slot, we have to can pick
                            # next slots with doing comparing start_time object
                            # because datetime object comparision is way slower
                            # than a simple boolean check
                            slots_allowed = True

                    if slots_allowed:
                        # formatting slot timings as per output format
                        s_hour, s_minute = map(
                            int, each_slot['start_time'].split(":"))
                        e_hour, e_minute = map(
                            int, each_slot['end_time'].split(":"))
                        slot_dict = {
                            'start_time': str(new_time.replace(hour=s_hour, minute=s_minute)),
                            'end_time': str(new_time.replace(hour=e_hour, minute=e_minute))
                        }
                        next_n_slots.append(slot_dict)
                        n -= 1
                else:
                    # if we have completed n slots, then no need to iterate
                    # further
                    break

            # increasing datetime object for next day
            new_time += timedelta(days=1)

    return next_n_slots

if __name__ == '__main__':
    time_of_run = datetime(2017, 1, 1, 20, 30)  # Sunday
    for ip, expected_output in SAMPLE_INPUT_OUTPUTS:
        output = get_next_n_slots(ip, time_of_run)
        assert output == expected_output
