import os

from django.conf import settings


def test_gitignore():
    target_path = settings.BASE_DIR / ".gitignore"

    if not os.path.exists(target_path):
        return

    try:
        with open(target_path, "r", encoding="utf-8", errors="ignore") as fh:
            content = fh.read()
    except Exception as e:
        raise AssertionError(f"Ошибка чтения файла: {e}")

    assert "sent_emails/" in content, (
        "Убедитесь, что директория `sent_emails/` "
        "указана в файле `.gitignore`."
    )
