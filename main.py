set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
result = []
for element in set1:
        if element in set2:
            result.append(element)

final = set(result)
print(final)