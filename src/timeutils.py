def in_between(now, start, end):
    """To check that the local time is in between start and end of a specific period.

    :argument
    now = datetime.now().time()
    if in_between(now, time(4), time(5)):
        return "Welcome!"
    else:
    """
    if start <= end:
        return start <= now < end
    else:
        return start <= now or now < end
