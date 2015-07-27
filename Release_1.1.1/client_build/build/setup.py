import cx_Freeze


executables = [cx_Freeze.Executable("client.py")]

cx_Freeze.setup(
    name="Client",
    options={"build_exe": {"packages":["socket"],
                           "include_files": []}},
    executables = executables
    )
