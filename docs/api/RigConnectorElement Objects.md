## RigConnectorElement Objects

```python
class RigConnectorElement(RigBaseElement)
```

Rig Connector Element

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigHierarchyElements.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``created_at_instruction_index`` (int32):  [Read-Write]
- ``index`` (int32):  [Read-Only]
- ``key`` (RigElementKey):  [Read-Only]
- ``selected`` (bool):  [Read-Write]
- ``settings`` (RigConnectorSettings):  [Read-Write]
- ``sub_index`` (int32):  [Read-Only]

<a id="unreal.RigConnectorElement.__init__"></a>

#### __init__

```python
def __init__(
    key: RigElementKey = [RigElementType.NONE, "None"],
    index: int = 0,
    sub_index: int = 0,
    created_at_instruction_index: int = 0,
    selected: bool = False,
    settings: RigConnectorSettings = ["", ConnectorType.PRIMARY, False, []]
) -> None
```

<a id="unreal.RigConnectorElement.settings"></a>

#### settings

```python
@property
def settings() -> RigConnectorSettings
```

(RigConnectorSettings):  [Read-Only]

<a id="unreal.RigSocketState"></a>