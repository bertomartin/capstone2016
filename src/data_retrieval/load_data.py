# converts data to csv, helpers for loading data: df = load_top_100()
# iopro allows you to slice small parts of your data efficiently and then just create pandas data frame
# also use iopro to load from say s3, db, local text into dataframes.
import os
import re
import csv

DELIMITER = "##########"


def convert_to_csv(input_file):
    pattern = re.compile(r'^.*:.+$')

    csv_lines = []
    with open(input_file, 'r') as f:
        lines = []
        for line in f:
            line = line.rstrip()
            if line == DELIMITER:
                if len(lines) > 0:
                    lyrics = "\n".join(lines)
                    csv_line = (singer, title, lyrics)
                    csv_lines.append(csv_line)
                    lines = []
                else:
                    continue # first time
            elif pattern.match(line):
                singer, title = line.split(":")
            else:
                lines.append(line)
        write_to_csv("song_lyrics.csv", csv_lines)


def write_to_csv(file_name, csv_lines):
    with open(file_name, 'w') as f:
        f_csv = csv.writer(f)
        headers = ['singer', 'title', 'lyrics']
        f_csv.writerow(headers)
        f_csv.writerows(csv_lines)


if __name__ == '__main__':
    INPUT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "download_lyrics", "song_lyrics.txt")
    convert_to_csv(INPUT_FILE)