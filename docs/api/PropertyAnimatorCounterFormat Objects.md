## PropertyAnimatorCounterFormat Objects

```python
class PropertyAnimatorCounterFormat(StructBase)
```

Format options used to convert a number to string

**C++ Source:**

- **Plugin**: PropertyAnimator
- **Module**: PropertyAnimator
- **File**: PropertyAnimatorCounter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``decimal_character`` (str):  [Read-Write] Decimal separator character
- ``format_name`` (Name):  [Read-Write] Format friendly name
- ``grouping_character`` (str):  [Read-Write] Thousands separator character
- ``grouping_size`` (uint8):  [Read-Write] Used to group numbers together like thousands
- ``max_decimal_count`` (uint8):  [Read-Write] Maximum number of decimal precision after the decimal separator
- ``min_integer_count`` (uint8):  [Read-Write] Minimum number of integer before the decimal separator for padding
- ``padding_character`` (str):  [Read-Write] Filling character for leading blanks
- ``rounding_mode`` (PropertyAnimatorCounterRoundingMode):  [Read-Write] Whether rounding the number is needed
- ``truncate`` (bool):  [Read-Write] Truncate when the value exceeds the display format
- ``use_sign`` (bool):  [Read-Write] Add a prefix symbol to show the sign of the number (+, -)

<a id="unreal.PropertyAnimatorCounterFormat.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.PropertyAnimatorCurveEasing"></a>