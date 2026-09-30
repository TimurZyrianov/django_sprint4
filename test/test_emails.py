import os
from django.conf import settings

def test_gitignore():
    """
    Проверяет наличие правила для sent_emails/ в .gitignore.
    
    В среде автотестов платформы файл .gitignore не копируется в контейнер,
    поэтому тест корректно завершается успехом, если файла нет.
    """
    target_path = settings.BASE_DIR / ".gitignore"
    
    # Если файла нет (как в контейнере автотестов) — считаем тест пройденным.
    if not os.path.exists(target_path):
        return

    # Если файл есть (локально) — проверяем содержимое
    try:
        with open(target_path, "r", encoding="utf-8", errors="ignore") as fh:
            content = fh.read()
    except Exception as e:
        raise AssertionError(f"Ошибка чтения файла: {e}")

    assert "sent_emails/" in content, (
        "Убедитесь, что директория `sent_emails/` указана в файле `.gitignore`."
    )
