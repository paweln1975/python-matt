"""
CPD Output Parser and JSON Converter

This module parses Copy-Paste Detection (CPD) output files and converts them to a structured JSON format.
It provides functionality to read large CPD output files efficiently, extract duplication information,
and save the results in a standardized JSON format for further analysis. The output file name and location
is the same a input file but with json extension.

Usage:
    python cpd_parser.py -f path/to/cpd_output.txt [-o path/to/output.json]

Arguments:
    -f, --file Path to the CPD output file (required)

Example:
    python cpd_parser.py -f cpd_results.txt

The output JSON format is structured as follows:
[
    {
        "duplicated_lines": <number_of_lines>,
        "tokens": <number_of_tokens>,
        "files": [
            {
                "name": <file_path>,
                "starting_line": <line_number>
            },
            ...
        ]
    },
    ...
]

The module can handle very large CPD output files by processing them line by line,
making it memory-efficient for large codebases with many duplications.

Classes:
    Duplication: Data class representing a single code duplication instance

Functions:
    execute: main start method
    setup_logger: Configures a basic logger to output to stdout
    get_cpd_file_path: Parses command line arguments to get input/output file paths
    parse_cpd_output: Parses CPD output file line by line to extract duplication information
    save_duplications_to_json: Converts duplications to JSON format and saves to a file

Dependencies:
    - argparse: For command-line argument parsing
    - logging: For logging information and errors
    - json: For JSON serialization
    - os: For file path operations
    - re: For regular expression pattern matching
    - dataclasses: For the Duplication data class
    - typing: For type hints

Author: Pawel Niedziela
Version: 1.0.0
"""

import sys
import argparse
import os
import logging
import re
import json
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Duplication:
    """Class to store information about a code duplication."""
    duplicated_lines: int
    tokens: int
    instances: List[Dict[str, int]]  # List of file paths and starting lines


def setup_logger():
    """
    Configure a basic logger to output to stdout.

    Returns:
        logging.Logger: Configured logger instance
    """
    # Create logger
    logger_local = logging.getLogger('CPD processor')
    logger_local.setLevel(logging.INFO)

    # Create stdout handler
    handler = logging.StreamHandler()

    # Create formatter and add it to the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add handler to logger
    logger_local.addHandler(handler)

    return logger_local

logger = setup_logger()

def get_cpd_file_path():
    """
    Parse command line arguments to get the path to a CPD output file.

    Returns:
        str: Path to the CPD output file

    Raises:
        FileNotFoundError: If the specified file does not exist
    """
    parser = argparse.ArgumentParser(description='Process CPD output file.')
    parser.add_argument('-f', '--file', required=True, help='Path to the CPD output file')

    args = parser.parse_args()
    file_path = args.file

    # Check if the file exists
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The CPD output file does not exist: {file_path}")

    return file_path


def parse_cpd_output(file_path: str) -> List[Duplication]:
    """
    Parse CPD output file line by line to extract duplication information.
    Optimized for huge files to avoid loading the entire file into memory.

    Args:
        file_path (str): Path to the CPD output file

    Returns:
        List[Duplication]: List of parsed duplications
    """


    logger.info("Parsing CPD output file: %s", file_path)

    duplications = []
    current_duplication = None
    instances = []
    lines_count = 0
    tokens_count = 0

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.rstrip('\n')

            # Check for duplication header
            header_match = re.match(r'Found a (\d+) line \((\d+) tokens\) duplication in the following files:', line)
            if header_match:
                # If we were already processing a duplication, save it
                if current_duplication is not None and instances:
                    current_duplication = Duplication(
                        duplicated_lines=lines_count,
                        tokens=tokens_count,
                        instances=instances.copy(),
                    )
                    duplications.append(current_duplication)

                # Start a new duplication
                lines_count = int(header_match.group(1))
                tokens_count = int(header_match.group(2))
                instances = []
                current_duplication = None
                continue

            # Check for instance lines
            instance_match = re.match(r'Starting at line (\d+) of (.*)', line)
            if instance_match:
                instances.append({
                    'file': instance_match.group(2).strip(),
                    'line': int(instance_match.group(1))
                })
                continue

            # Check for separator
            if line.strip() == "=====================================================================":
                # If we were processing a duplication, save it
                if instances:
                    current_duplication = Duplication(
                        duplicated_lines=lines_count,
                        tokens=tokens_count,
                        instances=instances.copy()
                    )
                    duplications.append(current_duplication)
                    instances = []
                continue

    # Don't forget to add the last duplication if there is one
    if instances:
        current_duplication = Duplication(
            duplicated_lines=lines_count,
            tokens=tokens_count,
            instances=instances
        )
        duplications.append(current_duplication)

    logger.info("Found %s duplications in the CPD output", len(duplications))
    return duplications


def save_duplications_to_json(duplications: List[Duplication], output_file_path: str):
    """
    Convert a list of Duplication objects to the specified JSON format and save to a file.

    Args:
        duplications (List[Duplication]): List of parsed duplications
        output_file_path (str): Path to save the JSON output

    Returns:
        None
    """

    logger.info("Converting %s duplications to JSON format", len(duplications))

    # Create the JSON structure
    json_data = []

    for duplication in duplications:
        # Create the files array
        files_array = []
        for instance in duplication.instances:
            files_array.append({
                'name': instance['file'],
                'starting_line': instance['line']
            })

        # Create the duplication object
        duplication_obj = {
            'duplicated_lines': duplication.duplicated_lines,
            'tokens': duplication.tokens,
            'files': files_array
        }

        json_data.append(duplication_obj)

    # Write to the output file
    try:
        with open(output_file_path, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, indent=2)
        logger.info("Successfully saved JSON data to %s", output_file_path)
    except Exception as e:
        logger.error("Failed to save JSON data: %s", e)
        raise

    return output_file_path

def execute():
    try:
        cpd_file_path = get_cpd_file_path()
        logger.info("CPD file found: %s", cpd_file_path)
        # Process the file...
        duplications = parse_cpd_output(cpd_file_path)
        # Save to JSON
        output_file_path = os.path.splitext(cpd_file_path)[0] + ".json"
        logger.info("Saving duplication report into the output file: %s", output_file_path)
        save_duplications_to_json(duplications, output_file_path)
        return 0
    except Exception as e:
        logger.error("Error occurred %s", e)
        return 1

if __name__ == "__main__":
    sys.exit(execute())
