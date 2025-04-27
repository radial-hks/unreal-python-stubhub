## PCGAttributeReduceSettings Objects

```python
class PCGAttributeReduceSettings(PCGSettings)
```

Take all the entries/points from the input and perform a reduce operation on the given attribute/property
and output the result into a ParamData.
Note: Special case for average on Quaternion since they are not trivially averageable. We have a simplistic approximation
that would be accurate only if the quaternions are close to each other. The accurate version of the average is using eigenvectors/eigenvalues
which is way more complicated and computationally expensive. Quaternion will also be normatilzed at the end. Beware if you are using this average.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGAttributeReduceElement.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
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
- ``join_delimiter`` (str):  [Read-Write]
- ``merge_output_attributes`` (bool):  [Read-Write] Option to merge all results into a single attribute set with multiple entries, instead of multiple attribute sets with a single value in them.
- ``operation`` (PCGAttributeReduceOperation):  [Read-Write]
- ``output_attribute_name`` (Name):  [Read-Write]
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``seed`` (int32):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGAttributeReduceSettings.input_source"></a>

#### input_source

```python
@property
def input_source() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write]

<a id="unreal.PCGAttributeReduceSettings.input_source"></a>

#### input_source

```python
@input_source.setter
def input_source(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGAttributeReduceSettings.output_attribute_name"></a>

#### output_attribute_name

```python
@property
def output_attribute_name() -> Name
```

(Name):  [Read-Write]

<a id="unreal.PCGAttributeReduceSettings.output_attribute_name"></a>

#### output_attribute_name

```python
@output_attribute_name.setter
def output_attribute_name(value: Name) -> None
```

<a id="unreal.PCGAttributeReduceSettings.operation"></a>

#### operation

```python
@property
def operation() -> PCGAttributeReduceOperation
```

(PCGAttributeReduceOperation):  [Read-Write]

<a id="unreal.PCGAttributeReduceSettings.operation"></a>

#### operation

```python
@operation.setter
def operation(value: PCGAttributeReduceOperation) -> None
```

<a id="unreal.PCGAttributeReduceSettings.join_delimiter"></a>

#### join_delimiter

```python
@property
def join_delimiter() -> str
```

(str):  [Read-Write]

<a id="unreal.PCGAttributeReduceSettings.join_delimiter"></a>

#### join_delimiter

```python
@join_delimiter.setter
def join_delimiter(value: str) -> None
```

<a id="unreal.PCGAttributeReduceSettings.merge_output_attributes"></a>

#### merge_output_attributes

```python
@property
def merge_output_attributes() -> bool
```

(bool):  [Read-Write] Option to merge all results into a single attribute set with multiple entries, instead of multiple attribute sets with a single value in them.

<a id="unreal.PCGAttributeReduceSettings.merge_output_attributes"></a>

#### merge_output_attributes

```python
@merge_output_attributes.setter
def merge_output_attributes(value: bool) -> None
```

<a id="unreal.PCGAttributeSelectSettings"></a>