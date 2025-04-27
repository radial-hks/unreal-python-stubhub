## ComponentMaterialInfo Objects

```python
class ComponentMaterialInfo(StructBase)
```

Contains what is necessary to uniquely identify a material on a component, whether that be an indexed material, one with a slot name, or an overlay material.

**C++ Source:**

- **Module**: MovieSceneTracks
- **File**: MovieSceneMaterialTrack.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``material_slot_index`` (int32):  [Read-Write]
- ``material_slot_name`` (Name):  [Read-Write]
- ``material_type`` (ComponentMaterialType):  [Read-Write]

<a id="unreal.ComponentMaterialInfo.__init__"></a>

#### __init__

```python
def __init__(
    material_slot_name: Name = "None",
    material_slot_index: int = 0,
    material_type: ComponentMaterialType = ComponentMaterialType.EMPTY
) -> None
```

<a id="unreal.ComponentMaterialInfo.material_slot_name"></a>

#### material_slot_name

```python
@property
def material_slot_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.ComponentMaterialInfo.material_slot_name"></a>

#### material_slot_name

```python
@material_slot_name.setter
def material_slot_name(value: Name) -> None
```

<a id="unreal.ComponentMaterialInfo.material_slot_index"></a>

#### material_slot_index

```python
@property
def material_slot_index() -> int
```

(int32):  [Read-Write]

<a id="unreal.ComponentMaterialInfo.material_slot_index"></a>

#### material_slot_index

```python
@material_slot_index.setter
def material_slot_index(value: int) -> None
```

<a id="unreal.ComponentMaterialInfo.material_type"></a>

#### material_type

```python
@property
def material_type() -> ComponentMaterialType
```

(ComponentMaterialType):  [Read-Write]

<a id="unreal.ComponentMaterialInfo.material_type"></a>

#### material_type

```python
@material_type.setter
def material_type(value: ComponentMaterialType) -> None
```

<a id="unreal.TimedDataChannelSampleTime"></a>