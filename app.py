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
    for x in tasks:
        i+=1
        if (x['completed'] == True): 
            print(f"{i}. {x['name']} - Hoàn thành")
        else: print(f"{i}. {x['name']} - Chưa hoàn thành")
# --- Điểm bắt đầu của chương trình ---
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!\n")
add_task("Học bài Git và GitHub")
add_task("Làm bài tập thực hành ở nhà")
list_tasks()