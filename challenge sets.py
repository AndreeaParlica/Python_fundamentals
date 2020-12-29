# rezolvarea 1
vowels = {'a', 'e', 'i', 'o', 'u'}
sentence = "ana are mere dulci si aromate"
sentence_set = set(sentence)
# print(sentence_set)

print(sorted(sentence_set.symmetric_difference(vowels)))
#
# # rezolvarea 2
#
# def vowels_out(str):
#     vowels = {'a', 'e', 'i', 'o', 'u'}
#     return sorted(set(str).symmetric_difference(vowels))
#
# while True:
#     sentence = input("Te rog sa introduci o propozitie: ")
#     print(vowels_out(sentence))

# rezolvarea nr 3 tim

sample_text = "ana are mere dulci si aromate"
vowels = frozenset("aeiou")
final_set = set(sample_text).difference(vowels)
print(final_set)
finalist = sorted(final_set)
print(finalist)