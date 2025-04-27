## CompositingElementMaterialPass Objects

```python
class CompositingElementMaterialPass(CompositingPostProcessPass)
```

UCompositingElementMaterialPass

**C++ Source:**

- **Plugin**: Composure
- **Module**: Composure
- **File**: CompositingElementTransforms.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``enabled`` (bool):  [Read-Write]
- ``intermediate`` (bool):  [Read-Write] Marks this pass for 'internal use only' - prevents it from being exposed to parent elements.
  When set, render target resources used by this element will be reused. For transforms, all 'Intermediate'
  passes are available to the next transform pass, and released after that.
- ``material`` (CompositingMaterial):  [Read-Write]
- ``pass_name`` (Name):  [Read-Write]
- ``post_process_passes`` (Array[ComposurePostProcessPassPolicy]):  [Read-Write]
- ``render_scale`` (float):  [Read-Write]

<a id="unreal.CompositingElementMaterialPass.material"></a>

#### material

```python
@property
def material() -> CompositingMaterial
```

(CompositingMaterial):  [Read-Write]

<a id="unreal.CompositingElementMaterialPass.material"></a>

#### material

```python
@material.setter
def material(value: CompositingMaterial) -> None
```

<a id="unreal.CompositingElementMaterialPass.set_parameter_mapping"></a>

#### set_parameter_mapping

```python
def set_parameter_mapping(texture_param_name: Name,
                          composure_layer_name: Name) -> bool
```

x.set_parameter_mapping(texture_param_name, composure_layer_name) -> bool
Set the parameter mappings between texture parameters and composure layers. Users can not create new entries into the map as the keys are read only.
Invalid Texture parameter names will result in a failed setting operation.

Args:
    texture_param_name (Name): The name of the texture parameter inside the material interface. Used as key.
    composure_layer_name (Name): The name of the composure layer the texture parameter is mapped to. Used as value.

Returns:
    bool: bool                  True if set operation is successful.

<a id="unreal.CompositingElementMaterialPass.set_material_interface"></a>

#### set_material_interface

```python
def set_material_interface(new_material: MaterialInterface) -> None
```

x.set_material_interface(new_material) -> None
Set the material interface used by current material pass.

Args:
    new_material (MaterialInterface): The new material interface users want to set.

<a id="unreal.CompositingElementMaterialPass.apply_material_params"></a>

#### apply_material_params

```python
def apply_material_params(mid: MaterialInstanceDynamic) -> None
```

x.apply_material_params(mid) -> None
Apply Material Params

Args:
    mid (MaterialInstanceDynamic):

<a id="unreal.CompositingTonemapPass"></a>