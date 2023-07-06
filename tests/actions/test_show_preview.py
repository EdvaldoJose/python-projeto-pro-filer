from pro_filer.actions.main_actions import show_preview  # NOQA


def test_show_preview_with_files_and_dirs(capsys):
    context = {
        "all_files":
            ["src/__init__.py", "src/app.py", "src/utils/__init__.py"],
        "all_dirs": ["src", "src/utils"]
    }

    show_preview(context)

    captured = capsys.readouterr()

    expected_output = (
        "Found 3 files and 2 directories\n"
        "First 5 files: ['src/__init__.py', 'src/app.py', "
                        "'src/utils/__init__.py']\n"
        "First 5 directories: ['src', 'src/utils']\n"
    )

    assert captured.out == expected_output


def test_show_preview_without_files_or_dirs(capsys):
    context = {
        "all_files":
            ["file1.txt", "file2.txt",
                "file3.txt", "file4.txt", "file5.txt", "file6.txt"],
        "all_dirs":
            ["dir1", "dir2", "dir3", "dir4", "dir5", "dir6"]
    }

    show_preview(context)

    captured = capsys.readouterr()

    expected_output = (
        "Found 6 files and 6 directories\n"
        "First 5 files: ['file1.txt', 'file2.txt', "
                        "'file3.txt', 'file4.txt', 'file5.txt']\n"
        "First 5 directories: ['dir1', 'dir2', 'dir3', "
                        "'dir4', 'dir5']\n"
    )

    assert captured.out == expected_output
