# AppendZipPython

`AppendZipPython` is a simple Python project that allows you to extract potential ZIP files from JPEG images and merge them back into a new JPEG file. This can be useful for understanding how ZIP files can be hidden within other file types.

## Features

- **Extract ZIP from JPEG**: Identifies and extracts potential ZIP file content from a JPEG image.
- **Merge ZIP into JPEG**: Appends ZIP content to an existing JPEG file.

## Technologies Used

- Python 3
- Standard libraries: `os`, `io`, and `zipfile`

## Getting Started

### Prerequisites

- Python 3.x installed on your machine.

### Installation

1. Clone the repository or download the files.
2. Navigate to the project directory.

### File Structure

- **extract.py**: A script that reads a JPEG file and extracts ZIP content if detected.
- **merge.py**: A script that merges ZIP content into an existing JPEG file.

## Usage

### Merging ZIP into JPEG

1. Prepare a JPEG file named `jpgToPutZipIn.jpg` and ensure the ZIP file you want to merge is named `zipfile.zip`.
2. Run the script:

   ```bash
   python merge.py

### Extracting ZIP from JPEG

1. Place a JPEG file named `FileWithZip.jpg` in the same directory as `extract.py`.
2. Run the script:

   ```bash
   python extract.py

## License

This project is licensed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html). 

You can redistribute and modify this project under the terms of the License.

### Summary of the License

- **Freedom to use**: You can use this software for any purpose.
- **Freedom to study and modify**: You can study how the program works and change it to make it do what you wish. Access to the source code is a precondition for this.
- **Freedom to distribute copies**: You can redistribute copies of the original program so you can help others.
- **Freedom to distribute modified versions**: You can distribute copies of your modified versions to others. By doing this you can give the whole community a chance to benefit from your changes. Access to the source code is a precondition for this.

For more details, see the [LICENSE](LICENSE) file in the repository.

