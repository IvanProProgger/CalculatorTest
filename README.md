# Test windows calculator function 

Необходимое ПО:
1. Windows Application Driver
2. IDE with python interpreter (pycharm or other)


Для запуска необходимо выполнить следующие шаги:
1. git clone https://github.com/IvanProProgger/CalculatorTest.git
2. python.exe -m pip install --upgrade pip
3. pip install Appium-Python-Client==1.3.0
4. pip install unidecode
5. pip install pytest
6. pip uninstall urllib3
7. pip install urllib3==1.26.16

Включите режим разработчика в Windows:
https://remontka.pro/developer-mode-enable-windows-10/ - для windows 10
Запустите winappdriver (дефолтный путь: C:\Program Files (x86)\Windows Application Driver)
Перейдите в папку с проектом командой:  cd .\CalculatorTest
Введите в терминал: pytest test_calculator_functions.py 
