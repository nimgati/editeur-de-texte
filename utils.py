import time
import ctypes

import customtkinter


def get_time(func: callable):
    def wrapper(n):
        start = time.time()
        result = func(n)
        print(f'Execution time: {time.time() - start}')
        return result

    return wrapper


class root_ctk:
    @staticmethod
    def place_center(root: customtkinter.CTk):
        dimension_root = (root.winfo_width(), root.winfo_height())
        dimension_window = (ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))

        x = (dimension_window[0] - dimension_root[0]) // 2
        y = (dimension_window[1] - dimension_root[1]) // 2

        root.geometry(f'{dimension_root[0]}x{dimension_root[1]}+{x}+{y}')

    @staticmethod
    def clear(root: customtkinter.CTk):
        for widget in root.winfo_children():
            try:
                widget.destroy()
            except:
                continue


class default_root(root_ctk):
    @staticmethod
    def generate_root(size: tuple[int, int], title: str, icon: str = None, ovveride: bool = False
                      , resizable: tuple[bool, bool] = (False, False)) -> customtkinter.CTk:
        root = customtkinter.CTk()
        root.geometry(f'{size[0]}x{size[1]}')
        root.title(title)
        root.iconbitmap(icon)
        root.resizable(resizable[0], resizable[1])
        root.overrideredirect(ovveride)

        root_ctk.place_center(root)

        return root
