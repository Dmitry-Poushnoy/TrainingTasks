def format_duration(seconds: int) -> str:
    if seconds == 0:
        return "now"
    periods = (('years', 31536000), ('days', 86400), ('hours', 3600), ('minutes', 60))
    human_duration = {'years': 0, 'days': 0, 'hours': 0, 'minutes': 0, 'seconds': 0}
    for period in periods:
        human_duration[period[0]] = seconds // period[1]
        seconds = seconds % period[1]
    human_duration['seconds'] = seconds
    res = ", ".join(
        [f"{str(_val)} {_key[:-1] if _val == 1 else _key}" for _key, _val in human_duration.items() if _val != 0])
    index_of_last_comma = res.rfind(",")
    if index_of_last_comma != -1:
        res = res[:index_of_last_comma] + ' and' + res[index_of_last_comma + 1:]
    return res


if __name__ == '__main__':
    print(format_duration(3600))
