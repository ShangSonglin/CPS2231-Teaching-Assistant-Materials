from rich import print as rprint
from rich.console import Console
import subprocess
import sys
import os
import re
import argparse
from datetime import datetime
import zipfile

console = Console()

# Define test cases for each lab
test_cases = {
    "Lab1_1": [
        {"input": "1.1.1.1\n", "expected": "1[.]1[.]1[.]1", "desc": "Valid IP 1"},
        {"input": "255.100.50.0\n", "expected": "255[.]100[.]50[.]0", "desc": "Valid IP 2"},
        {"input": "255.100.0\n", "expected": "Invalid IP address.", "desc": "Invalid IP"},
    ],
    "Lab1_2": [
        {"input": "A man, a plan, a canal: Panama\n", "expected": "true", "desc": "Palindrome 1"},
        {"input": "race a car\n", "expected": "false", "desc": "Not a Palindrome"},
        {"input": " \n", "expected": "true", "desc": "Empty String"},
    ],
    "Lab1_3": [
        {"input": "1\n3\n", "expected": "Today is Monday and the future day is Thursday", "desc": "Monday + 3 days"},
        {"input": "0\n31\n", "expected": "Today is Sunday and the future day is Wednesday", "desc": "Sunday + 31 days"},
        {"input": "7\n5\n", "expected": "Invalid Input", "desc": "Invalid day"},
    ],
    "Lab1_4": [
        {"input": "2.5 4 2.5 43\n1.5 5 0.5 3\n", "expected": "r2 is inside r1", "desc": "r2 inside r1"},
        {"input": "1 2 3 5.5\n3 4 4.5 5\n", "expected": "r2 overlaps r1", "desc": "r2 overlaps r1"},
        {"input": "1 2 3 3\n40 45 3 2\n", "expected": "r2 does not overlap r1", "desc": "No overlap"},
    ],
}

def modify_package_statement(java_file, comment=True):
    """
    Modify the package statement in a Java file by adding or removing double slash comments.
    
    Args:
        java_file (str): Path to the Java file.
        comment (bool): True to comment out the package statement, False to uncomment it.
    
    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        with open(java_file, 'r') as file:
            content = file.read()
        if comment:
            modified_content = re.sub(r'^(package\s+[^;]+;)', r'//\1', content, flags=re.MULTILINE)
        else:
            modified_content = re.sub(r'^//(package\s+[^;]+;)', r'\1', content, flags=re.MULTILINE)
        with open(java_file, 'w') as file:
            file.write(modified_content)
        return True
    except Exception as e:
        console.print(f"\n[bold red]❌ Failed to modify {java_file}: {str(e)}[/bold red]")
        return False

def compile_java_file(java_file):
    """
    Compile a Java file after commenting out the package statement.
    
    Args:
        java_file (str): Path to the Java file.
    
    Returns:
        bool: True if compilation succeeds, False otherwise.
    """
    console.print(f"\n[bold cyan]********* Compiling Java file: {java_file} *********[/bold cyan]")
    if not modify_package_statement(java_file, comment=True):
        return False
    result = subprocess.run(["javac", java_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    modify_package_statement(java_file, comment=False)
    if result.returncode != 0:
        console.print(f"\n[bold red]❌ Compilation failed![/bold red]")
        console.print(result.stderr)
        return False
    else:
        console.print(f"\n[bold green]✅ Compilation succeeded![/bold green]")
        return True

import re

def run_java_program(class_name, input_str):
    """
    Run a Java program with given input and capture its output.
    """
    console.print(f"\n[bold cyan]********* Running Java program: {class_name} *********[/bold cyan]")
    result = subprocess.run(["java", class_name], input=input_str, capture_output=True, text=True)
    if result.returncode != 0:
        console.print(f"\n[bold red]❌ Execution failed![/bold red]")
        console.print(result.stderr)
        return None
    else:
        console.print(f"\n[bold green]✅ Execution succeeded![/bold green]")
        # Capture the full output and split into lines
        output = result.stdout.strip()
        output_lines = [line for line in output.split('\n') if line.strip()]
        # Return the last non-empty line, or an empty string if none exist
        if output_lines:
            return output_lines[-1].strip()
        return ""
    
    

def check_output(output, expected_output):
    """
    Check if the program's output matches the expected output.
    
    Args:
        output (str): Actual output from the program.
        expected_output (str): Expected output for the test case.
    
    Returns:
        bool: True if the output matches, False otherwise.
    """
    if output == expected_output:
        console.print(f"\n[bold green]✅ Output is correct: {output}[/bold green]")
        return True
    else:
        console.print(f"\n[bold red]❌ Output is incorrect![/bold red]")
        console.print(f"Expected output: {expected_output}")
        console.print(f"Actual output: {output}")
        return False

def zip_files(student_id):
    """
    Zip the Java files for submission.
    
    Args:
        student_id (str): Student's ID to include in the zip filename.
    
    Returns:
        str: Name of the created zip file.
    
    Raises:
        FileNotFoundError: If any required file is missing.
    """
    console.print(f"\n[bold cyan]********* Zipping Files *********[/bold cyan]")
    submit_files = ["Lab1_1.java", "Lab1_2.java", "Lab1_3.java", "Lab1_4.java"]
    timestamp = datetime.now().strftime("%m%d_%H%M")
    zip_file_name = f"Lab1_{student_id}_{timestamp}.zip"
    with zipfile.ZipFile(zip_file_name, "w") as zip_file:
        for file in submit_files:
            if not os.path.exists(file):
                raise FileNotFoundError(f"File {file} not found in {os.getcwd()}")
            console.print(f"Zipping {file}...", end=" ")
            zip_file.write(file)
            console.print("[green]Done.[/green]")
    return zip_file_name

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Check Java labs or submit all.")
    parser.add_argument("--lab", type=str, choices=["Lab1_1", "Lab1_2", "Lab1_3", "Lab1_4"], help="Specific lab to check.")
    parser.add_argument("--uid", type=str, help="Student ID to check all labs and zip files.")
    args = parser.parse_args()

    # Determine which labs to check
    if args.lab:
        labs_to_check = [args.lab]
        check_all = False
    elif args.uid:
        labs_to_check = ["Lab1_1", "Lab1_2", "Lab1_3", "Lab1_4"]
        student_id = args.uid
        check_all = True
    else:
        console.print("[bold red]❌ Please specify --lab or --uid[/bold red]")
        sys.exit(1)

    all_passed = True

    # Check each lab
    for lab in labs_to_check:
        java_file = f"{lab}.java"
        class_name = lab

        # Compile the Java file
        if not os.path.exists(java_file):
            console.print(f"\n[bold red]❌ File {java_file} not found![/bold red]")
            all_passed = False
            break
        if not compile_java_file(java_file):
            all_passed = False
            break

        # Run test cases
        for test_case in test_cases[lab]:
            console.print(f"\n[bold cyan]Running test case: {test_case['desc']}[/bold cyan]")
            output = run_java_program(class_name, test_case["input"])
            if output is None:
                all_passed = False
                break
            if not check_output(output, test_case["expected"]):
                all_passed = False
                break
        if not all_passed:
            break

    # Handle results
    if all_passed and check_all:
        console.print("\n[bold green]✅ All checks passed![/bold green]")
        console.print(f"\nYour Student ID is [bold]{student_id}[/bold]. Is this correct? (y/n): ", end="")
        if input().lower() == "y":
            try:
                zip_name = zip_files(student_id)
                console.print(f"\n[bold green]📦 Successfully created submission package: {zip_name}[/bold green]")
            except Exception as e:
                console.print(f"\n[bold red]❌ Error during zipping: {str(e)}[/bold red]")
                sys.exit(1)
        else:
            console.print("[yellow]Zip operation canceled.[/yellow]")
    elif all_passed:
        console.print("\n[bold green]✅ All checks passed for the specified lab![/bold green]")
    else:
        console.print("\n[bold red]❌ Some checks failed.[/bold red]")