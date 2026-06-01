# Первоначальная настройка проекта TeamFinder

## 1. Виртуальное окружение

Перед началом работы необходимо создать и активировать виртуальное окружение Python.  


1. **Создайте виртуальное окружение (в папке проекта):**
   ```bash
   python3 -m venv venv
   ```

   После этого появится папка `venv`, где будут храниться зависимости проекта.

2. **Активируйте окружение:**

    - **Windows (PowerShell):**
      ```bash
      venv\Scripts\Activate.ps1
      ```
    - **Windows (cmd):**
      ```bash
      venv\Scripts\activate
      ```
    - **Linux/Mac:**
      ```bash
      source venv/bin/activate
      ```

3. **Установите зависимости из `requirements.txt`:**
   ```bash
   pip install -r requirements.txt
   ```

   После установки в окружении будут доступны все нужные библиотеки Django-проекта.