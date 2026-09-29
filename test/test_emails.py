def test_gitignore():
    try:
        # Путь теперь верный: сразу в корень, без шага назад
        with open(
            settings.BASE_DIR / ".gitignore", 
            "r", encoding="utf-8", errors="ignore",
        ) as fh:
            gitignore = fh.read()
    except Exception as e:
        raise AssertionError(
            "При чтении файла `.gitignore` в корне проекта возникла ошибка:\n"
            f"{type(e).__name__}: {e}"
        )
    
    # Эта строка проверяет: "Есть ли внутри текста фраза sent_emails/?"
    assert "sent_emails/" in gitignore, (
        "Убедитесь, что директория `sent_emails/` указана в файле `.gitignore`."
    )
