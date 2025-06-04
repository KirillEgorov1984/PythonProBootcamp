def calculate_love_score(name_one, name_two):
    combined_names = name_one + name_two
    lower_names = combined_names.lower()

    t = lower_names.count("t")
    print(t)

    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")

    first_digit = t + r + u + e

    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")

    second_digit = l + o + v + e

    score = int(str(first_digit) + str(second_digit))
    print(score)


calculate_love_score(name_one="Kanye West", name_two="Kim Kardashian")