## DynamicMaterialModelBase Objects

```python
class DynamicMaterialModelBase(Object)
```

Base version of a dynamic material model.

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterial
- **File**: DynamicMaterialModelBase.h

<a id="unreal.DynamicMaterialModelBase.resolve_material_model"></a>

#### resolve_material_model

```python
def resolve_material_model() -> DynamicMaterialModel
```

x.resolve_material_model() -> DynamicMaterialModel
Returns the Material Designer Model that is the base for this Model.
It will be this object for a Model.
It will be the parent Model for a Model Instance.

Returns:
    DynamicMaterialModel:

<a id="unreal.DynamicMaterialModelBase.get_generated_material"></a>

#### get_generated_material

```python
def get_generated_material() -> Material
```

x.get_generated_material() -> Material
Returns the UMaterial from the resolved Material Model.

Returns:
    Material:

<a id="unreal.DynamicMaterialModelBase.get_dynamic_material_instance"></a>

#### get_dynamic_material_instance

```python
def get_dynamic_material_instance() -> DynamicMaterialInstance
```

x.get_dynamic_material_instance() -> DynamicMaterialInstance
Returns the Material Designer Material that contains this Model, if there is one.

Returns:
    DynamicMaterialInstance:

<a id="unreal.DynamicMaterialModel"></a>