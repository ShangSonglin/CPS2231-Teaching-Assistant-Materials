from rich import print as rprint
from rich.console import Console
import subprocess
import sys
import os
import re

console = Console()

def modify_package_statement(java_file, comment=True):
    """
    Modify the package statement in a Java file by adding or removing double slash comments.
    
    Parameters:
        java_file (str): The name of the Java file (e.g., "Lab0.java").
        comment (bool): True to add comments, False to remove comments.
    Returns:
        bool: True if modification succeeds, False otherwise.
    """
    try:
        with open(java_file, 'r') as file:
            content = file.read()
        
        if comment:
            # Add double slash comment to package statement
            modified_content = re.sub(r'^(package\s+[^;]+;)', r'//\1', content, flags=re.MULTILINE)
        else:
            # Remove double slash comment from package statement
            modified_content = re.sub(r'^//(package\s+[^;]+;)', r'\1', content, flags=re.MULTILINE)
        
        with open(java_file, 'w') as file:
            file.write(modified_content)
        
        return True
    except Exception as e:
        console.print(f"\n[bold red]❌ Failed to modify {java_file}: {str(e)}[/bold red]")
        return False

def compile_java_file(java_file):
    """
    Compile a Java file.
    
    Parameters:
        java_file (str): The name of the Java file (e.g., "Lab0.java").
    Returns:
        bool: True if compilation succeeds, False otherwise.
    """
    console.print(f"\n[bold cyan]********* Compiling Java file: {java_file} *********[/bold cyan]")
    
    # Comment out the package statement before compilation
    if not modify_package_statement(java_file, comment=True):
        return False
    
    # Compile the Java file
    result = subprocess.run(["javac", java_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # Restore the package statement after compilation
    modify_package_statement(java_file, comment=False)
    
    if result.returncode != 0:
        console.print(f"\n[bold red]❌ Compilation failed![/bold red]")
        console.print(result.stderr)
        return False
    else:
        console.print(f"\n[bold green]✅ Compilation succeeded![/bold green]")
        return True

def run_java_program(class_name):
    """
    Run a Java program and capture its output.
    
    Parameters:
        class_name (str): The name of the Java class (e.g., "Lab0").
    Returns:
        str: The output of the Java program, or None if execution fails.
    """
    console.print(f"\n[bold cyan]********* Running Java program: {class_name} *********[/bold cyan]")
    result = subprocess.run(["java", class_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        console.print(f"\n[bold red]❌ Execution failed![/bold red]")
        console.print(result.stderr)
        return None
    else:
        console.print(f"\n[bold green]✅ Execution succeeded![/bold green]")
        return result.stdout.strip()

def check_output(output, expected_output):
    """
    Check if the Java program's output matches the expected output.
    
    Parameters:
        output (str): The actual output of the Java program.
        expected_output (str): The expected output.
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

def main():
    java_file = "Lab0.java"  # Java file name
    class_name = "Lab0"      # Java class name
    expected_output = "I love you"  # Expected output

    # Compile the Java file
    if not compile_java_file(java_file):
        sys.exit(1)

    # Run the Java program
    output = run_java_program(class_name)
    if output is None:
        sys.exit(1)

    # Check the output
    if not check_output(output, expected_output):
        sys.exit(1)

    console.print("\n[bold green]✅ All checks passed![/bold green]")

if __name__ == "__main__":
    main()