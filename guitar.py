import os


def load_project(filename):
    if os.path.exists(filename):
        # 在这里添加加载项目的代码
        print(f"成功加载项目：{filename}")
    else:
        print(f"文件 '{filename}' 不存在，请输入有效的文件名。")


def save_project(filename, project_data):
    # 在这里添加保存项目的代码
    with open(filename, 'w') as file:
        file.write(project_data)
        print(f"成功保存项目到文件：{filename}")


if __name__ == "__main__":
    while True:
        user_input = input("选择操作: Q (加载项目) / S (保存项目) / 退出：")

        if user_input.lower() == "退出":
            break
        elif user_input.lower() == "q":
            filename = input("请输入要加载的项目文件名：")
            load_project(filename)
        elif user_input.lower() == "s":
            filename = input("请输入要保存的项目文件名：")
            project_data = input("请输入要保存的项目数据：")
            save_project(filename, project_data)
        else:
            print("无效的操作选项，请重新输入。")

