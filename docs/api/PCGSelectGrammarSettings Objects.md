## PCGSelectGrammarSettings Objects

```python
class PCGSelectGrammarSettings(PCGSettings)
```

Select a grammar by comparing an input attribute against a provided set criteria one-by-one in a sequential order.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGSelectGrammar.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``break_debugger`` (bool):  [Read-Write] If a debugger is attached, triggers a breakpoint inside IPCGElement::Execute(). Editor only. Transient.
- ``category`` (Text):  [Read-Write]
- ``compared_value_attribute`` (PCGAttributePropertyInputSelector):  [Read-Write] The attribute on the input data to be compared against. Will be numerically evaluated.
- ``copy_key_for_unselected_grammar`` (bool):  [Read-Write] If no grammar is selected for a given point, pass through the key value.
- ``criteria`` (Array[PCGSelectGrammarCriterion]):  [Read-Write] Selection criteria that will be evaluated in order.
- ``criteria_as_input`` (bool):  [Read-Write] Pass criteria info as an attribute set matching the structure type 'FPCGSelectGrammarCriteria'.
- ``criteria_attribute_names`` (PCGSelectGrammarCriteriaAttributeNames):  [Read-Write] The attribute names expected for the comparison criteria.
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
- ``key`` (Name):  [Read-Write] An attribute key that represents the desired set of grammars.
- ``key_as_attribute`` (bool):  [Read-Write] Select the key with an attribute.
- ``key_attribute`` (PCGAttributePropertyInputSelector):  [Read-Write] An attribute selector for a key that represents the desired set of grammars.
- ``output_grammar_attribute`` (PCGAttributePropertyOutputSelector):  [Read-Write] The attribute to output the selected grammar.
- ``print_shader_debug_values`` (bool):  [Read-Write] Enable use of 'WriteDebugValue(uint Index, float Value)' function in your kernel. Allows you to write float values to a buffer for logging on the CPU.
- ``remap_criteria_attribute_names`` (bool):  [Read-Write] Remap expected attribute names for the comparison criteria.
- ``seed`` (int32):  [Read-Write]
- ``use_seed`` (bool):  [Read-Write]
  deprecated: Implement the PCGSettings virtual UseSeed() override.

<a id="unreal.PCGSelectGrammarSettings.key_as_attribute"></a>

#### key_as_attribute

```python
@property
def key_as_attribute() -> bool
```

(bool):  [Read-Write] Select the key with an attribute.

<a id="unreal.PCGSelectGrammarSettings.key_as_attribute"></a>

#### key_as_attribute

```python
@key_as_attribute.setter
def key_as_attribute(value: bool) -> None
```

<a id="unreal.PCGSelectGrammarSettings.key"></a>

#### key

```python
@property
def key() -> Name
```

(Name):  [Read-Write] An attribute key that represents the desired set of grammars.

<a id="unreal.PCGSelectGrammarSettings.key"></a>

#### key

```python
@key.setter
def key(value: Name) -> None
```

<a id="unreal.PCGSelectGrammarSettings.key_attribute"></a>

#### key_attribute

```python
@property
def key_attribute() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write] An attribute selector for a key that represents the desired set of grammars.

<a id="unreal.PCGSelectGrammarSettings.key_attribute"></a>

#### key_attribute

```python
@key_attribute.setter
def key_attribute(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGSelectGrammarSettings.compared_value_attribute"></a>

#### compared_value_attribute

```python
@property
def compared_value_attribute() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write] The attribute on the input data to be compared against. Will be numerically evaluated.

<a id="unreal.PCGSelectGrammarSettings.compared_value_attribute"></a>

#### compared_value_attribute

```python
@compared_value_attribute.setter
def compared_value_attribute(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGSelectGrammarSettings.criteria_as_input"></a>

#### criteria_as_input

```python
@property
def criteria_as_input() -> bool
```

(bool):  [Read-Write] Pass criteria info as an attribute set matching the structure type 'FPCGSelectGrammarCriteria'.

<a id="unreal.PCGSelectGrammarSettings.criteria_as_input"></a>

#### criteria_as_input

```python
@criteria_as_input.setter
def criteria_as_input(value: bool) -> None
```

<a id="unreal.PCGSelectGrammarSettings.criteria"></a>

#### criteria

```python
@property
def criteria() -> Array[PCGSelectGrammarCriterion]
```

(Array[PCGSelectGrammarCriterion]):  [Read-Write] Selection criteria that will be evaluated in order.

<a id="unreal.PCGSelectGrammarSettings.criteria"></a>

#### criteria

```python
@criteria.setter
def criteria(value: Array[PCGSelectGrammarCriterion]) -> None
```

<a id="unreal.PCGSelectGrammarSettings.copy_key_for_unselected_grammar"></a>

#### copy_key_for_unselected_grammar

```python
@property
def copy_key_for_unselected_grammar() -> bool
```

(bool):  [Read-Write] If no grammar is selected for a given point, pass through the key value.

<a id="unreal.PCGSelectGrammarSettings.copy_key_for_unselected_grammar"></a>

#### copy_key_for_unselected_grammar

```python
@copy_key_for_unselected_grammar.setter
def copy_key_for_unselected_grammar(value: bool) -> None
```

<a id="unreal.PCGSelectGrammarSettings.remap_criteria_attribute_names"></a>

#### remap_criteria_attribute_names

```python
@property
def remap_criteria_attribute_names() -> bool
```

(bool):  [Read-Write] Remap expected attribute names for the comparison criteria.

<a id="unreal.PCGSelectGrammarSettings.remap_criteria_attribute_names"></a>

#### remap_criteria_attribute_names

```python
@remap_criteria_attribute_names.setter
def remap_criteria_attribute_names(value: bool) -> None
```

<a id="unreal.PCGSelectGrammarSettings.criteria_attribute_names"></a>

#### criteria_attribute_names

```python
@property
def criteria_attribute_names() -> PCGSelectGrammarCriteriaAttributeNames
```

(PCGSelectGrammarCriteriaAttributeNames):  [Read-Write] The attribute names expected for the comparison criteria.

<a id="unreal.PCGSelectGrammarSettings.criteria_attribute_names"></a>

#### criteria_attribute_names

```python
@criteria_attribute_names.setter
def criteria_attribute_names(
        value: PCGSelectGrammarCriteriaAttributeNames) -> None
```

<a id="unreal.PCGSelectGrammarSettings.output_grammar_attribute"></a>

#### output_grammar_attribute

```python
@property
def output_grammar_attribute() -> PCGAttributePropertyOutputSelector
```

(PCGAttributePropertyOutputSelector):  [Read-Write] The attribute to output the selected grammar.

<a id="unreal.PCGSelectGrammarSettings.output_grammar_attribute"></a>

#### output_grammar_attribute

```python
@output_grammar_attribute.setter
def output_grammar_attribute(
        value: PCGAttributePropertyOutputSelector) -> None
```

<a id="unreal.PCGSortAttributesSettings"></a>