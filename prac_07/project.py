from project_management import ProjectManager

if __name__ == "__main__":
    project_manager = ProjectManager()
    while True:
        MENU = """
- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit
            """
        print(MENU)
        option = input(">>> ").upper()

        if option == "L":
            file_name = input("Please enter the filename you want to load: ")
            project_manager.load_data(file_name)
            print("Project data has been loaded.")
        elif option == "S":
            file_name = input("Please enter the filename you want to save data to: ")
            project_manager.save_data(file_name)
            print("Data has been saved.")
        elif option == "D":
            project_manager.display_projects()
        elif option == "F":
            project_manager.filter_projects_by_date()
        elif option == "A":
            project_manager.add_new_project()
        elif option == "U":
            project_manager.update_project()
        elif option == "Q":
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid option, please try again.")


