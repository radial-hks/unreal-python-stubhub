## OnMoveAlongPathProcessEventArgs Objects

```python
class OnMoveAlongPathProcessEventArgs(EventArgsBase)
```

On Move Along Path Process Event Args

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: CoveringBoundAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``move_along_eid`` (str):  [Read-Write]
- ``move_entity_eid`` (str):  [Read-Write]
- ``passed_original_point`` (Vector):  [Read-Write]
- ``passed_point`` (Vector):  [Read-Write]
- ``passed_point_index`` (int32):  [Read-Write]
- ``path_eid`` (str):  [Read-Write]

<a id="unreal.OnMoveAlongPathProcessEventArgs.__init__"></a>

#### \_\_init\_\_

```python
def __init__(move_along_eid: str = "",
             path_eid: str = "",
             move_entity_eid: str = "",
             passed_point: Vector = [0.000000, 0.000000, 0.000000],
             passed_original_point: Vector = [0.000000, 0.000000, 0.000000],
             passed_point_index: int = 0) -> None
```

<a id="unreal.OnMoveAlongPathProcessEventArgs.move_along_eid"></a>

#### move\_along\_eid

```python
@property
def move_along_eid() -> str
```

(str):  [Read-Write]

<a id="unreal.OnMoveAlongPathProcessEventArgs.move_along_eid"></a>

#### move\_along\_eid

```python
@move_along_eid.setter
def move_along_eid(value: str) -> None
```

<a id="unreal.OnMoveAlongPathProcessEventArgs.path_eid"></a>

#### path\_eid

```python
@property
def path_eid() -> str
```

(str):  [Read-Write]

<a id="unreal.OnMoveAlongPathProcessEventArgs.path_eid"></a>

#### path\_eid

```python
@path_eid.setter
def path_eid(value: str) -> None
```

<a id="unreal.OnMoveAlongPathProcessEventArgs.move_entity_eid"></a>

#### move\_entity\_eid

```python
@property
def move_entity_eid() -> str
```

(str):  [Read-Write]

<a id="unreal.OnMoveAlongPathProcessEventArgs.move_entity_eid"></a>

#### move\_entity\_eid

```python
@move_entity_eid.setter
def move_entity_eid(value: str) -> None
```

<a id="unreal.OnMoveAlongPathProcessEventArgs.passed_point"></a>

#### passed\_point

```python
@property
def passed_point() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.OnMoveAlongPathProcessEventArgs.passed_point"></a>

#### passed\_point

```python
@passed_point.setter
def passed_point(value: Vector) -> None
```

<a id="unreal.OnMoveAlongPathProcessEventArgs.passed_original_point"></a>

#### passed\_original\_point

```python
@property
def passed_original_point() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.OnMoveAlongPathProcessEventArgs.passed_original_point"></a>

#### passed\_original\_point

```python
@passed_original_point.setter
def passed_original_point(value: Vector) -> None
```

<a id="unreal.OnMoveAlongPathProcessEventArgs.passed_point_index"></a>

#### passed\_point\_index

```python
@property
def passed_point_index() -> int
```

(int32):  [Read-Write]

<a id="unreal.OnMoveAlongPathProcessEventArgs.passed_point_index"></a>

#### passed\_point\_index

```python
@passed_point_index.setter
def passed_point_index(value: int) -> None
```

<a id="unreal.OnMoveAlongPathBlockEventArgs"></a>