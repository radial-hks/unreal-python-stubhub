## OnMoveAlongPathBlockEventArgs Objects

```python
class OnMoveAlongPathBlockEventArgs(EventArgsBase)
```

On Move Along Path Block Event Args

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: CoveringBoundAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``block_point`` (Vector):  [Read-Write]
- ``block_range_id`` (str):  [Read-Write]
- ``move_entity_id`` (str):  [Read-Write]

<a id="unreal.OnMoveAlongPathBlockEventArgs.__init__"></a>

#### \_\_init\_\_

```python
def __init__(move_entity_id: str = "",
             block_range_id: str = "",
             block_point: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.OnMoveAlongPathBlockEventArgs.move_entity_id"></a>

#### move\_entity\_id

```python
@property
def move_entity_id() -> str
```

(str):  [Read-Write]

<a id="unreal.OnMoveAlongPathBlockEventArgs.move_entity_id"></a>

#### move\_entity\_id

```python
@move_entity_id.setter
def move_entity_id(value: str) -> None
```

<a id="unreal.OnMoveAlongPathBlockEventArgs.block_range_id"></a>

#### block\_range\_id

```python
@property
def block_range_id() -> str
```

(str):  [Read-Write]

<a id="unreal.OnMoveAlongPathBlockEventArgs.block_range_id"></a>

#### block\_range\_id

```python
@block_range_id.setter
def block_range_id(value: str) -> None
```

<a id="unreal.OnMoveAlongPathBlockEventArgs.block_point"></a>

#### block\_point

```python
@property
def block_point() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.OnMoveAlongPathBlockEventArgs.block_point"></a>

#### block\_point

```python
@block_point.setter
def block_point(value: Vector) -> None
```

<a id="unreal.custompoiStyle_marker_image"></a>