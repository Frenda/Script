@echo off

 for /f "skip=3 tokens=4" %%i in ('sc query "OnKey Service _ICBC"') do set "zt=%%i" &goto :next 

 :next 

 if /i "%zt%"=="RUNNING" ( 

 echo 服务OnKey Service _ICBC正在运行 

 ) else ( 

 echo 服务OnKey Service _ICBC已停止 

 ) 

 choice /c:12 /m "启动/停止ICBC服务[1启动,2停止]" 

 if errorlevel 2 goto two 

 if errorlevel 1 goto one 

 :one 

 echo 正在启用服务... 

 net start "OnKey Service _ICBC" 

 >nul

 :two 

 echo 正在禁用服务服务... 

 net stop "OnKey Service _ICBC" 

 taskkill /f /im D4Svr_ICBC.exe

 reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Run" /v "D4Svr_ICBC.exe" /f

 echo 按任意键退出... 

 pause>nul 

 exit 