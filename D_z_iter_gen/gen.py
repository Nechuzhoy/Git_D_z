nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]

def flat_generator(list):
    for r in (list):
        i = 0
        while i < len(r):
            yield   r[i]
            i += 1


if __name__ == '__main__':

    for item in  flat_generator(nested_list):
        print(item)


