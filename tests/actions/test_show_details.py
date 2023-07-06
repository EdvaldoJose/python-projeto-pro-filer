from pro_filer.actions.main_actions import show_details  # NOQA
import pytest
from unittest.mock import Mock, patch


def test_show_details_files_notfound(capsys):
    mock_os_path_exists = Mock(return_value=False)
    fake_file_context = {"base_path": "/home/trybe/????"}

    with patch("os.path.exists", mock_os_path_exists):
        show_details(fake_file_context)
        captured = capsys.readouterr()
        assert captured.out == "File '????' does not exist\n"


@pytest.fixture
def mock_os_path_exists():
    with patch("os.path.exists") as mock:
        yield mock


@pytest.fixture
def mock_os_path_getsize():
    with patch("os.path.getsize") as mock:
        yield mock


@pytest.fixture
def mock_os_path_isdir():
    with patch("os.path.isdir") as mock:
        yield mock


@pytest.fixture
def mock_os_path_splitext():
    with patch("os.path.splitext") as mock:
        yield mock


@pytest.fixture
def mock_os_path_getmtime():
    with patch("os.path.getmtime") as mock:
        yield mock


@pytest.mark.parametrize(
    "context, expected_output",
    [
        (
            {"base_path": "/home/trybe/Downloads/Trybe_logo.png"},
            [
                "File name: Trybe_logo.png\n",
                "File size in bytes: 100\n",
                "File type: file\n",
                "File extension: .png\n",
                "Last modified date: 2019-05-21\n",
            ]
        )
    ]
)
def test_show_details_files_found(
    capsys, context, expected_output, mock_os_path_exists,
    mock_os_path_getmtime, mock_os_path_getsize, mock_os_path_isdir,
    mock_os_path_splitext
):
    mock_os_path_exists.return_value = True
    mock_os_path_getmtime.return_value = 1558447897.0442736
    mock_os_path_getsize.return_value = 100
    mock_os_path_isdir.return_value = False
    mock_os_path_splitext.return_value = ("Trybe_logo", ".png")

    show_details(context)
    captured = capsys.readouterr()
    for output in expected_output:
        assert output in captured.out


@pytest.mark.parametrize(
    "context, expected_output",
    [
        (
            {"base_path": "/home/trybe/Downloads"},
            [
                "File name: Downloads\n",
                "File size in bytes: 500\n",
                "File type: directory\n",
                "File extension: [no extension]\n",
                "Last modified date: 2019-05-21\n",
            ]
        )
    ]
)
def test_show_details_directory_found(
    capsys, context, expected_output, mock_os_path_exists,
    mock_os_path_getmtime, mock_os_path_getsize, mock_os_path_isdir,
    mock_os_path_splitext
):
    mock_os_path_exists.return_value = True
    mock_os_path_getmtime.return_value = 1558447897.0442736
    mock_os_path_getsize.return_value = 500
    mock_os_path_isdir.return_value = True
    mock_os_path_splitext.return_value = ("Downloads", "")

    show_details(context)
    captured = capsys.readouterr()
    for output in expected_output:
        assert output in captured.out
