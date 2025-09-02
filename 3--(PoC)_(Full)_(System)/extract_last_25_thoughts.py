#!/usr/bin/env python3
"""
Sequential Thinking Thought Extractor - Last 25 Thoughts
Extracts the last 25 thoughts from MCP logs for text-to-speech conversion
"""
import json
import re
import sys
from datetime import datetime

def extract_last_n_thoughts(log_file_path, output_file_path, n=25):
    """
    Extract the last N sequential thinking thoughts from MCP log files.
    
    Args:
        log_file_path: Path to the MCP log file containing sequential thoughts
        output_file_path: Path where cleaned thoughts should be saved
        n: Number of last thoughts to extract (default: 25)
    """
    # Read the log file
    with open(log_file_path, "r") as f:
        content = f.read()

    # Find all lines containing sequential thinking calls
    # This pattern matches the JSON structure in MCP logs for sequentialthinking tool calls
    pattern = r'"arguments":\{[^}]*"thought":"([^"]*)"[^}]*"thoughtNumber":(\d+\.0)[^}]*"totalThoughts":(\d+\.0)[^}]*\}'
    matches = re.findall(pattern, content)

    # Create a list to store all thoughts with their original order
    all_thoughts = []
    for thought_text, thought_num, total_thoughts in matches:
        num = int(float(thought_num))
        total = int(float(total_thoughts))
        # Unescape the thought text
        thought_text = thought_text.replace('\\n', '\n')
        thought_text = thought_text.replace('\\"', '"')
        thought_text = thought_text.replace('\\\\', '\\')
        all_thoughts.append({
            'text': thought_text,
            'number': num,
            'total': total,
            'order': len(all_thoughts)  # Track the order they appear in the log
        })

    # Get the last N thoughts based on their order in the log
    last_n_thoughts = all_thoughts[-n:] if len(all_thoughts) >= n else all_thoughts

    # Write to the output file
    with open(output_file_path, "w") as f:
        f.write(f"# Last {min(n, len(last_n_thoughts))} Sequential Thinking Thoughts\n")
        f.write(f"Extracted from: {log_file_path}\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("---\n\n")
        
        for i, thought in enumerate(last_n_thoughts, 1):
            # Add thought metadata and text
            f.write(f"## Thought {i} (Original: {thought['number']}/{thought['total']})\n\n")
            f.write(thought['text'] + "\n\n")
            f.write("---\n\n")

    print(f"Extracted {len(last_n_thoughts)} thoughts to {output_file_path}")
    return len(last_n_thoughts)

# Main execution
if __name__ == "__main__":
    # Use the most recent log file
    LOG_FILE = "/Users/chrishamlin/Library/Application Support/dev.warp.Warp-Stable/mcp/lmfv2eiQCmRNiHuKzhxBWo.log"
    OUTPUT_FILE = "/Users/chrishamlin/CodingProjects/Fractal-RMO/3--(PoC)_(Full)_(System)/last_25_thoughts.md"
    NUM_THOUGHTS = 25
    
    # Allow command line arguments to override defaults
    if len(sys.argv) > 1:
        LOG_FILE = sys.argv[1]
    if len(sys.argv) > 2:
        OUTPUT_FILE = sys.argv[2]
    if len(sys.argv) > 3:
        NUM_THOUGHTS = int(sys.argv[3])
    
    extract_last_n_thoughts(LOG_FILE, OUTPUT_FILE, NUM_THOUGHTS)
