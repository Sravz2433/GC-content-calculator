import matplotlib.pyplot as plt

def read_gc_content_from_file(output_file):
    """
    Reads sequence IDs and GC content from the output file.
    :param output_file: Path to the output file containing processed GC content data.
    :return: A tuple (sequence_ids, gc_content, average_gc).
    """
    sequence_ids = []
    gc_content = []
    average_gc = None

    with open(output_file, "r") as file:
        for line in file:
            if line.startswith("Sequence:"):
                parts = line.split(",")
                seq_id = parts[0].split(":")[1].strip()
                gc = float(parts[1].split(":")[1].strip().replace("%", ""))
                sequence_ids.append(seq_id)
                gc_content.append(gc)
            elif line.startswith("Average GC Content"):
                average_gc = float(line.split(":")[1].strip().replace("%", ""))
    
    return sequence_ids, gc_content, average_gc

# Path to the output file
output_file = "result.txt"  # Replace with the actual path to your output file

# Read data
sequence_ids, gc_content, average_gc = read_gc_content_from_file(output_file)

# Plot
plt.figure(figsize=(10, 6))
bars = plt.bar(sequence_ids, gc_content, color=["orange" if gc < average_gc else "yellow" for gc in gc_content])

# Highlight the average GC content as a horizontal line
plt.axhline(y=average_gc, color="red", linestyle="--", label=f"Average GC Content: {average_gc:.2f}%")

# Add labels above the bars to show the difference from the average
for bar, gc in zip(bars, gc_content):
    diff = gc - average_gc
    label = f"{diff:+.2f}%"  # Show positive or negative difference
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), label, ha="center", va="bottom", fontsize=10)

# Add labels and title
plt.xlabel("Sequence ID", fontsize=12)
plt.ylabel("GC Content (%)", fontsize=12)
plt.title("GC Content Across Sequences with Average Comparison", fontsize=14)
plt.legend()
plt.tight_layout()

plt.show()
