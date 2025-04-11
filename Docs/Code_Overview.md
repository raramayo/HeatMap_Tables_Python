# HeatMap_Tables_Pseudocode

```
BEGIN

  DEFINE main():

    // 1. Argument Parsing and Initialization
    CREATE an argument parser with a description and raw help formatting.

    ADD required argument:
      --title: string, required, help = "Title for the heatmap (use '\n' for new lines)"

    ADD required argument:
      --data: string, required, help = "Path to the TSV file containing numeric data with headers"

    ADD optional argument:
      --format: string, choices = ["png", "pdf"], default = "png",
          help = "Output file format\nDefault: png"

    ADD optional argument:
      --resolution: integer, default = 300,
          help = "Resolution for PNG output in DPI\nDefault: 300, ignored for PDF"

    ADD optional argument:
      --size: string, choices = ["small", "large"], help = "Override preset font sizes (optional)"

    ADD optional argument:
      --correction: float, default = 2,
          help = "Font color mean correction value\nDefault: 2"

    ADD optional argument:
      --palette: string, choices = ["Blues", "viridis", "coolwarm", "YlGnBu", "RdYlGn", "bwr", "seismic"],
          default = "Blues",
          help = "Color scheme for the heatmap\nDefault: Blues\nChoices: 'Blues', 'viridis', 'coolwarm', 'YlGnBu', 'RdYlGn', 'bwr', 'seismic'"

    ADD flag argument:
      --normalize_rows: if present, enable row min–max normalization

    ADD flag argument:
      --normalize_columns: if present, enable column min–max normalization

    ADD optional argument:
      --cell_font_size: integer, default = None,
          help = "Override cell annotation font size (e.g., 20).\nFont Size Default for Large Tables: 8\nFont Size Default for Small Tables: 12"

    ADD optional argument:
      --cell_height: float, default = None,
          help = "Set the height (in inches) for each cell.\nFigure height is computed as (number of rows) x (cell height).\nDefault: 1.5"

    ADD version argument:
      -v / --version: show script version and exit

    PARSE command-line arguments and assign them to a variable `args`.

    REPLACE all literal "\n" in args.title with actual newline characters.
    SET local variables: title, data_file, file_format, resolution, correction, palette, etc.

    // 2. File Verification and Data Loading
    IF the file specified by data_file does NOT exist OR is NOT readable THEN:
      PRINT error message and EXIT.

    TRY:
      READ the TSV file (using tab delimiter, header row, first column as index)
          into a dataframe `df`.
    CATCH any error:
      PRINT error message and EXIT.

    // 3. Data Cleaning and Preprocessing
    TRY:
      REMOVE any rows from df whose index contains "TOTAL:".

      IF column named "% Public" exists THEN:
          For that column, remove "%" characters and convert values to float.

      SELECT only numeric columns from df → store in `numeric_cols`.

      CONVERT values in numeric_cols to numeric using conversion with errors="coerce",
          then fill any NaN values with 0.

      ASSIGN the resulting dataframe to `df_numerical`.
    CATCH any error:
      PRINT error message and EXIT.

    // Save original numeric data copy (for annotations)
    SET original_values = copy of df_numerical.

    // 4. Optional Normalization (Min–Max Scaling)
    IF normalize_rows flag is set THEN:
      FOR each row in df_numerical:
          COMPUTE row_min (minimum value) and row_max (maximum value).
          COMPUTE row_range = row_max - row_min.
          IF row_range equals zero, replace it with 1.
          PERFORM row normalization: (each value - row_min) / row_range.
          UPDATE df_numerical with normalized row values.

    IF normalize_columns flag is set THEN:
      FOR each column in df_numerical:
          COMPUTE col_min (minimum value) and col_max (maximum value).
          COMPUTE col_range = col_max - col_min.
          IF col_range equals zero, replace it with 1.
          PERFORM column normalization: (each value - col_min) / col_range.
          UPDATE df_numerical with normalized column values.

    // 5. Figure and Font Configuration
    DETERMINE number of rows (n_rows) and columns (n_cols) in df_numerical.

    SET auto-size flag is_large_auto = TRUE if (n_rows > 50 OR n_cols > 6).

    IF args.size is provided THEN:
       SET is_large = (args.size equals "large")
    ELSE:
       SET is_large = is_large_auto.

    IF is_large is TRUE THEN:
       SET font_scale = 1.0, annotation font size = 8, label font size = 12, tick font size = 12.
    ELSE:
       SET font_scale = 1.2, annotation font size = 12, label font size = 12, tick font size = 12.

    IF args.cell_font_size is provided THEN:
       OVERRIDE annotation font size with this value (assign annot_kws accordingly).

    SET the overall seaborn font scale using font_scale.

    // Compute figure dimensions:
    IF args.cell_height is provided THEN:
       SET cell_height = args.cell_height.
    ELSE:
       SET default cell_height = 1.5 inches.

    CALCULATE figure_width = maximum of (8.5, n_cols * 0.5).
    CALCULATE figure_height = n_rows * cell_height.
    CREATE matplotlib figure with figsize = (figure_width, figure_height).

    // 6. Heatmap Generation and Dynamic Text Color Adjustment
    CALCULATE threshold_value_adjusted = mean of all values in df_numerical.

    GET colormap object `cmap` for the chosen palette.
    COMPUTE data_vmin = minimum value in df_numerical, and data_vmax = maximum value.
    SET data_range = data_vmax - data_vmin (use 1 if equal).

    TRY:
      GENERATE heatmap using seaborn:
         - Data: df_numerical.
         - Annotations: show original_values (for readability).
         - Format: display numbers with two decimals (".2f").
         - Colormap: use chosen palette.
         - Set line widths = 0.5.
         - Set colorbar with label "Count".
         - Use annot_kws for annotation text size.

      SET heatmap title using the provided title with styling (fontsize=18, dark blue color, bold weight).

      FOR each cell’s annotation (text object) and its corresponding value in df_numerical (flattened):
         COMPUTE normalized value norm_val = (value - data_vmin) / data_range.

         IF palette is "viridis" THEN:
             OBTAIN the background color for norm_val from cmap.
             CALCULATE luminance = 0.299*R + 0.587*G + 0.114*B of the background color.
             IF luminance < 0.5 THEN:
                SET text color to white.
             ELSE:
                SET text color to black.

         ELSE IF palette is in ["coolwarm", "RdYlGn", "bwr", "seismic"] THEN:
             IF norm_val < 0.3 OR norm_val > 0.7 THEN:
                SET text color to white.
             ELSE:
                SET text color to black.

         ELSE:   // For other palettes (e.g., Blues, YlGnBu)
             IF value > (correction * threshold_value_adjusted) THEN:
                SET text color to white.
             ELSE IF value > threshold_value_adjusted THEN:
                SET text color to black.
             ELSE:
                SET text color to dark blue.

      SET y-axis tick labels to italic font.

      SET x-axis label "Data Categories" with styling (fontsize = label_fontsize, bold, dark blue).
      SET y-axis label "Features" with similar styling.
      CONFIGURE x-axis and y-axis tick label properties (fontsize = tick_fontsize, rotation, alignment, color).

      DETERMINE output filename by replacing extension of data_file with the chosen file_format.

      IF file_format is "png" THEN:
         SAVE the figure as a PNG with the specified resolution and bbox_inches="tight".
      ELSE IF file_format is "pdf" THEN:
         SAVE the figure as a PDF with bbox_inches="tight".

    CATCH any exceptions during heatmap generation:
         PRINT error message.

    FINALLY:
         CLOSE the matplotlib figure.

  END DEFINE main

  // 7. Program Entry Point
  IF __name__ == "__main__" THEN:
      CALL main()

END
```
