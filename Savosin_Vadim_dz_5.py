import random
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
def get_jokes(n, f, nouns, adverbs, adjectives):
    joke_list = []
    for i in range(n):
        joke_sample = random.choice(nouns), random.choice(adverbs), random.choice(adjectives)
        joke_list.append(' '.join(joke_sample))
        if f == 'n':
            nouns.remove(joke_sample[0])
            adverbs.remove(joke_sample[1])
            adjectives.remove(joke_sample[2])
    print(joke_list)

get_jokes(int(input('сколько шуток: ')), input('разрешены ли повторы(y/n): ').lower(), nouns, adverbs, adjectives)