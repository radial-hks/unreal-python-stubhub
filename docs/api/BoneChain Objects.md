## BoneChain Objects

```python
class BoneChain(StructBase)
```

Bone Chain

**C++ Source:**

- **Plugin**: IKRig
- **Module**: IKRig
- **File**: IKRigDefinition.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``chain_name`` (Name):  [Read-Write]
- ``end_bone`` (BoneReference):  [Read-Only]
- ``ik_goal_name`` (Name):  [Read-Only]
- ``start_bone`` (BoneReference):  [Read-Only]

<a id="unreal.BoneChain.__init__"></a>

#### \_\_init\_\_

```python
def __init__(chain_name: Name = "None", ik_goal_name: Name = "None") -> None
```

<a id="unreal.BoneChain.chain_name"></a>

#### chain\_name

```python
@property
def chain_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.BoneChain.chain_name"></a>

#### chain\_name

```python
@chain_name.setter
def chain_name(value: Name) -> None
```

<a id="unreal.BoneChain.ik_goal_name"></a>

#### ik\_goal\_name

```python
@property
def ik_goal_name() -> Name
```

(Name):  [Read-Only]

<a id="unreal.RetargetDefinition"></a>