from cx_Freeze import setup, Executable

setup(
    name="To Do List",
    version="1.0",
    description="to do tasks",
    executables=[Executable("main.py")]
)