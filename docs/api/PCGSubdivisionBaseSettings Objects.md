## PCGSubdivisionBaseSettings Objects

```python
class PCGSubdivisionBaseSettings(PCGSettings)
```

PCGSubdivision Base Settings

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGSubdivisionBase.h

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
- ``forward_attributes_from_modules_info`` (bool):  [Read-Write] Do a match and set with the incoming modules info, only if the modules info is passed as input.
- ``grammar_selection`` (PCGGrammarSelection):  [Read-Write] An encoded string that represents how to apply a set of rules to a series of defined modules.
- ``module_info_as_input`` (bool):  [Read-Write] Set it to true to pass the info as attribute set.
- ``modules_info`` (Array[PCGSubdivisionSubmodule]):  [Read-Write] Fixed array of modules used for the subdivision.
- ``modules_info_attribute_names`` (PCGSubdivisionModuleAttributeNames):  [Read-Write] Fixed array of modules used for the subdivision.
- ``output_debug_color_attribute`` (bool):  [Read-Write]
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

<a id="unreal.PCGSubdivisionBaseSettings.module_info_as_input"></a>

#### module_info_as_input

```python
@property
def module_info_as_input() -> bool
```

(bool):  [Read-Write] Set it to true to pass the info as attribute set.

<a id="unreal.PCGSubdivisionBaseSettings.module_info_as_input"></a>

#### module_info_as_input

```python
@module_info_as_input.setter
def module_info_as_input(value: bool) -> None
```

<a id="unreal.PCGSubdivisionBaseSettings.modules_info"></a>

#### modules_info

```python
@property
def modules_info() -> Array[PCGSubdivisionSubmodule]
```

(Array[PCGSubdivisionSubmodule]):  [Read-Write] Fixed array of modules used for the subdivision.

<a id="unreal.PCGSubdivisionBaseSettings.modules_info"></a>

#### modules_info

```python
@modules_info.setter
def modules_info(value: Array[PCGSubdivisionSubmodule]) -> None
```

<a id="unreal.PCGSubdivisionBaseSettings.modules_info_attribute_names"></a>

#### modules_info_attribute_names

```python
@property
def modules_info_attribute_names() -> PCGSubdivisionModuleAttributeNames
```

(PCGSubdivisionModuleAttributeNames):  [Read-Write] Fixed array of modules used for the subdivision.

<a id="unreal.PCGSubdivisionBaseSettings.modules_info_attribute_names"></a>

#### modules_info_attribute_names

```python
@modules_info_attribute_names.setter
def modules_info_attribute_names(
        value: PCGSubdivisionModuleAttributeNames) -> None
```

<a id="unreal.PCGSubdivisionBaseSettings.grammar_selection"></a>

#### grammar_selection

```python
@property
def grammar_selection() -> PCGGrammarSelection
```

(PCGGrammarSelection):  [Read-Write] An encoded string that represents how to apply a set of rules to a series of defined modules.

<a id="unreal.PCGSubdivisionBaseSettings.grammar_selection"></a>

#### grammar_selection

```python
@grammar_selection.setter
def grammar_selection(value: PCGGrammarSelection) -> None
```

<a id="unreal.PCGSubdivisionBaseSettings.use_seed_attribute"></a>

#### use_seed_attribute

```python
@property
def use_seed_attribute() -> bool
```

(bool):  [Read-Write] Controls whether we'll use an attribute to drive random seeding for stochastic processes in the subdivision.

<a id="unreal.PCGSubdivisionBaseSettings.use_seed_attribute"></a>

#### use_seed_attribute

```python
@use_seed_attribute.setter
def use_seed_attribute(value: bool) -> None
```

<a id="unreal.PCGSubdivisionBaseSettings.seed_attribute"></a>

#### seed_attribute

```python
@property
def seed_attribute() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write] Attribute to use to drive seed selection. It should be convertible to an integer.

<a id="unreal.PCGSubdivisionBaseSettings.seed_attribute"></a>

#### seed_attribute

```python
@seed_attribute.setter
def seed_attribute(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGSubdivisionBaseSettings.forward_attributes_from_modules_info"></a>

#### forward_attributes_from_modules_info

```python
@property
def forward_attributes_from_modules_info() -> bool
```

(bool):  [Read-Write] Do a match and set with the incoming modules info, only if the modules info is passed as input.

<a id="unreal.PCGSubdivisionBaseSettings.forward_attributes_from_modules_info"></a>

#### forward_attributes_from_modules_info

```python
@forward_attributes_from_modules_info.setter
def forward_attributes_from_modules_info(value: bool) -> None
```

<a id="unreal.PCGSubdivisionBaseSettings.symbol_attribute_name"></a>

#### symbol_attribute_name

```python
@property
def symbol_attribute_name() -> Name
```

(Name):  [Read-Write] Name of the Symbol output attribute name.

<a id="unreal.PCGSubdivisionBaseSettings.symbol_attribute_name"></a>

#### symbol_attribute_name

```python
@symbol_attribute_name.setter
def symbol_attribute_name(value: Name) -> None
```

<a id="unreal.PCGSubdivisionBaseSettings.output_size_attribute"></a>

#### output_size_attribute

```python
@property
def output_size_attribute() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGSubdivisionBaseSettings.output_size_attribute"></a>

#### output_size_attribute

```python
@output_size_attribute.setter
def output_size_attribute(value: bool) -> None
```

<a id="unreal.PCGSubdivisionBaseSettings.size_attribute_name"></a>

#### size_attribute_name

```python
@property
def size_attribute_name() -> Name
```

(Name):  [Read-Write] Name of the Size output attribute name, ignored if Forward Attributes From Modules Info is true.

<a id="unreal.PCGSubdivisionBaseSettings.size_attribute_name"></a>

#### size_attribute_name

```python
@size_attribute_name.setter
def size_attribute_name(value: Name) -> None
```

<a id="unreal.PCGSubdivisionBaseSettings.output_scalable_attribute"></a>

#### output_scalable_attribute

```python
@property
def output_scalable_attribute() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGSubdivisionBaseSettings.output_scalable_attribute"></a>

#### output_scalable_attribute

```python
@output_scalable_attribute.setter
def output_scalable_attribute(value: bool) -> None
```

<a id="unreal.PCGSubdivisionBaseSettings.scalable_attribute_name"></a>

#### scalable_attribute_name

```python
@property
def scalable_attribute_name() -> Name
```

(Name):  [Read-Write] Name of the Scalable output attribute name, ignored if Forward Attributes From Modules Info is true.

<a id="unreal.PCGSubdivisionBaseSettings.scalable_attribute_name"></a>

#### scalable_attribute_name

```python
@scalable_attribute_name.setter
def scalable_attribute_name(value: Name) -> None
```

<a id="unreal.PCGSubdivisionBaseSettings.output_debug_color_attribute"></a>

#### output_debug_color_attribute

```python
@property
def output_debug_color_attribute() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGSubdivisionBaseSettings.output_debug_color_attribute"></a>

#### output_debug_color_attribute

```python
@output_debug_color_attribute.setter
def output_debug_color_attribute(value: bool) -> None
```

<a id="unreal.PCGSubdivisionBaseSettings.debug_color_attribute_name"></a>

#### debug_color_attribute_name

```python
@property
def debug_color_attribute_name() -> Name
```

(Name):  [Read-Write] Name of the Debug Color output attribute name, ignored if Forward Attributes From Modules Info is true.

<a id="unreal.PCGSubdivisionBaseSettings.debug_color_attribute_name"></a>

#### debug_color_attribute_name

```python
@debug_color_attribute_name.setter
def debug_color_attribute_name(value: Name) -> None
```

<a id="unreal.PCGDuplicateCrossSectionsSettings"></a>