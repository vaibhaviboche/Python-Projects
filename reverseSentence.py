def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)
print(reverse_sentence("world hello")) 
# "hello world"

print(reverse_sentence("push commit git")) 
# "git commit push"

print(reverse_sentence("npm  install  sudo")) 
# "sudo install npm"

print(reverse_sentence("import    default   function  export")) 
# "export function default import"
