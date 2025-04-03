# HeatMap_Tables_Pseudocode

```
BEGIN

  DEFINE main():

    // ---------------------------------------------
    // 1. Argument Parsing and Initialization
    // ---------------------------------------------
    CREATE an argument parser with a description and raw help formatting.

    ADD required argument:
      - Title (flags: -t/--title)
      - Type: string
      - Help: "Title for the heatmap (use '\\n' for new lines)"

    ADD required argument:
      - Data file (flags: -d/--data)
      - Type: string
      - Help: "Path to the TSV file containing numeric data with headers"

    ADD optional argument:
      - Output format (flags: -f/--format)
      - Choices: "png" or "pdf"
      - Default: "png"
      - Help: "Output file format (default: png)"

    ADD optional argument:
      - Resolution (flags: -r/--resolution)
      - Type: integer
      - Default: 300
      - Help: "Resolution for PNG output in DPI (default: 300, ignored for PDF)"

    ADD optional argument:
      - Size override (flags: -s/--size)
      - Choices: "small" or "large"
      - Help: "Override preset font sizes (optional)"

    ADD optional argument:
      - Correction factor (flags: -c/--correction)
      - Type: float
      - Default: 2
      - Help: "Font color mean correction value (default: 2)"

    ADD optional argument:
      - Color palette (flags: -p/--palette)
      - Choices: ["Blues", "viridis", "coolwarm", "YlGnBu", "RdYlGn", "bwr", "seismic"]
      - Default: "Blues"
      - Help: "Color scheme for the heatmap (default: Blues)"

    ADD flag argument:
      - Normalize rows (flag: --normalize_rows)
      - Action: store_true
      - Help: "Normalize each row independently (min-max scaling)"

    ADD flag argument:
      - Normalize columns (flag: --normalize_columns)
      - Action: store_true
      - Help: "Normalize each column independently (min-max scaling)"

    ADD optional argument:
      - Cell annotation font size (flag: --cell_font_size)
      - Type: integer
      - Default: None
      - Help: "Override cell annotation font size (e.g., 20)"

    ADD version flag:
      - (flags: -v/--version) to display the script version.

    PARSE the command-line arguments.

    REPLACE any literal "\n" in the title with actual newline characters.

    ASSIGN values from arguments to variables:
      title, data_file, file_format, resolution, correction, palette, size option, normalization flags, cell_font_size.

    // ---------------------------------------------
    // 2. File Verification and Data Loading
    // ---------------------------------------------
    IF data_file does NOT exist OR is not readable THEN:
      PRINT an error message.
      EXIT the program.

    TRY:
      READ the TSV file into a dataframe (using tab as the separator, with header and index).
    CATCH any error:
      PRINT error message.
      EXIT the program.

    // ---------------------------------------------
    // 3. Data Cleaning and Preprocessing
    // ---------------------------------------------
    TRY:
      REMOVE any rows whose index contains "TOTAL:".

      IF a column "% Public" exists THEN:
        REMOVE "%" characters and convert values to float.

      SELECT only numeric columns from the dataframe.
      CONVERT these columns to numeric (set conversion errors to NaN).
      FILL any NaN values with 0.
    CATCH any error:
      PRINT error message.
      EXIT the program.

    SAVE a copy of the numeric data as original_values (to be used for annotations).

    // ---------------------------------------------
    // 4. Normalization (Optional)
    // ---------------------------------------------
    IF normalize_rows flag is set THEN:
      FOR each row in the numeric data:
        COMPUTE the row's minimum and maximum.
        CALCULATE the range (max - min).
        IF the range is zero THEN:
          SET the range to 1 (to avoid division by zero).
        PERFORM min–max scaling for that row.

    IF normalize_columns flag is set THEN:
      FOR each column in the numeric data:
        COMPUTE the column's minimum and maximum.
        CALCULATE the range (max - min).
        IF the range is zero THEN:
          SET the range to 1.
        PERFORM min–max scaling for that column.

    // ---------------------------------------------
    // 5. Figure and Font Configuration
    // ---------------------------------------------
    DETERMINE the number of rows (n_rows) and columns (n_cols) of the normalized data.

    SET is_large_auto to TRUE if (n_rows > 50 OR n_cols > 6).

    IF the size override argument is provided THEN:
      SET is_large based on the override ("large" means true).
    ELSE:
      SET is_large to is_large_auto.

    IF is_large is TRUE THEN:
      SET font_scale = 1.0,
      SET annotation font size to 8,
      SET label and tick font sizes to 12.
    ELSE:
      SET font_scale = 1.2,
      SET annotation font size to 12,
      SET label and tick font sizes to 12.

    IF cell_font_size is provided THEN:
      OVERRIDE the annotation font size with the provided value.

    SET the global seaborn font scale to font_scale.

    COMPUTE figure dimensions:
      width = MAX(8.5, n_cols * 0.5)
      height = MAX(11, n_rows * 0.3)
    CREATE a matplotlib figure with these dimensions.

    // ---------------------------------------------
    // 6. Heatmap Generation and Annotation
    // ---------------------------------------------
    CALCULATE threshold_value_adjusted as the mean of all normalized data values.

    TRY:
      GENERATE the heatmap using seaborn with:
        - Data: normalized dataframe.
        - Annotations: use original_values to display the original data.
        - Format: ".2f" (two decimal places).
        - Color map: selected palette.
        - Line widths: 0.5.
        - Colorbar with label "Count".
        - Annotation keyword arguments: annot_kws (including cell font size).

      SET the heatmap title using the provided title, with styling (fontsize, color, weight).

      FOR each annotation text and its corresponding normalized value in the heatmap:
        IF value > (correction * threshold_value_adjusted) THEN:
          SET text color to white.
        ELSE IF value > threshold_value_adjusted THEN:
          SET text color to black.
        ELSE:
          SET text color to white.

      SET row labels (y-axis) to italic.

      SET x-axis label to "Data Categories" with appropriate styling.
      SET y-axis label to "Features" with appropriate styling.
      CONFIGURE x-axis and y-axis tick labels (font sizes, rotations, alignment, color).

      DETERMINE the output file name by replacing the extension of data_file with the chosen file format.

      IF the output format is "png" THEN:
        SAVE the figure as a PNG file with the specified resolution.
      ELSE IF the output format is "pdf" THEN:
        SAVE the figure as a PDF file.
    CATCH any error:
      PRINT an error message indicating heatmap generation failure.
    FINALLY:
      CLOSE the matplotlib figure to free resources.

  END DEFINE main

  // ---------------------------------------------
  // 7. Program Entry Point
  // ---------------------------------------------
  IF this script is executed as the main program THEN:
    CALL main()

END
```
