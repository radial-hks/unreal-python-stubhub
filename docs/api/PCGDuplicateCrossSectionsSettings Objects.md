## PCGDuplicateCrossSectionsSettings Objects

```python
class PCGDuplicateCrossSectionsSettings(PCGSubdivisionBaseSettings)
```

PCGDuplicate Cross Sections Settings

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGDuplicateCrossSections.h

**Editor Properties:** (see get_editor_property/set_editor_property)

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
- ``extrude_vector`` (Vector):  [Read-Write]
- ``extrude_vector_as_attribute`` (bool):  [Read-Write] Set it to true if you want the extrude vector to be taken from the input spline as attribute, or fixed in the settings.
- ``extrude_vector_attribute`` (PCGAttributePropertyInputSelector):  [Read-Write] Attribute to be taken from the input spline containing the extrude vector for the slicing.
- ``forward_attributes_from_modules_info`` (bool):  [Read-Write] Do a match and set with the incoming modules info, only if the modules info is passed as input.
- ``grammar_selection`` (PCGGrammarSelection):  [Read-Write] An encoded string that represents how to apply a set of rules to a series of defined modules.
- ``module_info_as_input`` (bool):  [Read-Write] Set it to true to pass the info as attribute set.
- ``modules_info`` (Array[PCGSubdivisionSubmodule]):  [Read-Write] Fixed array of modules used for the subdivision.
- ``modules_info_attribute_names`` (PCGSubdivisionModuleAttributeNames):  [Read-Write] Fixed array of modules used for the subdivision.
- ``output_debug_color_attribute`` (bool):  [Read-Write]
- ``output_scalable_attribute`` (bool):  [Read-Write]
- ``output_size_attribute`` (bool):  [Read-Write]
- ``output_spline_index_attribute`` (bool):  [Read-Write]
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``scalable_attribute_name`` (Name):  [Read-Write] Name of the Scalable output attribute name, ignored if Forward Attributes From Modules Info is true.
- ``seed`` (int32):  [Read-Write]
- ``seed_attribute`` (PCGAttributePropertyInputSelector):  [Read-Write] Attribute to use to drive seed selection. It should be convertible to an integer.
- ``size_attribute_name`` (Name):  [Read-Write] Name of the Size output attribute name, ignored if Forward Attributes From Modules Info is true.
- ``spline_index_attribute_name`` (Name):  [Read-Write] Name of the spline index output attribute name.
- ``symbol_attribute_name`` (Name):  [Read-Write] Name of the Symbol output attribute name.
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.
- ``use_seed_attribute`` (bool):  [Read-Write] Controls whether we'll use an attribute to drive random seeding for stochastic processes in the subdivision.

<a id="unreal.PCGDuplicateCrossSectionsSettings.extrude_vector_as_attribute"></a>

#### extrude_vector_as_attribute

```python
@property
def extrude_vector_as_attribute() -> bool
```

(bool):  [Read-Write] Set it to true if you want the extrude vector to be taken from the input spline as attribute, or fixed in the settings.

<a id="unreal.PCGDuplicateCrossSectionsSettings.extrude_vector_as_attribute"></a>

#### extrude_vector_as_attribute

```python
@extrude_vector_as_attribute.setter
def extrude_vector_as_attribute(value: bool) -> None
```

<a id="unreal.PCGDuplicateCrossSectionsSettings.extrude_vector"></a>

#### extrude_vector

```python
@property
def extrude_vector() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.PCGDuplicateCrossSectionsSettings.extrude_vector"></a>

#### extrude_vector

```python
@extrude_vector.setter
def extrude_vector(value: Vector) -> None
```

<a id="unreal.PCGDuplicateCrossSectionsSettings.extrude_vector_attribute"></a>

#### extrude_vector_attribute

```python
@property
def extrude_vector_attribute() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write] Attribute to be taken from the input spline containing the extrude vector for the slicing.

<a id="unreal.PCGDuplicateCrossSectionsSettings.extrude_vector_attribute"></a>

#### extrude_vector_attribute

```python
@extrude_vector_attribute.setter
def extrude_vector_attribute(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGDuplicateCrossSectionsSettings.output_spline_index_attribute"></a>

#### output_spline_index_attribute

```python
@property
def output_spline_index_attribute() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGDuplicateCrossSectionsSettings.output_spline_index_attribute"></a>

#### output_spline_index_attribute

```python
@output_spline_index_attribute.setter
def output_spline_index_attribute(value: bool) -> None
```

<a id="unreal.PCGDuplicateCrossSectionsSettings.spline_index_attribute_name"></a>

#### spline_index_attribute_name

```python
@property
def spline_index_attribute_name() -> Name
```

(Name):  [Read-Write] Name of the spline index output attribute name.

<a id="unreal.PCGDuplicateCrossSectionsSettings.spline_index_attribute_name"></a>

#### spline_index_attribute_name

```python
@spline_index_attribute_name.setter
def spline_index_attribute_name(value: Name) -> None
```

<a id="unreal.PCGDuplicatePointSettings"></a>