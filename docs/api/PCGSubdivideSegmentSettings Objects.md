## PCGSubdivideSegmentSettings Objects

```python
class PCGSubdivideSegmentSettings(PCGSubdivisionBaseSettings)
```

PCGSubdivide Segment Settings

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGSubdivideSegment.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accept_incomplete_subdivision`` (bool):  [Read-Write] If the subdivision with a given grammar doesn't fill the entire segment, setting it to true makes it a valid case.
- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
- ``debug`` (bool):  [Read-Write]
- ``debug_buffer_size`` (int32):  [Read-Write] Size (in number of floats) of the shader debug print buffer.
- ``debug_color_attribute_name`` (Name):  [Read-Write] Name of the Debug Color output attribute name, ignored if Forward Attributes From Modules Info is true.
- ``debug_settings`` (PCGDebugVisualizationSettings):  [Read-Write]
- ``description`` (Text):  [Read-Write]
- ``determinism_settings`` (PCGDeterminismSettings):  [Read-Write]
- ``dump_cooked_hlsl`` (bool):  [Read-Write] Dump the cooked HLSL into the log after it is generated.
- ``dump_data_descriptions`` (bool):  [Read-Write] Dump the data descriptions of input/output pins to the log.
- ``enabled`` (bool):  [Read-Write]
- ``execute_on_gpu`` (bool):  [Read-Write] Whether this node should be executed on the GPU.
- ``expose_to_library`` (bool):  [Read-Write]
- ``extremity_neighbor_index_attribute_name`` (Name):  [Read-Write] Name of the extremity neighbor index output attribute name.
- ``flip_axis_as_attribute`` (bool):  [Read-Write] Use an attribute to determine whether we should flip axis.
- ``flip_axis_attribute`` (PCGAttributePropertyInputSelector):  [Read-Write] Name of the attribute to know if we need to flip axis.
- ``forward_attributes_from_modules_info`` (bool):  [Read-Write] Do a match and set with the incoming modules info, only if the modules info is passed as input.
- ``grammar_selection`` (PCGGrammarSelection):  [Read-Write] An encoded string that represents how to apply a set of rules to a series of defined modules.
- ``is_final_attribute_name`` (Name):  [Read-Write] Name of the attribute labeling the final output point from the final module.
- ``is_first_attribute_name`` (Name):  [Read-Write] Name of the attribute labeling the first output point from the first module.
- ``module_index_attribute_name`` (Name):  [Read-Write] Name of the module index output attribute name.
- ``module_info_as_input`` (bool):  [Read-Write] Set it to true to pass the info as attribute set.
- ``modules_info`` (Array[PCGSubdivisionSubmodule]):  [Read-Write] Fixed array of modules used for the subdivision.
- ``modules_info_attribute_names`` (PCGSubdivisionModuleAttributeNames):  [Read-Write] Fixed array of modules used for the subdivision.
- ``output_debug_color_attribute`` (bool):  [Read-Write]
- ``output_extremity_attributes`` (bool):  [Read-Write] Output attributes labeling the first and final points after subdivision.
- ``output_extremity_neighbor_index_attribute`` (bool):  [Read-Write]
- ``output_module_index_attribute`` (bool):  [Read-Write]
- ``output_scalable_attribute`` (bool):  [Read-Write]
- ``output_size_attribute`` (bool):  [Read-Write]
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``scalable_attribute_name`` (Name):  [Read-Write] Name of the Scalable output attribute name, ignored if Forward Attributes From Modules Info is true.
- ``seed`` (int32):  [Read-Write]
- ``seed_attribute`` (PCGAttributePropertyInputSelector):  [Read-Write] Attribute to use to drive seed selection. It should be convertible to an integer.
- ``should_flip_axis`` (bool):  [Read-Write] If we need to flip axis.
- ``size_attribute_name`` (Name):  [Read-Write] Name of the Size output attribute name, ignored if Forward Attributes From Modules Info is true.
- ``subdivision_axis`` (PCGSplitAxis):  [Read-Write] Subdivision direction in point local space.
- ``symbol_attribute_name`` (Name):  [Read-Write] Name of the Symbol output attribute name.
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.
- ``use_seed_attribute`` (bool):  [Read-Write] Controls whether we'll use an attribute to drive random seeding for stochastic processes in the subdivision.

<a id="unreal.PCGSubdivideSegmentSettings.subdivision_axis"></a>

#### subdivision_axis

```python
@property
def subdivision_axis() -> PCGSplitAxis
```

(PCGSplitAxis):  [Read-Write] Subdivision direction in point local space.

<a id="unreal.PCGSubdivideSegmentSettings.subdivision_axis"></a>

#### subdivision_axis

```python
@subdivision_axis.setter
def subdivision_axis(value: PCGSplitAxis) -> None
```

<a id="unreal.PCGSubdivideSegmentSettings.flip_axis_as_attribute"></a>

#### flip_axis_as_attribute

```python
@property
def flip_axis_as_attribute() -> bool
```

(bool):  [Read-Write] Use an attribute to determine whether we should flip axis.

<a id="unreal.PCGSubdivideSegmentSettings.flip_axis_as_attribute"></a>

#### flip_axis_as_attribute

```python
@flip_axis_as_attribute.setter
def flip_axis_as_attribute(value: bool) -> None
```

<a id="unreal.PCGSubdivideSegmentSettings.should_flip_axis"></a>

#### should_flip_axis

```python
@property
def should_flip_axis() -> bool
```

(bool):  [Read-Write] If we need to flip axis.

<a id="unreal.PCGSubdivideSegmentSettings.should_flip_axis"></a>

#### should_flip_axis

```python
@should_flip_axis.setter
def should_flip_axis(value: bool) -> None
```

<a id="unreal.PCGSubdivideSegmentSettings.flip_axis_attribute"></a>

#### flip_axis_attribute

```python
@property
def flip_axis_attribute() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write] Name of the attribute to know if we need to flip axis.

<a id="unreal.PCGSubdivideSegmentSettings.flip_axis_attribute"></a>

#### flip_axis_attribute

```python
@flip_axis_attribute.setter
def flip_axis_attribute(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGSubdivideSegmentSettings.accept_incomplete_subdivision"></a>

#### accept_incomplete_subdivision

```python
@property
def accept_incomplete_subdivision() -> bool
```

(bool):  [Read-Write] If the subdivision with a given grammar doesn't fill the entire segment, setting it to true makes it a valid case.

<a id="unreal.PCGSubdivideSegmentSettings.accept_incomplete_subdivision"></a>

#### accept_incomplete_subdivision

```python
@accept_incomplete_subdivision.setter
def accept_incomplete_subdivision(value: bool) -> None
```

<a id="unreal.PCGSubdivideSegmentSettings.output_module_index_attribute"></a>

#### output_module_index_attribute

```python
@property
def output_module_index_attribute() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGSubdivideSegmentSettings.output_module_index_attribute"></a>

#### output_module_index_attribute

```python
@output_module_index_attribute.setter
def output_module_index_attribute(value: bool) -> None
```

<a id="unreal.PCGSubdivideSegmentSettings.module_index_attribute_name"></a>

#### module_index_attribute_name

```python
@property
def module_index_attribute_name() -> Name
```

(Name):  [Read-Write] Name of the module index output attribute name.

<a id="unreal.PCGSubdivideSegmentSettings.module_index_attribute_name"></a>

#### module_index_attribute_name

```python
@module_index_attribute_name.setter
def module_index_attribute_name(value: Name) -> None
```

<a id="unreal.PCGSubdivideSegmentSettings.output_extremity_attributes"></a>

#### output_extremity_attributes

```python
@property
def output_extremity_attributes() -> bool
```

(bool):  [Read-Write] Output attributes labeling the first and final points after subdivision.

<a id="unreal.PCGSubdivideSegmentSettings.output_extremity_attributes"></a>

#### output_extremity_attributes

```python
@output_extremity_attributes.setter
def output_extremity_attributes(value: bool) -> None
```

<a id="unreal.PCGSubdivideSegmentSettings.is_first_attribute_name"></a>

#### is_first_attribute_name

```python
@property
def is_first_attribute_name() -> Name
```

(Name):  [Read-Write] Name of the attribute labeling the first output point from the first module.

<a id="unreal.PCGSubdivideSegmentSettings.is_first_attribute_name"></a>

#### is_first_attribute_name

```python
@is_first_attribute_name.setter
def is_first_attribute_name(value: Name) -> None
```

<a id="unreal.PCGSubdivideSegmentSettings.is_final_attribute_name"></a>

#### is_final_attribute_name

```python
@property
def is_final_attribute_name() -> Name
```

(Name):  [Read-Write] Name of the attribute labeling the final output point from the final module.

<a id="unreal.PCGSubdivideSegmentSettings.is_final_attribute_name"></a>

#### is_final_attribute_name

```python
@is_final_attribute_name.setter
def is_final_attribute_name(value: Name) -> None
```

<a id="unreal.PCGSubdivideSegmentSettings.output_extremity_neighbor_index_attribute"></a>

#### output_extremity_neighbor_index_attribute

```python
@property
def output_extremity_neighbor_index_attribute() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGSubdivideSegmentSettings.output_extremity_neighbor_index_attribute"></a>

#### output_extremity_neighbor_index_attribute

```python
@output_extremity_neighbor_index_attribute.setter
def output_extremity_neighbor_index_attribute(value: bool) -> None
```

<a id="unreal.PCGSubdivideSegmentSettings.extremity_neighbor_index_attribute_name"></a>

#### extremity_neighbor_index_attribute_name

```python
@property
def extremity_neighbor_index_attribute_name() -> Name
```

(Name):  [Read-Write] Name of the extremity neighbor index output attribute name.

<a id="unreal.PCGSubdivideSegmentSettings.extremity_neighbor_index_attribute_name"></a>

#### extremity_neighbor_index_attribute_name

```python
@extremity_neighbor_index_attribute_name.setter
def extremity_neighbor_index_attribute_name(value: Name) -> None
```

<a id="unreal.PCGSubdivideSplineSettings"></a>