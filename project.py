n = 4

clauses = 0

output = ""

# queen ij
for i in range(n):
    # make sure there is one queen per row
    for j in range(n):
        output += str(i + (j * n) + 1) + " "
    output += "0\n"
    clauses += 1

    for j in range(n):
        # do not allow any in the same column
        for i2 in range(n):
            if i2 != i:
                # -ij V -i2j
                output += "-" + str(i + (j * n) + 1) + " -" + str(i2 + (j * n) + 1) + " 0\n"
                clauses += 1

        # do not allow any in the same row
        for j2 in range(n):
            if j2 != j:
                # -ij V -ij2
                output += "-" + str(i + (j * n) + 1) + " -" + str(i + (j2 * n) + 1) + " 0\n"
                clauses += 1

        # do not allow any same diagonal

        # up left
        i2 = i - 1
        j2 = j - 1

        while i2 >= 0 and j2 >= 0:
            # -ij V -i2j2
            output += "-" + str(i + (j * n) + 1) + " -" + str(i2 + (j2 * n) + 1) + " 0\n"
            clauses += 1
            i2 -= 1
            j2 -= 1

        # up right
        i2 = i + 1
        j2 = j - 1

        while i2 < n and j2 >= 0:
            # -ij V -i2j2
            output += "-" + str(i + (j * n) + 1) + " -" + str(i2 + (j2 * n) + 1) + " 0\n"
            clauses += 1
            i2 += 1
            j2 -= 1

        # down left
        i2 = i - 1
        j2 = j + 1

        while i2 >= 0 and j2 < n:
            # -ij V -i2j2
            output += "-" + str(i + (j * n) + 1) + " -" + str(i2 + (j2 * n) + 1) + " 0\n"
            clauses += 1
            i2 -= 1
            j2 += 1

        # down right
        i2 = i + 1
        j2 = j + 1

        while i2 < n and j2 < n:
            # -ij V -i2j2
            output += "-" + str(i + (j * n) + 1) + " -" + str(i2 + (j2 * n) + 1) + " 0\n"
            clauses += 1
            i2 += 1
            j2 += 1

# write all out to file
out = open("out.sat", "w")

out.write("p cnf " + str(n ** 2) + " " + str(clauses) + "\n")
out.write(output)

out.close()