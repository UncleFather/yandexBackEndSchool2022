S, Q = input(), input()
my_len = len(S)
answers = ['absent' for i in range(my_len)]
my_map = {i: 0 for i in S}
for i in range(my_len):
    if Q[i] == S[i]:
        answers[i] = 'correct'
    else:
        my_map[S[i]] += 1
        answers[i] = 'absent'
for i in range(my_len):
    if answers[i] != 'correct':
        try:
            if my_map[Q[i]]:
                my_map[Q[i]] -= 1
                answers[i] = 'present'
        except Exception:
            ss = ''
    print(answers[i])