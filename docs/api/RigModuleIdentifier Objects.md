## RigModuleIdentifier Objects

```python
class RigModuleIdentifier(StructBase)
```

Rig Module Identifier

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRig
- **File**: RigModuleDefines.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``name`` (str):  [Read-Write] The name of the module used to find it in the module library
- ``type`` (str):  [Read-Write] The kind of module this is (for example "Arm")

<a id="unreal.RigModuleIdentifier.__init__"></a>

#### __init__

```python
def __init__(name: str = "", type: str = "") -> None
```

<a id="unreal.RigModuleIdentifier.name"></a>

#### name

```python
@property
def name() -> str
```

(str):  [Read-Write] The name of the module used to find it in the module library

<a id="unreal.RigModuleIdentifier.name"></a>

#### name

```python
@name.setter
def name(value: str) -> None
```

<a id="unreal.RigModuleIdentifier.type"></a>

#### type

```python
@property
def type() -> str
```

(str):  [Read-Write] The kind of module this is (for example "Arm")

<a id="unreal.RigModuleIdentifier.type"></a>

#### type

```python
@type.setter
def type(value: str) -> None
```

<a id="unreal.RigInfluenceMapPerEvent"></a>