## IntPoint Objects

```python
class IntPoint(StructBase)
```

Screen coordinates.
note: The full C++ class is located here: Engine\Source\Runtime\Core\Public\Math\IntPoint.h

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``x`` (int32):  [Read-Write]
- ``y`` (int32):  [Read-Write]

<a id="unreal.IntPoint.__init__"></a>

#### __init__

```python
def __init__(x: int = 0, y: int = 0) -> None
```

<a id="unreal.IntPoint.x"></a>

#### x

```python
@property
def x() -> int
```

(int32):  [Read-Write]

<a id="unreal.IntPoint.x"></a>

#### x

```python
@x.setter
def x(value: int) -> None
```

<a id="unreal.IntPoint.y"></a>

#### y

```python
@property
def y() -> int
```

(int32):  [Read-Write]

<a id="unreal.IntPoint.y"></a>

#### y

```python
@y.setter
def y(value: int) -> None
```

<a id="unreal.IntPoint.subtract"></a>

#### subtract

```python
def subtract(b: IntPoint) -> IntPoint
```

x.subtract(b) -> IntPoint
Returns IntPoint A subtracted by B

Args:
    b (IntPoint): 

Returns:
    IntPoint:

<a id="unreal.IntPoint.subtract_int"></a>

#### subtract_int

```python
def subtract_int(b: int) -> IntPoint
```

x.subtract_int(b) -> IntPoint
Subtraction (A - B)

Args:
    b (int32): 

Returns:
    IntPoint:

<a id="unreal.IntPoint.not_equal"></a>

#### not_equal

```python
def not_equal(b: IntPoint) -> bool
```

x.not_equal(b) -> bool
Returns true if IntPoint A is NOT equal to IntPoint B (A != B)

Args:
    b (IntPoint): 

Returns:
    bool:

<a id="unreal.IntPoint.multiply"></a>

#### multiply

```python
def multiply(b: IntPoint) -> IntPoint
```

x.multiply(b) -> IntPoint
Returns IntPoint A multiplied by B

Args:
    b (IntPoint): 

Returns:
    IntPoint:

<a id="unreal.IntPoint.multiply_int"></a>

#### multiply_int

```python
def multiply_int(b: int) -> IntPoint
```

x.multiply_int(b) -> IntPoint
Multiplication (A * B)

Args:
    b (int32): 

Returns:
    IntPoint:

<a id="unreal.IntPoint.equals"></a>

#### equals

```python
def equals(b: IntPoint) -> bool
```

x.equals(b) -> bool
Returns true if IntPoint A is equal to IntPoint B (A == B)

Args:
    b (IntPoint): 

Returns:
    bool:

<a id="unreal.IntPoint.divide"></a>

#### divide

```python
def divide(b: IntPoint) -> IntPoint
```

x.divide(b) -> IntPoint
Returns IntPoint A divided by B

Args:
    b (IntPoint): 

Returns:
    IntPoint:

<a id="unreal.IntPoint.divide_int"></a>

#### divide_int

```python
def divide_int(b: int) -> IntPoint
```

x.divide_int(b) -> IntPoint
Division (A * B)

Args:
    b (int32): 

Returns:
    IntPoint:

<a id="unreal.IntPoint.vector2d"></a>

#### vector2d

```python
def vector2d() -> Vector2D
```

x.vector2d() -> Vector2D
Converts an IntPoint to a Vector2D

Returns:
    Vector2D:

<a id="unreal.IntPoint.add"></a>

#### add

```python
def add(b: IntPoint) -> IntPoint
```

x.add(b) -> IntPoint
Returns IntPoint A added by B

Args:
    b (IntPoint): 

Returns:
    IntPoint:

<a id="unreal.IntPoint.add_int"></a>

#### add_int

```python
def add_int(b: int) -> IntPoint
```

x.add_int(b) -> IntPoint
Addition (A - B)

Args:
    b (int32): 

Returns:
    IntPoint:

<a id="unreal.IntPoint.__eq__"></a>

#### __eq__

```python
def __eq__(other: object) -> bool
```

**Overloads:**

- ``IntPoint`` Returns true if IntPoint A is NOT equal to IntPoint B (A != B)
- ``IntPoint`` Returns true if IntPoint A is equal to IntPoint B (A == B)

<a id="unreal.IntPoint.__add__"></a>

#### __add__

```python
def __add__(other: IntPoint) -> None
```

**Overloads:**

- ``IntPoint`` Returns IntPoint A added by B
- ``int32`` Addition (A - B)

<a id="unreal.IntPoint.__iadd__"></a>

#### __iadd__

```python
def __iadd__(other: IntPoint) -> None
```

**Overloads:**

- ``IntPoint`` Returns IntPoint A added by B
- ``int32`` Addition (A - B)

<a id="unreal.IntPoint.__sub__"></a>

#### __sub__

```python
def __sub__(other: IntPoint) -> None
```

**Overloads:**

- ``IntPoint`` Returns IntPoint A subtracted by B
- ``int32`` Subtraction (A - B)

<a id="unreal.IntPoint.__isub__"></a>

#### __isub__

```python
def __isub__(other: IntPoint) -> None
```

**Overloads:**

- ``IntPoint`` Returns IntPoint A subtracted by B
- ``int32`` Subtraction (A - B)

<a id="unreal.IntPoint.__mul__"></a>

#### __mul__

```python
def __mul__(other: IntPoint) -> None
```

**Overloads:**

- ``IntPoint`` Returns IntPoint A multiplied by B
- ``int32`` Multiplication (A * B)

<a id="unreal.IntPoint.__imul__"></a>

#### __imul__

```python
def __imul__(other: IntPoint) -> None
```

**Overloads:**

- ``IntPoint`` Returns IntPoint A multiplied by B
- ``int32`` Multiplication (A * B)

<a id="unreal.IntPoint.__truediv__"></a>

#### __truediv__

```python
def __truediv__(other: IntPoint) -> None
```

**Overloads:**

- ``IntPoint`` Returns IntPoint A divided by B
- ``int32`` Division (A * B)

<a id="unreal.IntPoint.ZERO"></a>

#### ZERO

(IntPoint): Zero Int Point (0, 0)

<a id="unreal.IntPoint.UP"></a>

#### UP

(IntPoint): Up Int Point (0, -1)

<a id="unreal.IntPoint.RIGHT"></a>

#### RIGHT

(IntPoint): Right Int Point (1, 0)

<a id="unreal.IntPoint.ONE"></a>

#### ONE

(IntPoint): One Int Point (1, 1)

<a id="unreal.IntPoint.LEFT"></a>

#### LEFT

(IntPoint): Left Int Point (-1, 0)

<a id="unreal.IntPoint.DOWN"></a>

#### DOWN

(IntPoint): Down Int Point (0, 1)

<a id="unreal.IntRect"></a>