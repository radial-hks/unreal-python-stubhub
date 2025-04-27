## OptimusVariableDescription Objects

```python
class OptimusVariableDescription(Object)
```

Optimus Variable Description

**C++ Source:**

- **Plugin**: DeformerGraph
- **Module**: OptimusCore
- **File**: OptimusVariableDescription.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``data_type`` (OptimusDataTypeRef):  [Read-Write] The data type of the variable
- ``default_value`` (OptimusValueContainer):  [Read-Write] Deprecated
  deprecated: use DefaultValueStruct instead
- ``default_value_struct`` (OptimusValueContainerStruct):  [Read-Write] The default value for the variable.
- ``value_data`` (Array[uint8]):  [Read-Write] Deprecated
  deprecated: Use CachedShaderValue instead
- ``variable_name`` (Name):  [Read-Write] Name of the variable

<a id="unreal.OptimusVariableDescription.value_data"></a>

#### value_data

```python
@property
def value_data() -> Array[int]
```

(Array[uint8]):  [Read-Write] Deprecated
deprecated: Use CachedShaderValue instead

<a id="unreal.OptimusVariableDescription.value_data"></a>

#### value_data

```python
@value_data.setter
def value_data(value: Array[int]) -> None
```

<a id="unreal.OptimusVariableDescription.default_value"></a>

#### default_value

```python
@property
def default_value() -> OptimusValueContainer
```

(OptimusValueContainer):  [Read-Write] Deprecated
deprecated: use DefaultValueStruct instead

<a id="unreal.OptimusVariableDescription.default_value"></a>

#### default_value

```python
@default_value.setter
def default_value(value: OptimusValueContainer) -> None
```

<a id="unreal.RetargetOpBase"></a>