## LayerBlendInput Objects

```python
class LayerBlendInput(StructBase)
```

Layer Blend Input

**C++ Source:**

- **Module**: Landscape
- **File**: MaterialExpressionLandscapeLayerBlend.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blend_type`` (LandscapeLayerBlendType):  [Read-Write]
- ``const_height_input`` (float):  [Read-Write] only used if HeightInput is not hooked up
- ``const_layer_input`` (Vector):  [Read-Write] only used if LayerInput is not hooked up
- ``layer_name`` (Name):  [Read-Write]
- ``preview_weight`` (float):  [Read-Write]

<a id="unreal.LayerBlendInput.__init__"></a>

#### __init__

```python
def __init__() -> None
```

<a id="unreal.PhysicalMaterialInput"></a>