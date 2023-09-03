import datetime


class ProjectManager:
    def __init__(self):
        self.task_data = {}

    def load_data(self,file_name):
        try:
            with open(file_name, 'r') as file:

                first_line = True
                for line in file:
                    if not line.strip():
                        continue

                    if first_line:
                        first_line = False
                        continue

                    values = line.strip().split('\t')
                    name, start_date, priority, cost_estimate, completion_percentage = values

                    self.task_data[name] = {
                        'Start Date': start_date,
                        'Priority': int(priority),
                        'Cost Estimate': float(cost_estimate),
                        'Completion Percentage': int(completion_percentage)
                    }

            print("successfully loaded file")

        except FileNotFoundError:
            print("can not found file")

    def save_data(self,file_name):
        try:
            with open(file_name, 'w') as file:
                file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
                for task, info in self.task_data.items():
                    file.write(f"{task}\t{info['Start Date']}\t{info['Priority']}\t{info['Cost Estimate']}\t{info['Completion Percentage']}\n")
            print("already save data")

        except Exception as e:
            print(f"error: {str(e)}")

    def display_projects(self):

        incomplete_projects = []
        completed_projects = []

        for task, info in sorted(self.task_data.items(), key=lambda x: x[1]['Priority']):
            status = "Completed" if info["Completion Percentage"] == 100 else "Incomplete"
            project_info = f"{task}, start: {info['Start Date']}, priority {info['Priority']}, estimate: ${info['Cost Estimate']:.2f}, completion: {info['Completion Percentage']}%"
            if status == "Completed":
                completed_projects.append(project_info)
            else:
                incomplete_projects.append(project_info)

        print("Incomplete projects:")
        for project in incomplete_projects:
            print(f"  {project}")

        print("Completed projects:")
        for project in completed_projects:
            print(f"  {project}")

    def filter_projects_by_date(self):
        date_filter = input("Show projects that start after date (dd/mm/yyyy): ")

        try:
            filter_date = datetime.datetime.strptime(date_filter, "%d/%m/%Y")
            filtered_projects = []

            for task, info in sorted(self.task_data.items(), key=lambda x: x[1]['Start Date']):
                task_start_date = datetime.datetime.strptime(info['Start Date'], "%d/%m/%Y")
                if task_start_date >= filter_date:
                    project_info = f"{task}, start: {info['Start Date']}, priority {info['Priority']}, estimate: ${info['Cost Estimate']:.2f}, completion: {info['Completion Percentage']}%"
                    filtered_projects.append(project_info)

            if filtered_projects:
                print("Eligible items：")
                for project in filtered_projects:
                    print(project)
            else:
                print("Items that do not qualify")

        except ValueError:
            print("invalid date form")


    def add_new_project(self):
        print("Let's add a new project")

        name = input("Name: ")
        start_date = input("Start date (dd/mm/yy): ")
        priority = input("Priority: ")
        cost_estimate = input("Cost estimate: $")
        completion_percentage = input("Percent complete: ")

        try:
            start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y")
            priority = int(priority)
            cost_estimate = float(cost_estimate)
            completion_percentage = int(completion_percentage)

            self.task_data[name] = {
                'Start Date': start_date.strftime("%d/%m/%Y"),
                'Priority': priority,
                'Cost Estimate': cost_estimate,
                'Completion Percentage': completion_percentage
            }

            print("project added")
        except ValueError:
            print("invalid input")

    def update_project(self):
        project_list = list(self.task_data.items())

        while True:

            for idx, (task, info) in enumerate(sorted(project_list, key=lambda x: x[1]['Priority'])):
                print(f"{idx}  {task}, start: {info['Start Date']}, priority {info['Priority']}, estimate: ${info['Cost Estimate']:.2f}, completion: {info['Completion Percentage']}%")

            project_choice = input("Project choice(input Q exit):")

            if project_choice.upper() == "Q":
                break

            try:
                project_choice = int(project_choice) - 1
                if 0 <= project_choice < len(project_list):
                    project_name, project_info = project_list[project_choice]
                    print(f"{project_name}, start: {project_info['Start Date']}, priority {project_info['Priority']}, estimate: ${project_info['Cost Estimate']:.2f}, completion: {project_info['Completion Percentage']}%")

                    new_percentage = input("New Percentage: ")
                    new_priority = input("New Priority:")

                    if new_percentage:
                        project_info['Completion Percentage'] = int(new_percentage)
                    if new_priority:
                        project_info['Priority'] = int(new_priority)

                    print("project has been updated")
                else:
                    print("invalid input")
            except ValueError:
                print("Invalid project number.")


















