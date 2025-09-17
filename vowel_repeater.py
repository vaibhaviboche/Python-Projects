def repeat_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    result = ''

    for ch in s:
        if ch in vowels:
            count += 1
            result += ch + ch.lower() * (count - 1)
        else:
            result += ch

    return result
print(repeat_vowels("hello world"))
# "helloo wooorld"

print(repeat_vowels("freeCodeCamp"))
# "freeeCooodeeeeCaaaaamp"

print(repeat_vowels("AEIOU"))
# "AEeIiiOoooUuuuu"

print(repeat_vowels("I like eating ice cream in Iceland"))
# "I liikeee eeeeaaaaatiiiiiing iiiiiiiceeeeeeee creeeeeeeeeaaaaaaaaaam iiiiiiiiiiin Iiiiiiiiiiiiceeeeeeeeeeeeelaaaaaaaaaaaaaand"
