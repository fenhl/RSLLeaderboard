import argparse
import data_access as dba
import calculate_ratings as cr
import settings


def main(reset):
    if reset:
        dba.delete_databases()
        return

    dba.initialize_databases()
    dba.load_json_races()
    cr.calculate_ratings(settings.current_season)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate Leaderboard')
    parser.add_argument('--reset', action='store_true', help='Reset the database')

    args = parser.parse_args()
    main(args.reset)