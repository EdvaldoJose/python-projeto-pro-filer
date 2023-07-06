from pro_filer.actions.main_actions import show_preview  # NOQA


def test_show_preview_with_diles_and_dirs(capsys):
    context = {
        "all_files":
            ["file1.txt", "file2.txt", "file3.txt", "file4.txt", "file5.txt"],
        "all_dirs": ["dir1", "dir2", "dir3", "dir4", "dir5"]
    }

    show_preview(context)

    captured = capsys.readouterr()

    expected_output = "Found 5 files and 5 directories\n"
    expected_output += "First 5 files: ['file1.txt', 'file2.txt', " \
                        "'file3.txt', 'file4.txt', 'file5.txt']\n"
    expected_output += "First 5 directories: ['dir1', 'dir2', 'dir3', " \
                        "'dir4', 'dir5']\n"
    assert captured.out == expected_output


def test_show_preview_without_files_or_dirs(capsys):
    context = {
        "all_files": [],
        "all_dirs": []
    }

    show_preview(context)

    captured = capsys.readouterr()
    expected_output = "Found 0 files and 0 directories\n"
    assert captured.out == expected_output
