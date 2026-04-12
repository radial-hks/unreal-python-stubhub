## EntityDbClickedEventArgs Objects

```python
class EntityDbClickedEventArgs(EventArgsBase)
```

Entity Db Clicked Event Args

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: WdpInteractionAPI
- **File**: WdpPickerAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eid`` (str):  [Read-Write]
- ``node_id`` (str):  [Read-Write]
- ``position`` (Vector):  [Read-Write]
- ``type`` (Name):  [Read-Write]

<a id="unreal.EntityDbClickedEventArgs.__init__"></a>

#### \_\_init\_\_

```python
def __init__(eid: str = "",
             node_id: str = "",
             type: Name = "None",
             position: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.EntityDbClickedEventArgs.eid"></a>

#### eid

```python
@property
def eid() -> str
```

(str):  [Read-Write]

<a id="unreal.EntityDbClickedEventArgs.eid"></a>

#### eid

```python
@eid.setter
def eid(value: str) -> None
```

<a id="unreal.EntityDbClickedEventArgs.node_id"></a>

#### node\_id

```python
@property
def node_id() -> str
```

(str):  [Read-Write]

<a id="unreal.EntityDbClickedEventArgs.node_id"></a>

#### node\_id

```python
@node_id.setter
def node_id(value: str) -> None
```

<a id="unreal.EntityDbClickedEventArgs.type"></a>

#### type

```python
@property
def type() -> Name
```

(Name):  [Read-Write]

<a id="unreal.EntityDbClickedEventArgs.type"></a>

#### type

```python
@type.setter
def type(value: Name) -> None
```

<a id="unreal.EntityDbClickedEventArgs.position"></a>

#### position

```python
@property
def position() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.EntityDbClickedEventArgs.position"></a>

#### position

```python
@position.setter
def position(value: Vector) -> None
```

<a id="unreal.EntityMouseEnterEventArgs"></a>