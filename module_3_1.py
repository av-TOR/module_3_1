calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()


def is_contains(string, list_to_search):
    count_calls()
    flag = False
    for i in range(len(list_to_search)):
        if string.upper() == list_to_search[i].upper():
            flag = True
            break
        else:
            flag = False
    return flag



print(string_info("Print"))
print(string_info("String"))
print(is_contains("Den", ["Niff", "Naff", "Den"]))
print(is_contains("Big", ["Moon", "BIG", "Den"]))
print(is_contains("PrInt", ["Start", "print", "Stop"]))
print(is_contains("STR", ["Nina", "Alex", "Tor"]))

print(calls)
