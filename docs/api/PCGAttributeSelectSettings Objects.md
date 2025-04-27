## PCGAttributeSelectSettings Objects

```python
class PCGAttributeSelectSettings(PCGSettings)
```

Take all the entries/points from the input and perform a select operation on the given attribute/property on the given axis
(if the attribute/property is a vector) and output the result into a ParamData.
It will also output the selected point if the input is a PointData.

Only support vector attributes and scalar attributes.

CustomAxis is overridable.

In case of the median operation, and the number of elements is even, we arbitrarily chose a point (Index = Num / 2)

If the OutputAttributeName is None, we will use InputSource.GetName().

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGAttributeSelectElement.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``axis`` (PCGAttributeSelectAxis):  [Read-Write]
- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
- ``custom_axis`` (Vector4):  [Read-Write]
- ``debug`` (bool):  [Read-Write]
- ``debug_buffer_size`` (int32):  [Read-Write] Size (in number of floats) of the shader debug print buffer.
- ``debug_settings`` (PCGDebugVisualizationSettings):  [Read-Write]
- ``description`` (Text):  [Read-Write]
- ``determinism_settings`` (PCGDeterminismSettings):  [Read-Write]
- ``dump_cooked_hlsl`` (bool):  [Read-Write] Dump the cooked HLSL into the log after it is generated.
- ``dump_data_descriptions`` (bool):  [Read-Write] Dump the data descriptions of input/output pins to the log.
- ``enabled`` (bool):  [Read-Write]
- ``execute_on_gpu`` (bool):  [Read-Write] Whether this node should be executed on the GPU.
- ``expose_to_library`` (bool):  [Read-Write]
- ``input_source`` (PCGAttributePropertyInputSelector):  [Read-Write]
- ``operation`` (PCGAttributeSelectOperation):  [Read-Write]
- ``output_attribute_name`` (Name):  [Read-Write]
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGAttributeSelectSettings.input_source"></a>

#### input_source

```python
@property
def input_source() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write]

<a id="unreal.PCGAttributeSelectSettings.input_source"></a>

#### input_source

```python
@input_source.setter
def input_source(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGAttributeSelectSettings.output_attribute_name"></a>

#### output_attribute_name

```python
@property
def output_attribute_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.PCGAttributeSelectSettings.output_attribute_name"></a>

#### output_attribute_name

```python
@output_attribute_name.setter
def output_attribute_name(value: Name) -> None
```

<a id="unreal.PCGAttributeSelectSettings.operation"></a>

#### operation

```python
@property
def operation() -> PCGAttributeSelectOperation
```

(PCGAttributeSelectOperation):  [Read-Write]

<a id="unreal.PCGAttributeSelectSettings.operation"></a>

#### operation

```python
@operation.setter
def operation(value: PCGAttributeSelectOperation) -> None
```

<a id="unreal.PCGAttributeSelectSettings.axis"></a>

#### axis

```python
@property
def axis() -> PCGAttributeSelectAxis
```

(PCGAttributeSelectAxis):  [Read-Write]

<a id="unreal.PCGAttributeSelectSettings.axis"></a>

#### axis

```python
@axis.setter
def axis(value: PCGAttributeSelectAxis) -> None
```

<a id="unreal.PCGAttributeSelectSettings.custom_axis"></a>

#### custom_axis

```python
@property
def custom_axis() -> Vector4
```

(Vector4):  [Read-Write]

<a id="unreal.PCGAttributeSelectSettings.custom_axis"></a>

#### custom_axis

```python
@custom_axis.setter
def custom_axis(value: Vector4) -> None
```

<a id="unreal.PCGBoundsModifierSettings"></a>