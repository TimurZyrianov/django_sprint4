# tests/test_emails.py
from django.conf import settings
from django.core.mail.backends.locmem import EmailBackend


def test_gitignore():
    try:
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
    assert "sent_emails/" in gitignore, (
        "Убедитесь, что директория `sent_emails/`, служащая для хранения"
        " e-mail сообщений, указана в файле `.gitignore` в корне проекта."
    )
