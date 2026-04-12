## APIEventSwitch Objects

```python
class APIEventSwitch(StructBase)
```

APIEvent Switch

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: DataModelAPI
- **File**: WdpAPISystem.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``event_name`` (str):  [Read-Write]
- ``open`` (bool):  [Read-Write]

<a id="unreal.APIEventSwitch.__init__"></a>

#### \_\_init\_\_

```python
def __init__(event_name: str = "", open: bool = False) -> None
```

<a id="unreal.APIEventSwitch.event_name"></a>

#### event\_name

```python
@property
def event_name() -> str
```

(str):  [Read-Write]

<a id="unreal.APIEventSwitch.event_name"></a>

#### event\_name

```python
@event_name.setter
def event_name(value: str) -> None
```

<a id="unreal.APIEventSwitch.open"></a>

#### open

```python
@property
def open() -> bool
```

(bool):  [Read-Write]

<a id="unreal.APIEventSwitch.open"></a>

#### open

```python
@open.setter
def open(value: bool) -> None
```

<a id="unreal.ToggleAPIEventChannelParams"></a>