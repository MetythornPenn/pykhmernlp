import sys
import os
import re

# Add the directory containing your module to the Python path (wants absolute paths)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pykhmernlp.number import to_latin_num, to_khmer_num

def test_khmer_to_latin():
    assert to_latin_num("០") == "0"
    assert to_latin_num("១២៣៤៥៦៧៨៩០") == "1234567890"
    assert to_latin_num("១២៣") == "123"
    assert to_latin_num("៤៥៦") == "456"
    assert to_latin_num("៧៨៩") == "789"
    print("khmer_to_latin tests passed.")

def test_latin_to_khmer():
    assert to_khmer_num("0") == "០"
    assert to_khmer_num("1234567890") == "១២៣៤៥៦៧៨៩០"
    assert to_khmer_num("123") == "១២៣"
    assert to_khmer_num("456") == "៤៥៦"
    assert to_khmer_num("789") == "៧៨៩"
    print("latin_to_khmer tests passed.")

if __name__ == "__main__":
    test_khmer_to_latin()
    test_latin_to_khmer()
