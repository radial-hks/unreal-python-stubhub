## PresetEntityData Objects

```python
class PresetEntityData(StructBase)
```

Preset Entity Data

**C++ Source:**

- **Plugin**: AesRuntimeCore
- **Module**: WdpDataModel
- **File**: WdpBuiltInEntity.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``actor_entity_class`` (type(Class)):  [Read-Write]
- ``atom_class_to_preset_atom`` (Map[type(Class), EntityAtomBase]):  [Read-Write]
- ``entity_class`` (type(Class)):  [Read-Write]

<a id="unreal.PresetEntityData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        actor_entity_class: Class = None,
        entity_class: Class = None,
        atom_class_to_preset_atom: Map[Class, EntityAtomBase] = {}) -> None
```

<a id="unreal.PresetEntityData.actor_entity_class"></a>

#### actor\_entity\_class

```python
@property
def actor_entity_class() -> Class
```

(type(Class)):  [Read-Write]

<a id="unreal.PresetEntityData.actor_entity_class"></a>

#### actor\_entity\_class

```python
@actor_entity_class.setter
def actor_entity_class(value: Class) -> None
```

<a id="unreal.PresetEntityData.entity_class"></a>

#### entity\_class

```python
@property
def entity_class() -> Class
```

(type(Class)):  [Read-Write]

<a id="unreal.PresetEntityData.entity_class"></a>

#### entity\_class

```python
@entity_class.setter
def entity_class(value: Class) -> None
```

<a id="unreal.PresetEntityData.atom_class_to_preset_atom"></a>

#### atom\_class\_to\_preset\_atom

```python
@property
def atom_class_to_preset_atom() -> Map[Class, EntityAtomBase]
```

(Map[type(Class), EntityAtomBase]):  [Read-Write]

<a id="unreal.PresetEntityData.atom_class_to_preset_atom"></a>

#### atom\_class\_to\_preset\_atom

```python
@atom_class_to_preset_atom.setter
def atom_class_to_preset_atom(value: Map[Class, EntityAtomBase]) -> None
```

<a id="unreal.UpdateDependency"></a>