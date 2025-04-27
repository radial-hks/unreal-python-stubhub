## MaterialExpressionFunctionInput Objects

```python
class MaterialExpressionFunctionInput(MaterialExpression)
```

Material Expression Function Input

**C++ Source:**

- **Module**: Engine
- **File**: MaterialExpressionFunctionInput.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``desc`` (str):  [Read-Write] A description that level designers can add (shows in the material editor UI).
- ``description`` (str):  [Read-Write] The input's description, which will be used as a tooltip on the connector in function call expressions that use this function.
- ``input_name`` (Name):  [Read-Write] The input's name, which will be drawn on the connector in function call expressions that use this function.
- ``input_type`` (FunctionInputType):  [Read-Write] Type of this input.
  Input code chunks will be cast to this type, and a compiler error will be emitted if the cast fails.
- ``material_expression_editor_x`` (int32):  [Read-Write]
- ``material_expression_editor_y`` (int32):  [Read-Write]
- ``preview_value`` (Vector4f):  [Read-Write] Value used to preview this input when editing the material function.
- ``sort_priority`` (int32):  [Read-Write] Controls where the input is displayed relative to the other inputs.
- ``use_preview_value_as_default`` (bool):  [Read-Write] Whether to use the preview value or texture as the default value for this input.

<a id="unreal.MaterialExpressionFunctionInput.input_name"></a>

#### input_name

```python
@property
def input_name() -> Name
```

(Name):  [Read-Write] The input's name, which will be drawn on the connector in function call expressions that use this function.

<a id="unreal.MaterialExpressionFunctionInput.input_name"></a>

#### input_name

```python
@input_name.setter
def input_name(value: Name) -> None
```

<a id="unreal.MaterialExpressionFunctionInput.input_type"></a>

#### input_type

```python
@property
def input_type() -> FunctionInputType
```

(FunctionInputType):  [Read-Write] Type of this input.
Input code chunks will be cast to this type, and a compiler error will be emitted if the cast fails.

<a id="unreal.MaterialExpressionFunctionInput.input_type"></a>

#### input_type

```python
@input_type.setter
def input_type(value: FunctionInputType) -> None
```

<a id="unreal.MaterialExpressionFunctionInput.preview_value"></a>

#### preview_value

```python
@property
def preview_value() -> Vector4f
```

(Vector4f):  [Read-Write] Value used to preview this input when editing the material function.

<a id="unreal.MaterialExpressionFunctionInput.preview_value"></a>

#### preview_value

```python
@preview_value.setter
def preview_value(value: Vector4f) -> None
```

<a id="unreal.MaterialExpressionFunctionInput.use_preview_value_as_default"></a>

#### use_preview_value_as_default

```python
@property
def use_preview_value_as_default() -> bool
```

(bool):  [Read-Write] Whether to use the preview value or texture as the default value for this input.

<a id="unreal.MaterialExpressionFunctionInput.use_preview_value_as_default"></a>

#### use_preview_value_as_default

```python
@use_preview_value_as_default.setter
def use_preview_value_as_default(value: bool) -> None
```

<a id="unreal.MaterialExpressionFunctionInput.sort_priority"></a>

#### sort_priority

```python
@property
def sort_priority() -> int
```

(int32):  [Read-Write] Controls where the input is displayed relative to the other inputs.

<a id="unreal.MaterialExpressionFunctionInput.sort_priority"></a>

#### sort_priority

```python
@sort_priority.setter
def sort_priority(value: int) -> None
```

<a id="unreal.MaterialExpressionFunctionOutput"></a>