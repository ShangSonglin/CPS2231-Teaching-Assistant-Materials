from rich import print as rprint
from rich.console import Console
import subprocess
import sys
import os
import re
import argparse
from datetime import datetime
import zipfile
import pickle

console = Console()

# Define test cases.  Lab5_3 is now included, but the check for it is conditional.
test_cases = {
    "Lab5_1": [
        {
            "input": "0\n-10\n",
            "expected": "Integer Object: 0\nPrimitive int value (after unboxing): 0\nInteger Object + 5 = 5\nInteger Object (this line might not be reached): -10",
            "desc": "Valid input: 0 and -10"
        },
        {
            "input": "999999999\n1\n",
            "expected": "Integer Object: 999999999\nPrimitive int value (after unboxing): 999999999\nInteger Object + 5 = 1000000004\nInteger Object (this line might not be reached): 1",
            "desc": "Valid input: large number and 1"
        },
        {
            "input": "abc\n123\n",
            "expected": "Invalid Input.",  # Expect "Invalid Input." from main method
            "desc": "Invalid first input: abc"
        },
        {
            "input": "123\nabc\n",
            "expected": "Integer Object: 123\nPrimitive int value (after unboxing): 123\nInteger Object + 5 = 128\n",  # Output before the crash
            "desc": "Invalid second input: abc (expecting NumberFormatException)"
        },
        {
            "input": "123\n1.23\n",
            "expected": "Integer Object: 123\nPrimitive int value (after unboxing): 123\nInteger Object + 5 = 128\n",
            "desc": "Invalid input: 1.23 (expecting NumberFormatException)"
        },
    ],
    "Lab5_2": [
        {"input": "100\n", "expected": "93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000", "desc": "Large input"},
        {"input": "-5\n", "expected": "Invalid Input.", "desc": "Negative input"},
        {"input": "0\n", "expected": "1", "desc": "Zero input"},
        {"input": "abc\n", "expected": "Invalid Input.", "desc": "Non-numeric input"},
        {"input": "\n", "expected": "Invalid Input.", "desc": "Empty input"},
    ],
    "Lab5_3": [
    {
        "input": "hello world",
        "expected": "olleh dlrow",
        "desc": "Reverse each word in the sentence"
    },
    {
        "input": "java programming",
        "expected": "avaj gnimmargorp",
        "desc": "Reverse each word in the sentence"
    },
    {
        "input": "apple banana cherry",
        "expected": "elppa ananab yrrehc",
        "desc": "Reverse each word in the sentence"
    },
    {
        "input": "race car",
        "expected": "ecar rac",
        "desc": "Reverse each word in the sentence"
    },
    {
        "input": "hello",
        "expected": "olleh",
        "desc": "Reverse a single word"
    },

]

}

ANSWER_SHEET_FILE = 'answer_sheet.pickle'

def load_answer_sheet():
    """Load the answer sheet from pickle file, or return an empty list if it doesn't exist."""
    if os.path.exists(ANSWER_SHEET_FILE):
        with open(ANSWER_SHEET_FILE, 'rb') as f:
            return pickle.load(f)
    return []

def save_answer_sheet(answer_sheet):
    """Save the answer sheet to a pickle file."""
    with open(ANSWER_SHEET_FILE, 'wb') as f:
        pickle.dump(answer_sheet, f)

def modify_package_statement(java_file, comment=True):
    """Add or remove comments from the package statement in the Java file."""
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
    """Compile the Java file after commenting out the package statement."""
    console.print(f"\n[bold cyan]********* Compiling Java file: {java_file} *********[/bold cyan]")
    if not modify_package_statement(java_file, comment=True):
        return False
    result = subprocess.run(["javac", java_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    modify_package_statement(java_file, comment=False)
    if result.returncode != 0:
        console.print(f"\n[bold red]❌ Compilation failed![/bold red]")
        console.print(result.stderr)
        return False
    console.print(f"\n[bold green]✅ Compilation succeeded![/bold green]")
    return True

def run_java_program(class_name, input_str):
    """Run the Java program and capture its output."""
    console.print(f"\n[bold cyan]********* Running Java program: {class_name} *********[/bold cyan]")
    result = subprocess.run(["java", class_name], input=input_str, capture_output=True, text=True)
    if result.returncode != 0:
        console.print(f"\n[bold red]❌ Execution failed![/bold red]")
        console.print(result.stderr)
        return None, result.stderr
    console.print(f"\n[bold green]✅ Execution succeeded![/bold green]")
    output = result.stdout.strip()
    return output, None

import re

import re

def check_output(output, expected_output, lab, test_case_desc):
    """Check if the output matches the expected output."""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    answer_sheet = load_answer_sheet()

    #  Use regular expressions to remove the prompts
    if lab == "Lab5_1":
        cleaned_output = re.sub(r"Enter the first integer:\s*", "", output)
        cleaned_output = re.sub(r"Enter the second value \(might be invalid\):\s*", "", cleaned_output)
    elif lab == "Lab5_3":
        cleaned_output = re.sub(r"Enter a sentence:\s*", "", output)
        cleaned_output = re.sub(r"Reversed sentence:\s*", "", cleaned_output)
    else:
        cleaned_output = output  # If it's another lab, don't modify the output

    cleaned_output = cleaned_output.strip()  # Remove any leading/trailing whitespace

    if cleaned_output == expected_output.strip():
        console.print(f"\n[bold green]✅ Output is correct:\n{cleaned_output}[/bold green]")
        answer_sheet.append({
            'time': current_time,
            'lab': lab,
            'test_case': test_case_desc,
            'result': 'Passed',
            'output': cleaned_output
        })
        save_answer_sheet(answer_sheet)
        return True
    else:
        console.print(f"\n[bold red]❌ Output is incorrect!\nExpected:\n{expected_output}\nGot:\n{cleaned_output}[/bold red]")
        answer_sheet.append({
            'time': current_time,
            'lab': lab,
            'test_case': test_case['desc'],
            'result': 'Failed',
            'error': f"Expected:\n{expected_output}\nActual:\n{cleaned_output}"
        })
        save_answer_sheet(answer_sheet)
        return False
    

def zip_files(student_id, labs):
    """Zip the Java files and answer sheet into a submission package."""
    console.print(f"\n[bold cyan]********* Zipping Files *********[/bold cyan]")
    timestamp = datetime.now().strftime("%m%d_%H%M")
    zip_file_name = f"Lab5_{student_id}_{timestamp}.zip"
    files_to_zip = []
    for lab in labs:
        java_file = f"{lab}.java"
        if os.path.exists(java_file):  # Only include if file exists
            files_to_zip.append(java_file)
        else:
            console.print(f"[yellow]⚠️  File {java_file} not found. Skipping.[/yellow]")

    files_to_zip.append("answer_sheet.pickle")  # Always include answer sheet

    if not files_to_zip:
        console.print("[bold red]❌  No files to zip.  Check that the required files exist.[/bold red]")
        sys.exit(1)
        
    with zipfile.ZipFile(zip_file_name, "w") as zip_file:
        for file in files_to_zip:
            if not os.path.exists(file):
                raise FileNotFoundError(f"File {file} not found in {os.getcwd()}")
            console.print(f"Zipping {file}...", end=" ")
            zip_file.write(file)
            console.print("[green]Done.[/green]")
    return zip_file_name

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check Java labs or submit all.")
    parser.add_argument("--lab", type=str, choices=["Lab5_1", "Lab5_2", "Lab5_3"], help="Specific lab to check.")
    parser.add_argument("--uid", type=str, help="Student ID to check all labs and zip files.")
    args = parser.parse_args()

    # Default behavior: check all labs that have test cases defined
    labs_to_check = ["Lab5_1", "Lab5_2"]  #  Always check Lab5_1 and Lab5_2
    if args.lab:
        labs_to_check = [args.lab]
        check_all = False
    elif args.uid:
        completed_lab3 = console.input("\n[bold yellow]Have you completed Lab5_3? (y/n): [/bold yellow]").strip().lower()
        include_lab3 = completed_lab3 == 'y'
        labs_to_check = ["Lab5_1", "Lab5_2", "Lab5_3"] if include_lab3 else ["Lab5_1", "Lab5_2"]
        student_id = args.uid
        check_all = True
    else:
        check_all = False # If no args, do not check all and do not zip.

    all_passed = True
    labs_checked = [] # Keep track of which labs were actually checked

    for lab in labs_to_check:
        java_file = f"{lab}.java"
        class_name = lab

        if not os.path.exists(java_file):
            console.print(f"\n[bold red]❌ File {java_file} not found![/bold red]")
            #  Don't set all_passed to False here.  We want to allow partial submissions.
            continue  # Skip to the next lab
        
        labs_checked.append(lab) # Add to the list of checked labs

        if not compile_java_file(java_file):
            all_passed = False
            break  # Stop checking if compilation fails

        if lab in test_cases: # Only try to run tests if test cases exist.
            for test_case in test_cases[lab]:
                console.print(f"\n[bold cyan]Running test case: {test_case['desc']}[/bold cyan]")
                input_str = test_case["input"]
                output, error = run_java_program(class_name, input_str)
                
                if output is None:  # Execution failed
                    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    answer_sheet = load_answer_sheet()
                    answer_sheet.append({
                        'time': current_time,
                        'lab': lab,
                        'test_case': test_case['desc'],
                        'result': 'Failed',
                        'error': error
                    })
                    save_answer_sheet(answer_sheet)
                    all_passed = False
                    break
                    
                if not check_output(output, test_case["expected"], lab, test_case['desc']):
                    all_passed = False
                    break
            if not all_passed:
                break # Stop checking other test cases for the same lab.

    if check_all:
        if all_passed:
            console.print("\n[bold green]✅ All checks passed![/bold green]")
        else:
            console.print("\n[bold red]❌ Some checks failed.[/bold red]")
            
        console.print(f"\nYour Student ID is [bold]{student_id}[/bold]. Is this correct? (y/n): ", end="")
        if input().lower() == "y":
            try:
                zip_name = zip_files(student_id, labs_checked) # Pass the list of checked labs to zip_files
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
