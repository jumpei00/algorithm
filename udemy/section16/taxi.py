from collections import defaultdict


def generate_taxi_number(max_answer: int, match_number: int):
    cusum = defaultdict(list)
    result = []
    counter = 0

    n = 1
    while True:
        for num in range(1, n):
            exponential = num ** 3 + n ** 3
            cusum[exponential].append((num, n))
            counter += 1

            if len(cusum[exponential]) == match_number:
                result.append((exponential, cusum[exponential]))
                if len(result) == max_answer:
                    print(counter)
                    return result
        n += 1


def taxi_cab_number(max_answer_num: int, match_answer_number: int = 2):
    result = []
    got_answer_count = 0
    answer = 1
    counter = 0

    while got_answer_count < max_answer_num:
        match_answer_count = 0
        memo = defaultdict(list)

        max_param = int(pow(answer, 1.0 / 3)) + 1
        for x in range(1, max_param):
            counter += 1
            for y in range(x + 1, max_param):
                counter += 1
                if x ** 3 + y ** 3 == answer:
                    match_answer_count += 1
                    memo[answer].append((x, y))

        if match_answer_count == match_answer_number:
            result.append((answer, memo[answer]))
            got_answer_count += 1

        answer += 1

    print(counter)
    return result


if __name__ == "__main__":
    import time

    start = time.time()
    print(generate_taxi_number(1, 3))
    print(time.time() - start)

    # start = time.time()
    # print(taxi_cab_number(1, 2))
    # print(time.time() - start)
