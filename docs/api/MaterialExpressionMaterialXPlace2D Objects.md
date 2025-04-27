## MaterialExpressionMaterialXPlace2D Objects

```python
class MaterialExpressionMaterialXPlace2D(MaterialExpression)
```

Transform incoming UV texture coordinates from one 2D frame of reference to another.
operationorder (integer enum): the order in which to perform the transform operations.
"0" or "SRT" performs -pivot, scale, rotate, translate, +pivot as per the original
implementation matching the behavior of certain DCC packages, and "1" or "TRS" performs
-pivot, translate, rotate, scale, +pivot which does not introduce texture shear.
Default is 0 "SRT" for backward compatibility.

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeImport
- **File**: MaterialExpressionPlace2D.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``const_coordinate`` (uint8):  [Read-Write] only used if Coordinates is not hooked up
- ``const_rotation_angle`` (float):  [Read-Write] only used if RotationAngle is not hooked up
- ``desc`` (str):  [Read-Write] A description that level designers can add (shows in the material editor UI).
- ``material_expression_editor_x`` (int32):  [Read-Write]
- ``material_expression_editor_y`` (int32):  [Read-Write]

<a id="unreal.MaterialExpressionPlace2D"></a>