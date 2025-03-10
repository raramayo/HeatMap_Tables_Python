[![alt_text](https://zenodo.org/badge/DOI/10.5281/zenodo.14977228.svg)](https://doi.org/10.5281/zenodo.14977228)
# HeatMap_Tables
![alt text](https://github.com/raramayo/HeatMap_Tables_Python/blob/main/Images/Heat_Map_Tables_Logo.png)

## Overview:

    --------------------------------------------------------------------------------
	The script reads a TSV file containing numeric data and generates a heatmap
	visualization.

	It is designed to be flexible by adjusting fonts and figure size based on the
	input data dimensions.

	Key Functions:

        Argument Parsing:
        Uses Python’s argparse to capture the title, data file, output format, resolution,
		optional size settings, and a correction factor for text color thresholds.

        Data Loading and Preprocessing:
        Reads the TSV file with Pandas, filters out unwanted rows (e.g., those with "TOTAL:"),
		converts specific percentage values if necessary, and ensures all selected columns are
		numeric.

        Dynamic Visualization Settings:
        Auto-detects if the data is "large" (more than 50 rows or 6 columns) and adjusts
		font sizes and figure dimensions accordingly.

    Heatmap Generation:
        Uses Seaborn to create the heatmap. Data values are annotated in each cell,
		and text colors are dynamically adjusted based on how the cell’s value compares
		to the overall mean (modified by a correction factor).

	Output:
        Saves the generated heatmap as a PNG (with a configurable DPI) or as a PDF.
    --------------------------------------------------------------------------------

## Motivation

	--------------------------------------------------------------------------------
	The script was developed to display numerical values in a table format while using
	color to visually emphasize the magnitude and variations of those values.
	--------------------------------------------------------------------------------

## Authorship:

    --------------------------------------------------------------------------------
	Author:                          Rodolfo Aramayo
    Work_Email:                      raramayo@tamu.edu
    Personal_Email:                  rodolfo@aramayo.org
    --------------------------------------------------------------------------------

## Copyright:

    --------------------------------------------------------------------------------
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or (at
    your option) any later version.

	This program is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
    General Public License for more details.

	You should have received a copy of the GNU General Public License
    along with this program. If not, see <https://www.gnu.org/licenses/>.
    --------------------------------------------------------------------------------

## Script_Version:

	--------------------------------------------------------------------------------
	v1.0.1
	--------------------------------------------------------------------------------

## Script_Usage:

	--------------------------------------------------------------------------------
	See Mini_Tutorial.md
	--------------------------------------------------------------------------------

## Script_Flags:

	--------------------------------------------------------------------------------
	FLAG:                            "-t", "--title"
    REQUIRED:                        "Yes"
    FORMAT:                          "Alphanumeric String"
    DEFAULT:                         "No default"
    HELP:                            "Title for the heatmap (use '\\n' for new lines)"
	--------------------------------------------------------------------------------
	FLAG:                            "-d", "--data"
    REQUIRED:                        "Yes"
    FORMAT:                          "Alphanumeric String"
    DEFAULT:                         "No default"
    HELP:                            "Path to the TSV file containing numeric data with headers"
	--------------------------------------------------------------------------------
    FLAG:                            "-f", "--format"
    REQUIRED:                        "No"
    FORMAT:                          "String"
	CHOICES:                         "png", "pdf"
    DEFAULT:                         "png"
    HELP:                            "Output file format (default: png)"
	--------------------------------------------------------------------------------
    FLAG:                            "-r", "--resolution"
    REQUIRED:                        "No"
    FORMAT:                          "Integer"
    DEFAULT:                         "300"
    HELP:                            "Resolution for PNG output in DPI (default: 300, ignored for PDF)"
	--------------------------------------------------------------------------------
    FLAG:                            "-s", "--size"
    REQUIRED:                        "No"
	FORMAT:                          "String"
    CHOICES:                         "small, large"
    HELP:                            "Override preset font sizes (optional)"
	--------------------------------------------------------------------------------
    FLAG:                            "-c", "--correction"
    REQUIRED:                        "Yes"
	FORMAT:                          "Float"
    DEFAULT:                         "2"
    HELP:                            "Font color mean correction value (default: 2)"
	--------------------------------------------------------------------------------
    FLAG:                            "-p", "--palette"
    REQUIRED:                        "No"
	FORMAT:                          "Alphanumeric String"
    CHOICES:                         "'Blues', 'viridis', 'coolwarm', 'YlGnBu'"
	DEFAULT:                         "Blues"
    HELP:                            "Color scheme for the heatmap (default: Blues).
	--------------------------------------------------------------------------------
    FLAG:                            "-v", "--version"
    REQUIRED:                        "No"
    ACTION:                          "version"
    FORMAT:                          "Alphanumeric String"
    HELP:                            "Show program version's number and exit"
	--------------------------------------------------------------------------------

## Dependencies:

	--------------------------------------------------------------------------------
    Python3:                         Required (see: https://www.python.org/downloads/)
	Matplotlib:                      Required (see: https://matplotlib.org/)
	Pandas:                          Required (see: https://pandas.pydata.org/)
	Seaborn:                         Required (see: https://seaborn.pydata.org/)
	--------------------------------------------------------------------------------

## Development/Testing Environment:

	--------------------------------------------------------------------------------
    Distributor ID:                  Apple, Inc.
    Description:                     Apple M1 Max
    Release:                         15.3.1
    Codename:                        Sequoia
	--------------------------------------------------------------------------------

## Repository:

	--------------------------------------------------------------------------------
    https://github.com/raramayo/HeatMap_Tables_Python
	--------------------------------------------------------------------------------

## Issues:

	--------------------------------------------------------------------------------
    https://github.com/raramayo/HeatMap_Tables_Python/issues
	--------------------------------------------------------------------------------
