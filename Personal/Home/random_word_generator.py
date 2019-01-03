import random
from itertools import permutations, chain

def generate_random_word():

    base_vowels = ['a', 'e', 'i', 'o', 'u']
    base_consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    selection_range = range(1, 4)
    chain_selection = random.choice(selection_range)

    vowel_conjunctions = []
    consonant_conjunctions = []

    # Generate the random sequence of vowels
    for num in range(1, 3):
        temp_vowel_conjunctions = list(permutations(base_vowels, num))
        temp_vowel_conjunctions = [''.join(vowels) for vowels in temp_vowel_conjunctions]
        vowel_conjunctions.append(temp_vowel_conjunctions)

    vowel_conjunctions = list(chain.from_iterable(vowel_conjunctions))

    # Generate the random sequence of consonants
    for num in range(1, 3):
        temp_consonant_conjunctions = list(permutations(base_consonants, num))
        temp_consonant_conjunctions = [''.join(consonants) for consonants in temp_consonant_conjunctions]
        consonant_conjunctions.append(temp_consonant_conjunctions)

    consonant_conjunctions = list(chain.from_iterable(consonant_conjunctions))

    # vowel_rand_choice = random.choice(vowel_conjunctions)
    # cons_rand_choice = random.choice(consonant_conjunctions)

    random_vowel_pool = []
    random_vowel_pool.append(random.sample(vowel_conjunctions, chain_selection))

    random_consonant_pool = []
    random_consonant_pool.append(random.sample(consonant_conjunctions, chain_selection))

    print(chain_selection)

    # Generate a random sequence of consonants and vowels beginning with a consonant
    random_name_list_consonant_start = []

    for x in random_vowel_pool:
        for y in random_consonant_pool:
            for z in range(0, chain_selection):
                random_name_list_consonant_start.append(y[z] + x[z])

    # Generate a random sequence of consonants and vowels beginning a vowel
    random_name_list_vowel_start = []
    for x in random_vowel_pool:
        for y in random_consonant_pool:
            for z in range(0, chain_selection):
                random_name_list_vowel_start.append(x[z] + y[z])

    # Join the consonant start and vowel start into a single list and then randomly select from the 2
    random_name_consonant_start = [''.join(random_name_list_consonant_start)]
    random_name_vowel_start = [''.join(random_name_list_vowel_start)]
    random_name_full_pool = random_name_consonant_start + random_name_vowel_start

    # Finally create the random word
    random_word = random.choice(random_name_full_pool)

    return random_word

ajax_random_word = generate_random_word()