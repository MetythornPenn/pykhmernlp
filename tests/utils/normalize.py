import sys
import os
import re

# Add the directory containing your module to the Python path (wants absolute paths)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

from pykhmernlp import (
    remove_duplicate_spaces, 
    remove_zero_width_characters
)

def test_remove_duplicate_spaces():
    assert remove_duplicate_spaces('ក    គ    ថ') == 'ក គ ថ'
    assert remove_duplicate_spaces('  ក   គ    ថ  ') == 'ក គ ថ'
    assert remove_duplicate_spaces('ក\n\n\nគ\n\nថ') == 'ក\nគ\nថ'
    assert remove_duplicate_spaces('ក\n   \nគ\n\n   ថ') == 'ក\nគ\nថ'
    print("remove_duplicate_spaces tests passed.")

def test_remove_zero_width_characters():
    assert remove_zero_width_characters('ក\u200bគ\u200cថ') == 'កគថ'
    assert remove_zero_width_characters('ក\u200b\u200bគ\u200c\u200cថ') == 'កគថ'
    assert remove_zero_width_characters('កគថ') == 'កគថ'  # No zero-width characters
    print("remove_zero_width_characters tests passed.")

if __name__ == "__main__":
    test_remove_duplicate_spaces()
    test_remove_zero_width_characters()
