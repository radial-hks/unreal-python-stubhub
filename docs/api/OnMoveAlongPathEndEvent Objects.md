## OnMoveAlongPathEndEvent Objects

```python
class OnMoveAlongPathEndEvent(EventArgsBase)
```

On Move Along Path End Event

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: CoveringBoundAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``move_along_eid`` (str):  [Read-Write]
- ``move_entity_eid`` (str):  [Read-Write]
- ``path_eid`` (str):  [Read-Write]
- ``reverse`` (bool):  [Read-Write]

<a id="unreal.OnMoveAlongPathEndEvent.__init__"></a>

#### \_\_init\_\_

```python
def __init__(move_along_eid: str = "",
             path_eid: str = "",
             move_entity_eid: str = "",
             reverse: bool = False) -> None
```

<a id="unreal.OnMoveAlongPathEndEvent.move_along_eid"></a>

#### move\_along\_eid

```python
@property
def move_along_eid() -> str
```

(str):  [Read-Write]

<a id="unreal.OnMoveAlongPathEndEvent.move_along_eid"></a>

#### move\_along\_eid

```python
@move_along_eid.setter
def move_along_eid(value: str) -> None
```

<a id="unreal.OnMoveAlongPathEndEvent.path_eid"></a>

#### path\_eid

```python
@property
def path_eid() -> str
```

(str):  [Read-Write]

<a id="unreal.OnMoveAlongPathEndEvent.path_eid"></a>

#### path\_eid

```python
@path_eid.setter
def path_eid(value: str) -> None
```

<a id="unreal.OnMoveAlongPathEndEvent.move_entity_eid"></a>

#### move\_entity\_eid

```python
@property
def move_entity_eid() -> str
```

(str):  [Read-Write]

<a id="unreal.OnMoveAlongPathEndEvent.move_entity_eid"></a>

#### move\_entity\_eid

```python
@move_entity_eid.setter
def move_entity_eid(value: str) -> None
```

<a id="unreal.OnMoveAlongPathEndEvent.reverse"></a>

#### reverse

```python
@property
def reverse() -> bool
```

(bool):  [Read-Write]

<a id="unreal.OnMoveAlongPathEndEvent.reverse"></a>

#### reverse

```python
@reverse.setter
def reverse(value: bool) -> None
```

<a id="unreal.OnMoveAlongPathProcessEventArgs"></a>