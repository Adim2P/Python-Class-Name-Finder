import win32gui

def enum_windows_proc(hwnd, results):
    if win32gui.IsWindowVisible(hwnd):
        class_name = win32gui.GetClassName(hwnd)
        window_text = win32gui.GetWindowText(hwnd)
        results.append((hwnd, class_name, window_text))

def main():
    results = []
    win32gui.EnumWindows(enum_windows_proc, results)
    for hwnd, class_name, window_text in results:
        print(f"Window Handle: {hwnd}, Class Name: {class_name}, Window Text: {window_text}")

if __name__ == "__main__":
    main()