## CompositingMaterial Objects

```python
class CompositingMaterial(CompositingParamPayload)
```

Compositing Material

**C++ Source:**

- **Plugin**: Composure
- **Module**: Composure
- **File**: CompositingMaterialPass.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``editor_hidden_params`` (Array[Name]):  [Read-Write]
- ``material`` (MaterialInterface):  [Read-Write]
- ``param_pass_mappings`` (Map[Name, Name]):  [Read-Write] Maps material texture param names to prior passes/elements. Overrides the element's param mapping list above.
- ``required_material_params`` (Map[Name, NamedCompMaterialParam]):  [Read-Write]
- ``vector_override_proxies`` (Map[Name, LinearColor]):  [Read-Write] Required for customizing the color picker widget - need a property to wrap (one for each material param).

<a id="unreal.CompositingMaterial.__init__"></a>

#### __init__

```python
def __init__(material: MaterialInterface = None,
             param_pass_mappings: Map[Name, Name] = {}) -> None
```

<a id="unreal.CompositingMaterial.material"></a>

#### material

```python
@property
def material() -> MaterialInterface
```

(MaterialInterface):  [Read-Write]

<a id="unreal.CompositingMaterial.material"></a>

#### material

```python
@material.setter
def material(value: MaterialInterface) -> None
```

<a id="unreal.CompositingMaterial.param_pass_mappings"></a>

#### param_pass_mappings

```python
@property
def param_pass_mappings() -> Map[Name, Name]
```

(Map[Name, Name]):  [Read-Write] Maps material texture param names to prior passes/elements. Overrides the element's param mapping list above.

<a id="unreal.CompositingMaterial.param_pass_mappings"></a>

#### param_pass_mappings

```python
@param_pass_mappings.setter
def param_pass_mappings(value: Map[Name, Name]) -> None
```

<a id="unreal.ComposurePostMoveSettings"></a>