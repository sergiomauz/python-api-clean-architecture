"""
Alembic Migration Management Script

This script provides a convenient wrapper around Alembic commands for database migrations.
All Alembic files are located in: infrastructure/persistence/migrations/
"""
import sys
import os
import subprocess


# Path configuration
ALEMBIC_DIR = f"{os.getcwd()}/infrastructure/persistence/migrations"
ALEMBIC_INI = f"{ALEMBIC_DIR}/alembic.ini"


def check_alembic_setup():
    """Check if Alembic files exist"""
    if not os.path.exists(ALEMBIC_DIR):
        print(f"Error: Directory {ALEMBIC_DIR} not found")
        return False
    
    if not os.path.exists(ALEMBIC_INI):
        print(f"Error: File {ALEMBIC_INI} not found")
        return False
    
    return True


def run_alembic_command(command_args):
    """Execute an Alembic command with the correct configuration"""
    if not check_alembic_setup():
        sys.exit(1)
    
    # Build the complete command
    cmd = ["alembic", "-c", ALEMBIC_INI] + command_args
    
    print(f"Executing: {' '.join(cmd)}")
    print("-" * 50)
    
    try:
        # Execute the command
        result = subprocess.run(cmd, cwd=os.getcwd(), check=True)
        print("-" * 50)
        print("Command executed successfully")
        return result.returncode
    except subprocess.CalledProcessError as e:
        print("-" * 50)
        print(f"Error executing command: {e}")
        return e.returncode
    except FileNotFoundError:
        print("Error: Alembic is not installed or not in PATH")
        print("Install Alembic with: pip install alembic")
        return 1


def show_help():
    """Show help with all available commands"""
    help_text = """
        main_db_migrations.py - Alembic Migration Manager
        =================================================

        Configuration:
        - Alembic Directory: infrastructure/persistence/migrations/
        - Configuration File: infrastructure/persistence/migrations/alembic.ini

        AVAILABLE COMMANDS:


        CREATE MIGRATIONS:
        
        # Empty migration
        python main_db_migrations.py revision -m "description"
        
        # Full migration
        python main_db_migrations.py revision --autogenerate -m "description"


        INFORMATION:
        
        # View current revision
        python main_db_migrations.py current
        
        # View migration history
        python main_db_migrations.py history
        
        # View available heads
        python main_db_migrations.py heads
        
        # View migration branches
        python main_db_migrations.py branches
        
        # View revision details
        python main_db_migrations.py show <revision>


        APPLY MIGRATIONS:
        
        # Apply all migrations
        python main_db_migrations.py upgrade head
        
        # Apply next migration
        python main_db_migrations.py upgrade +1
        
        # Apply up to specific revision
        python main_db_migrations.py upgrade <revision>  


        REVERT MIGRATIONS:
        
        # Revert one migration
        python main_db_migrations.py downgrade -1
        
        # Revert to specific revision
        python main_db_migrations.py downgrade <revision>
        
        # Revert all migrations
        python main_db_migrations.py downgrade base


        ADVANCED OPERATIONS:
        
        # Merge revisions
        python main_db_migrations.py merge -m "merge message" <rev1> <rev2>
        
        # Mark as applied without executing
        python main_db_migrations.py stamp <revision>
        
        # Edit a revision
        python main_db_migrations.py edit <revision>


        USAGE EXAMPLES:
        python main_db_migrations.py revision --autogenerate -m "Add users table"
        python main_db_migrations.py upgrade head
        python main_db_migrations.py current
        python main_db_migrations.py history --verbose
        python main_db_migrations.py downgrade -1


        HELP:
        
        # Show this help
        python main_db_migrations.py help
        
        # Command-specific help            
        python main_db_migrations.py <command> --help

        For more information about Alembic: https://alembic.sqlalchemy.org/
        """
    print(help_text)


def run_migrations_command():
    """Main script function"""
    if len(sys.argv) < 2:
        print("Error: At least one command is required")
        print("Use: python main_db_migrations.py help")
        sys.exit(1)
    
    command = sys.argv[1].lower()
    
    # Custom help command
    if command in ['help', '--help', '-h']:
        show_help()
        return
    
    # Command to check configuration
    if command == 'check':
        if check_alembic_setup():
            print("Alembic configuration is correct")
            print(f"Directory: {ALEMBIC_DIR}")
            print(f"Configuration: {ALEMBIC_INI}")
        else:
            sys.exit(1)
        return
    
    # All other commands are passed directly to Alembic
    alembic_arguments = sys.argv[1:]
    exit_code = run_alembic_command(alembic_arguments)
    sys.exit(exit_code)
