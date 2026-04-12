## EntityClickedEventArgs Objects

```python
class EntityClickedEventArgs(EventArgsBase)
```

Entity Clicked Event Args

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: WdpInteractionAPI
- **File**: WdpPickerAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``eid`` (str):  [Read-Write]
- ``node_id`` (str):  [Read-Write]
- ``position`` (Vector):  [Read-Write]
- ``trigger_type`` (EntityClickedTriggerType):  [Read-Write]
- ``type`` (Name):  [Read-Write]

<a id="unreal.EntityClickedEventArgs.__init__"></a>

#### \_\_init\_\_

```python
def __init__(eid: str = "",
             trigger_type: EntityClickedTriggerType = EntityClickedTriggerType.
             LEFT_MOUSE_BUTTON,
             node_id: str = "",
             type: Name = "None",
             position: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.EntityClickedEventArgs.eid"></a>

#### eid

```python
@property
def eid() -> str
```

(str):  [Read-Write]

<a id="unreal.EntityClickedEventArgs.eid"></a>

#### eid

```python
@eid.setter
def eid(value: str) -> None
```

<a id="unreal.EntityClickedEventArgs.trigger_type"></a>

#### trigger\_type

```python
@property
def trigger_type() -> EntityClickedTriggerType
```

(EntityClickedTriggerType):  [Read-Write]

<a id="unreal.EntityClickedEventArgs.trigger_type"></a>

#### trigger\_type

```python
@trigger_type.setter
def trigger_type(value: EntityClickedTriggerType) -> None
```

<a id="unreal.EntityClickedEventArgs.node_id"></a>

#### node\_id

```python
@property
def node_id() -> str
```

(str):  [Read-Write]

<a id="unreal.EntityClickedEventArgs.node_id"></a>

#### node\_id

```python
@node_id.setter
def node_id(value: str) -> None
```

<a id="unreal.EntityClickedEventArgs.type"></a>

#### type

```python
@property
def type() -> Name
```

(Name):  [Read-Write]

<a id="unreal.EntityClickedEventArgs.type"></a>

#### type

```python
@type.setter
def type(value: Name) -> None
```

<a id="unreal.EntityClickedEventArgs.position"></a>

#### position

```python
@property
def position() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.EntityClickedEventArgs.position"></a>

#### position

```python
@position.setter
def position(value: Vector) -> None
```

<a id="unreal.EntityDbClickedEventArgs"></a>