def build_acronym(phrase):
    ignore = {"a", "an", "and", "by", "for", "of"}
    words = phrase.split()
    acronym = ""

    for i, word in enumerate(words):
        if i == 0 or word.lower() not in ignore:
            acronym += word[0].upper()

    return acronym
print(build_acronym("Search Engine Optimization"))  # "SEO"
print(build_acronym("Frequently Asked Questions"))  # "FAQ"
print(build_acronym("National Aeronautics and Space Administration"))  # "NASA"
print(build_acronym("Federal Bureau of Investigation"))  # "FBI"
print(build_acronym("For your information"))  # "FYI"
print(build_acronym("By the way"))  # "BTW"
print(build_acronym("An unstoppable herd of waddling penguins overtakes the icy mountains and sings happily"))
# "AUHWPOTIMSH"
