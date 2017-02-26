import itertools as its

def is_power_2(n):
    top_bit_in_common = n & (n - 1)
    return n and not top_bit_in_common

def next_power_2(n):
    bits = n.bit_length()
    top_bit = (n >> bits - 1) << bits - 1
    return n if n == top_bit else top_bit << 1

def max_profit_buy_sell(daily_prices):
    if (not isinstance(daily_prices, (list, tuple)) or
        not isinstance(daily_prices[0], (int, float))):
        raise TypeError("max_subarray takes a {list, tuple} " +
                        "of {int, float}s, but you passed " +
                        "{}".format(daily_prices))
    daily_prices = list(daily_prices)
    for i in range(0, len(daily_prices) - 1):
        daily_prices[i] = daily_prices[i + 1] - daily_prices[i]
    daily_prices.pop()

    deltas = daily_prices
    deltas.extend(its.repeat(-1, next_power_2(len(deltas)) - len(deltas)))
    assert is_power_2(len(deltas)), "Length padding failed"

    def max_crossing_subarray(between):
        def peak_sum(indices):
            running, peak, peak_index = 0, deltas[indices[0]], indices[0]
            for i in indices:
                running += deltas[i]
                if running > peak:
                    peak, peak_index = running, i
            return peak, peak_index

        half_size = len(between) >> 1
        left_sum,  left_index  = peak_sum(between[half_size - 1::-1])
        right_sum, right_index = peak_sum(between[half_size:])
        return left_sum + right_sum, range(left_index, right_index + 1)

    def max_subarray(between):
        if len(between) == 1:
            return deltas[between[0]], between
        half_size = len(between) >> 1
        return max(max_subarray(between[:half_size]),
                   max_subarray(between[half_size:]),
                   max_crossing_subarray(between),
                   key = lambda pair: pair[0])

    max_sum, subarray = max_subarray(range(len(deltas)))
    return {"profit": max_sum, "buy": subarray.start, "sell": subarray.stop}

test_prices = [100, 113, 110, 85, 105, 102, 86, 63,
               81, 101, 94, 106, 101, 79, 94, 90, 97]
