## PCGMeshSelectorByAttribute Objects

```python
class PCGMeshSelectorByAttribute(PCGMeshSelectorBase)
```

PCGMesh Selector by Attribute

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGMeshSelectorByAttribute.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``attribute_name`` (Name):  [Read-Write]
- ``material_override_attributes`` (Array[Name]):  [Read-Write]
- ``template_descriptor`` (PCGSoftISMComponentDescriptor):  [Read-Write]
- ``use_attribute_material_overrides`` (bool):  [Read-Write]

<a id="unreal.PCGMeshSelectorByAttribute.attribute_name"></a>

#### attribute\_name

```python
@property
def attribute_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.PCGMeshSelectorByAttribute.attribute_name"></a>

#### attribute\_name

```python
@attribute_name.setter
def attribute_name(value: Name) -> None
```

<a id="unreal.PCGMeshSelectorByAttribute.use_attribute_material_overrides"></a>

#### use\_attribute\_material\_overrides

```python
@property
def use_attribute_material_overrides() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGMeshSelectorByAttribute.use_attribute_material_overrides"></a>

#### use\_attribute\_material\_overrides

```python
@use_attribute_material_overrides.setter
def use_attribute_material_overrides(value: bool) -> None
```

<a id="unreal.PCGMeshSelectorByAttribute.material_override_attributes"></a>

#### material\_override\_attributes

```python
@property
def material_override_attributes() -> Array[Name]
```

(Array[Name]):  [Read-Write]

<a id="unreal.PCGMeshSelectorByAttribute.material_override_attributes"></a>

#### material\_override\_attributes

```python
@material_override_attributes.setter
def material_override_attributes(value: Array[Name]) -> None
```

<a id="unreal.PCGMeshSelectorWeighted"></a>