# BlankScreen

<p align="center">
  <img src="public/logo.png" width="112" alt="BlankScreen logo">
</p>

BlankScreen is a fun, impactful, minimal Windows mini tool that covers every connected display with pure black while your background work keeps running.

Website: [blankscreen.rakibhq.xyz](https://blankscreen.rakibhq.xyz/)

Download: [Latest GitHub Release](https://github.com/0xmdrakib/BlankScreen/releases/latest)

---

## Features

- Pure-black, borderless overlay across every connected display
- Downloads, renders, scripts, backups, and other tasks continue uninterrupted
- Exit instantly with a click, Esc, or any key
- Standalone executable with no Python installation required
- Multi-monitor and mixed-DPI layout support
- No installer, account, network access, tray process, or background service

## Requirements

- Windows 10 or Windows 11 (64-bit)

## Download

Open the [latest release](https://github.com/0xmdrakib/BlankScreen/releases/latest) and choose either:

1. `BlankScreen.exe`
2. `BlankScreen-Windows-v1.0.0.zip`, containing only the same executable

## How It Works

1. Run `BlankScreen.exe` when you want the displays to go black.
2. Keep downloads, renders, scripts, or any other work running normally.
3. Click anywhere or press any key to return to the desktop instantly.

BlankScreen draws an opaque black layer over Windows. It does not power off the monitor, stop the video signal, pause applications, or change your display settings. Pure black avoids leaving a bright static interface on an OLED display; an LCD backlight remains active.

## Run From Source

Python 3.10 or newer with Tk support is required:

```powershell
python .\BlankScreen.pyw
```

To create the standalone executable:

```powershell
pyinstaller --clean --onefile --windowed --name BlankScreen .\BlankScreen.pyw
```

## License

The source code is available under the [MIT License](LICENSE).
