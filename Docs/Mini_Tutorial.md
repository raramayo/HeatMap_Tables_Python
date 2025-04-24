[![alt_text](https://zenodo.org/badge/DOI/10.5281/zenodo.14977228.svg)](https://doi.org/10.5281/zenodo.14977228)

# HeatMap_Tables Mini Tutorial

## How to Use the Script to Generate Heat Map Tables:

### Prepare Your Environment:

+ Ensure you have `Python 3` installed.

+ Install required libraries if not already available:

```
pip install matplotlib pandas seaborn
```

+ Save your data in a TSV file (tab-separated values) with headers.

+ The first column should be used as the index.

+ Example (`Table_00.tsv`):

```
Record_01 <tab> Record_02 <tab> Record03  <tab> Record_04
Field_01  <tab> 8000000   <tab> 700000    <tab> 50000 <tab> 2000
Field_02  <tab> 500000	  <tab> 20000     <tab> 2000  <tab> 50
Field_03  <tab> 50000     <tab> 25000     <tab> 20    <tab> 2
Field_04  <tab> 2000000   <tab> 200000    <tab> 20000 <tab> 2000
Field_05  <tab> 4000000   <tab> 400000    <tab> 40000 <tab> 4000
```

### Understand the Command-Line Options:

+ Title (`--title`):

Provide a title for your heatmap.

You can insert line breaks using the literal string '\n'.

+ Data (`--data`):

The path to your TSV file containing numeric data.

+ Format (`--format`):

Specify the output file format. Default is `png`. Use pdf if desired.

+ Resolution (`--resolution`):

For PNG outputs, specify the DPI (dots per inch).

The default is 300 DPI (this is ignored if you choose PDF).

+ Size (`--size`):

(Optional) Override the auto-detection of font sizes.
by specifying small (font size = 8) or large (font size = 12.

+ Correction (`--correction`):

Adjust the threshold factor for text color contrast. Default is 2.

Numerical values lower than '1' are acceptable.

+ Palette (`--palette`):

Choose a color scheme for the heatmap.

Available options include: `Blues` (default),
`viridis`, `coolwarm`, `YlGnBu`, `RdYlGn`, `bwr`, and `seismic`.

The options provided to this flag must be entered in a case-sensitive manner.

+ Normalize Rows (`--normalize_rows`):

Normalize each row independently (min-max scaling).

+ Normalize Columns (`--normalize_columns`):

Normalize each column independently (min-max scaling).

+ Cell Font Size (`--cell_font_size`):

Override cell annotation font size for another size (e.g., 20).

Font Size Default for Large Tables: 8.

Font Size Default for Small Tables: 12.

+ Cell Height (`--cell_height`):

Set the height (in inches) for each cell.

Figure height is computed as (number of rows) x (cell height).

Default: 1.5

+ Version (`-v`/`--version`):

Show the script’s version number.

+ Help (`-h`/`--help`):

+ show this help message and exit.

### Understand Row Normalization:

+ Step 1: For each row, find the smallest (min) and largest (max) values.

+ Step 2: Compute the range (max minus min) for each row.

+ Step 3: If a row’s range is 0 (i.e., all values are equal), set the range to 1 to prevent division by zero.

+ Step 4: Transform each element by subtracting the row’s minimum and then dividing by the row’s range.

+ The result is that every value in the row is scaled between 0 (original minimum) and 1 (original maximum).

### Understand Column Normalization:

+ Step 1: For each column, determine the minimum and maximum values.

+ Step 2: Compute the range for each column.

+ Step 3: If any column’s range is 0 (i.e., every value is the same), set that range to 1 to avoid division errors.

+ Step 4: Normalize each column by subtracting the column minimum from every element and then dividing by the column’s range.

+ This scales every value in each column to fall between 0 and 1.

### Run the Script Using the `Blues` Color Palette Without Any Normalization:

+ Open a terminal or command prompt.

Navigate to the directory where your script is located.

To demonstrate the different ways we can display the data contained in the

`Table_01.tsv` data, let's issue the following commands:

```
python3 Heatmap_Tables.py \
--title "HeatMap Tables\nExample" \
--data Table_00.tsv \
--format png \
--resolution 300 \
--palette Blues
```

+ Will produce the following table:

<p align="center">
<img src="https://github.com/raramayo/HeatMap_Tables_Python/blob/main/Images/Table_00_01_Blues.png" width="800" height="800" style="display: block; margin: 0 auto">
<p align="center">
Color Palette: <Blues>, No Normalization.

+ The `--format` option request the table to be generated in `png` format at a `300 dpi` resolution,

+ The `--palette` option requests the table table to be generated using the `Blues` palette.

+ The script will read your data, generate the heatmap,
    and save it to a file with the same base name as your data
	file but with the appropriate extension (either `.png` or `.pdf`).

+ The heatmap will have dynamic text color based on the data values,
	customized titles, and axes labels, making it easier to interpret the data.

### Using the `Blues` Color Palette With Rows Normalization:

+ To normalize the output color of the cells by rows, let's issue the following command:

```
python3 Heatmap_Tables.py \
--title "HeatMap Tables\nExample" \
--data Table_00.tsv \
--format png \
--resolution 300 \
--palette Blues \
--normalize_rows
```

+ Which results in the following table:

<p align="center">
<img src="https://github.com/raramayo/HeatMap_Tables_Python/blob/main/Images/Table_00_02_Blues_nrow.png" width="800" height="800" style="display: block; margin: 0 auto">
<p align="center">
Color Palette: <code class="language-markdown"> Blues </code>, Normalized by Rows.

### Using the `Blues` Color Palette With Columns Normalization:

+ To normalize the output color of the cells by columns, let's issue the following command:

```
python3 Heatmap_Tables.py \
--title "HeatMap Tables\nExample" \
--data Table_00.tsv \
--format png \
--resolution 300 \
--palette Blues \
--normalize_columns
```

+ Which results in the following table:

<p align="center">
<img src="https://github.com/raramayo/HeatMap_Tables_Python/blob/main/Images/Table_00_03_Blues_ncol.png" width="800" height="800" style="display: block; margin: 0 auto">
<p align="center">
Color Palette: <Blues>, Normalized by Columns.

+ Similarly, commands equivalent to the ones above can be issued to generate tables without any normalization, or normalized by either rows or columns using different color palettes.

+ In the tables presented below, note how the font color changes according to the color palette used.

### Using the `viridis` Color Palette Without Any Normalization:

+ The command:

```
python3 Heatmap_Tables.py \
--title "HeatMap Tables\nExample" \
--data Table_00.tsv \
--format png \
--resolution 300 \
--palette viridis
```

+ Produces the following table:

<p align="center">
<img src="https://github.com/raramayo/HeatMap_Tables_Python/blob/main/Images/Table_00_04_viridis.png" width="800" height="800" style="display: block; margin: 0 auto">
<p align="center">
Color Palette: <viridis>, No Normalization.

### Using the `viridis` Color Palette With Rows Normalization:

+ The command:

```
python3 Heatmap_Tables.py \
--title "HeatMap Tables\nExample" \
--data Table_00.tsv \
--format png \
--resolution 300 \
--palette viridis \
--normalize_rows
```

+ Produces the following table:

<p align="center">
<img src="https://github.com/raramayo/HeatMap_Tables_Python/blob/main/Images/Table_00_05_viridis_nrow.png" width="800" height="800" style="display: block; margin: 0 auto">
<p align="center">
Color Palette: <viridis>, Normalized by Rows.

### Using the `viridis` Color Palette With Columns Normalization:

+ The command:

```
python3 Heatmap_Tables.py \
--title "HeatMap Tables\nExample" \
--data Table_00.tsv \
--format png \
--resolution 300 \
--palette viridis \
--normalize_columns
```

+ Produces the following table:

<p align="center">
<img src="https://github.com/raramayo/HeatMap_Tables_Python/blob/main/Images/Table_00_06_viridis_ncol.png" width="800" height="800" style="display: block; margin: 0 auto">
<p align="center">
Color Palette: <viridis>, Normalized by Columns.

### Using the `coolwarm` Color Palette Without Any Normalization:

+ The command:

```
python3 Heatmap_Tables.py \
--title "HeatMap Tables\nExample" \
--data Table_00.tsv \
--format png \
--resolution 300 \
--palette coolwarm
```

+ Produces the following table:

<p align="center">
<img src="https://github.com/raramayo/HeatMap_Tables_Python/blob/main/Images/Table_00_07_coolwarm.png" width="800" height="800" style="display: block; margin: 0 auto">
<p align="center">
Color Palette: <coolwarm>, No Normalization.

### Using the `coolwarm` Color Palette With Rows Normalization:

+ The command:

```
python3 Heatmap_Tables.py \
--title "HeatMap Tables\nExample" \
--data Table_00.tsv \
--format png \
--resolution 300 \
--palette coolwarm \
--normalize_rows
```

+ Produces the following table:

<p align="center">
<img src="https://github.com/raramayo/HeatMap_Tables_Python/blob/main/Images/Table_00_08_coolwarm_nrow.png" width="800" height="800" style="display: block; margin: 0 auto">
<p align="center">
Color Palette: <coolwarm>, Normalized by Rows.

### Using the `coolwarm` Color Palette With Columns Normalization:

+ The command:

```
python3 Heatmap_Tables.py \
--title "HeatMap Tables\nExample" \
--data Table_00.tsv \
--format png \
--resolution 300 \
--palette coolwarm \
--normalize_columns
```

+ Produces the following table:

<p align="center">
<img src="https://github.com/raramayo/HeatMap_Tables_Python/blob/main/Images/Table_00_09_coolwarm_ncol.png" width="800" height="800" style="display: block; margin: 0 auto">
<p align="center">
Color Palette: <coolwarm>, Normalized by Columns.

### Using the `YlGnBu` Color Palette Without Any Normalization:

+ The command:

```
python3 Heatmap_Tables.py \
--title "HeatMap Tables\nExample" \
--data Table_00.tsv \
--format png \
--resolution 300 \
--palette YlGnBu
```

+ Produces the following table:

<p align="center">
<img src="https://github.com/raramayo/HeatMap_Tables_Python/blob/main/Images/Table_00_10_YlGnBu.png" width="800" height="800" style="display: block; margin: 0 auto">
<p align="center">
Color Palette: <YlGnBu>, No Normalization.

### Using the `YlGnBu` Color Palette With Rows Normalization:

+ The command:

```
python3 Heatmap_Tables.py \
--title "HeatMap Tables\nExample" \
--data Table_00.tsv \
--format png \
--resolution 300 \
--palette YlGnBu \
--normalize_rows
```

+ Produces the following table:

<p align="center">
<img src="https://github.com/raramayo/HeatMap_Tables_Python/blob/main/Images/Table_00_11_YlGnBu_nrow.png" width="800" height="800" style="display: block; margin: 0 auto">
<p align="center">
Color Palette: <YlGnBu>, Normalized by Rows.

### Using the `YlGnBu` Color Palette With Columns Normalization:

+ The command:

```
python3 Heatmap_Tables.py \
--title "HeatMap Tables\nExample" \
--data Table_00.tsv \
--format png \
--resolution 300 \
--palette YlGnBu \
--normalize_columns
```

+ Produces the following table:

<p align="center">
<img src="https://github.com/raramayo/HeatMap_Tables_Python/blob/main/Images/Table_00_12_YlGnBu_ncol.png" width="800" height="800" style="display: block; margin: 0 auto">
<p align="center">
Color Palette: <YlGnBu>, Normalized by Columns.

### Using the `RdYlGn` Color Palette Without Any Normalization:

+ The command:

```
python3 Heatmap_Tables.py \
--title "HeatMap Tables\nExample" \
--data Table_00.tsv \
--format png \
--resolution 300 \
--palette RdYlGn
```

+ Produces the following table:

<p align="center">
<img src="https://github.com/raramayo/HeatMap_Tables_Python/blob/main/Images/Table_00_13_RdYlGn.png" width="800" height="800" style="display: block; margin: 0 auto">
<p align="center">
Color Palette: <RdYlGn>, No Normalization.

### Using the `RdYlGn` Color Palette With Rows Normalization:

+ The command:

```
python3 Heatmap_Tables.py \
--title "HeatMap Tables\nExample" \
--data Table_00.tsv \
--format png \
--resolution 300 \
--palette RdYlGn \
--normalize_rows
```

+ Produces the following table:

<p align="center">
<img src="https://github.com/raramayo/HeatMap_Tables_Python/blob/main/Images/Table_00_14_RdYlGn_nrow.png" width="800" height="800" style="display: block; margin: 0 auto">
<p align="center">
Color Palette: <RdYlGn>, Normalized by Rows.

### Using the `RdYlGn` Color Palette With Columns Normalization:

+ The command:

```
python3 Heatmap_Tables.py \
--title "HeatMap Tables\nExample" \
--data Table_00.tsv \
--format png \
--resolution 300 \
--palette RdYlGn \
--normalize_columns
```

+ Produces the following table:

<p align="center">
<img src="https://github.com/raramayo/HeatMap_Tables_Python/blob/main/Images/Table_00_15_RdYlGn_ncol.png" width="800" height="800" style="display: block; margin: 0 auto">
<p align="center">
Color Palette: <RdYlGn>, Normalized by Columns.

### Using the `bwr` Color Palette Without Any Normalization:

+ The command:

```
python3 Heatmap_Tables.py \
--title "HeatMap Tables\nExample" \
--data Table_00.tsv \
--format png \
--resolution 300 \
--palette bwr
```

+ Produces the following table:

<p align="center">
<img src="https://github.com/raramayo/HeatMap_Tables_Python/blob/main/Images/Table_00_16_bwr.png" width="800" height="800" style="display: block; margin: 0 auto">
<p align="center">
Color Palette: <bwr>, No Normalization.

### Using the `bwr` Color Palette With Rows Normalization:

+ The command:

```
python3 Heatmap_Tables.py \
--title "HeatMap Tables\nExample" \
--data Table_00.tsv \
--format png \
--resolution 300 \
--palette bwr \
--normalize_rows
```

+ Produces the following table:

<p align="center">
<img src="https://github.com/raramayo/HeatMap_Tables_Python/blob/main/Images/Table_00_17_bwr_nrow.png" width="800" height="800" style="display: block; margin: 0 auto">
<p align="center">
Color Palette: <bwr>, Normalized by Rows.

### Using the `bwr` Color Palette With Columns Normalization:

+ The command:

```
python3 Heatmap_Tables.py \
--title "HeatMap Tables\nExample" \
--data Table_00.tsv \
--format png \
--resolution 300 \
--palette bwr \
--normalize_columns
```

+ Produces the following table:

<p align="center">
<img src="https://github.com/raramayo/HeatMap_Tables_Python/blob/main/Images/Table_00_18_bwr_ncol.png" width="800" height="800" style="display: block; margin: 0 auto">
<p align="center">
Color Palette: <bwr>, Normalized by Columns.

### Using the `seismic` Color Palette Without Any Normalization:

+ The command:

```
python3 Heatmap_Tables.py \
--title "HeatMap Tables\nExample" \
--data Table_00.tsv \
--format png \
--resolution 300 \
--palette seismic
```

+ Produces the following table:

<p align="center">
<img src="https://github.com/raramayo/HeatMap_Tables_Python/blob/main/Images/Table_00_19_seismic.png" width="800" height="800" style="display: block; margin: 0 auto">
<p align="center">
Color Palette: <seismic>, No Normalization.

### Using the `seismic` Color Palette With Rows Normalization:

+ The command:

```
python3 Heatmap_Tables.py \
--title "HeatMap Tables\nExample" \
--data Table_00.tsv \
--format png \
--resolution 300 \
--palette seismic \
--normalize_rows
```

+ Produces the following table:

<p align="center">
<img src="https://github.com/raramayo/HeatMap_Tables_Python/blob/main/Images/Table_00_20_seismic_nrow.png" width="800" height="800" style="display: block; margin: 0 auto">
<p align="center">
Color Palette: <seismic>, Normalized by Rows.

### Using the `seismic` Color Palette With Columns Normalization:

+ The command:

```
python3 Heatmap_Tables.py \
--title "HeatMap Tables\nExample" \
--data Table_00.tsv \
--format png \
--resolution 300 \
--palette seismic \
--normalize_columns
```

+ Produces the following table:

<p align="center">
<img src="https://github.com/raramayo/HeatMap_Tables_Python/blob/main/Images/Table_00_21_seismic_ncol.png" width="800" height="800" style="display: block; margin: 0 auto">
<p align="center">
Color Palette: <seismic>, Normalized by Columns.

### Version:

+ Get Script Version  Information

```
python3 HeatMap_Tables.py -v
```

or

```
python3 HeatMap_Tables.py --version
```

### Help:

+ Get Script Help

```
python3 HeatMap_Tables.py -v
```

or

```
python3 HeatMap_Tables.py --version
```


## Repository:

<pre>
<a href="https://github.com/raramayo/HeatMap_Tables_Python" target="_blank">HeatMap_Tables_Python</a>
</pre>

## Issues:

<pre>
<a href="https://github.com/raramayo/HeatMap_Tables_Python/issues" target="_blank">HeatMap_Tables_Python_Issues</a>
</pre>
