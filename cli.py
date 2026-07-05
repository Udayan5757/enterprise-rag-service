import sys

from src.core.container import container


def main():

    if len(sys.argv) < 2:

        print("Usage: python cli.py ingest")

        return

    command = sys.argv[1]

    if command == "ingest":

        container.warmup()
        container.get_ingestion_service().ingest()

        print("Ingestion Completed.")

    else:

        print("Unknown command.")


if __name__ == "__main__":

    main()
