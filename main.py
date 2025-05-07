
print("\nEXERCICIO 1")
print("A | B | C | (¬A ⋅ B ⋅ C) + (A ⋅ ¬B ⋅ C) + (A ⋅ B ⋅ ¬C)")
print("--------------------------------------------------------")
for A in range(2):
    for B in range(2):
        for C in range(2):
            out = 0
            if (((not A) and B and C) or (A and (not B) and C) or (A and B and (not C))):
                out += 1
            print(f'{A:>2} | {B:>2} | {C:>2} | {out:>2}')


print("\nEXERCICIO 2")
print("A | B | (¬A ⋅ B) + (A ⋅ ¬B)")
print("----------------------------")
for A in range(2):
    for B in range(2):
        out = 0
        if (((not A) and B) or (A and (not B))):
            out += 1
        print(f'{A:>2} | {B:>2} | {out:>2}')


print("\nEXERCICIO 3")
print("A | B | C | D | ((¬A ⋅ B) + C) ⋅ (¬A + D)")
print("------------------------------------------")
for A in range(2):
    for B in range(2):
        for C in range(2):
            for D in range(2):
                out = 0
                if ((((not A) and B) or C) and ((not A) or D)):
                    out += 1
                print(f'{A:>2} | {B:>2} | {C:>2} | {D:>2} | {out:>2}')

print("\nEXERCICIO 4")
print("A | B | C | D | ((A ⋅ B) + C) ⋅ ¬D")
print("-----------------------------------")
for A in range(2):
    for B in range(2):
        for C in range(2):
            for D in range(2):
                out = 0
                if ((((A and B) or C) and not D)):
                    out += 1
                print(f'{A:>2} | {B:>2} | {C:>2} | {D:>2} | {out:>2}')

print("\nEXERCICIO 5")
print("A | B | C | D | (A + B) ⋅ ¬C ⋅ D")
print("---------------------------------")
for A in range(2):
    for B in range(2):
        for C in range(2):
            for D in range(2):
                out = 0
                if ((A or B) and not C and D):
                    out += 1
                print(f'{A:>2} | {B:>2} | {C:>2} | {D:>2} | {out:>2}')

print("\nEXERCICIO 6")
print("A | B | C | D | ¬A ⋅ B ⋅ ¬C ⋅ D")
print("---------------------------------")
for A in range(2):
    for B in range(2):
        for C in range(2):
            for D in range(2):
                out = 0
                if ((not A) and B and (not C) and D):
                    out += 1
                print(f'{A:>2} | {B:>2} | {C:>2} | {D:>2} | {out:>2}')
