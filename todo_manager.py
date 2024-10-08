import os

# File where tasks will be saved
TODO_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from the file."""
    # Initialize an empty list to store tasks
    tasks = []
    # Check if the file exists
    if os.path.exists(TODO_FILE):
        # Open the file in read mode
        with open(TODO_FILE, 'r') as file:
            # Read all lines in the file and strip newline characters
            tasks = [task.strip() for task in file.readlines()]
    # Return the list of tasks
    return tasks

def save_tasks(tasks):
    """Save tasks to the file."""
    # Open the file in write mode
    with open(TODO_FILE, 'w') as file:
        # Write each task to the file followed by a newline character
        for task in tasks:
            file.write(task + "\n")

def add_task(task, tasks):
    """Add a new task to the list."""
    # Append the new task to the list
    tasks.append(task)
    # Save the updated list to the file
    save_tasks(tasks)
    # Print a success message
    print(f'Task "{task}" added.')

def view_tasks(tasks):
    """View all tasks."""
    # Check if the list is empty
    if not tasks:
        # Print a message if there are no tasks
        print("No tasks to display.")
    else:
        # Print a header
        print("\nYour Tasks:")
        # Enumerate the tasks and print them with their indices
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def delete_task(task_number, tasks):
    """Delete a task from the list."""
    try:
        # Remove the task at the specified index
        task = tasks.pop(task_number - 1)
        # Save the updated list to the file
        save_tasks(tasks)
        # Print a success message
        print(f'Task "{task}" deleted.')
    except IndexError:
        # Print an error message if the index is invalid
        print("Invalid task number.")

def display_menu():
    """Display the menu options."""
    # Print the menu header
    print("\nTo-Do List Manager")
    print("------------------")
    # Print the menu options
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Delete a task")
    print("4. Exit")

def main():
    # Load the tasks from the file
    tasks = load_tasks()

    # Loop until the user chooses to exit
    while True:
        # Display the menu
        display_menu()
        # Get the user's choice
        choice = input("\nEnter your choice (1-4): ")

        # Handle the user's choice
        if choice == '1':
            # Get the new task from the user
            task = input("Enter the new task: ")
            # Add the task to the list
            add_task(task, tasks)
        elif choice == '2':
            # View all tasks
            view_tasks(tasks)
        elif choice == '3':
            # View all tasks before deleting
            view_tasks(tasks)
            try:
                # Get the task number to delete from the user
                task_number = int(input("\nEnter the task number to delete: "))
                # Delete the task
                delete_task(task_number, tasks)
            except ValueError:
                # Print an error message if the input is not a valid number
                print("Please enter a valid number.")
        elif choice == '4':
            # Print a goodbye message and exit the loop
            print("Goodbye!")
            break
        else:
            # Print an error message if the choice is invalid
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    # Run the main function
    main()