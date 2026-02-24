def quicksort(arr, key):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = []
    right = []

    for item in arr[1:]:
        if get_value(item, key) <= get_value(pivot, key):
            left.append(item)
        else:
            right.append(item)

    return quicksort(left, key) + [pivot] + quicksort(right, key)


def get_value(movie, key):
    if key == "year":
        try:
            return int(movie.get("Year", 0))
        except:
            return 0
    elif key == "title":
        return movie.get("Title", "").lower()