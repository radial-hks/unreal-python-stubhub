## DynamicMaterialModelDynamic Objects

```python
class DynamicMaterialModelDynamic(DynamicMaterialModelBase)
```

Represents a MID-like version of a Material Designer Model. Uses dynamic values/texture uvs to link to the original model.

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterial
- **File**: DynamicMaterialModelDynamic.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``dynamic_components`` (Map[Name, DMMaterialComponentDynamic]):  [Read-Only] Map of the dynamic components that reference the parent model.
- ``dynamic_material_instance`` (DynamicMaterialInstance):  [Read-Only] Hard reference to the instance, if it exists.
- ``parent_model_soft`` (DynamicMaterialModel):  [Read-Only] Soft reference to the parent model.

<a id="unreal.DynamicMaterialModelDynamic.parent_model_soft"></a>

#### parent_model_soft

```python
@property
def parent_model_soft() -> DynamicMaterialModel
```

(DynamicMaterialModel):  [Read-Only] Soft reference to the parent model.

<a id="unreal.DynamicMaterialModelDynamic.dynamic_components"></a>

#### dynamic_components

```python
@property
def dynamic_components() -> Map[Name, DMMaterialComponentDynamic]
```

(Map[Name, DMMaterialComponentDynamic]):  [Read-Only] Map of the dynamic components that reference the parent model.

<a id="unreal.DynamicMaterialModelDynamic.dynamic_material_instance"></a>

#### dynamic_material_instance

```python
@property
def dynamic_material_instance() -> DynamicMaterialInstance
```

(DynamicMaterialInstance):  [Read-Only] Hard reference to the instance, if it exists.

<a id="unreal.DynamicMaterialModelDynamic.get_parent_model"></a>

#### get_parent_model

```python
def get_parent_model() -> DynamicMaterialModel
```

x.get_parent_model() -> DynamicMaterialModel
Resolves and returns the parent model from ParentModelSoft, saving it in the transient ParentModel.

Returns:
    DynamicMaterialModel:

<a id="unreal.DynamicMaterialModelDynamic.get_component_dynamic"></a>

#### get_component_dynamic

```python
def get_component_dynamic(name: Name) -> DMMaterialComponentDynamic
```

x.get_component_dynamic(name) -> DMMaterialComponentDynamic
Returns the component with the given name or nullptr.

Args:
    name (Name): 

Returns:
    DMMaterialComponentDynamic:

<a id="unreal.DynamicMaterialModelDynamic.get_component_by_path"></a>

#### get_component_by_path

```python
def get_component_by_path(path: str) -> DMMaterialComponent
```

x.get_component_by_path(path) -> DMMaterialComponent
Finds the component with the given path.

Args:
    path (str): 

Returns:
    DMMaterialComponent:

<a id="unreal.DynamicMaterialModelDynamic.create"></a>

#### create

```python
@classmethod
def create(cls, outer: Object,
           parent_model: DynamicMaterialModel) -> DynamicMaterialModelDynamic
```

X.create(outer, parent_model) -> DynamicMaterialModelDynamic
Create a new Material Designer Model Instance based on a parent Model.

Args:
    outer (Object): Could be the transient package, an asset package or a Material Designer Material.
    parent_model (DynamicMaterialModel): 

Returns:
    DynamicMaterialModelDynamic: A new Material Designer Model Instance with its components already initialized.

<a id="unreal.DynamicMaterialModelEditorOnlyDataInterface"></a>