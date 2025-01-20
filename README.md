# DNA Sequence GC Content Calculator

## Overview
The **DNA Sequence GC Content Calculator** is a Python-based project designed to calculate the GC content across large DNA sequences. GC content is the percentage of nucleotides in a DNA sequence that are either guanine (G) or cytosine (C). This metric is crucial for understanding genome stability, gene expression, and evolutionary relationships.

---

## Features
- Reads DNA sequences in FASTA format.
- Calculates the GC content of individual sequences and the entire dataset.
- Provides output in a clear and organized format for further analysis.

---

## Requirements

To run the script, ensure you have the following installed:

- Python 3.6+
- Required Python libraries:
  - `biopython`
  - `argparse`

Install dependencies using:
```bash
pip install biopython argparse
```

---

## Usage

### Input
- Input DNA sequences must be in FASTA format.

### Running the Script
1. Clone the repository:
   ```bash
   git clone https://github.com/Sravz2433/GC-content-calculator.git
   cd GC-content-calculator
   ```

2. Run the script:
   ```bash
   python gc_calculator.py --input <input_file.fasta>
   ```

3. Example:
   ```bash
   python gc_calculator.py --input example_sequences.fasta
   ```

### Output
- The script outputs the GC content for each sequence and the average GC content across the dataset.

---

## Example Output

Input file: `example_sequences.fasta`

```
>sequence_1
ATGCGCCTAG
>sequence_2
TTATTGCGGA
```

Output:
```
Sequence: sequence_1, GC Content: 60.0%
Sequence: sequence_2, GC Content: 50.0%
Average GC Content: 55.0%
```

---

## Repository Structure
```
GC-content-calculator/
├── gc_calculator.py      # Main Python script
├── example_sequences.fasta  # Sample input file
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies
```

---

## Contributing
Contributions are welcome! If you find a bug or have an idea for an enhancement, please submit an issue or pull request.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Author
- **Sravya Sri Mallampalli**  
  - [GitHub Profile](https://github.com/Sravz2433)
  - [LinkedIn](https://www.linkedin.com/in/sravya-sri-mallampalli)
