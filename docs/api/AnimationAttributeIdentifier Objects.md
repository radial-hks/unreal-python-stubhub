## AnimationAttributeIdentifier Objects

```python
class AnimationAttributeIdentifier(StructBase)
```

Script-friendly structure for identifying an attribute (curve).
Wrapping the attribute name, bone name and index, and underlying data type for use within the AnimDataController API.

**C++ Source:**

- **Module**: Engine
- **File**: AttributeIdentifier.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bone_index`` (int32):  [Read-Write]
- ``bone_name`` (Name):  [Read-Write]
- ``name`` (Name):  [Read-Write]
- ``script_struct`` (ScriptStruct):  [Read-Write]
- ``script_struct_path`` (SoftObjectPath):  [Read-Write]

<a id="unreal.AnimationAttributeIdentifier.__init__"></a>

#### __init__

```python
def __init__(name: Name = "None",
             bone_name: Name = "None",
             bone_index: int = 0,
             script_struct: ScriptStruct = None,
             script_struct_path: SoftObjectPath = [""]) -> None
```

<a id="unreal.AnimationAttributeIdentifier.name"></a>

#### name

```python
@property
def name() -> Name
```

(Name):  [Read-Only]

<a id="unreal.AnimationAttributeIdentifier.bone_name"></a>

#### bone_name

```python
@property
def bone_name() -> Name
```

(Name):  [Read-Only]

<a id="unreal.AnimationAttributeIdentifier.bone_index"></a>

#### bone_index

```python
@property
def bone_index() -> int
```

(int32):  [Read-Only]

<a id="unreal.AnimationAttributeIdentifier.script_struct"></a>

#### script_struct

```python
@property
def script_struct() -> ScriptStruct
```

(ScriptStruct):  [Read-Only]

<a id="unreal.AnimationAttributeIdentifier.script_struct_path"></a>

#### script_struct_path

```python
@property
def script_struct_path() -> SoftObjectPath
```

(SoftObjectPath):  [Read-Only]

<a id="unreal.AnimationAttributeIdentifier.is_valid"></a>

#### is_valid

```python
def is_valid() -> bool
```

x.is_valid() -> bool


Returns:
    bool: Whether or not the Attribute Identifier is valid

<a id="unreal.AnimNodeConstantData"></a>