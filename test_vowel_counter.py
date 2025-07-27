# test_vowel_counter.py

import pytest
from vowel_counter import count_vowels

def test_all_vowels():
    """Тест: строка содержит только гласные (латинские и русские)."""
    s = "aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ"
    assert count_vowels(s) == len(s)

def test_no_vowels():
    """Тест: строка не содержит ни одной гласной."""
    s = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ1234567890!@#"
    assert count_vowels(s) == 0

def test_mixed_string():
    """Тест: строка со смешанными символами, включая гласные и согласные, цифры и знаки."""
    s = "Hello, мир! 123 AEiou Юля"
    # e, o, i, A, E, i, o, u, Ю, я = 10 гласных
    assert count_vowels(s) == 10

def test_empty_string():
    """Тест: пустая строка."""
    assert count_vowels("") == 0

def test_only_consonants():
    """Тест: строка состоит только из согласных (русских)."""
    s = "бцкнгшщзхжЧЛРТ"
    assert count_vowels(s) == 0
