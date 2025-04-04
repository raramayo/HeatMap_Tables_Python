# HeatMap_Tables_Pseudocode

```
BEGIN

  DEFINE main():

    // ------------------------------------------------
    // 1. Argument Parsing and Initialization
    // ------------------------------------------------
    CREATE an argument parser with description and raw help formatting.

    ADD required arguments:
      - Title (-t/--title): String, with help "Title for the heatmap (use '\n' for new lines)"
      - Data file (-d/--data): String, with help "Path to the TSV file containing numeric data with headers"

    ADD optional arguments:
      - Output format (-f/--format): String, choices ["png", "pdf"], default "png"
      - Resolution (-r/--resolution): Integer, default 300 (ignored for PDF)
      - Size (-s/--size): String, choices ["small", "large"] (overrides auto-size detection)
      - Correction (-c/--correction): Float, default 2 (used for text color thresholding)
      - Color palette (-p/--palette): String, choices ["Blues", "viridis", "coolwarm", "YlGnBu", "RdYlGn", "bwr", "seismic"], default "Blues"
      - Normalize rows (--normalize_rows): Flag; if set, perform row-wise min–max normalization
      - Normalize columns (--normalize_columns): Flag; if set, perform column-wise min–max normalization
      - Cell annotation font size (--cell_font_size): Integer, default None (to override default annotation text size)
      - Version (-v/--version): Display version information and exit

    PARSE the command-line arguments.

    REPLACE any literal "\n" in the title with actual newline characters.

    ASSIGN variables: title, data_file, file_format, resolution, correction, palette, size, normalization flags, cell_font_size.

    // ------------------------------------------------
    // 2. File Verification and Data Loading
    // ------------------------------------------------
    IF the data file does NOT exist OR is not readable THEN:
      PRINT an error message.
      EXIT the program.

    TRY:
      READ the TSV file into a dataframe using tab separator, header row, and first column as index.
    CATCH error:
      PRINT error message.
      EXIT the program.

    // ------------------------------------------------
    // 3. Data Cleaning and Preprocessing
    // ------------------------------------------------
    TRY:
      REMOVE any rows where the index contains "TOTAL:".

      IF column "% Public" exists THEN:
        REMOVE "%" characters from that column and convert values to float.

      SELECT only numeric columns from the dataframe.
      CONVERT these columns to numeric values (convert errors to NaN) and fill NaN values with 0.
    CATCH error:
      PRINT error message.
      EXIT the program.

    SAVE a copy of the processed numeric data as "original_values" for later annotations.

    // ------------------------------------------------
    // 4. Optional Normalization
    // ------------------------------------------------
    IF normalize_rows flag is set THEN:
      FOR each row in the numeric data:
        COMPUTE the row’s minimum and maximum.
        COMPUTE the row’s range (max - min).
        IF the range is 0 THEN:
          SET the range to 1 (to avoid division by zero).
        PERFORM min–max scaling: subtract the minimum and divide by the range.

    IF normalize_columns flag is set THEN:
      FOR each column in the numeric data:
        COMPUTE the column’s minimum and maximum.
        COMPUTE the column’s range (max - min).
        IF the range is 0 THEN:
          SET the range to 1.
        PERFORM min–max scaling: subtract the minimum and divide by the range.

    // ------------------------------------------------
    // 5. Figure and Font Configuration
    // ------------------------------------------------
    DETERMINE the number of rows (n_rows) and columns (n_cols) in the (possibly normalized) data.

    SET is_large_auto to TRUE if (n_rows > 50 OR n_cols > 6).

    IF the user provided a size override THEN:
      SET is_large based on the override ("large" means TRUE).
    ELSE:
      SET is_large to is_large_auto.

    IF is_large is TRUE THEN:
      SET font_scale = 1.0, annotation text size = 8, label and tick font sizes = 12.
    ELSE:
      SET font_scale = 1.2, annotation text size = 12, label and tick font sizes = 12.

    IF cell_font_size is provided THEN:
      OVERRIDE the annotation text size with the provided value.

    SET the global seaborn font scale to font_scale.

    CALCULATE figure dimensions:
      width = MAX(8.5, n_cols * 0.5)
      height = MAX(11, n_rows * 0.3)
    CREATE a matplotlib figure with these dimensions.

    // ------------------------------------------------
    // 6. Heatmap Generation and Text Color Adjustment
    // ------------------------------------------------
    CALCULATE threshold_value_adjusted as the mean of the normalized data values.

    OBTAIN the colormap object for the selected palette.
    COMPUTE data_vmin as the minimum and data_vmax as the maximum of the normalized data.
    COMPUTE data_range = data_vmax - data_vmin (set to 1 if data_vmax equals data_vmin).

    TRY:
      GENERATE the heatmap using seaborn with:
        - Data: the normalized data.
        - Annotations: using original_values to show original numbers.
        - Number format: ".2f".
        - Colormap: the selected palette.
        - Line widths: 0.5.
        - Colorbar with label "Count".
        - Annotation keyword arguments (including cell_font_size).

      SET the heatmap title using the provided title and styling (fontsize, color, bold).

      FOR each annotation text (cell text) and its corresponding normalized data value:
        COMPUTE norm_val = (value - data_vmin) / data_range.

        IF the selected palette is "viridis" THEN:
          GET the background color for norm_val from the colormap.
          COMPUTE the luminance using the formula: 0.299*R + 0.587*G + 0.114*B.
          IF luminance < 0.5 THEN:
            SET the text color to white.
          ELSE:
            SET the text color to black.

        ELSE IF the palette is one of ["coolwarm", "RdYlGn", "bwr", "seismic"] THEN:
          IF norm_val < 0.3 OR norm_val > 0.7 THEN:
            SET text color to white.
          ELSE:
            SET text color to black.

        ELSE:
          // Default behavior using the correction factor:
          IF value > (correction * threshold_value_adjusted) THEN:
            SET text color to white.
          ELSE IF value > threshold_value_adjusted THEN:
            SET text color to black.
          ELSE:
            SET text color to dark blue.

      SET the y-axis tick labels to italic style.

      CONFIGURE the x-axis label ("Data Categories") and y-axis label ("Features") with styling (fontsize, bold, darkblue).
      CONFIGURE the x-axis and y-axis tick labels (font size, rotation, alignment, color).

      DETERMINE the output file name by replacing the extension of the data file with the chosen file format.

      IF the output format is "png" THEN:
        SAVE the figure as a PNG file with the specified resolution.
      ELSE IF the output format is "pdf" THEN:
        SAVE the figure as a PDF file.
    CATCH any error during heatmap generation:
      PRINT an error message indicating failure.
    FINALLY:
      CLOSE the matplotlib figure to release resources.

  END DEFINE main

  // ------------------------------------------------
  // 7. Program Entry Point
  // ------------------------------------------------
  IF this script is executed as the main program THEN:
    CALL main()

END
```
