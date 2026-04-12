## EntityMaterialSlot Objects

```python
class EntityMaterialSlot(StructBase)
```

Entity Material Slot

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: ApplicationAPI
- **File**: MaterialToolAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``material_index`` (Array[int32]):  [Read-Write]
- ``mesh_name`` (Name):  [Read-Write]

<a id="unreal.EntityMaterialSlot.__init__"></a>

#### \_\_init\_\_

```python
def __init__(mesh_name: Name = "None",
             material_index: Array[int] = []) -> None
```

<a id="unreal.EntityMaterialSlot.mesh_name"></a>

#### mesh\_name

```python
@property
def mesh_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.EntityMaterialSlot.mesh_name"></a>

#### mesh\_name

```python
@mesh_name.setter
def mesh_name(value: Name) -> None
```

<a id="unreal.EntityMaterialSlot.material_index"></a>

#### material\_index

```python
@property
def material_index() -> Array[int]
```

(Array[int32]):  [Read-Write]

<a id="unreal.EntityMaterialSlot.material_index"></a>

#### material\_index

```python
@material_index.setter
def material_index(value: Array[int]) -> None
```

<a id="unreal.EntityMaterialSlots"></a>