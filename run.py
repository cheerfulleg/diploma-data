import sys

from analyzer import Analyzer
from csv_writer import write_to_csv
from scrapper import Scrapper

COLUMNS = ['loc', 'lloc', 'sloc', 'comments', 'multi', 'single_comments', 'blank', 'classes_qnt', 'functions_qnt']

"""   * **loc**: The number of lines of code (total)
        * **lloc**: The number of logical lines of code
        * **sloc**: The number of source lines of code (not necessarily
            corresponding to the LLOC)
        * **comments**: The number of Python comment lines
        * **multi**: The number of lines which represent multi-line strings
        * **single_comments**: The number of lines which are just comments with
            no code
        * **blank**: The number of blank lines (or whitespace-only ones)
"""


def run():
    tag = sys.argv[1]
    filename = sys.argv[2]
    range_to = int(sys.argv[3])
    range_from = int(sys.argv[4])

    scrapper = Scrapper()
    analyzer = Analyzer()
    repos = scrapper.get_list_of_repos(tag=tag, range_from=range_from, range_to=range_to)
    metrics = analyzer.get_metrics(repos)
    write_to_csv(metrics, COLUMNS, filename)


if __name__ == '__main__':
    run()
