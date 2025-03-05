[![alt_text](https://zenodo.org/badge/DOI/10.5281/zenodo.14967827.svg)](https://doi.org/10.5281/zenodo.14967827)
# HeatMap_Tables
![alt text](https://github.com/raramayo/Taxonomy_Fasta_Headers_Python/blob/main/Images/Taxonomy_Fasta_Headers_Logo.png)

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
	v1.0.0
	--------------------------------------------------------------------------------

## Script_Usage:
### Tutorial: How to Use the Script to Generate Heat Map Tables
+ ### Prepare Your Environment:
  + Ensure you have Python 3 installed.
  + Install required libraries if not already available:
    ```
    pip install matplotlib pandas seaborn
    ```
  + Save your data in a TSV file (tab-separated values) with headers.
  + The first column should be used as the index.
  + Example:
    ```
	GRCh38.111 <tab> Gencode.v45
	protein_coding <tab> 20073 <tab> 20073
	lncRNA <tab> 19370 <tab> 19370
	processed_pseudogene <tab> 10145 <tab> 10145
	unprocessed_pseudogene <tab> 2604 <tab> 2604
	misc_RNA <tab> 2217 <tab> 2217
	...
	```
+ ### Understand the Command-Line Options:
  + Title (```-t```/```--title```):
    + Provide a title for your heatmap.
	+ You can insert line breaks using the literal string '\n'.
  + Data (```-d```/```--data```):
    + The path to your TSV file containing numeric data.
  + Format (```-f```/```--format```):
    + Specify the output file format. Default is png. Use pdf if desired.
  + Resolution (```-r```/```--resolution```):
    + For PNG outputs, specify the DPI (dots per inch).
	+ The default is 300 DPI (this is ignored if you choose PDF).
  + Size (```-s```/```--size```):
    + (Optional) Override the auto-detection of font sizes
	  by specifying small or large.
  + Correction (```-c```/```--correction```):
    + Adjust the threshold factor for text color contrast. Default is 2.
	+ Numerical values lower than '1' are acceptable.
  + Palette (```-p```/```--palette```):
    + Choose a color scheme for the heatmap.
	+ Available options include ```Blues``` (default), ```viridis```, ```coolwarm```, and ```YlGnBu```.
	+ The options provided to this flag must be entered in a case-sensitive manner.
  + Version (```-v```/```--version```):
    + Show the script’s version number.
+ ### Run the Script:
  + Open a terminal or command prompt.
  + Navigate to the directory where your script is located.
  + Execute the following command:
    ```
	python3 Heatmap_Tables.py \
	-t "HeatMap Tables\nExample" \
	-d Table_00.tsv \
	-f png \
	-r 300
	```
  + Which will result in the following table:

Table_00_01.png

+ The script will read your data, generate the heatmap,
    and save it to a file with the same base name as your data
	file but with the appropriate extension (either .png or .pdf).
  + Review Your Heatmap:
    + Open the generated file to view your heatmap.
    + The heatmap will have dynamic text color based on the data values,
	  customized titles, and axes labels, making it easier to interpret the data.
+ ### Optimize your Heatmap Table Display:
  + To demonstrate the different ways we can display the data contained in the
    ```Table_01.tsv``` data, let's issue the following commands:
    ```
	python3 Heatmap_Tables.py \
	-t "HeatMap Tables\nExample" \
	-d Table_00.tsv \
	-f png \
	-r 300 \
	-s large
	```
  + Which will result in the following table:

  Table_00_02.png

  + The ```smaller``` option is designed to reduce the font size of the resulting
    printed table.
  + This options should be used to indicate the script that the input data contains
    a large number of fields and records. In order to fit more fields and records
	into the printed table, the script will then reduce the font size of the numbers
	printed into each cell.
  + To use a different palette, you might need to adjust the font color using the
    ```--correction``` flag.
  + For example, in order to use the ```--palette viridis```, we would have to correct
	the cell's numbers font color using the ```--correction``` flag, as follows:
    ```
	python3 Heatmap_Tables.py \
	-t "HeatMap Tables\nExample" \
	-d Table_00.tsv \
	-f png \
	-r 300 \
	-p viridis \
	-c 0.000001
	```
  + Which will result in the following table:

  Table_00_03.png

  + The same consideration would have to be taken into account if we wanted to use
    the ```--palette coolwarm``` flag. In this case, the command:
	```
	python3 Heatmap_Tables.py \
	-t "HeatMap Tables\nExample" \
	-d Table_00.tsv \
	-f png \
	-r 300 \
	-p coolwarm \
	-c 0.000001
	```
	+ Would result in the following table:

	Table_00_04.png

  + In contrast, the command:
    ```
	python3 Heatmap_Tables.py \
	-t "HeatMap Tables\nExample" \
	-d Table_00.tsv \
	-f png \
	-r 300 \
	-p YlGnBu
	```
  + Which results in the following table:

  Table_00_05.png

  + Does not need any correction, althugh, the command:
    ```
	 python3 Heatmap_Tables.py \
	 -t "HeatMap Tables\nExample" \
	 -d Table_00.tsv \
	 -f png \
	 -r 300 \
	 -p YlGnBu \
	 -c 5
	 ```
   + Would result in the following table:

   Table_00_06.png

  + Arguably improves the font color representation of the cells' numerical values.

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
