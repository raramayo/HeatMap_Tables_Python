[![alt_text](https://zenodo.org/badge/DOI/10.5281/zenodo.14977228.svg)](https://doi.org/10.5281/zenodo.14977228)
# HeatMap_Tables Mini Tutorial

## How to Use the Script to Generate Heat Map Tables
+ ### Prepare Your Environment:
  + Ensure you have Python 3 installed.
  + Install required libraries if not already available:
    ```
    pip install matplotlib pandas seaborn
    ```
  + Save your data in a TSV file (tab-separated values) with headers.
  + The first column should be used as the index.
  + Example (```Table_00.tsv```):
    ```
    Record_01 <tab> Record_02 <tab> Record03  <tab> Record_04
    Field_01  <tab> 8000000   <tab> 700000    <tab> 50000 <tab> 2000
    Field_02  <tab> 500000	  <tab> 20000     <tab> 2000  <tab> 50
    Field_03  <tab> 50000     <tab> 25000     <tab> 20    <tab> 2
    Field_04  <tab> 2000000   <tab> 200000    <tab> 20000 <tab> 2000
    Field_05  <tab> 4000000   <tab> 400000    <tab> 40000 <tab> 4000
	```
+ ### Understand the Command-Line Options:
  + Title (```-t```/```--title```):
    + Provide a title for your heatmap.
	+ You can insert line breaks using the literal string '\n'.
  + Data (```-d```/```--data```):
    + The path to your TSV file containing numeric data.
  + Format (```-f```/```--format```):
    + Specify the output file format. Default is ```png```. Use pdf if desired.
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

![alt text](https://github.com/raramayo/HeatMap_Tables_Python/blob/main/Images/Table_00_01.png)

+ The script will read your data, generate the heatmap,
    and save it to a file with the same base name as your data
	file but with the appropriate extension (either ```.png``` or ```.pdf```).
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

![alt text](https://github.com/raramayo/HeatMap_Tables_Python/blob/main/Images/Table_00_02.png)

  + The ```smaller``` option is designed to reduce the font size of the resulting
    printed table.
  + This options should be used to indicate the script that the input data contains
    a large number of fields and records.
  + In order to fit more fields and records into the printed table, the script will
	then reduce the font size of the numbers printed into each cell.
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

![alt text](https://github.com/raramayo/HeatMap_Tables_Python/blob/main/Images/Table_00_03.png)

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

![alt text](https://github.com/raramayo/HeatMap_Tables_Python/blob/main/Images/Table_00_04.png)

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

![alt text](https://github.com/raramayo/HeatMap_Tables_Python/blob/main/Images/Table_00_05.png)

  + Does not need any correction, although, the command:
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

![alt text](https://github.com/raramayo/HeatMap_Tables_Python/blob/main/Images/Table_00_06.png)

  + Which, arguably improves the font color representation of the cells' numerical values.

## Repository:

	--------------------------------------------------------------------------------
    https://github.com/raramayo/HeatMap_Tables_Python
	--------------------------------------------------------------------------------

## Issues:

	--------------------------------------------------------------------------------
    https://github.com/raramayo/HeatMap_Tables_Python/issues
	--------------------------------------------------------------------------------
