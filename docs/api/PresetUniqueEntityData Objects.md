## PresetUniqueEntityData Objects

```python
class PresetUniqueEntityData(StructBase)
```

Preset Unique Entity Data

**C++ Source:**

- **Plugin**: AesRuntimeCore
- **Module**: WdpDataModel
- **File**: WdpBuiltInEntity.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``atom_class_to_preset_atom`` (Map[type(Class), EntityAtomBase]):  [Read-Write]

<a id="unreal.PresetUniqueEntityData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        atom_class_to_preset_atom: Map[Class, EntityAtomBase] = {}) -> None
```

<a id="unreal.PresetUniqueEntityData.atom_class_to_preset_atom"></a>

#### atom\_class\_to\_preset\_atom

```python
@property
def atom_class_to_preset_atom() -> Map[Class, EntityAtomBase]
```

(Map[type(Class), EntityAtomBase]):  [Read-Write]

<a id="unreal.PresetUniqueEntityData.atom_class_to_preset_atom"></a>

#### atom\_class\_to\_preset\_atom

```python
@atom_class_to_preset_atom.setter
def atom_class_to_preset_atom(value: Map[Class, EntityAtomBase]) -> None
```

<a id="unreal.ProjectInstance"></a>