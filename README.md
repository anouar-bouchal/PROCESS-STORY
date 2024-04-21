# STORY OF A PROCESS

This repository contains event log data in CSV format and a Python script for processing the data.

## Contents

- **data**: CSV files of event logs.
- **src**: Contains `discover.py` script.
- **output**: Directory for generated Directly-Follows Graph (DFG) images.

## Usage

1. Event logs as CSV files are in the `data` directory.
1. The `discover.py` script located in the `src` directory is used to discover the dfgs from the data.
1. The script generates a Directly-Follows Graph (DFG) based on the provided event logs.
1. The resulting DFG image will be saved in the `output` directory (there is an example of the hard coded path).

## Desired Contribution : Story of the Process

1. To generate a story of the process or answer questions about it:
1. Use RAG-llms or any other tool to analyze the generated DFG image(s) or the dictionary holding information about the discovered DFG.
1. Utilize the insights from the DFG to narrate the process or provide answers.