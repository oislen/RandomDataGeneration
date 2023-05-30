:: list all available conda environments
call conda env list

:: create and activate new environment
call conda env remove --name RandomTeleComData --yes
call conda env list
call conda create --name RandomTeleComData
call conda activate RandomTeleComData
call conda list

:: install relevant libraries
call pip install -r ..\requirements.txt

:: list all installed libraries
call conda list