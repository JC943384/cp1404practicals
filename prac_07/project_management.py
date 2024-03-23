from project import Project
import datetime


def main():
    file_name = "projects.txt"
    projects = load_projects(file_name)
    print(f"Welcome to Pythonic Project Management\nLoaded "
          f"{len(projects)} projects from {file_name}")
    while True:
        display_menu()
        choice = input(">>> ").upper()

        if choice == "L":
            file_name = input("Enter filename to load projects from: ")
            projects = load_projects(file_name)
            print(f"Loaded {len(projects)} projects from {file_name}")
        elif choice == 'S':
            save_choice = input("Would you like to save to projects.txt? (yes/no): ").lower()
            if save_choice == 'yes':
                save_projects("projects.txt", projects)
                print("Projects saved successfully.")
        elif choice == 'D':
            display_projects(projects)
        elif choice == 'F':
            filter_date = datetime.datetime.strptime(input("Show projects that start after date (dd/mm/yyyy): "),
                                                     "%d/%m/%Y").date()
            filter_projects_by_date(projects, filter_date)
        elif choice == 'A':
            add_new_project(projects)
        elif choice == 'U':
            update_project(projects)
        elif choice == 'Q':
            save_choice = input("Would you like to save to projects.txt? (yes/no): ").lower()
            if save_choice == 'yes':
                save_projects("projects.txt", projects)
                print("Projects saved successfully.")
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice. Please select again.")


def display_menu():
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")


def load_projects(file_name):
    projects = []
    with open(file_name, 'r') as file:
        next(file)
        for line in file:
            fields = line.strip().split('\t')
            projects.append(Project(*fields))
    return projects


def save_projects(file_name, projects):
    with open(file_name, "w") as file:
        file.write("Name\tStart Date\tPriority\tEstimate\tCompletion\n")
        for project in projects:
            file.write(
                f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.estimate}"
                f"\t{project.completion}\n")


def display_projects(projects):
    projects_sorted = sorted(projects, key=lambda x: x.priority)

    incomplete = [project for project in projects_sorted if project.completion < 100]
    completed = [project for project in projects_sorted if project.completion == 100]

    print("Incomplete projects: ")
    for project in incomplete:
        print(f" {project}")

    print("Completed projects: ")
    for project in completed:
        print(f" {project}")


def filter_projects_by_date(projects, filter_date):
    filtered_projects = [project for project in projects if project.start_date >= filter_date]
    for project in filtered_projects:
        print(project)


def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    estimate = input("Cost estimate: $")
    completion = input("Percent complete: ")
    projects.append(Project(name, start_date, priority, estimate, completion))


def update_project(projects):
    print("Choose a project to update:")
    for i, project in enumerate(projects):
        print(f"{i}: {project}")

    choice = int(input("Project choice: "))
    project = projects[choice]
    print(f" {project}")
    new_completion = input("New Percentage: ")
    if new_completion:
        project.completion = int(new_completion)

    new_priority = input("New Priority: ")
    if new_priority:
        project.priority = int(new_priority)


if __name__ == "__main__":
    main()
