import csv
import openpyxl

def convert_xlsx_to_tsv(xlsx_path, tsv_path):
    workbook = openpyxl.load_workbook(xlsx_path)
    sheet = workbook.active

    with open(tsv_path, 'w', newline='', encoding='utf-8') as tsv_file:
        writer = csv.writer(tsv_file, delimiter='\t')
        for row in sheet.iter_rows(values_only=True):
            writer.writerow(row)


if __name__ == "__main__":
    convert_xlsx_to_tsv('khmer_dictionary.xlsx', 'khmer_dictionary.tsv')