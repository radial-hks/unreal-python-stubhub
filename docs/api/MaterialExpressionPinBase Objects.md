## MaterialExpressionPinBase Objects

```python
class MaterialExpressionPinBase(MaterialExpression)
```

Material Expression Pin Base

**C++ Source:**

- **Module**: Engine
- **File**: MaterialExpressionPinBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``desc`` (str):  [Read-Write] A description that level designers can add (shows in the material editor UI).
- ``material_expression_editor_x`` (int32):  [Read-Write]
- ``material_expression_editor_y`` (int32):  [Read-Write]
- ``reroute_pins`` (Array[CompositeReroute]):  [Read-Write] Underlying reroute pins used to compile material. Must call Modify after editing to update output expressions.

<a id="unreal.MaterialExpressionPixelDepth"></a>