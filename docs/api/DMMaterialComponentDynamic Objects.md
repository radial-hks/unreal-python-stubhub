## DMMaterialComponentDynamic Objects

```python
class DMMaterialComponentDynamic(DMMaterialComponent)
```

Base version of a dynamic material component. Links to the original in the parent material model.

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterial
- **File**: DMMaterialComponentDynamic.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``parent_component_name`` (Name):  [Read-Only]

<a id="unreal.DMMaterialComponentDynamic.parent_component_name"></a>

#### parent_component_name

```python
@property
def parent_component_name() -> Name
```

(Name):  [Read-Only]

<a id="unreal.DMMaterialComponentDynamic.get_parent_component_name"></a>

#### get_parent_component_name

```python
def get_parent_component_name() -> Name
```

x.get_parent_component_name() -> Name
Get Parent Component Name

Returns:
    Name:

<a id="unreal.DMMaterialComponentDynamic.get_material_model_dynamic"></a>

#### get_material_model_dynamic

```python
def get_material_model_dynamic() -> DynamicMaterialModelDynamic
```

x.get_material_model_dynamic() -> DynamicMaterialModelDynamic
Get Material Model Dynamic

Returns:
    DynamicMaterialModelDynamic:

<a id="unreal.DMMaterialComponentDynamic.ge_resolved_parent_component"></a>

#### ge_resolved_parent_component

```python
def ge_resolved_parent_component() -> DMMaterialComponent
```

x.ge_resolved_parent_component() -> DMMaterialComponent
Resolves and returns the component this dynamic one is based on.

Returns:
    DMMaterialComponent:

<a id="unreal.DMMaterialParameter"></a>