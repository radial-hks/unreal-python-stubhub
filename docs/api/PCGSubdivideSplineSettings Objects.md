## PCGSubdivideSplineSettings Objects

```python
class PCGSubdivideSplineSettings(PCGSubdivisionBaseSettings)
```

PCGSubdivide Spline Settings

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGSubdivideSpline.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``accept_incomplete_subdivision`` (bool):  [Read-Write] If the subdivision with a given grammar doesn't fill the entire spline, setting it to true makes it a valid case.
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
- ``forward_attributes_from_modules_info`` (bool):  [Read-Write] Do a match and set with the incoming modules info, only if the modules info is passed as input.
- ``grammar_selection`` (PCGGrammarSelection):  [Read-Write] An encoded string that represents how to apply a set of rules to a series of defined modules.
- ``is_final_attribute_name`` (Name):  [Read-Write] Name of the attribute labeling the final output point from the final module.
- ``is_first_attribute_name`` (Name):  [Read-Write] Name of the attribute labeling the first output point from the first module.
- ``module_height`` (double):  [Read-Write] The height of each placed module.
- ``module_height_as_attribute`` (bool):  [Read-Write] Select the module height from an attribute.
- ``module_height_attribute`` (PCGAttributePropertyInputSelector):  [Read-Write] Selection will be used as the module height for placed modules.
- ``module_index_attribute_name`` (Name):  [Read-Write] Name of the module index output attribute name.
- ``module_info_as_input`` (bool):  [Read-Write] Set it to true to pass the info as attribute set.
- ``modules_info`` (Array[PCGSubdivisionSubmodule]):  [Read-Write] Fixed array of modules used for the subdivision.
- ``modules_info_attribute_names`` (PCGSubdivisionModuleAttributeNames):  [Read-Write] Fixed array of modules used for the subdivision.
- ``output_debug_color_attribute`` (bool):  [Read-Write]
- ``output_extremity_attributes`` (bool):  [Read-Write] Output attributes labeling the first and final points after subdivision.
- ``output_module_index_attribute`` (bool):  [Read-Write]
- ``output_scalable_attribute`` (bool):  [Read-Write]
- ``output_size_attribute`` (bool):  [Read-Write]
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``scalable_attribute_name`` (Name):  [Read-Write] Name of the Scalable output attribute name, ignored if Forward Attributes From Modules Info is true.
- ``seed`` (int32):  [Read-Write]
- ``seed_attribute`` (PCGAttributePropertyInputSelector):  [Read-Write] Attribute to use to drive seed selection. It should be convertible to an integer.
- ``size_attribute_name`` (Name):  [Read-Write] Name of the Size output attribute name, ignored if Forward Attributes From Modules Info is true.
- ``symbol_attribute_name`` (Name):  [Read-Write] Name of the Symbol output attribute name.
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.
- ``use_seed_attribute`` (bool):  [Read-Write] Controls whether we'll use an attribute to drive random seeding for stochastic processes in the subdivision.

<a id="unreal.PCGSubdivideSplineSettings.accept_incomplete_subdivision"></a>

#### accept_incomplete_subdivision

```python
@property
def accept_incomplete_subdivision() -> bool
```

(bool):  [Read-Write] If the subdivision with a given grammar doesn't fill the entire spline, setting it to true makes it a valid case.

<a id="unreal.PCGSubdivideSplineSettings.accept_incomplete_subdivision"></a>

#### accept_incomplete_subdivision

```python
@accept_incomplete_subdivision.setter
def accept_incomplete_subdivision(value: bool) -> None
```

<a id="unreal.PCGSubdivideSplineSettings.module_height_as_attribute"></a>

#### module_height_as_attribute

```python
@property
def module_height_as_attribute() -> bool
```

(bool):  [Read-Write] Select the module height from an attribute.

<a id="unreal.PCGSubdivideSplineSettings.module_height_as_attribute"></a>

#### module_height_as_attribute

```python
@module_height_as_attribute.setter
def module_height_as_attribute(value: bool) -> None
```

<a id="unreal.PCGSubdivideSplineSettings.module_height"></a>

#### module_height

```python
@property
def module_height() -> float
```

(double):  [Read-Write] The height of each placed module.

<a id="unreal.PCGSubdivideSplineSettings.module_height"></a>

#### module_height

```python
@module_height.setter
def module_height(value: float) -> None
```

<a id="unreal.PCGSubdivideSplineSettings.module_height_attribute"></a>

#### module_height_attribute

```python
@property
def module_height_attribute() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write] Selection will be used as the module height for placed modules.

<a id="unreal.PCGSubdivideSplineSettings.module_height_attribute"></a>

#### module_height_attribute

```python
@module_height_attribute.setter
def module_height_attribute(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGSubdivideSplineSettings.output_module_index_attribute"></a>

#### output_module_index_attribute

```python
@property
def output_module_index_attribute() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGSubdivideSplineSettings.output_module_index_attribute"></a>

#### output_module_index_attribute

```python
@output_module_index_attribute.setter
def output_module_index_attribute(value: bool) -> None
```

<a id="unreal.PCGSubdivideSplineSettings.module_index_attribute_name"></a>

#### module_index_attribute_name

```python
@property
def module_index_attribute_name() -> Name
```

(Name):  [Read-Write] Name of the module index output attribute name.

<a id="unreal.PCGSubdivideSplineSettings.module_index_attribute_name"></a>

#### module_index_attribute_name

```python
@module_index_attribute_name.setter
def module_index_attribute_name(value: Name) -> None
```

<a id="unreal.PCGSubdivideSplineSettings.output_extremity_attributes"></a>

#### output_extremity_attributes

```python
@property
def output_extremity_attributes() -> bool
```

(bool):  [Read-Write] Output attributes labeling the first and final points after subdivision.

<a id="unreal.PCGSubdivideSplineSettings.output_extremity_attributes"></a>

#### output_extremity_attributes

```python
@output_extremity_attributes.setter
def output_extremity_attributes(value: bool) -> None
```

<a id="unreal.PCGSubdivideSplineSettings.is_first_attribute_name"></a>

#### is_first_attribute_name

```python
@property
def is_first_attribute_name() -> Name
```

(Name):  [Read-Write] Name of the attribute labeling the first output point from the first module.

<a id="unreal.PCGSubdivideSplineSettings.is_first_attribute_name"></a>

#### is_first_attribute_name

```python
@is_first_attribute_name.setter
def is_first_attribute_name(value: Name) -> None
```

<a id="unreal.PCGSubdivideSplineSettings.is_final_attribute_name"></a>

#### is_final_attribute_name

```python
@property
def is_final_attribute_name() -> Name
```

(Name):  [Read-Write] Name of the attribute labeling the final output point from the final module.

<a id="unreal.PCGSubdivideSplineSettings.is_final_attribute_name"></a>

#### is_final_attribute_name

```python
@is_final_attribute_name.setter
def is_final_attribute_name(value: Name) -> None
```

<a id="unreal.PCGSwitchSettings"></a>