# T6SE predictor
## Описание
Это приложение позволяет предсказывать вероятности эффекторности белков, используя предварительно обученную модель. Программа принимает файл в формате FASTA и генерирует CSV-файл с результатами.
Формат выходного файла
Выходной файл — это CSV-файл, содержащий следующие столбцы:
ID: Идентификатор последовательности
Sequence: Последовательность белка
non-T6SE: Вероятность того, что последовательность не относится к классу неэффекторных белков
T6SE: Вероятность того, что последовательность относится к классу эффекторных белков

## Установка
### Linux
1. Убедитесь, что у вас установлены Python 3.8 (или новее) и pip. Установить можно следующим образом: 
    ```
    sudo apt-get install python3-pip python3-dev
    ```
    sudo apt install python-pip
    ```
2. Установите необходимые зависимости, выполнив следующую команду:
    ```
    pip install -r requirements.txt
    ```
    Если файл requirements.txt отсутствует, то его можно создать, либо вручную установить завмисимости:
    ```
    pip install torch transformers click
    ```
### Windows
1. Убедитесь, что у вас установлены Python 3.8 (или новее) и pip. Вы можете скачать Python с официального сайта python.org. При установке убедитесь, что выбрали опцию "Add Python to PATH".
2. Установите необходимые зависимости, выполнив следующую команду в командной строке (CMD) или PowerShell:
    ```
    pip install -r requirements.txt
    ```
    Если файл requirements.txt отсутствует, то вы можете установить зависимости вручную, используя следующую команду:
    ```
    pip install torch transformers click
    ```

## Использование

1. Убедитесь, что в папке с программой находятся два файла:
   - `my_trained_model.pkl`: файл с предобученной моделью.
   - `predict_proteins.py`: скрипт для предсказания.



## Запуск приложения
### Windows

1. Откройте командную строку (Command Prompt) или PowerShell.
2. Перейдите в директорию с файлами, где находится модель `my_trained_model.pkl` и скрипт запуска `predict_proteins.py`:
    ```cmd
    cd path\to\your\directory
    ```
3. Запустите скрипт:
    ```cmd
    python predict_proteins.py --input_file <path_to_fasta_file>
    ```

### Linux

1. Откройте терминал.
2. Перейдите в директорию с файлами, где находится модель `my_trained_model.pkl` и скрипт запуска `predict_proteins.py`:
    ```bash
    cd /path/to/your/directory
    ```
3. Запустите скрипт:
    ```bash
    python predict_proteins.py --input_file <path_to_fasta_file>
    ```

## Пример

Пример использования программы:

```cmd
python predict_proteins.py --input_file sample.fasta

