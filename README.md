# Шаблон для тестирования десктопных приложений с помощью Appium на примере калькулятора с запуском на удаленном сервере"

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
1. Включите режим разработчика в Windows. (https://remontka.pro/developer-mode-enable-windows-10/ - для windows 10)
2. Запустите winappdriver (дефолтный путь: C:\Program Files (x86)\Windows Application Driver)
3. Перейдите в папку с проектом и введите в терминал: pytest или pytest test_calculator_functions.py 

Для запуска на удаленном сервере:
1. Зайдите в "Монитор брандмауэра Защитника Windows в режиме повышенной безопасности"
- Правила для входящих подключений
- Создать правило
- Для порта
- Протокол TCP, введите номер порта: 4723
- Действие -> Разрешить подключение
- Профиль -> Выберите все
- Выберите имя (например: "WinAppDriver remote")
Также для идентичного результата вы можете ввести в командой строке:
- netsh advfirewall firewall add rule name="WinAppDriver remote" dir=in action=allow protocol=TCP localport=4723
2. В командной строке введите: ipconfig
- Вам нужен IPv4 Address используемого подключения, запомните его
3. - Запустите командную строку от имени Администратора
- cd C:\Program Files (x86)\Windows Application Driver\ (дефолтный путь)
- WinAppDriver.exe "IPv4 Address" 4723/wd/hub (Укажите IPv4 адрес)
4. В проекте в файле conftest.py установите значение command_executor='http://"IPv4 Address":4723/wd/hub'