## RemoteControlOptionalExposeArgs Objects

```python
class RemoteControlOptionalExposeArgs(StructBase)
```

Remote Control Optional Expose Args

**C++ Source:**

- **Plugin**: RemoteControl
- **Module**: RemoteControl
- **File**: RemoteControlFunctionLibrary.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``display_name`` (str):  [Read-Write] The display name of the exposed entity in the panel.
- ``group_name`` (str):  [Read-Write] The name of the group to expose the entity in.
  If it does not exist, a group with that name will be created.

<a id="unreal.RemoteControlOptionalExposeArgs.__init__"></a>

#### __init__

```python
def __init__(display_name: str = "", group_name: str = "") -> None
```

<a id="unreal.RemoteControlOptionalExposeArgs.display_name"></a>

#### display_name

```python
@property
def display_name() -> str
```

(str):  [Read-Write] The display name of the exposed entity in the panel.

<a id="unreal.RemoteControlOptionalExposeArgs.display_name"></a>

#### display_name

```python
@display_name.setter
def display_name(value: str) -> None
```

<a id="unreal.RemoteControlOptionalExposeArgs.group_name"></a>

#### group_name

```python
@property
def group_name() -> str
```

(str):  [Read-Write] The name of the group to expose the entity in.
If it does not exist, a group with that name will be created.

<a id="unreal.RemoteControlOptionalExposeArgs.group_name"></a>

#### group_name

```python
@group_name.setter
def group_name(value: str) -> None
```

<a id="unreal.ColorWheelColorBase"></a>