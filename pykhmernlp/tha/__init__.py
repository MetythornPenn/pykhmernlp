
import tha.normalize
import tha.phone_numbers
import tha.urls
import tha.datetime
import tha.hashtags
import tha.ascii_lines
import tha.license_plate
import tha.cardinals
import tha.decimals
import tha.ordinals
import tha.currency
import tha.parenthesis
import tha.repeater

def normalize(text):
    return tha.normalize.processor(text)

def process_phone_numbers(text, chunk_size=2):
    return tha.phone_numbers.processor(text, chunk_size=chunk_size)

def process_urls(text):
    return tha.urls.processor(text)

def process_time(text):
    return tha.datetime.time_processor(text)

def process_date(text):
    return tha.datetime.date_processor(text)

def process_hashtags(text):
    return tha.hashtags.processor(text)

def process_ascii_lines(text):
    return tha.ascii_lines.processor(text)

def process_license_plate(text):
    return tha.license_plate.processor(text)

def process_cardinals(text):
    return tha.cardinals.processor(text)

def process_decimals(text):
    return tha.decimals.processor(text)

def process_ordinals(text):
    return tha.ordinals.processor(text)

def process_currency(text):
    return tha.currency.processor(text)

def process_parenthesis(text):
    return tha.parenthesis.processor(text)

def process_repeater(text, tokenizer):
    return tha.repeater.processor(text, tokenizer=tokenizer)
