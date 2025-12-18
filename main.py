from db import main_db
import flet as ft 


def main(page: ft.Page):
    page.title = 'ToDO List'
    page.theme_mode = ft.ThemeMode.LIGHT


def add_task(_):
    if task_input.value and len(task_input.value) <= 100:
        task = task_input.value
        task_id = main_db.add_task(task=task)
        print(f'Задача {task} completed - id {task_id}')
        task_input.value = None
        page.update()
    
    elif task_input.value and len(task_input.value) > 100:
        task_input.value= 'Слишком много символов'
        


    task_input = ft.TextField(label='Введите задачу', on_submit=add_task, expand=True)
    task_input_button = ft.IconButton(icon=ft.Icons.SEND, on_click=add_task)

    page.add(ft.Row([task_input, task_input_button]))


if __name__ == '__main__':
    main_db.init_db()
    ft.app(target=main)
                                  
