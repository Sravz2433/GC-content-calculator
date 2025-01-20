import argparse
from Bio import SeqIO

def calculate_gc_content(sequence):
    """
    Calculate GC content percentage for a given DNA sequence.
    :param sequence: DNA sequence (string)
    :return: GC content as a float
    """
    g_count = sequence.upper().count("G")
    c_count = sequence.upper().count("C")
    total_count = len(sequence)

    if total_count == 0:
        return 0.0

    gc_content = ((g_count + c_count) / total_count) * 100
    return gc_content

def process_fasta(input_files, output_file):
    """
    Process multiple FASTA files and calculate GC content for each sequence.
    Save the results to a specified output file.
    :param input_files: List of FASTA file paths
    :param output_file: Path to the output file
    """
    with open(output_file, "w") as out:
        for input_file in input_files:
            out.write(f"\nProcessing file: {input_file}\n")
            print(f"\nProcessing file: {input_file}")
            try:
                sequences = SeqIO.parse(input_file, "fasta")
                total_gc = 0
                total_sequences = 0

                for record in sequences:
                    total_sequences += 1
                    gc_content = calculate_gc_content(str(record.seq))
                    total_gc += gc_content
                    result = f"Sequence: {record.id}, GC Content: {gc_content:.2f}%"
                    out.write(result + "\n")
                    print(result)

                if total_sequences > 0:
                    average_gc = total_gc / total_sequences
                    result = f"Average GC Content for {input_file}: {average_gc:.2f}%"
                    out.write(result + "\n")
                    print(result)
                else:
                    result = f"No sequences found in {input_file}."
                    out.write(result + "\n")
                    print(result)

            except Exception as e:
                error_message = f"Error processing file {input_file}: {e}"
                out.write(error_message + "\n")
                print(error_message)

def main():
    parser = argparse.ArgumentParser(description="Calculate GC content for sequences in multiple FASTA files.")
    parser.add_argument("--input", nargs="+", required=True, help="Paths to the input FASTA files (space-separated).")
    parser.add_argument("--output", required=True, help="Path to the output file.")

    args = parser.parse_args()

    print("Starting GC content calculation for multiple files...")
    process_fasta(args.input, args.output)

if __name__ == "__main__":
    main()
