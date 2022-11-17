import argparse

from analyzer import Analyzer
from csv_writer import write_to_csv
from scrapper import Scrapper

COLUMNS = ['loc', 'lloc', 'sloc', 'comments', 'multi', 'single_comments', 'blank', 'classes_qnt', 'functions_qnt']


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--tag', help='GitHub Topics Tag')
    parser.add_argument('--file', default='result.csv', help='Results filename')
    parser.add_argument('--start', default=1, help='Start page')
    parser.add_argument('--end', default=2, help='End page')
    return parser.parse_args()


def run():
    args = get_args()

    scrapper = Scrapper()
    analyzer = Analyzer()
    repos = scrapper.get_list_of_repos(tag=args.tag, range_from=int(args.start), range_to=int(args.end))
    metrics = analyzer.get_metrics(repos)
    write_to_csv(metrics, COLUMNS, args.filename)


if __name__ == '__main__':
    run()
