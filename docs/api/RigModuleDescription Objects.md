## RigModuleDescription Objects

```python
class RigModuleDescription(StructBase)
```

Rig Module Description

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigModuleDefines.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``path`` (SoftObjectPath):  [Read-Only]
- ``settings`` (RigModuleSettings):  [Read-Only]

<a id="unreal.RigModuleDescription.__init__"></a>

#### __init__

```python
def __init__(
    path: SoftObjectPath = [""],
    settings: RigModuleSettings = [["", "Module"], [""], "", "", "",
                                   []]) -> None
```

<a id="unreal.RigModuleDescription.path"></a>

#### path

```python
@property
def path() -> SoftObjectPath
```

(SoftObjectPath):  [Read-Only]

<a id="unreal.RigModuleDescription.settings"></a>

#### settings

```python
@property
def settings() -> RigModuleSettings
```

(RigModuleSettings):  [Read-Only]

<a id="unreal.RigControlCopy"></a>