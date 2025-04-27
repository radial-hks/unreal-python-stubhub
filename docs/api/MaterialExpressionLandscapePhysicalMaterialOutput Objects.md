## MaterialExpressionLandscapePhysicalMaterialOutput Objects

```python
class MaterialExpressionLandscapePhysicalMaterialOutput(
        MaterialExpressionCustomOutput)
```

Custom output node to write out physical material weights.
This can be used to generate the dominant physical material for each point on a landscape.
Note that the use of a material output node to generate this information is optional and when a node of this type is not present we fall back on a CPU path which analyzes landscape layer data.

**C++ Source:**

- **Module**: Landscape
- **File**: MaterialExpressionLandscapePhysicalMaterialOutput.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``desc`` (str):  [Read-Write] A description that level designers can add (shows in the material editor UI).
- ``inputs`` (Array[PhysicalMaterialInput]):  [Read-Write] Array of physical material inputs.
- ``material_expression_editor_x`` (int32):  [Read-Write]
- ``material_expression_editor_y`` (int32):  [Read-Write]

<a id="unreal.MaterialExpressionLandscapeVisibilityMask"></a>