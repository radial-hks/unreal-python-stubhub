## FrameNumber Objects

```python
class FrameNumber(StructBase)
```

A frame number value, representing discrete frames since the start of timing.
note: The full C++ class is located here: Engine\Source\Runtime\Core\Public\Misc\FrameNumber.h

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``value`` (int32):  [Read-Write]

<a id="unreal.FrameNumber.__init__"></a>

#### \_\_init\_\_

```python
def __init__(value: int = 0) -> None
```

<a id="unreal.FrameNumber.value"></a>

#### value

```python
@property
def value() -> int
```

(int32):  [Read-Write]

<a id="unreal.FrameNumber.value"></a>

#### value

```python
@value.setter
def value(value: int) -> None
```

<a id="unreal.FrameNumber.subtract_frame_number_integer"></a>

#### subtract\_frame\_number\_integer

```python
def subtract_frame_number_integer(b: int) -> None
```

x.subtract_frame_number_integer(b) -> None
Subtraction (FrameNumber A - int B)

Args:
    b (int32): 

Returns:
    FrameNumber:

<a id="unreal.FrameNumber.subtract_frame_number_frame_number"></a>

#### subtract\_frame\_number\_frame\_number

```python
def subtract_frame_number_frame_number(b: FrameNumber) -> None
```

x.subtract_frame_number_frame_number(b) -> None
Subtraction (FrameNumber A - FrameNumber B)

Args:
    b (FrameNumber): 

Returns:
    FrameNumber:

<a id="unreal.FrameNumber.multiply_frame_number_integer"></a>

#### multiply\_frame\_number\_integer

```python
def multiply_frame_number_integer(b: int) -> None
```

x.multiply_frame_number_integer(b) -> None
Multiply (FrameNumber A * B)

Args:
    b (int32): 

Returns:
    FrameNumber:

<a id="unreal.FrameNumber.divide_frame_number_integer"></a>

#### divide\_frame\_number\_integer

```python
def divide_frame_number_integer(b: int) -> None
```

x.divide_frame_number_integer(b) -> None
Divide (FrameNumber A / B)

Args:
    b (int32): 

Returns:
    FrameNumber:

<a id="unreal.FrameNumber.add_frame_number_integer"></a>

#### add\_frame\_number\_integer

```python
def add_frame_number_integer(b: int) -> None
```

x.add_frame_number_integer(b) -> None
Addition (FrameNumber A + int B)

Args:
    b (int32): 

Returns:
    FrameNumber:

<a id="unreal.FrameNumber.add_frame_number_frame_number"></a>

#### add\_frame\_number\_frame\_number

```python
def add_frame_number_frame_number(b: FrameNumber) -> None
```

x.add_frame_number_frame_number(b) -> None
Addition (FrameNumber A + FrameNumber B)

Args:
    b (FrameNumber): 

Returns:
    FrameNumber:

<a id="unreal.FrameNumber.__add__"></a>

#### \_\_add\_\_

```python
def __add__(other: FrameNumber) -> None
```

**Overloads:**

- ``int32`` Addition (FrameNumber A + int B)
- ``FrameNumber`` Addition (FrameNumber A + FrameNumber B)

<a id="unreal.FrameNumber.__iadd__"></a>

#### \_\_iadd\_\_

```python
def __iadd__(other: FrameNumber) -> None
```

**Overloads:**

- ``int32`` Addition (FrameNumber A + int B)
- ``FrameNumber`` Addition (FrameNumber A + FrameNumber B)

<a id="unreal.FrameNumber.__sub__"></a>

#### \_\_sub\_\_

```python
def __sub__(other: FrameNumber) -> None
```

**Overloads:**

- ``int32`` Subtraction (FrameNumber A - int B)
- ``FrameNumber`` Subtraction (FrameNumber A - FrameNumber B)

<a id="unreal.FrameNumber.__isub__"></a>

#### \_\_isub\_\_

```python
def __isub__(other: FrameNumber) -> None
```

**Overloads:**

- ``int32`` Subtraction (FrameNumber A - int B)
- ``FrameNumber`` Subtraction (FrameNumber A - FrameNumber B)

<a id="unreal.FrameNumber.__mul__"></a>

#### \_\_mul\_\_

```python
def __mul__(other: FrameNumber) -> None
```

**Overloads:**

- ``int32`` Multiply (FrameNumber A * B)

<a id="unreal.FrameNumber.__imul__"></a>

#### \_\_imul\_\_

```python
def __imul__(other: FrameNumber) -> None
```

**Overloads:**

- ``int32`` Multiply (FrameNumber A * B)

<a id="unreal.FrameNumber.__truediv__"></a>

#### \_\_truediv\_\_

```python
def __truediv__(other: FrameNumber) -> None
```

**Overloads:**

- ``int32`` Divide (FrameNumber A / B)

<a id="unreal.FrameNumberRange"></a>