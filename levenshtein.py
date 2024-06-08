def levenshtein(s1, s2):
    n, m = len(s1), len(s2)
    if n > m:
        m, n = n, m
        s1, s2 = s2, s1

    curr_row = range(n + 1)
    for i in range(1, m + 1):
        prev_row, curr_row = curr_row, [i] + [0] * n
        for j in range(1, n + 1):
            inser = prev_row[j] + 1
            delet = curr_row[j - 1] + 1
            subs = prev_row[j - 1] + (s1[j - 1] != s2[i - 1])
            curr_row[j] = min(inser, delet, subs)
    
    return curr_row[n]