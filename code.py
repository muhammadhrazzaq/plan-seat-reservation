import collections as c


def seat(n, s):
    d = c.defaultdict(int)
    fam = n * 2
    if " " in s:
        s = s.split(" ")
        for i in s:
            t = i[:-1]
            # print(t)
            if t in d:
                d[t] += [i[-1]]
            else:
                d[t] = [i[-1]]

        for i in d:
            dec = 0
            if ('B' in d[i] or 'C' in d[i] or 'D' in d[i]):
                dec += 1
                fam -= 1

            if ('F' in d[i] or 'G' in d[i] or 'H' in d[i] or 'J' in d[i]):

                dec += 1
                fam -= 1

            if ('D' not in d[i] and 'E' not in d[i] and 'F' not in d[i] and 'G' not in d[i]):
                if dec == 2:
                    fam += 1

        return fam

    else:
        return 2



x = seat(n=2, s="2B 7E 3K")
print(x)
