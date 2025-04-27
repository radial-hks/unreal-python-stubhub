## NiagaraRendererMaterialParameters Objects

```python
class NiagaraRendererMaterialParameters(StructBase)
```

Parameters to apply to the material, these are both constant and dynamic bindings
Having any bindings set will cause a MID to be generated

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraRendererProperties.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``attribute_bindings`` (Array[NiagaraMaterialAttributeBinding]):  [Read-Write]
- ``scalar_parameters`` (Array[NiagaraRendererMaterialScalarParameter]):  [Read-Write]
- ``static_bool_parameters`` (Array[NiagaraRendererMaterialStaticBoolParameter]):  [Read-Write]
- ``texture_parameters`` (Array[NiagaraRendererMaterialTextureParameter]):  [Read-Write]
- ``vector_parameters`` (Array[NiagaraRendererMaterialVectorParameter]):  [Read-Write]

<a id="unreal.NiagaraRendererMaterialParameters.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.WaterBodyStaticMeshSettings"></a>