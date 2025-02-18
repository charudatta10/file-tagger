from invoke import task, Collection, Context
import os

@task
def commit(ctx, message="init"):
    ctx.run("git add .")
    ctx.run(f"git commit -m \"{message}\"")

@task
def quit(ctx):
    print("Copyright © 2024 Charudatta")

@task
def test(ctx):
    ctx.run("python -m unittest discover -s tests")

@task
def run(ctx):
    choice = input("Enter the input argument add/ remove: ")
    print("Current directory files:")
    # Get the list of files in the current directory
    files = [f for f in os.listdir() if os.path.isfile(f)]
    
    # Display the list of files with indices
    print("Select a file from the list:")
    for i, file in enumerate(files):
        print(f"{i}: {file}")
    
    # Get the file index from the user
    file_index = int(input("Enter the file number: "))
    
    # Get the selected file name
    filename = files[file_index]
    tags = input("Enter the tags (separated by spaces): ").split()
    ctx.run(f"python __main__.py {choice} {filename} {' '.join(tags)}")

@task(default=True)
def default(ctx):
    # Get a list of tasks
    tasks = sorted(ns.tasks.keys())
    # Display tasks and prompt user
    for i, task_name in enumerate(tasks, 1):
        print(f"{i}: {task_name}")
    choice = int(input("Enter the number of your choice: "))
    ctx.run(f"invoke {tasks[choice - 1]}")

# Create a collection of tasks
ns = Collection(commit, quit, test, run, default)
