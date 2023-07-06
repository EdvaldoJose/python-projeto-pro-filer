from pro_filer.actions.main_actions import show_disk_usage
from pro_filer.cli_helpers import _get_printable_file_path
from typing import Dict, Any # NOQA


empty_context: Dict[str, Any] = {
    "all_files": []
}


def test_show_disk_usage_with_files(capsys, tmp_path):
    file = tmp_path / "test.py"
    file.touch()
    file.write_text("test")
    path = str(file)

    empty_file = tmp_path / "empty.py"
    empty_file.touch()
    path_empty = str(empty_file)

    context = {
        "all_files": [path, path_empty],
    }

    show_disk_usage(context)

    # captured = capsys.readouterr()
    result = capsys.readouterr()
    output = f"'{_get_printable_file_path(path)}':".ljust(90)
    empty_output = f"'{_get_printable_file_path(path_empty)}':".ljust(90)
    assert result.out == f"{output} 4 (100%)\n\
        {empty_output} 0 (0%)\nTotal size: 4\n"


def test_show_disk_usage_without_files(capsys):
    show_disk_usage(empty_context)
    result = capsys.readouterr()
    assert result.out == "Total size: 0\n"
