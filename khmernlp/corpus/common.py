# -*- coding: utf-8 -*-
# SPDX-FileCopyrightText: 2016-2024 PyThaiNLP Project
# SPDX-License-Identifier: Apache-2.0

"""
Common lists of words.
"""

__all__ = [
    "khmer_words",

]

from typing import FrozenSet, List, Union
import warnings

from khmernlp.corpus import get_corpus


_KHMER_WORDS: FrozenSet[str] = frozenset()
_KHMER_WORDS_FILENAME = "khmer_words.txt"




def khmer_words() -> FrozenSet[str]:
    """
    Return a frozenset of Khmer words such as "កម្ពុជា", "ប្រទេស", "ប្រទេសកម្ពុជា", etc. 

    :return: :class:`frozenset` containing words in the Khmer language.
    :rtype: :class:`frozenset`
    """
    global _KHMER_WORDS
    if not _KHMER_WORDS:
        _KHMER_WORDS = get_corpus(_KHMER_WORDS_FILENAME)

    return _KHMER_WORDS

