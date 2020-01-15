import arduino_command_line
import tkinter

init_window_w = 600
init_window_h = 600


def format_window(window):
    window.update_idletasks()
    screen_w = window.winfo_screenwidth()
    screen_h = window.winfo_screenheight()

    window_x = int((screen_w / 2) - (init_window_w / 2))
    window_y = int((screen_h / 2) - (init_window_h / 2))

    window.geometry('{}x{}'.format(init_window_w, init_window_h))
    window.geometry('+{}+{}'.format(window_x, window_y))

if __name__ == "__main__":
    window = tkinter.Tk()
    canvas = tkinter.Canvas(window, width=init_window_w, height=init_window_h)
    canvas.pack();
    canvas.update();

    format_window(window)

    open_ide_button = tkinter.Button(window, text="Hello")
    open_ide_button.place(x = canvas.winfo_width() / 2, y = canvas.winfo_height() / 2)

    window.mainloop()
