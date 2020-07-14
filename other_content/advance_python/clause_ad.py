


def not_efficient_code(items, divisor):
    for item  in items:
        if item % divisor  == 0:
            break
    else:
        items.append(divisor)


def efficient(items, divisor):
    for item in items:
        if item % divisor == 0:
            return item
    items.append(divisor)
    return items




