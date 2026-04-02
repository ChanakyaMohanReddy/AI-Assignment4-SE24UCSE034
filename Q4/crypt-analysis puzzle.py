digits = range(10)

for T in digits:
    if T == 0:
        continue
    for W in digits:
        if W == T:
            continue
        for O in digits:
            if O in (T, W):
                continue

            R = (O + O) % 10
            c1 = (O + O) // 10

            if R in (T, W, O):
                continue

            U = (W + W + c1) % 10
            c2 = (W + W + c1) // 10

            if U in (T, W, O, R):
                continue

            if (T + T + c2) % 10 != O:
                continue

            c3 = (T + T + c2) // 10
            F = c3

            if F == 0:
                continue

            if F in (T, W, O, U, R):
                continue

            TWO = 100*T + 10*W + O
            FOUR = 1000*F + 100*O + 10*U + R

            if TWO + TWO == FOUR:
                print("Solution:")
                print("T =", T, "W =", W, "O =", O)
                print("F =", F, "U =", U, "R =", R)
                print(TWO, "+", TWO, "=", FOUR)
                break
        else:
            continue
        break
    else:
        continue
    break
