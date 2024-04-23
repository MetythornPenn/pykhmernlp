"""
Trie data structure.

Designed to be used for tokenizer's dictionary, but can be for other purposes.
"""
from typing import Iterable, Iterator, List, Union, FrozenSet

# from typing import FrozenSet, List, Union
import warnings
import re
from collections import defaultdict

from _utils import (
    apply_postprocessors,
    rejoin_formatted_num,
    strip_whitespace,
)



_KHMER_WORDS: FrozenSet[str] = frozenset()
_KHMER_WORDS_FILENAME = "khmer_words.txt"



def get_corpus(path: str, comments: bool = True) -> frozenset:
    path = path.strip()
    lines = []
    with open(path, "r", encoding="utf-8-sig") as fh:
        lines = fh.read().splitlines()

    if not comments:
        # if the line has a '#' character, take only text before the first '#'
        lines = [line.split("#", 1)[0].strip() for line in lines]

    return frozenset(filter(None, lines))

def khmer_words() -> FrozenSet[str]:
    """

    :return: :class:`frozenset` containing words in the Khmer language.
    :rtype: :class:`frozenset`
    """
    global _KHMER_WORDS
    if not _KHMER_WORDS:
        _KHMER_WORDS = get_corpus(_KHMER_WORDS_FILENAME)

    return _KHMER_WORDS



class Trie(Iterable[str]):
    class Node:
        __slots__ = "end", "children"

        def __init__(self):
            self.end = False
            self.children = {}

    def __init__(self, words: Iterable[str]):
        self.words = set(words)
        self.root = Trie.Node()

        for word in words:
            self.add(word)

    def add(self, word: str) -> None:
        """
        Add a word to the trie.
        Spaces in front of and following the word will be removed.

        :param str text: a word
        """
        word = word.strip()
        self.words.add(word)
        cur = self.root
        for ch in word:
            child = cur.children.get(ch)
            if not child:
                child = Trie.Node()
                cur.children[ch] = child
            cur = child
        cur.end = True

    def remove(self, word: str) -> None:
        """
        Remove a word from the trie.
        If the word is not found, do nothing.

        :param str text: a word
        """
        # remove from set first
        if word not in self.words:
            return
        self.words.remove(word)
        # then remove from nodes
        parent = self.root
        data = []  # track path to leaf
        for ch in word:
            child = parent.children[ch]
            data.append((parent, child, ch))
            parent = child
        # remove the last one
        child.end = False
        # prune up the tree
        for parent, child, ch in reversed(data):
            if child.end or child.children:
                break
            del parent.children[ch]  # remove from parent dict

    def prefixes(self, text: str) -> List[str]:
        """
        List all possible words from first sequence of characters in a word.

        :param str text: a word
        :return: a list of possible words
        :rtype: List[str]
        """
        res = []
        cur = self.root
        for i, ch in enumerate(text):
            node = cur.children.get(ch)
            if not node:
                break
            if node.end:
                res.append(text[: i + 1])
            cur = node
        return res

    def __contains__(self, key: str) -> bool:
        return key in self.words

    def __iter__(self) -> Iterator[str]:
        yield from self.words

    def __len__(self) -> int:
        return len(self.words)



def dict_trie(dict_source: Union[str, Iterable[str], Trie]) -> Trie:
    """
    Create a dictionary trie from a file or an iterable.

    :param str|Iterable[str]|pythainlp.util.Trie dict_source: a path to
        dictionary file or a list of words or a pythainlp.util.Trie object
    :return: a trie object
    :rtype: pythainlp.util.Trie
    """
    trie = Trie([])

    if isinstance(dict_source, str) and len(dict_source) > 0:
        # dict_source is a path to dictionary text file
        with open(dict_source, "r", encoding="utf8") as f:
            _vocabs = f.read().splitlines()
            trie = Trie(_vocabs)
    elif isinstance(dict_source, Iterable) and not isinstance(
        dict_source, str
    ):
        # Note: Since Trie and str are both Iterable,
        # so the Iterable check should be here, at the very end,
        # because it has less specificality
        trie = Trie(dict_source)
    else:
        raise TypeError(
            "Type of dict_source must be pythainlp.util.Trie, "
            "or Iterable[str], or non-empty str (path to source file)"
        )

    return trie




"""
Multi cut -- Thai word segmentation with maximum matching.
Original codes from Korakot Chaovavanich.

"""

DEFAULT_WORD_DICT_TRIE = Trie(khmer_words())
# DEFAULT_WORD_DICT_TRIE = Trie("./khmer_words.txt")

_RE_NONKHMER = r"""(?x)
[-a-zA-Z]+|       # Latin characters
\d+([,\.]\d+)*|   # numbers
[ \t]+|           # spaces
\r?\n             # newlines
"""
_PAT_NONKHMER = re.compile(_RE_NONKHMER)



class LatticeString(str):
    """String that keeps possible tokenizations"""

    def __new__(cls, value, multi=None, in_dict=True):
        return str.__new__(cls, value)

    def __init__(self, value, multi=None, in_dict=True):
        self.unique = True
        if multi:
            self.multi = list(multi)
            if len(self.multi) > 1:
                self.unique = False
        else:
            self.multi = [value]
        self.in_dict = in_dict  # if in dictionary




def _multicut(
    text: str, custom_dict: Trie = DEFAULT_WORD_DICT_TRIE
) -> Iterator[LatticeString]:
    """Return LatticeString"""
    if not custom_dict:
        custom_dict = DEFAULT_WORD_DICT_TRIE

    len_text = len(text)
    words_at = defaultdict(list)  # main data structure

    def serialize(p, p2):  # helper function
        for w in words_at[p]:
            p_ = p + len(w)
            if p_ == p2:
                yield w
            elif p_ < p2:
                for path in serialize(p_, p2):
                    yield w + "/" + path

    q = {0}
    last_p = 0  # last position for yield
    while min(q) < len_text:
        p = min(q)
        q -= {p}  # q.pop, but for set

        for w in custom_dict.prefixes(text[p:]):
            words_at[p].append(w)
            q.add(p + len(w))

        len_q = len(q)

        if len_q == 1:
            q0 = min(q)
            yield LatticeString(text[last_p:q0], serialize(last_p, q0))
            last_p = q0
        elif len_q == 0:  # len(q) == 0  means not found in dictionary
            m = _PAT_NONKHMER.match(text[p:])
            if m:  # non-Thai token
                i = p + m.span()[1]
            else:  # non-Thai token, find minimum skip
                for i in range(p, len_text):
                    ww = custom_dict.prefixes(text[i:])
                    m = _PAT_NONKHMER.match(text[i:])
                    if ww or m:
                        break
                else:
                    i = len_text
            w = text[p:i]
            words_at[p].append(w)
            yield LatticeString(w, in_dict=False)
            last_p = i
            q.add(i)


def mmcut(text: str) -> List[str]:
    res = []
    for w in _multicut(text):
        mm = min(w.multi, key=lambda x: x.count("/"))
        res.extend(mm.split("/"))
    return res


def _combine(ww: List[LatticeString]) -> Iterator[str]:
    if ww == []:
        yield ""
    else:
        w = ww[0]
        for tail in _combine(ww[1:]):
            if w.unique:
                yield w + "|" + tail
            else:
                for m in w.multi:
                    yield m.replace("/", "|") + "|" + tail


def segment(
    text: str, custom_dict: Trie = DEFAULT_WORD_DICT_TRIE
) -> List[str]:
    """Dictionary-based maximum matching word segmentation.

    :param text: text to be tokenized
    :type text: str
    :param custom_dict: tokenization dictionary,\
        defaults to DEFAULT_WORD_DICT_TRIE
    :type custom_dict: Trie, optional
    :return: list of segmented tokens
    :rtype: List[str]
    """
    if not text or not isinstance(text, str):
        return []

    return list(_multicut(text, custom_dict=custom_dict))


def find_all_segment(
    text: str, custom_dict: Trie = DEFAULT_WORD_DICT_TRIE
) -> List[str]:
    """Get all possible segment variations.

    :param text: input string to be tokenized
    :type text: str
    :param custom_dict: tokenization dictionary,\
        defaults to DEFAULT_WORD_DICT_TRIE
    :type custom_dict: Trie, optional
    :return: list of segment variations
    :rtype: List[str]
    """
    if not text or not isinstance(text, str):
        return []

    ww = list(_multicut(text, custom_dict=custom_dict))

    return list(_combine(ww))




"""
Generic functions of tokenizers
"""


DEFAULT_WORD_TOKENIZE_ENGINE = "multi_cut"



# from khmernlp.util.trie import Trie, dict_trie


def word_tokenize(
    text: str,
    custom_dict: Trie = Trie([]),
    engine: str = DEFAULT_WORD_TOKENIZE_ENGINE,
    keep_whitespace: bool = True,
    join_broken_num: bool = True,
) -> List[str]:

    if not text or not isinstance(text, str):
        return []

    segments = []


    if engine in ("mm", "multi_cut"):
        # from pythainlp.tokenize.multi_cut import segment
        # import segment
        segments = segment(text, custom_dict)


    else:
        raise ValueError(
            f"""Tokenizer \"{engine}\" not found.
            It might be a typo; if not, please consult our document."""
        )

    postprocessors = []
    if join_broken_num:
        postprocessors.append(rejoin_formatted_num)

    if not keep_whitespace:
        postprocessors.append(strip_whitespace)

    segments = apply_postprocessors(segments, postprocessors)

    return segments


class Tokenizer:


    def __init__(
        self,
        custom_dict: Union[Trie, Iterable[str], str] = [],
        engine: str = "multi_cut",
        keep_whitespace: bool = True,
        join_broken_num: bool = True,
    ):

        self.__trie_dict = Trie([])
        if custom_dict:
            self.__trie_dict = dict_trie(custom_dict)
        else:
            self.__trie_dict = DEFAULT_WORD_DICT_TRIE
        self.__engine = engine
        if self.__engine not in ["newmm", "mm", "longest", "deepcut", "multi_cut"]:
            raise NotImplementedError(
                """
                The Tokenizer class is not support %s for custom tokenizer
                """
                % self.__engine
            )
        self.__keep_whitespace = keep_whitespace
        self.__join_broken_num = join_broken_num

    def word_tokenize(self, text: str) -> List[str]:
        """
        Main tokenization function.

        :param str text: text to be tokenized
        :return: list of words, tokenized from the text
        :rtype: list[str]
        """
        return word_tokenize(
            text,
            custom_dict=self.__trie_dict,
            engine=self.__engine,
            keep_whitespace=self.__keep_whitespace,
            join_broken_num=self.__join_broken_num,
        )

    def set_tokenize_engine(self, engine: str) -> None:
        """
        Set the tokenizer's engine.

        :param str engine: choose between different options of tokenizer engines
                           (i.e. *newmm*, *mm*, *longest*, *deepcut*)
        """
        self.__engine = engine
