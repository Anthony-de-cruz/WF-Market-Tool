import logging

log = logging.getLogger(__name__)


def setup_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s|%(levelname)s|%(name)s| %(message)s",
        datefmt="%H:%M:%S",
    )


def main() -> None:
    log.info("Starting")

    quit()


if __name__ == "__main__":
    main()
