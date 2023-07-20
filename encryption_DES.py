# Permutation tables
P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
P8 = [6, 3, 7, 4, 8, 5, 10, 9]

# Left shift tables
LS_1 = [2, 3, 4, 5, 1]
LS_2 = [3, 4, 5, 1, 2]


def apply_permutation(key, permutation_table):
    return [key[i - 1] for i in permutation_table]


def left_shift(key, num_shifts):
    return key[num_shifts:] + key[:num_shifts]


def generate_round_keys(master_key):
    key = apply_permutation(master_key, P10)

    left_half = key[:5]
    right_half = key[5:]

    round_keys = []

    for i in range(2):
        left_half = left_shift(left_half, LS_1[i])
        right_half = left_shift(right_half, LS_1[i])

        round_key = apply_permutation(left_half + right_half, P8)
        round_keys.append(round_key)

    return round_keys


# Example usage
master_key = [1, 0, 0, 1, 1, 1, 0, 0, 0, 0]  # 1001110000

round_keys = generate_round_keys(master_key)

print("Round Keys:")
for i, round_key in enumerate(round_keys):
    print(f"K{i + 1}: {round_key}")
