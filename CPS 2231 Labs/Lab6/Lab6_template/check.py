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

# Define test cases for Lab6_1, Lab6_2, and Lab6_3
test_cases = {
    "Lab6_1": [
        {
            "desc": "Bird Output",
            "type": "execution",
            "input": "Bird",
            "expected_output": r"Bird flies through the air\nBird chirps"
        },
        {
            "desc": "Panthera Output",
            "type": "execution",
            "input": "Panthera",
            "expected_output": r"Panthera stalks through the grass\nPanthera roars"
        },
        {
            "desc": "Animal Output",
            "type": "execution",
            "input": "Animal",
            "expected_output": r"Animal moves\nAnimal makes a sound"
        },
        {
            "desc": "Polymorphism with Bird",
            "type": "execution",
            "input": "PolyBird",
            "expected_output": r"Bird flies through the air\nBird chirps"
        },
        {
            "desc": "Polymorphism with Panthera",
            "type": "execution",
            "input": "PolyPanthera",
            "expected_output": r"Panthera stalks through the grass\nPanthera roars"
        }
    ],
    "Lab6_2": [
        {
            "desc": "Sorting Random Array",
            "type": "execution",
            "input": "5 3 8 4 2",
            "expected_output": r"Original array: \[5, 3, 8, 4, 2\]\nAfter sorting: \[2, 3, 4, 5, 8\]\nSort validation: PASSED"
        },
        {
            "desc": "Sorting Already Sorted Array",
            "type": "execution",
            "input": "1 2 3 4 5",
            "expected_output": r"Original array: \[1, 2, 3, 4, 5\]\nAfter sorting: \[1, 2, 3, 4, 5\]\nSort validation: PASSED"
        },
        {
            "desc": "Sorting Reverse Sorted Array",
            "type": "execution",
            "input": "5 4 3 2 1",
            "expected_output": r"Original array: \[5, 4, 3, 2, 1\]\nAfter sorting: \[1, 2, 3, 4, 5\]\nSort validation: PASSED"
        },
        {
            "desc": "Sorting Array with Duplicates",
            "type": "execution",
            "input": "3 1 4 1 5",
            "expected_output": r"Original array: \[3, 1, 4, 1, 5\]\nAfter sorting: \[1, 1, 3, 4, 5\]\nSort validation: PASSED"
        },
        {
            "desc": "Empty Array Handling",
            "type": "execution",
            "input": "",
            "expected_output": r"Original array: \[\]\nAfter sorting: \[\]\nSort validation: PASSED"
        }
    ],
    "Lab6_3": [
        {
            "desc": "Constructor Implementation",
            "type": "execution",
            "input": "create",
            "expected_output": r"Testing constructor\.\.\.\nCreated account: Account #A1001, Holder: John Doe, Balance: \$1,000\.00\nFields initialized correctly: OK\nCreated account with custom values: OK\nAll constructor tests passed!"
        },
        {
            "desc": "Getter/Setter Methods",
            "type": "execution",
            "input": "getset",
            "expected_output": r"Testing getter/setter methods\.\.\.\nInitial values:\nAccount #A1001, Holder: John Doe, Balance: \$1,000\.00\n\nSetting new values\.\.\.\nNew account number: B2002\nNew account holder: Jane Smith\nNew balance: \$2,500\.00\n\nGetting values after update:\nAccount #B2002, Holder: Jane Smith, Balance: \$2,500\.00\nAll getter/setter tests passed!"
        },
        {
            "desc": "Deposit Method",
            "type": "execution",
            "input": "deposit 500",
            "expected_output": r"Testing deposit[\s\S]*Initial balance: \$1,000\.00[\s\S]*Depositing: \$500\.00[\s\S]*New balance: \$1,500\.00[\s\S]*Deposit test passed!"
        },
        {
            "desc": "Withdraw Method",
            "type": "execution",
            "input": "withdraw 300",
            "expected_output": r"Testing withdrawal[\s\S]*Initial balance: \$1,000\.00[\s\S]*Withdrawing: \$300\.00[\s\S]*New balance: \$700\.00[\s\S]*Withdrawal test passed!"
        },
        {
            "desc": "Insufficient Funds",
            "type": "execution",
            "input": "withdraw 1500",
            "expected_output": r"Testing insufficient funds[\s\S]*Initial balance: \$1,000\.00[\s\S]*Attempting to withdraw: \$1,500\.00[\s\S]*Insufficient funds[\s\S]*Balance unchanged: \$1,000\.00[\s\S]*Insufficient funds test passed!"
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
    console.print(f"\n[bold cyan]********* Compiling {java_file} *********[/bold cyan]")
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
    console.print(f"\n[bold cyan]********* Running test for {class_name} *********[/bold cyan]")
    
    # Split input string into arguments and handle spaces correctly
    args = ["java", class_name]
    if input_str:
        # Remove surrounding quotes if present
        input_str = input_str.strip('"')
        # For Lab6_2, keep the input as a single argument
        if class_name == "Lab6_2":
            args.append(input_str)
        else:
            # For other labs, split the input into separate arguments
            args.extend(input_str.split())
    
    result = subprocess.run(args, capture_output=True, text=True)
    if result.returncode != 0:
        console.print(f"\n[bold red]❌ Execution failed![/bold red]")
        console.print(result.stderr)
        return None, result.stderr
    console.print(f"\n[bold green]✅ Execution succeeded![/bold green]")
    output = result.stdout.strip()
    return output, None

def check_output(output, expected_output, lab, test_case):
    """Check if the output matches the expected pattern."""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    answer_sheet = load_answer_sheet()

    pattern = re.compile(expected_output, re.DOTALL)
    if pattern.search(output.strip()):
        console.print(f"\n[bold green]✅ Test passed: {test_case['desc']}[/bold green]")
        answer_sheet.append({
            'time': current_time,
            'lab': lab,
            'test_case': test_case['desc'],
            'result': 'Passed',
            'output': output
        })
        save_answer_sheet(answer_sheet)
        return True
    
    console.print(f"\n[bold red]❌ Test failed: {test_case['desc']}[/bold red]")
    console.print(f"Expected pattern: {expected_output}")
    console.print(f"Actual output: {output}")
    answer_sheet.append({
        'time': current_time,
        'lab': lab,
        'test_case': test_case['desc'],
        'result': 'Failed',
        'error': f"Expected pattern: {expected_output}, Actual: {output}"
    })
    save_answer_sheet(answer_sheet)
    return False

def zip_files(student_id):
    """Zip the Java files and answer sheet into a submission package."""
    console.print(f"\n[bold cyan]********** Zipping Files **********[/bold cyan]")
    submit_files = ["Lab6_1.java", "Lab6_2.java", "Lab6_3.java"]
    
    timestamp = datetime.now().strftime("%m%d_%H%M")
    zip_file_name = f"Lab6_{student_id}_{timestamp}.zip"
    
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
    parser.add_argument("--lab", type=str, choices=["Lab6_1", "Lab6_2", "Lab6_3"], help="Specific lab to check.")
    parser.add_argument("--uid", type=str, help="Student ID to check all labs and zip files.")
    args = parser.parse_args()

    if args.lab:
        labs_to_check = [args.lab]
        check_all = False
    elif args.uid:
        labs_to_check = ["Lab6_1", "Lab6_2", "Lab6_3"]
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
            output, error = run_java_program(class_name, test_case["input"])
            
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
            
            if not check_output(output, test_case["expected_output"], lab, test_case):
                all_passed = False
                break

        if not all_passed:
            break

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