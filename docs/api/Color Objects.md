## Color Objects

```python
class Color(StructBase)
```

Stores a color with 8 bits of precision per channel. (BGRA).
note: The full C++ class is located here: Engine\Source\Runtime\Core\Public\Math\Color.h

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``a`` (uint8):  [Read-Write]
- ``b`` (uint8):  [Read-Write]
- ``g`` (uint8):  [Read-Write]
- ``r`` (uint8):  [Read-Write]

<a id="unreal.Color.__init__"></a>

#### __init__

```python
def __init__(b: int = 0, g: int = 0, r: int = 0, a: int = 0) -> None
```

<a id="unreal.Color.b"></a>

#### b

```python
@property
def b() -> int
```

(uint8):  [Read-Write]

<a id="unreal.Color.b"></a>

#### b

```python
@b.setter
def b(value: int) -> None
```

<a id="unreal.Color.g"></a>

#### g

```python
@property
def g() -> int
```

(uint8):  [Read-Write]

<a id="unreal.Color.g"></a>

#### g

```python
@g.setter
def g(value: int) -> None
```

<a id="unreal.Color.r"></a>

#### r

```python
@property
def r() -> int
```

(uint8):  [Read-Write]

<a id="unreal.Color.r"></a>

#### r

```python
@r.setter
def r(value: int) -> None
```

<a id="unreal.Color.a"></a>

#### a

```python
@property
def a() -> int
```

(uint8):  [Read-Write]

<a id="unreal.Color.a"></a>

#### a

```python
@a.setter
def a(value: int) -> None
```

<a id="unreal.DirectoryPath"></a>