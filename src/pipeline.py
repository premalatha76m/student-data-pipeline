import json
import os

from reader import read_csv
from cleaner import clean_data
from transformer import transform_data
from logger import setup_logger


CONFIG_FILE = "config/config.json"


def load_config():

    with open(CONFIG_FILE, "r") as file:
        return json.load(file)


def main():

    logger = setup_logger()

    logger.info("Pipeline started")

    try:

        # Load configuration
        config = load_config()

        input_file = config["input_file"]
        output_file = config["output_file"]

        minimum_mark = config["minimum_mark"]
        maximum_mark = config["maximum_mark"]

        logger.info("Configuration loaded")

        # Read data
        df = read_csv(input_file)

        logger.info(
            f"Input records: {len(df)}"
        )

        # Clean data
        df = clean_data(
            df,
            minimum_mark,
            maximum_mark
        )

        logger.info(
            "Data cleaning completed"
        )

        # Transform data
        df = transform_data(df)

        logger.info(
            "Data transformation completed"
        )

        # Create output folder
        output_directory = os.path.dirname(
            output_file
        )

        os.makedirs(
            output_directory,
            exist_ok=True
        )

        # Save output
        df.to_csv(
            output_file,
            index=False
        )

        logger.info(
            f"Output saved: {output_file}"
        )

        print(
            "Data processing completed successfully!"
        )

        print(
            f"Processed records: {len(df)}"
        )

        print(
            f"Output file: {output_file}"
        )

    except Exception as error:

        logger.error(
            f"Pipeline failed: {error}"
        )

        print(
            f"Pipeline failed: {error}"
        )


if __name__ == "__main__":
    main()
