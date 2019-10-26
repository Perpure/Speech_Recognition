# Speech-Recognition

Программа, позволяющая пользователю автоматически распознать и сохранить текст речи в аудиофайле

## Инструкции по использованию
1. Склонировать репозиторий и перейти в его папку

    ```
    git clone https://github.com/R6Fall/Speech_Recognition.git
    cd Speech_Recognition
    ```
    
2. Создать виртуальное окружение и активировать его

    ```
    virtualenv --python=python3 venv
    source venv/bin/activate
    ```
    
3. Установить зависимости

    ```
    pip install -r requirements.txt
    ```

4. Поместить в папку с программой файл `Interview.wav`, речь в котором вы хотите распознать.

5. Запустить программу

    ```
    python run.py
    ```
    
6. Результат выполнения программы будет записан в файл `Interview.txt`
