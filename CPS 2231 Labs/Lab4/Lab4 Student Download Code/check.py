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

# Define test cases for Lab4_1 and Lab4_2 with problem description for Lab4_2
test_cases = {
    "Lab4_1": [
        {
            "input": "banana\na\n",
            "expected": "3",
            "desc": "countChar(\"banana\", 'a') should return 3"
        },
        {
            "input": "hello\nl\n",
            "expected": "2",
            "desc": "countChar(\"hello\", 'l') should return 2"
        },
        {
            "input": "xyz\nw\n",
            "expected": "0",
            "desc": "countChar(\"xyz\", 'w') should return 0"
        },
        {
            "input": "\na\n",
            "expected": "0",
            "desc": "countChar(\"\", 'a') should return 0"
        },
        {
            "input": "a\na\n",
            "expected": "1",
            "desc": "countChar(\"a\", 'a') should return 1"
        },
        {
            "input": "aa\na\n",
            "expected": "2",
            "desc": "countChar(\"aa\", 'a') should return 2"
        },
        {
            "input": "abc\nb\n",
            "expected": "1",
            "desc": "countChar(\"abc\", 'b') should return 1"
        },
        {
            "input": "abcabc\nc\n",
            "expected": "2",
            "desc": "countChar(\"abcabc\", 'c') should return 2"
        },
        {
            "input": "ABC\na\n",
            "expected": "0",
            "desc": "countChar(\"ABC\", 'a') should return 0"
        },
        {
            "input": "Aa\na\n",
            "expected": "1",
            "desc": "countChar(\"Aa\", 'a') should return 1"
        }
    ],
    "Lab4_2": [
        {
            "input": "aba\n",
            "expected": "4",
            "desc": "countPalindromicSubstrings(\"aba\") should return 4 (palindromes: \"a\", \"b\", \"a\", \"aba\")"
        },
        {
            "input": "aaa\n",
            "expected": "6",
            "desc": "countPalindromicSubstrings(\"aaa\") should return 6 (palindromes: \"a\", \"a\", \"a\", \"aa\", \"aa\", \"aaa\")"
        },
        {
            "input": "xy\n",
            "expected": "2",
            "desc": "countPalindromicSubstrings(\"xy\") should return 2 (palindromes: \"x\", \"y\")"
        },
        {
            "input": "\n",
            "expected": "0",
            "desc": "countPalindromicSubstrings(\"\") should return 0 (empty string has no substrings)"
        },
        {
            "input": "a\n",
            "expected": "1",
            "desc": "countPalindromicSubstrings(\"a\") should return 1 (palindrome: \"a\")"
        },
        {
            "input": "aa\n",
            "expected": "3",
            "desc": "countPalindromicSubstrings(\"aa\") should return 3 (palindromes: \"a\", \"a\", \"aa\")"
        },
        {
            "input": "abc\n",
            "expected": "3",
            "desc": "countPalindromicSubstrings(\"abc\") should return 3 (palindromes: \"a\", \"b\", \"c\")"
        },
        {
            "input": "abba\n",
            "expected": "6",
            "desc": "countPalindromicSubstrings(\"abba\") should return 6 (palindromes: \"a\", \"b\", \"b\", \"a\", \"bb\", \"abba\")"
        },
        {
            "input": "racecar\n",
            "expected": "10",
            "desc": "countPalindromicSubstrings(\"racecar\") should return 10 (palindromes: \"r\", \"a\", \"c\", \"e\", \"c\", \"a\", \"r\", \"cec\", \"aceca\", \"racecar\")"
        },
        {
            "input": "abcd\n",
            "expected": "4",
            "desc": "countPalindromicSubstrings(\"abcd\") should return 4 (palindromes: \"a\", \"b\", \"c\", \"d\")"
        }
    ]
}

# Problem Description for Lab4_2 included as a docstring

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

def check_output(output, expected_output, lab, test_case_desc):
    """Check if the output matches the expected pattern."""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    answer_sheet = load_answer_sheet()

    try:
        output_int = int(output.strip())
        expected_int = int(expected_output)
        if output_int == expected_int:
            console.print(f"\n[bold green]✅ Output is correct: {output_int}[/bold green]")
            answer_sheet.append({
                'time': current_time,
                'lab': lab,
                'test_case': test_case_desc,
                'result': 'Passed',
                'output': output_int
            })
            save_answer_sheet(answer_sheet)
            return True
        else:
            console.print(f"\n[bold red]❌ Output is incorrect! Expected {expected_int}, got {output_int}[/bold red]")
            answer_sheet.append({
                'time': current_time,
                'lab': lab,
                'test_case': test_case_desc,
                'result': 'Failed',
                'error': f"Expected: {expected_int}, Actual: {output_int}"
            })
            save_answer_sheet(answer_sheet)
            return False
    except ValueError:
        console.print(f"\n[bold red]❌ Output is not an integer: {output}[/bold red]")
        answer_sheet.append({
            'time': current_time,
            'lab': lab,
            'test_case': test_case_desc,
            'result': 'Failed',
            'error': f"Output is not an integer: {output}"
        })
        save_answer_sheet(answer_sheet)
        return False

def zip_files(student_id, labs):
    """Zip the Java files and answer sheet into a submission package."""
    console.print(f"\n[bold cyan]********* Zipping Files *********[/bold cyan]")
    submit_files = [f"{lab}.java" for lab in labs] + ["answer_sheet.pickle"]
    timestamp = datetime.now().strftime("%m%d_%H%M")
    zip_file_name = f"Lab4_{student_id}_{timestamp}.zip"
    with zipfile.ZipFile(zip_file_name, "w") as zip_file:
        for file in submit_files:
            if not os.path.exists(file):
                raise FileNotFoundError(f"File {file} not found in {os.getcwd()}")
            console.print(f"Zipping {file}...", end=" ")
            zip_file.write(file)
            console.print("[green]Done.[/green]")
    return zip_file_name

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check Java labs or submit all.")
    parser.add_argument("--lab", type=str, choices=["Lab4_1", "Lab4_2"], help="Specific lab to check.")
    parser.add_argument("--uid", type=str, help="Student ID to check all labs and zip files.")
    args = parser.parse_args()

    if args.lab:
        labs_to_check = [args.lab]
        check_all = False
    elif args.uid:
        labs_to_check = ["Lab4_1", "Lab4_2"]
        student_id = args.uid
        check_all = True
    else:
        console.print("[bold red]❌ Please specify --lab or --uid[/bold red]")
        sys.exit(1)

    all_passed = True

    for lab in labs_to_check:
        java_file = f"{lab}.java"
        class_name = lab

        if not os.path.exists(java_file):
            console.print(f"\n[bold red]❌ File {java_file} not found![/bold red]")
            all_passed = False
            break

        if not compile_java_file(java_file):
            all_passed = False
            break

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
            break

    if all_passed and check_all:
        console.print("\n[bold green]✅ All checks passed![/bold green]")
        
        console.print(f"\nYour Student ID is [bold]{student_id}[/bold]. Is this correct? (y/n): ", end="")
        if input().lower() == "y":
            try:
                zip_name = zip_files(student_id, labs_to_check)
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