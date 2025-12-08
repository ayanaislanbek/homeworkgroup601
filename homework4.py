import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT
    greeting_text = ft.Text(value='Hello world')

    greeting_history = []
    history_text = ft.Text(value="История приветствий:")


    
    def on_button_click(_):
        name = name_input.value.strip()
        
        timestamp = datetime.now().strftime("%y:%m:%d - %H:%M:%S")

        if name:
            greeting_text.value = f'{timestamp} Hello {name}'
            greeting_text.color = None
            name_input.value = None

            greeting_history.append(f"{timestamp} - {name}")
            print(greeting_history)
            history_text.value = "История приветствий:\n" + '\n'.join(greeting_history)
        else:
            greeting_text.value = 'Введите корректное имя'
            greeting_text.color = ft.Colors.RED

        # print(greeting_text)
        page.update()

    name_input = ft.TextField(label='Введите имя', on_submit=on_button_click, expand=True)

    button_text = ft.TextButton(text='send', on_click=on_button_click)
    button_elevated = ft.ElevatedButton(text='send', on_click=on_button_click)
    button_icon = ft.IconButton(icon=ft.Icons.SEND, on_click=on_button_click)

    def clear_history(_):
        print(greeting_history)
        greeting_history.clear()
        history_text.value = 'История приветствий:'
        page.update()
        print(greeting_history)
    
    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)


    def popped_last_name(_):
       if greeting_history:
            greeting_history.pop()         
       else:
         history_text.value = 'История пуста!'
         page.update()


    popped_name_button = ft.IconButton(icon=ft.Icons.DELETE_SHARP, on_click=popped_last_name)

    # page.add(greeting_text, name_input, button_text, history_text )

    view_greeting_text = ft.Row([greeting_text], alignment=ft.MainAxisAlignment.CENTER)
    view_popped_name = ft.Row([popped_name_button], alignment=ft.MainAxisAlignment.END)

    page.add(view_greeting_text, view_popped_name,ft.Row([name_input, button_elevated, clear_button]), history_text)

ft.app(target=main)