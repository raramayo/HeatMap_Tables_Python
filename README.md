[![alt_text](https://zenodo.org/badge/DOI/10.5281/zenodo.14977228.svg)](https://doi.org/10.5281/zenodo.14977228)
# HeatMap_Tables
<p align="center">
<img src="https://github.com/raramayo/HeatMap_Tables_Python/blob/main/Images/Heat_Map_Tables_Logo.png" width="400" height="400" style="display: block; margin: 0 auto">

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
	Author:         Rodolfo Aramayo
    Work_Email:     raramayo@tamu.edu
    Personal_Email: rodolfo@aramayo.org
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
	v1.0.2
	--------------------------------------------------------------------------------

## Script_Logic:

<pre>
--------------------------------------------------------------------------------
See: <a href="https://github.com/raramayo/HeatMap_Tables_Python/blob/main/Docs/Code_Overview.md" target="_blank">Code_Overview.md</a>
--------------------------------------------------------------------------------
</pre>

## Script_Usage:

<pre>
--------------------------------------------------------------------------------
See: <a href="https://github.com/raramayo/HeatMap_Tables_Python/blob/main/Docs/Mini_Tutorial.md" target="_blank">Mini_Tutorial.md</a>
--------------------------------------------------------------------------------
</pre>

## Script_Flags:

	--------------------------------------------------------------------------------
	FLAG:           "-t", "--title"
    REQUIRED:       Yes
    FORMAT:         Alphanumeric String
    DEFAULT:        No default
    HELP:           Title for the heatmap (use '\\n' for new lines)
	----------------------------------------------------------------
	FLAG:           "-d", "--data"
    REQUIRED:       Yes
    FORMAT:         Alphanumeric String
    DEFAULT:        No default
    HELP:           Path to the TSV file containing numeric data with headers
	----------------------------------------------------------------
    FLAG:           "-f", "--format"
    REQUIRED:       No
    FORMAT:         String
	CHOICES:        png, pdf
    DEFAULT:        png
    HELP:           Output file format (default: png)
	----------------------------------------------------------------
    FLAG:           "-r", "--resolution"
    REQUIRED:       No
    FORMAT:         Integer
    DEFAULT:        300
    HELP:           Resolution for PNG output in DPI (default: 300, ignored for PDF)
	--------------------------------------------------------------------------------
    FLAG:           "-s", "--size"
    REQUIRED:       No
	FORMAT:         String
    CHOICES:        small, large
    HELP:           Override preset font sizes (optional)
	---------------------------------------------------------------
    FLAG:           "-c", "--correction"
    REQUIRED:       Yes
	FORMAT:         Float
    DEFAULT:        2
    HELP:           Font color mean correction value (default: 2)
	---------------------------------------------------------------
    FLAG:           "-p", "--palette"
    REQUIRED:       No
	FORMAT:         Alphanumeric String
    CHOICES:        'Blues', 'viridis', 'coolwarm', 'YlGnBu', 'RdYlGn', 'bwr', 'seismic'
	DEFAULT:        'Blues'
    HELP:           Color scheme for the heatmap.
	---------------------------------------------------------------
    FLAG:           "--normalize_rows"
	REQUIRED:       No
	FORMAT:         Alphanumeric String
	ACTION:         "Store_True"
    CHOICES:        "Omitting the flag:  == "False""
                    "Providing the flag: == "True""
	HELP:           Normalize each row independently (min-max scaling)
	---------------------------------------------------------------
    FLAG:           "--normalize_columns"
	REQUIRED:       No
	FORMAT:         Alphanumeric String
	ACTION:         "Store_True"
    CHOICES:        "Omitting the flag:  == "False""
                    "Providing the flag: == "True""
	HELP:           Normalize each column independently (min-max scaling)
	---------------------------------------------------------------
    FLAG:           "--cell_font_size"
	REQUIRED:       No
	FORMAT:         Integer
	DEFAULT:        12
	HELP:           Override cell annotation font size (e.g., 20)
	---------------------------------------------------------------
    FLAG:           "-v", "--version"
    REQUIRED:       No
    ACTION:         version
    FORMAT:         Alphanumeric String
    HELP:           Show program version's number and exit
	--------------------------------------------------------------------------------

## Dependencies:

	--------------------------------------------------------------------------------
    Python3:        Required:
	                https://www.python.org/downloads/
	Matplotlib:     Required:
	                https://matplotlib.org/
				    https://pypi.org/project/matplotlib/
	Pandas:         Required:
	                https://pandas.pydata.org/docs/index.html
					https://pypi.org/project/pandas/
	Seaborn:        Required:
	                https://seaborn.pydata.org/
                    https://pypi.org/project/seaborn/
	--------------------------------------------------------------------------------

## Development/Testing Environment:

	--------------------------------------------------------------------------------
	Distributor ID: Apple, Inc.
	Description:    Apple M1 Max
	Release:        15.3.1
	Codename:       Sequoia

	Script was tested with:
                    | Python Version | matplotlib | pandas | seaborn |
                    |----------------|------------|--------|---------|
                    | 3.8.20         | 3.7.5      | 2.0.3  | 0.13.2  |
                    | 3.9.21         | 3.9.4      | 2.2.3  | 0.13.2  |
                    | 3.10.16        | 3.10.1     | 2.2.3  | 0.13.2  |
                    | 3.11.11        | 3.10.1     | 2.2.3  | 0.13.2  |
                    | 3.12.9         | 3.10.1     | 2.2.3  | 0.13.2  |
                    | 3.13.2         | 3.10.1     | 2.2.3  | 0.13.2  |
	--------------------------------------------------------------------------------

## Repository:

<pre>
--------------------------------------------------------------------------------
See: <a href="https://github.com/raramayo/HeatMap_Tables_Python" target="_blank">HeatMap_Tables_Python</a>
--------------------------------------------------------------------------------
</pre>

## Issues:

<pre>
--------------------------------------------------------------------------------
See: <a href="https://github.com/raramayo/HeatMap_Tables_Python/issues" target="_blank">HeatMap_Tables_Python_Issues</a>
--------------------------------------------------------------------------------
</pre>
