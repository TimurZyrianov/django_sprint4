def test_gitignore():
    import os
    
    # 1. Показываем, где мы ищем файл
    target_path = settings.BASE_DIR / ".gitignore"
    print(f"🔍 ПОПЫТКА: Ищем файл по пути: {target_path}")
    print(f"📂 Существует ли папка, где мы ищем? {os.path.isdir(settings.BASE_DIR)}")
    print(f"📄 Существует ли сам файл? {os.path.exists(target_path)}")
    
    try:
        with open(target_path, "r", encoding="utf-8", errors="ignore") as fh:
            gitignore = fh.read()
            print(f"📖 УСПЕХ: Файл прочитан! Его содержимое:\n---\n{gitignore}\n---")
    except Exception as e:
        print(f"💥 ОШИБКА при чтении: {type(e).__name__}: {e}")
        raise AssertionError(
            "При чтении файла `.gitignore` в корне проекта возникла ошибка:\n"
            f"{type(e).__name__}: {e}"
        )
    
    # 2. Проверяем наличие нужной строки
    if "sent_emails/" not in gitignore:
        print(f"❌ ОШИБКА: Строка 'sent_emails/' НЕ найдена в файле!")
        print(f"📋 Всё содержимое файла было: {repr(gitignore)}")
        raise AssertionError(
            "Убедитесь, что директория `sent_emails/` указана в файле `.gitignore`."
        )
    
    print("✅ ТЕСТ ПРОЙДЕН: Строка найдена!")
