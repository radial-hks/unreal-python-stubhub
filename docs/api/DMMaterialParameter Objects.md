## DMMaterialParameter Objects

```python
class DMMaterialParameter(DMMaterialLinkedComponent)
```

A parameter on a Material Designer Material.

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterial
- **File**: DMMaterialParameter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``component_dirty`` (bool):  [Read-Only]
- ``component_state`` (DMComponentLifetimeState):  [Read-Only]
- ``editable_properties`` (Array[Name]):  [Read-Only]
- ``parameter_name`` (Name):  [Read-Only]

<a id="unreal.DMMaterialParameter.parameter_name"></a>

#### parameter_name

```python
@property
def parameter_name() -> Name
```

(Name):  [Read-Only]

<a id="unreal.DMMaterialParameter.rename_parameter"></a>

#### rename_parameter

```python
def rename_parameter(base_parameter_name: Name) -> None
```

x.rename_parameter(base_parameter_name) -> None
Changes the parameter name registered with the Model.

Args:
    base_parameter_name (Name):

<a id="unreal.DMMaterialParameter.get_parameter_name"></a>

#### get_parameter_name

```python
def get_parameter_name() -> Name
```

x.get_parameter_name() -> Name
Get Parameter Name

Returns:
    Name:

<a id="unreal.DMMaterialParameter.get_material_model"></a>

#### get_material_model

```python
def get_material_model() -> DynamicMaterialModel
```

x.get_material_model() -> DynamicMaterialModel
Get Material Model

Returns:
    DynamicMaterialModel:

<a id="unreal.DMMaterialValueDynamic"></a>