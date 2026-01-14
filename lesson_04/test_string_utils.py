import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize(
    'input_str, expected',
    [
        ('Hello', 'Hello'),
        ('hello', 'Hello'),
        ('hello world', 'Hello world'),
        ('a', 'A')
    ]
)
def test_string_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    'input_str, expected',
    [
        ('123abc', '123abc'),
        ('', ''),
        (' ', ' '),
        (' skypro', ' skypro'),
        ('-skypro', '-skypro'),
        (None, AttributeError),
        (123, AttributeError),
        ('@#&', '@#&')
    ]
)
def test_string_capitalize_negative(input_str, expected):
    if isinstance(input_str, str):
        assert string_utils.capitalize(input_str) == expected
    else:
        print(AttributeError)


@pytest.mark.positive
@pytest.mark.parametrize(
    'input_str, expected',
    [
        ('  Hello', 'Hello'),
        ('hello', 'hello'),
        ('the best', 'the best'),
        ('SkyPro ', 'SkyPro ')
    ]
)
def test_string_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    'input_str, expected',
    [
        ('  ', ''),
        ('', ''),
        (123, AttributeError),
        (None, AttributeError),
        ('\nskypro', '\nskypro'),
        ('\tskypro', '\tskypro')
    ]
)
def test_string_trim_negative(input_str, expected):
    if isinstance(input_str, str):
        assert string_utils.trim(input_str) == expected
    else:
        print(AttributeError)


@pytest.mark.positive
@pytest.mark.parametrize(
    'input_str, symbol, expected',
    [
        ('Hello', 'H', True),
        ('hello', 'o', True),
        ('Skypro', 'y', True),
        ('Skypro', 'ky', True),
        ('SkyproSky', 'ky', True),
        ('Skypro', 's', False)
    ]
)
def test_string_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize(
    'input_str, symbol, expected',
    [
        (None, 'H', AttributeError),
        ('Skypro', None, TypeError),
        ('SkyPro', '', True),
        (123, '1', AttributeError),
        ('a', 'abc', False)
    ]
)
def test_string_contains_negative(input_str, symbol, expected):
    if isinstance(input_str, str) and isinstance(symbol, str):
        assert string_utils.contains(input_str, symbol) == expected
    else:
        print(AttributeError)



@pytest.mark.positive
@pytest.mark.parametrize(
    'input_str, symbol, expected',
    [
        ('SkyPro', 'k', 'SyPro'),
        ('SkyPro', 'Pro', 'Sky'),
        ('SkyProSky', 'ky', 'SProS'),
        ('aaaaa', 'a', ''),
        ('SkyPro', 'x', 'SkyPro'),
        ('Sky-Pro', '-', 'SkyPro')
    ]
)
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected



@pytest.mark.negative
@pytest.mark.parametrize(
    'input_str, symbol, expected',
    [
        (None, 'k', AttributeError),
        ('SkyPro', None, TypeError),
        ('SkyPro', '', 'SkyPro'),
        ('abc', 'abc', ''),
        ('aaa', 'aa', 'a')
    ]
)
def test_delete_symbol_negative(input_str, symbol, expected):
    if isinstance(input_str, str) and isinstance(symbol, str):
        assert string_utils.delete_symbol(input_str, symbol) == expected
    else:
        print(AttributeError)