## MaterialExpressionTime Objects

```python
class MaterialExpressionTime(MaterialExpression)
```

Material Expression Time

**C++ Source:**

- **Module**: Engine
- **File**: MaterialExpressionTime.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``desc`` (str):  [Read-Write] A description that level designers can add (shows in the material editor UI).
- ``ignore_pause`` (bool):  [Read-Write] This time continues advancing regardless of whether the game is paused.
- ``material_expression_editor_x`` (int32):  [Read-Write]
- ``material_expression_editor_y`` (int32):  [Read-Write]
- ``override_period`` (bool):  [Read-Write] Enables or disables the Period value.
- ``period`` (float):  [Read-Write] Period at which to wrap around time

<a id="unreal.MaterialExpressionTransform"></a>