## MaterialExpressionFunctionOutput Objects

```python
class MaterialExpressionFunctionOutput(MaterialExpression)
```

Material Expression Function Output

**C++ Source:**

- **Module**: Engine
- **File**: MaterialExpressionFunctionOutput.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``desc`` (str):  [Read-Write] A description that level designers can add (shows in the material editor UI).
- ``description`` (str):  [Read-Write] The output's description, which will be used as a tooltip on the connector in function call expressions that use this function.
- ``material_expression_editor_x`` (int32):  [Read-Write]
- ``material_expression_editor_y`` (int32):  [Read-Write]
- ``output_name`` (Name):  [Read-Write] The output's name, which will be drawn on the connector in function call expressions that use this function.
- ``sort_priority`` (int32):  [Read-Write] Controls where the output is displayed relative to the other outputs.

<a id="unreal.MaterialExpressionFunctionOutput.output_name"></a>

#### output_name

```python
@property
def output_name() -> Name
```

(Name):  [Read-Write] The output's name, which will be drawn on the connector in function call expressions that use this function.

<a id="unreal.MaterialExpressionFunctionOutput.output_name"></a>

#### output_name

```python
@output_name.setter
def output_name(value: Name) -> None
```

<a id="unreal.MaterialExpressionGenericConstant"></a>