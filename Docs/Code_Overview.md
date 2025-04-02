# HeatMap_Tables_Pseudocode

```
BEGIN

    DEFINE main():

        // -----------------------------------------
        // Setup Command-Line Arguments
        // -----------------------------------------
        INITIALIZE argument parser with a description and raw help formatting

        ADD required argument:
            - Title (flags: -t, --title)
            - Type: string
            - Help: "Title for the heatmap (use '\n' for new lines)"

        ADD required argument:
            - Data file (flags: -d, --data)
            - Type: string
            - Help: "Path to the TSV file containing numeric data with headers"

        ADD optional argument:
            - Output format (flags: -f, --format)
            - Choices: "png" or "pdf"
            - Default: "png"
            - Help: "Output file format (default: png)"

        ADD optional argument:
            - Resolution (flags: -r, --resolution)
            - Type: integer
            - Default: 300
            - Help: "Resolution for PNG output in DPI (default: 300, ignored for PDF)"

        ADD optional argument:
            - Size override (flags: -s, --size)
            - Choices: "small" or "large"
            - Help: "Override preset font sizes (optional)"

        ADD optional argument:
            - Correction factor (flags: -c, --correction)
            - Type: float
            - Default: 2
            - Help: "Font color mean correction value (default: 2)"

        ADD optional argument:
            - Color palette (flags: -p, --palette)
            - Choices: "Blues", "viridis", "coolwarm", "YlGnBu"
            - Default: "Blues"
            - Help: "Color scheme for the heatmap (default: Blues)"

        ADD version flag:
            - (flags: -v, --version)
            - Action: show version and exit

        PARSE command-line arguments

        REPLACE literal "\n" in the title argument with actual newline characters

        STORE values from arguments into local variables:
            title, data_file, file_format, resolution, correction, palette, size option

        // -----------------------------------------
        // File Existence and Readability Check
        // -----------------------------------------
        IF the file specified by data_file does NOT exist OR is NOT readable THEN
            PRINT error message: "The data file '<data_file>' does not exist or is not readable."
            EXIT the program
        END IF

        // -----------------------------------------
        // Data Loading and Preprocessing
        // -----------------------------------------
        TRY:
            READ the TSV file specified by data_file into a dataframe using tab as separator
        CATCH error:
            PRINT error message indicating failure to load the file
            EXIT program

        TRY:
            REMOVE rows where the index contains "TOTAL:"

            IF a column named "% Public" exists THEN
                REMOVE "%" from each entry and CONVERT values to float

            SELECT only numeric columns from the dataframe

            CONVERT these columns to numeric values (errors become NaN)
            REPLACE any NaN values with 0
        CATCH error:
            PRINT error message indicating data processing failure
            EXIT program

        // -----------------------------------------
        // Determine Figure and Font Settings
        // -----------------------------------------
        GET the number of rows and columns from the numeric dataframe

        SET is_large_auto to TRUE if (rows > 50 OR columns > 6)

        IF the user provided a size override THEN
            SET is_large based on whether the override is "large"
        ELSE:
            SET is_large to is_large_auto

        IF is_large is TRUE THEN:
            SET font_scale = 1.0
            SET annotation font size = 8
            SET label font size = 12
            SET tick font size = 12
        ELSE:
            SET font_scale = 1.2
            SET annotation font size = 12
            SET label font size = 12
            SET tick font size = 12

        CONFIGURE the global seaborn font scale using font_scale

        CALCULATE figure width = MAX(8.5, (number of columns * 0.5))
        CALCULATE figure height = MAX(11, (number of rows * 0.3))

        CREATE a matplotlib figure with the calculated dimensions

        // -----------------------------------------
        // Heatmap Generation
        // -----------------------------------------
        CALCULATE threshold_value_adjusted as the mean of all values in the numeric dataframe

        TRY:
            GENERATE heatmap using seaborn with parameters:
                - Data: numeric dataframe
                - Annotations enabled (format: one decimal place)
                - Color map: use the user-selected palette
                - Line widths: 0.5
                - Colorbar labeled "Count"
                - Annotation keyword arguments as determined by font size settings

            SET the heatmap title using the provided title with styling (fontsize, color, bold)

            FOR each cell's annotation and its corresponding data value:
                IF value > (correction factor * threshold_value_adjusted) THEN:
                    SET text color to white
                ELSE IF value > threshold_value_adjusted THEN:
                    SET text color to black
                ELSE:
                    SET text color to darkblue

            SET y-axis tick labels to italic

            SET x-axis label to "Data Categories" with styling (fontsize, bold, darkblue)
            SET y-axis label to "Features" with styling (fontsize, bold, darkblue)

            CONFIGURE x-axis tick labels:
                - Font size as defined
                - Rotation: 45 degrees
                - Horizontal alignment: right
                - Bold and darkblue
            CONFIGURE y-axis tick labels similarly (rotation: 0)

            DETERMINE the output file name by replacing the extension of data_file with the chosen file_format

            IF output format is "png" THEN:
                SAVE the figure as a PNG file using the specified DPI
            ELSE IF output format is "pdf" THEN:
                SAVE the figure as a PDF file
        CATCH error:
            PRINT error message indicating heatmap generation failure
        FINALLY:
            CLOSE the matplotlib plot to free resources

    END DEFINE main

    // -----------------------------------------
    // Execution Entry Point
    // -----------------------------------------
    IF the script is executed as the main program THEN:
        CALL main()

END
```
