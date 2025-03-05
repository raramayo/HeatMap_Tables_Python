#!/usr/bin/env python3
"""
--------------------------------------------------------------------------------
HeatMap_Tables Script
--------------------------------------------------------------------------------
Author:                            Rodolfo Aramayo
Work_Email:                        raramayo@tamu.edu
Personal_Email:                    rodolfo@aramayo.org
--------------------------------------------------------------------------------
Overview:
This script generates a heatmap from a TSV file containing numeric data.
It auto-adjusts fonts and figure sizes based on the data dimensions,
applies dynamic text color corrections, and saves the heatmap in PNG or PDF format.
--------------------------------------------------------------------------------
Copyright:
This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program. If not, see <https://www.gnu.org/licenses/>.
--------------------------------------------------------------------------------
Version Number:
Version: 1.0.0
--------------------------------------------------------------------------------
"""

#-------------------------------------------------------------------------------
# Import dependencies
import argparse
import matplotlib.pyplot as plt
import os
import pandas as pd
import seaborn as sns
import sys
#-------------------------------------------------------------------------------
# Define script name and version information
script_name = os.path.basename(sys.argv[0])
script_version = "1.0.0"
current_version_date = "DATE:2025/03/05"          # Script version date
#-------------------------------------------------------------------------------

def main():
    # Set up argument parser with description and formatted help text
    parser = argparse.ArgumentParser(
        description="Generate a heatmap from a TSV file containing numeric data.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    # Title for the heatmap; use "\n" in the string for new lines.
    parser.add_argument(
        "-t",
        "--title",
        type=str,
        required=True,
        help="Title for the heatmap (use '\\n' for new lines)"
    )
    # Path to the TSV data file (tab-separated values)
    parser.add_argument(
        "-d",
        "--data",
        type=str,
        required=True,
        help="Path to the TSV file containing numeric data with headers"
    )
    # Output file format: default is "png"
    parser.add_argument(
        "-f",
        "--format",
        type=str,
        choices=["png", "pdf"],
        default="png",
        help="Output file format (default: png)"
    )
    # Resolution for PNG output in DPI; ignored if output is PDF (default: 300)
    parser.add_argument(
        "-r",
        "--resolution",
        type=int,
        default=300,
        help="Resolution for PNG output in DPI (default: 300, ignored for PDF)"
    )
    # Optional override for preset font sizes; choices are "small" or "large"
    parser.add_argument(
        "-s",
        "--size",
        type=str,
        choices=["small", "large"],
        help="Override preset font sizes (optional)"
    )
    # Correction factor for text color thresholding (default: 2)
    parser.add_argument(
        "-c",
        "--correction",
        type=float,
        default=2,
        help="Font color mean correction value (default: 2)"
    )
    # Color palette option for the heatmap
    parser.add_argument(
        "-p",
        "--palette",
        type=str,
        choices=["Blues", "viridis", "coolwarm", "YlGnBu"],
        default="Blues",
        help="Color scheme for the heatmap (default: Blues). Choices: 'Blues', 'viridis', 'coolwarm', 'YlGnBu'"
    )
    # Version flag to show script version and exit
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"%(prog)s {script_version}",
        help="Show program's version number and exit"
    )

    # Parse arguments
    args = parser.parse_args()
    # Replace literal "\n" with an actual newline in the title
    title = args.title.replace("\\n", "\n")
    data_file = args.data
    file_format = args.format
    resolution = args.resolution
    correction = args.correction
    palette = args.palette                        # Selected color palette

    # Load the data from the provided TSV file
    try:
        df = pd.read_csv(
            data_file, sep="\t", header=0, index_col=0, skip_blank_lines=True
        )
    except Exception as e:
        print(f"[Error] Could not load data file: {e}")
        sys.exit(1)

    # Data cleaning and preprocessing
    try:
        # Remove rows whose index contains "TOTAL:" (if any)
        df = df[~df.index.str.contains("TOTAL:", na=False)]

        # If a column named "% Public" exists, remove "%" and convert to float
        if "% Public" in df.columns:
            df["% Public"] = df["% Public"].str.replace("%", "", regex=False).astype(float)

        # Select only numeric columns and ensure conversion to numeric values;
        # Any conversion errors will be set to NaN, then filled with 0.
        numeric_cols = df.select_dtypes(include="number")
        df_numerical = numeric_cols.apply(pd.to_numeric, errors="coerce", axis=1).fillna(0)
        df_numerical = df_numerical.fillna(0)     # Ensure no NaNs remain

    except Exception as e:
        print(f"[Error] Data processing failed: {e}")
        sys.exit(1)

    # Determine dimensions of the data to auto-scale figure and fonts
    n_rows, n_cols = df_numerical.shape
    # Auto-detect whether to use "large" settings based on data dimensions
    is_large_auto = (n_rows > 50 or n_cols > 6)

    # Use user-specified size if provided, otherwise use auto-detection
    if args.size:
        is_large = (args.size == "large")
    else:
        is_large = is_large_auto

    # Configure font sizes based on table size
    if is_large:
        font_scale = 1.0
        annot_kws = {"size": 8}
        label_fontsize = 12
        tick_fontsize = 12
    else:
        font_scale = 1.2
        annot_kws = {"size": 12}
        label_fontsize = 12
        tick_fontsize = 12

    # Set the overall font scale for seaborn plots
    sns.set(font_scale=font_scale)

    # Dynamically set figure size based on number of columns and rows
    plt.figure(
        figsize=(
            max(8.5, n_cols * 0.5),
            max(11, n_rows * 0.3)
        )
    )

    # Calculate the mean value to be used for dynamic text color adjustment
    threshold_value_adjusted = df_numerical.values.mean()

    # Generate the heatmap using seaborn with the selected palette
    try:
        heatmap = sns.heatmap(
            df_numerical,
            annot=True,                           # Show data values in each cell
            fmt=".1f",                            # Format numbers with one decimal place
            cmap=palette,                         # Use the selected color palette
            linewidths=0.5,                       # Line width between cells
            cbar_kws={"label": "Count"},          # Colorbar label
            annot_kws=annot_kws                   # Annotation text size
        )

        # Set the heatmap title with styling
        heatmap.set_title(title, fontsize=18, color="darkblue", weight="bold")

        # Adjust text color in each cell based on the value and correction factor
        for text, value in zip(heatmap.texts, df_numerical.values.flatten()):
            if value > correction * threshold_value_adjusted:
                text.set_color("white")           # High values get white text
            elif value > threshold_value_adjusted:
                text.set_color("black")           # Moderately high values get black text
            else:
                text.set_color("darkblue")        # Lower values use dark blue

        # Set row labels (y-axis) to italic
        for text in heatmap.get_yticklabels():
            text.set_fontstyle("italic")

        # Set labels and tick parameters with styling
        plt.xlabel(
            "Data Categories",
            fontsize=label_fontsize,
            weight="bold",
            color="darkblue"
        )
        plt.ylabel(
            "Features",
            fontsize=label_fontsize,
            weight="bold",
            color="darkblue"
        )
        plt.xticks(
            fontsize=tick_fontsize,
            rotation=45,
            ha="right",
            weight="bold",
            color="darkblue"
        )
        plt.yticks(
            fontsize=tick_fontsize,
            rotation=0,
            weight="bold",
            color="darkblue"
        )

        # Save the heatmap to a file with the appropriate format and resolution
        output_file = os.path.splitext(data_file)[0] + f".{file_format}"
        if file_format == "png":
            plt.savefig(output_file, format="png", dpi=resolution, bbox_inches="tight")
        elif file_format == "pdf":
            plt.savefig(output_file, format="pdf", bbox_inches="tight")

    except Exception as e:
        print(f"[Error] Heatmap generation failed: {e}")
    finally:
        plt.close()

if __name__ == "__main__":
    main()
