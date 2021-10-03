###3 Distinct item generator
def distinct(iterable):
    """Return unique items by removing duplicate items

    Args:
        iterable: The source series

    Yields:
        Unique elements in order from iterable
    """
    seen = set()
    for item in iterable:
        if item in seen:
            continue #finishes the current iteration of the loop and begins the next iteration immediately
        yield item
        seen.add(item)

def run_distinct():
    items = [5, 7, 7, 6, 5, 5]
    for item in distinct(items): #when the iteration resumes for the next item the distinct function first completes the previous iteration and adds the item in the seen list and then resumes the for loop in that function
        print(item)

if __name__ == '__main__':
    run_distinct()
