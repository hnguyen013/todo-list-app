# Danh sách để lưu các công việc
tasks = []
def add_task():
    task_name = input("Nhập tên công việc:")
    tasks.append({'name': task_name, 'completed': False})
    print(f"Đã thêm công việc: '{task_name}'")
# Danh sách công việc
def list_tasks():
    i=0
    if not tasks:
        print("Chưa có công việc nào trong danh sách!")
        return
    print("\nDanh sách công việc:")
    for task in tasks:
        i+=1
        if (task['completed'] == True): 
            print(f"[X] {i}. {task['name']}")
        else: print(f"[ ] {i}. {task['name']}")
# Kiểm tra xem công việc hoàn thành chưa
def complete_task():
    index = int(input("Nhập STT công việc muốn đánh dấu hoàn thành:"))
    if (index<1 or index>len(tasks)): 
        print("Chỉ số không hợp lệ!")
    else:
        tasks[index-1]['completed'] = True
        print(f"Đã hoàn thành công việc {tasks[index-1]['name']}")
# Xoá công việc theo chỉ số
def delete_task():
    index = int(input("Nhập STT công việc muốn xóa:"))
    if (index<1 or index>len(tasks)): 
        print("Chỉ số không hợp lệ!")
    else:
        task = tasks.pop(index-1)
        print(f"Đã xóa công việc {task['name']}")
# Menu thao tác
def menu_task():
    print("------ MENU ------")
    print("1. Thêm công việc")
    print("2. Hoàn thành công việc")
    print("3. Xóa công việc")
    print("4. Xem danh sách công việc")
    print("5. Thoát")
    n = int(input("Nhập 1-5:"))
    print("------------------")
    return n
    
# --- Điểm bắt đầu của chương trình ---
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!\n")
n = menu_task()
while (n!=5):
    if (n==1): add_task()
    elif (n==2): complete_task()
    elif (n==3): delete_task()
    elif (n==4): list_tasks()
    n = menu_task()