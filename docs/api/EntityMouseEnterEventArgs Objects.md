## EntityMouseEnterEventArgs Objects

```python
class EntityMouseEnterEventArgs(EventArgsBase)
```

Entity Mouse Enter Event Args

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: WdpInteractionAPI
- **File**: WdpPickerAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eid`` (str):  [Read-Write]
- ``mouse_pos`` (Vector2D):  [Read-Write]
- ``type`` (Name):  [Read-Write]

<a id="unreal.EntityMouseEnterEventArgs.__init__"></a>

#### \_\_init\_\_

```python
def __init__(eid: str = "",
             type: Name = "None",
             mouse_pos: Vector2D = [0.000000, 0.000000]) -> None
```

<a id="unreal.EntityMouseEnterEventArgs.eid"></a>

#### eid

```python
@property
def eid() -> str
```

(str):  [Read-Write]

<a id="unreal.EntityMouseEnterEventArgs.eid"></a>

#### eid

```python
@eid.setter
def eid(value: str) -> None
```

<a id="unreal.EntityMouseEnterEventArgs.type"></a>

#### type

```python
@property
def type() -> Name
```

(Name):  [Read-Write]

<a id="unreal.EntityMouseEnterEventArgs.type"></a>

#### type

```python
@type.setter
def type(value: Name) -> None
```

<a id="unreal.EntityMouseEnterEventArgs.mouse_pos"></a>

#### mouse\_pos

```python
@property
def mouse_pos() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.EntityMouseEnterEventArgs.mouse_pos"></a>

#### mouse\_pos

```python
@mouse_pos.setter
def mouse_pos(value: Vector2D) -> None
```

<a id="unreal.PickAesTilesNodesByRectParam"></a>