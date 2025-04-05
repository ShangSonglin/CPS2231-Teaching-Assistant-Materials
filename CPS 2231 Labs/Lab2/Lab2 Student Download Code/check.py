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

# Define test cases for Lab2_1 and Lab2_2
test_cases = {
    "Lab2_1": [
        {
            "input": "12\n",
            "expected": r"After .+'s contribution, Fibonacci Series till 12 terms: 1 1 2 3 5 8 13 21 34 55 89 144",
            "desc": "Valid input 12"
        },
        {
            "input": "5\n",
            "expected": r"After .+'s contribution, Fibonacci Series till 5 terms: 1 1 2 3 5",
            "desc": "Valid input 5"
        },
        {
            "input": "a\n",
            "expected": "Invalid Input.",
            "desc": "Invalid input a"
        },
        {
            "input": "-1\n",
            "expected": "Invalid Input.",
            "desc": "Invalid input -1"
        },
        {
            "input": "0\n",
            "expected": "Invalid Input.",
            "desc": "Invalid input 0"
        }
    ],
    "Lab2_2": [
        {
            "input": "5 10\n",
            "expected": r".+ multiplicative table is:\s*1\s+2\s+3\s+4\s+5\s+6\s+7\s+8\s+9\s+10\s*2\s+4\s+6\s+8\s+10\s+12\s+14\s+16\s+18\s+20\s*3\s+6\s+9\s+12\s+15\s+18\s+21\s+24\s+27\s+30\s*4\s+8\s+12\s+16\s+20\s+24\s+28\s+32\s+36\s+40\s*5\s+10\s+15\s+20\s+25\s+30\s+35\s+40\s+45\s+50",
            "desc": "Valid input 5 10"
        },
        {
            "input": "3 5\n",
            "expected": r".+ multiplicative table is:\s*1\s+2\s+3\s+4\s+5\s*2\s+4\s+6\s+8\s+10\s*3\s+6\s+9\s+12\s+15",
            "desc": "Valid input 3 5"
        },
        {
            "input": "a b\n",
            "expected": "Invalid Input.",
            "desc": "Invalid input a b"
        },
        {
            "input": "-1 10\n",
            "expected": "Invalid Input.",
            "desc": "Invalid input -1 10"
        },
        {
            "input": "0 0\n",
            "expected": "Invalid Input.",
            "desc": "Invalid input 0 0"
        }
    ],
    "Lab2_3": [
        {
            "input": "1 3 4 2 5 3\n",
            "expected": 3,
            "desc": "Example 1: cycle starts at 3"
        },
        {
            "input": "1 2 3 4\n",
            "expected": -1,
            "desc": "Example 2: no cycle"
        },
        {
            "input": "1 2 0\n",
            "expected": 0,
            "desc": "Example 3: cycle starts at 0"
        },
        {
            "input": "3 1 2 0\n",
            "expected": 0,
            "desc": "Example 4: cycle starts at 0"
        },
        {
            "input": "0\n",
            "expected": 0,
            "desc": "Single element cycle"
        },
        {
            "input": "5\n",
            "expected": -1,
            "desc": "Single element jumps out"
        },
        {
            "input": "1 0\n",
            "expected": 0,
            "desc": "Two elements forming a cycle"
        },
        {
            "input": "2 2 3\n",
            "expected": -1,
            "desc": "Path jumps out of array"
        },
        {
            "input": "2 0 1\n",
            "expected": 0,
            "desc": "Cycle 0→2→1→0"
        }
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

def check_output(output, expected_output, lab, test_case_desc):
    """Check if the output matches the expected pattern."""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    answer_sheet = load_answer_sheet()

    if lab == "Lab2_3":
        try:
            output_int = int(output.strip())
        except:
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
        if output_int == expected_output:
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
            console.print(f"\n[bold red]❌ Output is incorrect! Expected {expected_output}, got {output_int}[/bold red]")
            answer_sheet.append({
                'time': current_time,
                'lab': lab,
                'test_case': test_case_desc,
                'result': 'Failed',
                'error': f"Expected: {expected_output}, Actual: {output_int}"
            })
            save_answer_sheet(answer_sheet)
            return False

    elif lab in ["Lab2_1", "Lab2_2"]:
        if expected_output == "Invalid Input.":
            if output.strip() == "Invalid Input.":
                console.print(f"\n[bold green]✅ Output is correct: {output}[/bold green]")
                answer_sheet.append({'time': current_time, 'lab': lab, 'test_case': test_case_desc, 'result': 'Passed', 'output': output})
                save_answer_sheet(answer_sheet)
                return True
            console.print(f"\n[bold red]❌ Output is incorrect![/bold red]")
            console.print(f"Expected: Invalid Input.")
            console.print(f"Actual: {output}")
            answer_sheet.append({'time': current_time, 'lab': lab, 'test_case': test_case_desc, 'result': 'Failed', 'error': f"Expected: Invalid Input., Actual: {output}"})
            save_answer_sheet(answer_sheet)
            return False
        
        pattern = re.compile(expected_output, re.DOTALL) if lab == "Lab2_2" else re.compile(expected_output)
        if pattern.fullmatch(output.strip()):
            console.print(f"\n[bold green]✅ Output is correct: {output}[/bold green]")
            answer_sheet.append({'time': current_time, 'lab': lab, 'test_case': test_case_desc, 'result': 'Passed', 'output': output})
            save_answer_sheet(answer_sheet)
            return True
        console.print(f"\n[bold red]❌ Output format is incorrect![/bold red]")
        console.print(f"Expected pattern: {expected_output}")
        console.print(f"Actual output: {output}")
        answer_sheet.append({'time': current_time, 'lab': lab, 'test_case': test_case_desc, 'result': 'Failed', 'error': f"Expected pattern: {expected_output}, Actual: {output}"})
        save_answer_sheet(answer_sheet)
        return False

    else:
        console.print(f"\n[bold red]❌ Unknown lab: {lab}[/bold red]")
        return False


def zip_files(student_id, include_lab3):
    """Zip the Java files and answer sheet into a submission package."""
    console.print(f"\n[bold cyan]********* Zipping Files *********[/bold cyan]")
    submit_files = ["Lab2_1.java", "Lab2_2.java", "answer_sheet.pickle"]
    if include_lab3:
        submit_files.append("Lab2_3.java")
    
    timestamp = datetime.now().strftime("%m%d_%H%M")
    zip_file_name = f"Lab2_{student_id}_{timestamp}.zip"
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
    parser.add_argument("--lab", type=str, choices=["Lab2_1", "Lab2_2", "Lab2_3"], help="Specific lab to check.")
    parser.add_argument("--uid", type=str, help="Student ID to check all labs and zip files.")
    args = parser.parse_args()

    if args.lab:
        labs_to_check = [args.lab]
        check_all = False
    elif args.uid:
        # Ask about Lab2_3 completion
        completed_lab3 = console.input("\n[bold yellow]Have you completed Lab2_3? (y/n): [/bold yellow]").strip().lower()
        include_lab3 = completed_lab3 == 'y'
        
        labs_to_check = ["Lab2_1", "Lab2_2", "Lab2_3"] if include_lab3 else ["Lab2_1", "Lab2_2"]
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
            
            if output is None:  # 执行失败
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
                zip_name = zip_files(student_id, include_lab3)
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