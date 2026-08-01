"""BlankScreen: cover every Windows display with pure black."""

import ctypes
import os
import sys
from ctypes import wintypes


if sys.platform != "win32":
    raise SystemExit("BlankScreen is available for Windows only.")


APP_NAME = "BlankScreen"
APP_VERSION = "1.0.1"

SM_XVIRTUALSCREEN = 76
SM_YVIRTUALSCREEN = 77
SM_CXVIRTUALSCREEN = 78
SM_CYVIRTUALSCREEN = 79

BLACK_BRUSH = 4
HWND_TOPMOST = wintypes.HWND(-1)
SWP_SHOWWINDOW = 0x0040
SW_SHOW = 5
WS_POPUP = 0x80000000
WS_EX_TOPMOST = 0x00000008
WS_EX_TOOLWINDOW = 0x00000080

WM_CLOSE = 0x0010
WM_DESTROY = 0x0002
WM_SETCURSOR = 0x0020
WM_KEYDOWN = 0x0100
WM_SYSKEYDOWN = 0x0104
WM_TIMER = 0x0113
WM_LBUTTONDOWN = 0x0201
WM_RBUTTONDOWN = 0x0204
WM_MBUTTONDOWN = 0x0207
WM_MOUSEWHEEL = 0x020A
WM_XBUTTONDOWN = 0x020B

POINTER_TIMER_ID = 1
POINTER_ARM_DELAY_MS = 350

LRESULT = ctypes.c_ssize_t
WNDPROC = ctypes.WINFUNCTYPE(
    LRESULT,
    wintypes.HWND,
    wintypes.UINT,
    wintypes.WPARAM,
    wintypes.LPARAM,
)


class WNDCLASSEXW(ctypes.Structure):
    _fields_ = [
        ("cbSize", wintypes.UINT),
        ("style", wintypes.UINT),
        ("lpfnWndProc", WNDPROC),
        ("cbClsExtra", ctypes.c_int),
        ("cbWndExtra", ctypes.c_int),
        ("hInstance", wintypes.HINSTANCE),
        ("hIcon", wintypes.HICON),
        ("hCursor", wintypes.HANDLE),
        ("hbrBackground", wintypes.HBRUSH),
        ("lpszMenuName", wintypes.LPCWSTR),
        ("lpszClassName", wintypes.LPCWSTR),
        ("hIconSm", wintypes.HICON),
    ]


user32 = ctypes.WinDLL("user32", use_last_error=True)
kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
gdi32 = ctypes.WinDLL("gdi32", use_last_error=True)

user32.GetSystemMetrics.argtypes = [ctypes.c_int]
user32.GetSystemMetrics.restype = ctypes.c_int
user32.RegisterClassExW.argtypes = [ctypes.POINTER(WNDCLASSEXW)]
user32.RegisterClassExW.restype = wintypes.ATOM
user32.CreateWindowExW.argtypes = [
    wintypes.DWORD,
    wintypes.LPCWSTR,
    wintypes.LPCWSTR,
    wintypes.DWORD,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_int,
    wintypes.HWND,
    wintypes.HMENU,
    wintypes.HINSTANCE,
    wintypes.LPVOID,
]
user32.CreateWindowExW.restype = wintypes.HWND
user32.DefWindowProcW.argtypes = [
    wintypes.HWND,
    wintypes.UINT,
    wintypes.WPARAM,
    wintypes.LPARAM,
]
user32.DefWindowProcW.restype = LRESULT
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
user32.ShowWindow.argtypes = [wintypes.HWND, ctypes.c_int]
user32.ShowWindow.restype = wintypes.BOOL
user32.UpdateWindow.argtypes = [wintypes.HWND]
user32.UpdateWindow.restype = wintypes.BOOL
user32.SetForegroundWindow.argtypes = [wintypes.HWND]
user32.SetForegroundWindow.restype = wintypes.BOOL
user32.SetFocus.argtypes = [wintypes.HWND]
user32.SetFocus.restype = wintypes.HWND
user32.SetCursor.argtypes = [wintypes.HANDLE]
user32.SetCursor.restype = wintypes.HANDLE
user32.SetTimer.argtypes = [
    wintypes.HWND,
    ctypes.c_size_t,
    wintypes.UINT,
    wintypes.LPVOID,
]
user32.SetTimer.restype = ctypes.c_size_t
user32.KillTimer.argtypes = [wintypes.HWND, ctypes.c_size_t]
user32.KillTimer.restype = wintypes.BOOL
user32.DestroyWindow.argtypes = [wintypes.HWND]
user32.DestroyWindow.restype = wintypes.BOOL
user32.PostQuitMessage.argtypes = [ctypes.c_int]
user32.GetMessageW.argtypes = [
    ctypes.POINTER(wintypes.MSG),
    wintypes.HWND,
    wintypes.UINT,
    wintypes.UINT,
]
user32.GetMessageW.restype = wintypes.BOOL
user32.TranslateMessage.argtypes = [ctypes.POINTER(wintypes.MSG)]
user32.TranslateMessage.restype = wintypes.BOOL
user32.DispatchMessageW.argtypes = [ctypes.POINTER(wintypes.MSG)]
user32.DispatchMessageW.restype = LRESULT
user32.GetWindowRect.argtypes = [wintypes.HWND, ctypes.POINTER(wintypes.RECT)]
user32.GetWindowRect.restype = wintypes.BOOL
user32.UnregisterClassW.argtypes = [wintypes.LPCWSTR, wintypes.HINSTANCE]
user32.UnregisterClassW.restype = wintypes.BOOL

kernel32.GetModuleHandleW.argtypes = [wintypes.LPCWSTR]
kernel32.GetModuleHandleW.restype = wintypes.HINSTANCE
gdi32.GetStockObject.argtypes = [ctypes.c_int]
gdi32.GetStockObject.restype = wintypes.HANDLE


def enable_dpi_awareness() -> None:
    """Use physical pixels so the exact virtual desktop bounds are covered."""
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


def virtual_desktop_bounds() -> tuple[int, int, int, int]:
    """Return the physical-pixel rectangle containing every display."""
    return (
        user32.GetSystemMetrics(SM_XVIRTUALSCREEN),
        user32.GetSystemMetrics(SM_YVIRTUALSCREEN),
        user32.GetSystemMetrics(SM_CXVIRTUALSCREEN),
        user32.GetSystemMetrics(SM_CYVIRTUALSCREEN),
    )


class BlankScreen:
    """A native borderless window spanning the Windows virtual desktop."""

    def __init__(self) -> None:
        enable_dpi_awareness()
        self.pointer_armed = False
        self.hwnd: wintypes.HWND | None = None
        self.instance = kernel32.GetModuleHandleW(None)
        self.class_name = f"BlankScreenWindow-{os.getpid()}"
        self._wndproc_callback = WNDPROC(self._window_proc)
        self._register_window_class()

    def _register_window_class(self) -> None:
        window_class = WNDCLASSEXW()
        window_class.cbSize = ctypes.sizeof(WNDCLASSEXW)
        window_class.lpfnWndProc = self._wndproc_callback
        window_class.hInstance = self.instance
        window_class.hbrBackground = wintypes.HBRUSH(
            gdi32.GetStockObject(BLACK_BRUSH)
        )
        window_class.lpszClassName = self.class_name

        if not user32.RegisterClassExW(ctypes.byref(window_class)):
            raise ctypes.WinError(ctypes.get_last_error())

    def create_window(self, *, visible: bool) -> None:
        x, y, width, height = virtual_desktop_bounds()
        if width <= 0 or height <= 0:
            raise RuntimeError("Windows returned invalid display bounds.")

        self.hwnd = user32.CreateWindowExW(
            WS_EX_TOPMOST | WS_EX_TOOLWINDOW,
            self.class_name,
            APP_NAME,
            WS_POPUP,
            x,
            y,
            width,
            height,
            None,
            None,
            self.instance,
            None,
        )
        if not self.hwnd:
            raise ctypes.WinError(ctypes.get_last_error())

        flags = SWP_SHOWWINDOW if visible else 0
        if not user32.SetWindowPos(
            self.hwnd,
            HWND_TOPMOST,
            x,
            y,
            width,
            height,
            flags,
        ):
            raise ctypes.WinError(ctypes.get_last_error())

        if visible:
            user32.ShowWindow(self.hwnd, SW_SHOW)
            user32.UpdateWindow(self.hwnd)
            user32.SetForegroundWindow(self.hwnd)
            user32.SetFocus(self.hwnd)
            if not user32.SetTimer(
                self.hwnd,
                POINTER_TIMER_ID,
                POINTER_ARM_DELAY_MS,
                None,
            ):
                raise ctypes.WinError(ctypes.get_last_error())

    def _window_proc(
        self,
        hwnd: wintypes.HWND,
        message: int,
        wparam: int,
        lparam: int,
    ) -> int:
        if message == WM_TIMER and wparam == POINTER_TIMER_ID:
            user32.KillTimer(hwnd, POINTER_TIMER_ID)
            self.pointer_armed = True
            return 0

        if message in (WM_KEYDOWN, WM_SYSKEYDOWN, WM_CLOSE):
            user32.DestroyWindow(hwnd)
            return 0

        if self.pointer_armed and message in (
            WM_LBUTTONDOWN,
            WM_RBUTTONDOWN,
            WM_MBUTTONDOWN,
            WM_XBUTTONDOWN,
            WM_MOUSEWHEEL,
        ):
            user32.DestroyWindow(hwnd)
            return 0

        if message == WM_SETCURSOR:
            user32.SetCursor(None)
            return 1

        if message == WM_DESTROY:
            user32.PostQuitMessage(0)
            return 0

        return user32.DefWindowProcW(hwnd, message, wparam, lparam)

    def window_bounds(self) -> tuple[int, int, int, int]:
        if not self.hwnd:
            raise RuntimeError("The BlankScreen window has not been created.")

        rect = wintypes.RECT()
        if not user32.GetWindowRect(self.hwnd, ctypes.byref(rect)):
            raise ctypes.WinError(ctypes.get_last_error())
        return rect.left, rect.top, rect.right - rect.left, rect.bottom - rect.top

    def close(self) -> None:
        if self.hwnd:
            user32.DestroyWindow(self.hwnd)
            self.hwnd = None

    def unregister(self) -> None:
        user32.UnregisterClassW(self.class_name, self.instance)

    def run(self) -> None:
        self.create_window(visible=True)
        message = wintypes.MSG()

        try:
            while True:
                result = user32.GetMessageW(ctypes.byref(message), None, 0, 0)
                if result == -1:
                    raise ctypes.WinError(ctypes.get_last_error())
                if result == 0:
                    break
                user32.TranslateMessage(ctypes.byref(message))
                user32.DispatchMessageW(ctypes.byref(message))
        finally:
            self.unregister()


def self_test() -> None:
    """Verify that the native window matches the full virtual desktop."""
    app = BlankScreen()
    try:
        app.create_window(visible=False)
        expected = virtual_desktop_bounds()
        actual = app.window_bounds()
        if actual != expected:
            raise SystemExit(
                f"Coverage mismatch: expected {expected}, received {actual}."
            )
    finally:
        app.close()
        app.unregister()


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        self_test()
    else:
        BlankScreen().run()
