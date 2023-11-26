def oxford_comma(items):
    if len(items) ==1:
        return items[0]
    elif len(items) == 2:
        return f"{items[0]} and {items[1]}"
    else:
        seperated_by_comma = ", ".join(items[:-1])
        return f"{seperated_by_comma}, and {items[-1]}"
