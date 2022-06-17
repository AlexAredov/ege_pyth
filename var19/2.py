for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if ((not(z) and not(x == y)) <= (x and not(w))) == 0:
                    print(x, y, z, w)