from pro_filer.actions.main_actions import show_preview  # NOQA
from io import StringIO
import sys


def test_show_preview_with_diles_and_dirs():
    context = {
        "all_files":
            ["file1.txt", "file2.txt", "file3.txt", "file4.txt", "file5.txt"],
        "all_dirs": ["dir1", "dir2", "dir3", "dir4", "dir5"]
    }

    captured_output = StringIO()
    sys.stdout = captured_output

    show_preview(context)

    sys.stdout = sys.__stdout__

    expected_output = "Found 5 files and 5 directories\n"
    expected_output += "First 5 files: ['file1.txt', 'file2.txt', " \
                        "'file3.txt', 'file4.txt', 'file5.txt']\n"
    expected_output += "First 5 directories: ['dir1', 'dir2', 'dir3', " \
                        "'dir4', 'dir5']\n"
    assert captured_output.getvalue() == expected_output


def test_show_preview_without_files_or_dirs():
    context = {
        "all_files": [],
        "all_dirs": []
    }

    captured_output = StringIO()
    sys.stdout = captured_output

    show_preview(context)

    sys.stdout = sys.__stdout__

    expected_output = "Found 0 files and 0 directories\n"
    assert captured_output.getvalue() == expected_output
