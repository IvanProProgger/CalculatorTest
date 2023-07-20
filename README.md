# Test windows calculator function 

Необходимое ПО:
1. Windows Application Driver
2. Python3
2. IDE with python3 interpreter (pycharm или другой)
 

Для подготоки к запуску необходимо выполнить следующие шаги:
1. создайте новый проект, выберите interpreter => python3 
2. git clone https://github.com/IvanProProgger/CalculatorTest.git
3. python.exe -m pip install --upgrade pip
4. pip install Appium-Python-Client==1.3.0
5. pip install unidecode
6. pip install pytest
7. pip uninstall urllib3
8. pip install urllib3==1.26.16

Для запуска:
1. Включите режим разработчика в Windows:
https://remontka.pro/developer-mode-enable-windows-10/ - для windows 10
2. Запустите winappdriver (дефолтный путь: C:\Program Files (x86)\Windows Application Driver)
3. Перейдите в папку с проектом командой:  cd .\CalculatorTest
4. Введите в терминал: pytest test_calculator_functions.py 
