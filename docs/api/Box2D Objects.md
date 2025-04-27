## Box2D Objects

```python
class Box2D(StructBase)
```

A rectangular 2D Box.
note: The full C++ class is located here: Engine\Source\Runtime\Core\Public\Math\Box2D.h

**C++ Source:**

- **Module**: CoreUObject
- **File**: NoExportTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``is_valid`` (bool):  [Read-Write]
- ``max`` (Vector2D):  [Read-Write]
- ``min`` (Vector2D):  [Read-Write]

<a id="unreal.Box2D.__init__"></a>

#### __init__

```python
def __init__(min: Vector2D = [0.000000, 0.000000],
             max: Vector2D = [0.000000, 0.000000]) -> None
```

<a id="unreal.Box2D.min"></a>

#### min

```python
@property
def min() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.Box2D.min"></a>

#### min

```python
@min.setter
def min(value: Vector2D) -> None
```

<a id="unreal.Box2D.max"></a>

#### max

```python
@property
def max() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.Box2D.max"></a>

#### max

```python
@max.setter
def max(value: Vector2D) -> None
```

<a id="unreal.Box2D.is_valid"></a>

#### is_valid

```python
@property
def is_valid() -> bool
```

(bool):  [Read-Write]

<a id="unreal.Box2D.is_valid"></a>

#### is_valid

```python
@is_valid.setter
def is_valid(value: bool) -> None
```

<a id="unreal.Vector2D"></a>