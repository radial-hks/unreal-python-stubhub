## MoveLinearData Objects

```python
class MoveLinearData(StructBase)
```

Move Linear Data

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: MoveLinearAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eids`` (Array[str]):  [Read-Write]
- ``location`` (Vector):  [Read-Write]
- ``time`` (float):  [Read-Write]

<a id="unreal.MoveLinearData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(eids: Array[str] = [],
             time: float = 0.000000,
             location: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.MoveLinearData.eids"></a>

#### eids

```python
@property
def eids() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.MoveLinearData.eids"></a>

#### eids

```python
@eids.setter
def eids(value: Array[str]) -> None
```

<a id="unreal.MoveLinearData.time"></a>

#### time

```python
@property
def time() -> float
```

(float):  [Read-Write]

<a id="unreal.MoveLinearData.time"></a>

#### time

```python
@time.setter
def time(value: float) -> None
```

<a id="unreal.MoveLinearData.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.MoveLinearData.location"></a>

#### location

```python
@location.setter
def location(value: Vector) -> None
```

<a id="unreal.MoveLinearDatas"></a>