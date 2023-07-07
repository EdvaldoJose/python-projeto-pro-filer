from pro_filer.actions.main_actions import find_duplicate_files  # NOQA
import pytest


def test_find_duplicate_files_no_duplicate(tmp_path):
    output_path_1 = tmp_path / "file1.py"
    output_path_2 = tmp_path / "file2.py"
    output_path_3 = tmp_path / "file3.py"
    output_path_4 = tmp_path / "file4.py"

    output_path_1.write_text("string 1")
    output_path_2.write_text("string 2")
    output_path_3.write_text("string 3")
    output_path_4.write_text("string 4")

    context = {
        "all_files": [output_path_1, output_path_2, output_path_3, output_path_4]
    }
    check_duplicates = find_duplicate_files(context)

    assert len(check_duplicates) == 0


def test_find_duplicate_files_with_all_different(tmp_path):
    output_path_1 = tmp_path / "file1.py"
    output_path_2 = tmp_path / "file2.py"
    output_path_3 = tmp_path / "file3.py"

    output_path_1.write_text("string 1")
    output_path_2.write_text("string 2")
    output_path_3.write_text("string 3")

    context = {
        "all_files": [output_path_1, output_path_2, output_path_3]
    }
    duplicates = find_duplicate_files(context)

    assert len(duplicates) == 0


def test_find_duplicate_files_with_all_equal(tmp_path):
    output_path_1 = tmp_path / "file1.py"
    output_path_2 = tmp_path / "file2.py"
    output_path_3 = tmp_path / "file3.py"

    output_path_1.write_text("string")
    output_path_2.write_text("string")
    output_path_3.write_text("string")

    context = {
        "all_files": [output_path_1, output_path_2, output_path_3]
    }
    duplicates = find_duplicate_files(context)

    assert len(duplicates) == 3
    assert (output_path_1, output_path_2) in duplicates
    assert (output_path_1, output_path_3) in duplicates
    assert (output_path_2, output_path_3) in duplicates


def test_find_duplicate_files_file_not_found(tmp_path):
    output_path_1 = tmp_path / "file1.py"
    output_path_2 = tmp_path / "file2.py"
    output_path_3 = tmp_path / "file3.py"

    output_path_1.write_text("string 1")
    output_path_2.write_text("string 2")

    context = {
        "all_files": [output_path_1, output_path_2, output_path_3]
    }

    with pytest.raises(ValueError):
        find_duplicate_files(context)
