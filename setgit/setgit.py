import subprocess
import sys

def run_command(command, description):
    try:
        print(f"Running: {description}...")
        subprocess.check_call(command, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error during {description}: {e}")
        sys.exit(1)

def main():
    run_command("git init", "Initializing git repository")
    run_command("git add .", "Adding all files")
    run_command('git commit -m "Initial Commit"', "Making initial commit")
    run_command('code .', "Open current project on visual code")
    print("✅ All commands completed successfully!")

if __name__ == "__main__":
    main()
