import random


def top_k_frequent(numbers, k):
    counter = {}
    freq = [[] for i in range(len(numbers) + 1)]
    print(freq)

    for n in numbers:
        # if n in counter.keys():
        #     counter[n] += 1
        # else:
        #     counter[n] = 1
        counter[n] = counter.get(n, 0) + 1
        print(counter)

    for n, c in counter.items():
        freq[c].append(n)

    print(counter)
    print(freq)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res


def gen_random_list():
    lst = []
    unique_vals = {}
    for i in range(random.randint(1, 50)):
        rand_num = random.randint(0, 9)
        lst.append(rand_num)
        unique_vals[rand_num] = unique_vals.get(rand_num, 0) + 1

    print("Unique values: ", len(unique_vals.keys()))
    print("Random list: ", lst)
    return lst, len(unique_vals.keys())


rand_lst, unique_k = gen_random_list()
rand_k = random.randint(1, unique_k)
print("Number of values to return: ", rand_k)
print(top_k_frequent(rand_lst, rand_k))

