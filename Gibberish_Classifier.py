# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 13:30:11 2022

@author: sain
"""

from __future__ import division
import re
import math


def split(text, chunk_size):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])
    if len(chunks) > 1 and len(chunks[-1]) < 10:
        chunks[-2] += chunks[-1]
        chunks.pop(-1)
    return chunks


def chunk_per(text, chunk_size):
    chunks = split(text, chunk_size)
    chars_per = []
    for chunk in chunks:
        total = len(chunk)
        unique = len(set(chunk))
        chars_per.append(unique / total)
    return sum(chars_per) / len(chars_per) * 100


def vowels_per(text):
    vowels = 0
    total = 0
    for c in text:
        if not c.isalpha():
            continue
        total += 1
        if c in "aeiouAEIOU":
            vowels += 1
    if total != 0:
        return vowels / total * 100
    else:
        return 0


def word_to_char_ratio(text):
    chars = len(text)
    words = len([x for x in re.split(r"[\W_]", text) if x.strip() != ""])
    return words / chars * 100


def deviation_score(percentage, lower_bound, upper_bound):
    if percentage < lower_bound:
        return math.log(lower_bound - percentage, lower_bound) * 100
    elif percentage > upper_bound:
        return math.log(percentage - upper_bound, 100 - upper_bound) * 100
    else:
        return 0

def Gib_score(text):
    if text is None or len(text) == 0:
        return 0.0
    cp = chunk_per(text, 35)
    vp = vowels_per(text)
    wtcr = word_to_char_ratio(text)

    cp_dev = max(deviation_score(cp, 45, 50), 1)
    vp_dev = max(deviation_score(vp, 35, 45), 1)
    wtcr_dev = max(deviation_score(wtcr, 15, 20), 1)

    return max((math.log10(cp_dev) + math.log10(vp_dev) +
                math.log10(wtcr_dev)) / 6 * 100, 1)

txt = ['abbbb','ram medicals','abhi stores','bhdsbfsjl']

def main():
    Og = []
    for i in txt:
        if Gib_score(i) < 50:
            Og.append(i)
    print(Og)
