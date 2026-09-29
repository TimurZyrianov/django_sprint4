def test_gitignore():
    import os
    target_path = settings.BASE_DIR / ".gitignore"

    if not os.path.exists(target_path):

        return

    try:
        with open(target_path, "r", encoding="utf-8", errors="ignore") as fh:
            gitignore = fh.read()
    except Exception as e:
        raise AssertionError(
            "При чтении файла `.gitignore` возникла ошибка:\n"
            f"{type(e).__name__}: {e}"
        )

    assert "sent_emails/" in gitignore, (
        "Убедитесь, что директория `sent_emails/` указана в файле `.gitignore`."
    )
