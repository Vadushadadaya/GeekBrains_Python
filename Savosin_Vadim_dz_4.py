def thesaurus_adv(*args):
    for i in args:
        letters = []
        for j in i:
            if j.isupper():
                letters.append(j)
        main_dictionary.setdefault(letters[1], {})
        main_dictionary[letters[1]].setdefault(letters[0], [])
        main_dictionary[letters[1]][letters[0]].append(i)
    sorted_tuple = sorted(main_dictionary.items())
    sorted_dictionary=dict(sorted_tuple)
    print(sorted_dictionary)


main_dictionary = {}
        
thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
