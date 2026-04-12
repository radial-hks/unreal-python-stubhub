## RetargetDefinition Objects

```python
class RetargetDefinition(StructBase)
```

Retarget Definition

**C++ Source:**

- **Plugin**: IKRig
- **Module**: IKRig
- **File**: IKRigDefinition.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bone_chains`` (Array[BoneChain]):  [Read-Write]
- ``root_bone`` (Name):  [Read-Write]

<a id="unreal.RetargetDefinition.__init__"></a>

#### \_\_init\_\_

```python
def __init__(root_bone: Name = "None",
             bone_chains: Array[BoneChain] = []) -> None
```

<a id="unreal.RetargetDefinition.root_bone"></a>

#### root\_bone

```python
@property
def root_bone() -> Name
```

(Name):  [Read-Write]

<a id="unreal.RetargetDefinition.root_bone"></a>

#### root\_bone

```python
@root_bone.setter
def root_bone(value: Name) -> None
```

<a id="unreal.RetargetDefinition.bone_chains"></a>

#### bone\_chains

```python
@property
def bone_chains() -> Array[BoneChain]
```

(Array[BoneChain]):  [Read-Write]

<a id="unreal.RetargetDefinition.bone_chains"></a>

#### bone\_chains

```python
@bone_chains.setter
def bone_chains(value: Array[BoneChain]) -> None
```

<a id="unreal.RigVMBlueprintLoadLogEntry"></a>