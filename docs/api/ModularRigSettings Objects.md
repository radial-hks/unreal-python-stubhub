## ModularRigSettings Objects

```python
class ModularRigSettings(StructBase)
```

Modular Rig Settings

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigModuleDefines.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``auto_resolve`` (bool):  [Read-Write] Whether or not to autoresolve secondary connectors once the primary connector is resolved

<a id="unreal.ModularRigSettings.__init__"></a>

#### __init__

```python
def __init__(auto_resolve: bool = False) -> None
```

<a id="unreal.ModularRigSettings.auto_resolve"></a>

#### auto_resolve

```python
@property
def auto_resolve() -> bool
```

(bool):  [Read-Write] Whether or not to autoresolve secondary connectors once the primary connector is resolved

<a id="unreal.ModularRigSettings.auto_resolve"></a>

#### auto_resolve

```python
@auto_resolve.setter
def auto_resolve(value: bool) -> None
```

<a id="unreal.RigModuleDescription"></a>