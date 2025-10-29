# Danh sách để lưu các công việc
tasks = []
def add_task(task_name):
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
            print(f"{i}. {task['name']} - Hoàn thành")
        else: print(f"{i}. {task['name']} - Chưa hoàn thành")
# Kiểm tra xem công việc hoàn thành chưa
def complete_task():
    print("\nTrạng thái:")
    check = True
    for task in tasks:
        if (task['completed'] == False): 
            check = False
            break
    if (check == True): print("Đã hoàn thành công việc!")
    else: print("Chưa hoàn thành công việc!")
    
# --- Điểm bắt đầu của chương trình ---
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!\n")
add_task("Học bài Git và GitHub")
add_task("Làm bài tập thực hành ở nhà")
list_tasks()
complete_task()