"""test cases for 7-eleven"""

# Standard library

# 3rd Party library
import pytest

#Project library
from seven_eleven.seven import print_7_eleven

@pytest.mark.parametrize(
    "number,expected",
    [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, "seven"),
        (8, 8),
        (9, 9),
        (10, 10),
        (11, "Eleven"),
        (14, "seven"),
        (21, "seven"),
        (22, "Eleven"),
        (76, 76),
        (77, "7-Eleven"),
        (78, 78),
        (154, "7-Eleven")
    ]
)
def test_print_7_eleven(number, expected):
    """Print 7-eleven."""
    
    # Arrange
    
    # Act
    result = print_7_eleven(number)
  
    # Assert
    assert result == expected