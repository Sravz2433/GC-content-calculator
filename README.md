# GC Content Analysis of *Lampyris noctiluca* Clones

## Overview
This project analyzes the GC content of genomic sequences from *Lampyris noctiluca* (common glow-worm). The goal is to understand genome characteristics, such as coding and noncoding regions, evolutionary adaptations, and potential functional elements, particularly those related to bioluminescence.

---

## Data Summary
The dataset consists of genomic sequences with varying GC content:
| **Sequence ID** | **GC Content (%)** | **Description** |
|------------------|--------------------|------------------|
| MZ265787.1       | 28.50%            | AT-rich; likely noncoding or regulatory region. |
| MZ265786.1       | 32.06%            | Slightly higher GC content; may represent mixed coding/noncoding region. |
| MZ265784.1       | 41.61%            | GC-rich; possibly a protein-coding region or GC-rich gene. |
| MZ265782.1       | 27.93%            | Strong AT bias; likely a noncoding or repetitive region. |
| MZ265783.1       | 29.70%            | Near average GC content; potential regulatory or intergenic region. |
| MZ265781.1       | 27.08%            | AT-dominant region; possibly noncoding or repetitive. |
| MZ265779.1       | 34.34%            | GC-enriched; likely indicative of coding sequences. |
| MZ265778.1       | 33.33%            | Moderate GC content; could represent coding DNA. |
| MZ265776.1       | 27.87%            | AT-rich; likely a noncoding or repetitive region. |
| MZ265774.1       | 29.79%            | Close to average GC content; potential regulatory region or intergenic DNA. |

---

## Objectives
1. **Analyze GC Content**:
   - Calculate GC content for each sequence and compare across regions.
   - Identify regions with significant AT or GC biases.

2. **Cluster GC Content**:
   - Group sequences based on GC content using K-means clustering.
   - Identify optimal cluster numbers with the Elbow Method.

3. **Functional and Evolutionary Insights**:
   - Explore potential coding and noncoding regions.
   - Investigate evolutionary adaptations, including bioluminescence-related genes.

---

## Tools and Technologies
- **Programming Language**: Python
- **Libraries**: Biopython, Matplotlib, Scikit-learn, Pandas

---

## Methodology
1. **Input Data**:
   - DNA sequences provided in FASTA format (`sequence.fasta`).

2. **GC Content Calculation**:
   - Python scripts were developed to compute GC content for each sequence.

3. **Clustering**:
   - Applied the Elbow Method to determine the optimal number of clusters.
   - Performed K-means clustering to group sequences based on GC content.

4. **Visualization**:
   - Created bar charts to illustrate GC content variations.
   - Used scatterplots to visualize clustering results.

---

## Results
1. **GC Content Analysis**:
   - **Average GC Content**: 31.22% (AT-rich genome).
   - GC content ranged from 27.08% to 41.61%, indicating diverse genomic regions.

2. **Clustering**:
   - The Elbow Method determined **3 clusters** as the optimal grouping:
     - **GC-poor regions (AT-rich)**: Likely noncoding or repetitive sequences.
     - **GC-neutral regions**: A mix of coding and noncoding regions.
     - **GC-rich regions**: Likely protein-coding or regulatory sequences.

---

## How to Use
### Prerequisites
- Python 3.6+
- Required Libraries:
  ```bash
  pip install biopython matplotlib scikit-learn pandas
  ```
### Key Findings
- Functional Regions:
  - GC-rich regions are likely coding or regulatory.
  - AT-rich regions correspond to noncoding or repetitive sequences.

- Evolutionary Insights:
  - The AT-rich genome aligns with known insect genome characteristics.
  - Potential evolutionary adaptations for bioluminescence.

## Future Work
- Extend analysis to larger datasets.
- Investigate bioluminescence-related genes and their evolutionary significance.
- Functional annotation of GC-rich regions.

---

## Author
- **Sravya Sri Mallampalli**
  - [GitHub Profile](https://github.com/Sravz2433)
  - [LinkedIn](https://www.linkedin.com/in/sravya-sri-mallampalli)

---

## License
This project is licensed under the MIT License.
