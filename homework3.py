import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT
    greeting_text = ft.Text(value='Hello world')

    # greeting_text.value = 'Привет'
    # greeting_text.color = ft.Colors.GREEN
    
    def on_button_click(_):
        # print(name_input.value)
        name = name_input.value.strip()
        
        timestamp = datetime.now().strftime("%y:%m:%d - %H:%M:%S")
        
        if name:
            greeting_text.value = f'{timestamp} Hello {name}'
            greeting_text.color = None
            name_input.value = None
        else:
            greeting_text.value = 'Введите корректное имя'
            greeting_text.color = ft.Colors.RED

        # print(greeting_text)
        page.update()

        def switch_theme(_):
            if page.theme_mode == ft.ThemeMode.LIGHT:
                page.theme_mode = ft.ThemeMode.DARK
                theme_button = ft.Icons.DARK_MODE

            else:
                page.theme_mode = ft.ThemeMode.LIGHT
                theme_button= ft.Icons.BRIGHTNESS_7


    name_input = ft.TextField(label='Введите имя', on_submit=on_button_click)

    button_text = ft.TextButton(text='send', on_click=on_button_click)
    button_elevated = ft.ElevatedButton(text='send', on_click=on_button_click)
    button_icon = ft.IconButton(icon=ft.Icons.SEND, on_click=on_button_click)
    
    theme_button = ft.IconButton(icon= ft.Icons.BRIGHTNESS_7, on_click=switch_theme)
    page.add(greeting_text, name_input, button_text, button_elevated, button_icon, theme_button)


ft.app(target=main, view=ft.WEB_BROWSER)