# vowel_counter.py

def count_vowels(s: str) -> int:
    """
    Подсчитывает количество гласных в строке.

    Поддерживаются латинские и русские гласные, как в нижнем, так и в верхнем регистре.
    """
    vowels = "aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ"
    return sum(1 for char in s if char in vowels)
