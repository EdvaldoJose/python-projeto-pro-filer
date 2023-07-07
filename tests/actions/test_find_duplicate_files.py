from pro_filer.actions.main_actions import find_duplicate_files  # NOQA
import pytest


def test_find_duplicate_files_no_duplicates(tmp_path):
    output_path1 = tmp_path / "file1.py"
    output_path2 = tmp_path / "file2.py"
    output_path3 = tmp_path / "file3.py"

    output_path1.write_text("string_1")
    output_path2.write_text("string_2")
    output_path3.write_text("string_3")

    context = {
        "all_files": [
            output_path1, output_path2, output_path3,
        ]
    }

    check_duplicates = find_duplicate_files(context)
    assert len(check_duplicates) == 0


def test_find_duplicate_files_with_duplicates(tmp_path):
    output_path1 = tmp_path / "file1.py"
    output_path2 = tmp_path / "file2.py"
    output_path3 = tmp_path / "file3.py"

    output_path1.write_text("string_1")
    output_path2.write_text("string_2")
    output_path3.write_text("string_3")

    context = {
        "all_files": [
            output_path1, output_path2, output_path3,
        ]
    }

    duplicates = find_duplicate_files(context)
    assert len(duplicates) == 0


def test_find_duplicate_files_with_all_equal(tmp_path):
    output_path1 = tmp_path / "file1.py"
    output_path2 = tmp_path / "file2.py"
    output_path3 = tmp_path / "file3.py"

    output_path1.write_text("string")
    output_path2.write_text("string")
    output_path3.write_text("string")

    context = {
        "all_files": [
            output_path1, output_path2, output_path3
            ]
    }

    duplicates = find_duplicate_files(context)
    assert len(duplicates) == 3
    assert (output_path1, output_path2) in duplicates
    assert (output_path1, output_path3) in duplicates
    assert (output_path2, output_path3) in duplicates


def test_find_duplicate_files_not_found(tmp_path):
    output_path1 = tmp_path / "file1.py"
    output_path2 = tmp_path / "file2.py"
    output_path3 = tmp_path / "file3.py"

    output_path1.write_text("string_1")
    output_path2.write_text("string_2")

    context = {
        "all_files": [
            output_path1, output_path2, output_path3
            ]
    }

    with pytest.raises(ValueError):
        find_duplicate_files(context)
