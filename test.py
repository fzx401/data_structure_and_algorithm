# # If you need to import additional packages or classes, please import here.
#
# def func(words: str):
#     words = words.strip().split(' ')
#     if len(words) == 0:
#         return 0
#     words = list(''.join(words))
#     vowel_dict = {'a': 'A', 'e': 'E', 'i': 'I', 'o': 'O', 'u': 'U'}
#     for i in range(len(words)):
#         if words[i] in ('a', 'e', 'i', 'o', 'u'):
#             words[i] = vowel_dict[words[i]]
#
#     for i in range(len(words)):
#         for j in range(len(words[i])):
#             if words[i][j] in ('a', 'e', 'i', 'o', 'u'):
#                 words[i] = words[i][:j] + vowel_dict[words[i][j]]
#     return ' '.join(words)
#
#
# words = input().strip()
# print(func(words))
# # please define the python3 input here. For example: a,b = map(int, input().strip().split())
# # please finish the function body here.
# # please define the python3 output here. For example: print().
#
# if __name__ == "__main__":
#     func()
def vowel_to_upper(string: str) -> str:
    string = string.strip()
    dic = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(string)):
        if string[i] in dic:
            x = string[:i]
            y = string[i]
            z = string[i+1:]
            string = string[:i] + string[i].upper() + string[i+1:]
    return string

words = 'Who Love Solo'
print(vowel_to_upper(words))