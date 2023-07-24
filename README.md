# Шаблон для тестирования десктопных приложений с помощью Appium на примере калькулятора

Необходимое ПО:
1. Windows Application Driver
2. Python3
3. IDE c python3 interpreter (pycharm или другой)

Введите в терминале Pycharm следующие команды:
1. git clone https://github.com/IvanProProgger/CalculatorTest.git
2. python.exe -m pip install --upgrade pip
3. pip install Appium-Python-Client==1.3.0
4. pip install unidecode
5. pip install pytest
6. pip uninstall urllib3
7. pip install urllib3==1.26.16


Для запуска:
1. Включите режим разработчика в Windows:
https://remontka.pro/developer-mode-enable-windows-10/ - для windows 10
2. Запустите winappdriver (дефолтный путь: C:\Program Files (x86)\Windows Application Driver)
3. Перейдите в папку с проектом и введите в терминал: pytest или pytest test_calculator_functions.py 
