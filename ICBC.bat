@echo off

 for /f "skip=3 tokens=4" %%i in ('sc query "OnKey Service _ICBC"') do set "zt=%%i" &goto :next 

 :next 

 if /i "%zt%"=="RUNNING" ( 

 echo ����OnKey Service _ICBC�������� 

 ) else ( 

 echo ����OnKey Service _ICBC��ֹͣ 

 ) 

 choice /c:12 /m "����/ֹͣICBC����[1����,2ֹͣ]" 

 if errorlevel 2 goto two 

 if errorlevel 1 goto one 

 :one 

 echo �������÷���... 

 net start "OnKey Service _ICBC" 

 >nul

 :two 

 echo ���ڽ��÷������... 

 net stop "OnKey Service _ICBC" 

 taskkill /f /im D4Svr_ICBC.exe

 reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Run" /v "D4Svr_ICBC.exe" /f

 echo ��������˳�... 

 pause>nul 

 exit 