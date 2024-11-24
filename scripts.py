import subprocess
import tempfile

def build_exe() -> None:
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete_on_close=False) as f:
        f.write("from ultttt.__main__ import main; main()")
        f.close()
        subprocess.run(["pyinstaller", "-y", "--name=ultttt", "--collect-all=ultttt", "--icon=src/ultttt/icon.png", "--windowed", f.name], check=True)