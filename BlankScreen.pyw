"""BlankScreen: cover every Windows display with pure black."""

import ctypes
import sys
import tkinter as tk
from ctypes import wintypes


if sys.platform != "win32":
    raise SystemExit("BlankScreen is available for Windows only.")


APP_NAME = "BlankScreen"
APP_VERSION = "1.0.0"

SM_XVIRTUALSCREEN = 76
SM_YVIRTUALSCREEN = 77
SM_CXVIRTUALSCREEN = 78
SM_CYVIRTUALSCREEN = 79

HWND_TOPMOST = wintypes.HWND(-1)
SWP_SHOWWINDOW = 0x0040

user32 = ctypes.WinDLL("user32", use_last_error=True)
user32.GetSystemMetrics.argtypes = [ctypes.c_int]
user32.GetSystemMetrics.restype = ctypes.c_int
user32.SetWindowPos.argtypes = [
    wintypes.HWND,
    wintypes.HWND,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
    wintypes.UINT,
]
user32.SetWindowPos.restype = wintypes.BOOL


def enable_dpi_awareness() -> None:
    """Use physical pixels so mixed-DPI multi-monitor layouts are covered."""
    try:
        user32.SetProcessDpiAwarenessContext(wintypes.HANDLE(-4))
        return
    except (AttributeError, OSError):
        pass

    try:
        ctypes.WinDLL("shcore").SetProcessDpiAwareness(2)
        return
    except (AttributeError, OSError):
        pass

    try:
        user32.SetProcessDPIAware()
    except (AttributeError, OSError):
        pass


class BlankScreen:
    """A borderless, topmost black window spanning the virtual desktop."""

    def __init__(self) -> None:
        enable_dpi_awareness()

        self.root = tk.Tk()
        self.root.withdraw()
        self.root.title(APP_NAME)
        self.root.configure(background="#000000", cursor="none")
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.root.protocol("WM_DELETE_WINDOW", self.close)

        self.closed = False
        self.root.bind_all("<KeyPress>", self.close)
        self.root.after(350, self._arm_pointer_exit)
        self.root.after_idle(self._show)

    def _show(self) -> None:
        x = user32.GetSystemMetrics(SM_XVIRTUALSCREEN)
        y = user32.GetSystemMetrics(SM_YVIRTUALSCREEN)
        width = user32.GetSystemMetrics(SM_CXVIRTUALSCREEN)
        height = user32.GetSystemMetrics(SM_CYVIRTUALSCREEN)

        self.root.update_idletasks()
        hwnd = wintypes.HWND(self.root.winfo_id())
        if not user32.SetWindowPos(
            hwnd,
            HWND_TOPMOST,
            x,
            y,
            width,
            height,
            SWP_SHOWWINDOW,
        ):
            raise ctypes.WinError(ctypes.get_last_error())

        self.root.deiconify()
        self.root.lift()
        self.root.focus_force()

    def _arm_pointer_exit(self) -> None:
        if self.closed:
            return
        self.root.bind_all("<ButtonPress>", self.close)
        self.root.bind_all("<MouseWheel>", self.close)

    def close(self, _event: tk.Event | None = None) -> None:
        if self.closed:
            return
        self.closed = True
        try:
            self.root.destroy()
        except tk.TclError:
            pass

    def run(self) -> None:
        self.root.mainloop()


def self_test() -> None:
    """Validate the packaged runtime without displaying the blackout window."""
    enable_dpi_awareness()
    width = user32.GetSystemMetrics(SM_CXVIRTUALSCREEN)
    height = user32.GetSystemMetrics(SM_CYVIRTUALSCREEN)
    if width <= 0 or height <= 0:
        raise SystemExit(1)

    root = tk.Tk()
    root.withdraw()
    root.update_idletasks()
    root.destroy()


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        self_test()
    else:
        BlankScreen().run()
