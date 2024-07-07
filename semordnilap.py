# first iteration
# Let us say
# n - number of words in the "words" list.
# k - length of the longest string in the "words" list
# p - number of semordnilap strings in the "words" list
# O(n^2) time | O(kp) space
# def semordnilap(words):
#     # Write your code here.
#     semordnilap_pairs = []                                              # O(kp) space
#     known_words = []                                                    # O(kp) space
#     for _idx, word in enumerate(words):                                 # O(n) time
#         if word not in known_words:                                     # O(p) time
#             semordnilap_word = word[::-1]                               # O(k) time
#             if semordnilap_word in words[(_idx + 1):]:                  # O(n) + O(n) time
#                 semordnilap_pairs.append([word, semordnilap_word])      # O(1) time
#                 known_words.extend([word, semordnilap_word])            # O(1) time
#     return semordnilap_pairs


# second iteration
# Let us say
# n - number of words in the "words" list.
# k - length of the longest string in the "words" list
# p - number of semordnilap strings in the "words" list
def semordnilap(words):
    _dict = {}
    _lst = []
    for _idx, word in enumerate(words):                                     # O(n) time
        if word not in _dict:                                               # O(1) time
            reverse_word = word[::-1]                                       # O(k) time
            if reverse_word in words[(_idx + 1):]:                          # O(n) + O(n) time
                _dict[reverse_word] = word
                _lst.append([word, reverse_word])
    return _lst


words = ["dog", "hello", "desserts", "test", "god", "stressed"]
semordnilap(words)