## NiagaraScript Objects

```python
class NiagaraScript(NiagaraScriptBase)
```

Scripts are function graphs that define the runtime execution for a Niagara system (similar to a Blueprint).

There are three types of scripts:
1) Module: can be added as a standalone part to the emitter stack and encapsulates a single behavior, for example "Add Velocity"
2) Dynamic input: has a single output value and can be added to any input in the stack to compute such a value, for example "Random Vector"
3) Function: usually reserved for helper functions; can only be called from within modules or dynamic inputs

**C++ Source:**

- **Plugin**: Niagara
- **Module**: Niagara
- **File**: NiagaraScript.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``category`` (Text):  [Read-Write] Use property in struct returned from GetScriptData() instead
  deprecated: Property 'Category' is deprecated.
- ``collapsed_view_format`` (Text):  [Read-Write] Deprecated, use LibraryVisibility instead.
  deprecated: Property 'CollapsedViewFormat' is deprecated.
- ``conversion_utility`` (type(Class)):  [Read-Write] Use property in struct returned from GetScriptData() instead
  deprecated: Property 'ConversionUtility' is deprecated.
- ``deprecated`` (bool):  [Read-Write] Use property in struct returned from GetScriptData() instead
  deprecated: Property 'bDeprecated' is deprecated.
- ``deprecation_message`` (Text):  [Read-Write] Use property in struct returned from GetScriptData() instead
  deprecated: Property 'DeprecationMessage' is deprecated.
- ``deprecation_recommendation`` (NiagaraScript):  [Read-Write] Use property in struct returned from GetScriptData() instead
  deprecated: Property 'DeprecationRecommendation' is deprecated.
- ``description`` (Text):  [Read-Write] Use property in struct returned from GetScriptData() instead
  deprecated: Property 'Description' is deprecated.
- ``experimental`` (bool):  [Read-Write] Use property in struct returned from GetScriptData() instead
  deprecated: Property 'bExperimental' is deprecated.
- ``experimental_message`` (Text):  [Read-Write] Use property in struct returned from GetScriptData() instead
  deprecated: Property 'ExperimentalMessage' is deprecated.
- ``expose_to_library`` (bool):  [Read-Write] Deprecated, use LibraryVisibility instead.
  deprecated: Property 'bExposeToLibrary' is deprecated.
- ``keywords`` (Text):  [Read-Write] Use property in struct returned from GetScriptData() instead
  deprecated: Property 'Keywords' is deprecated.
- ``library_visibility`` (NiagaraScriptLibraryVisibility):  [Read-Write] Use property in struct returned from GetScriptData() instead
  deprecated: Property 'LibraryVisibility' is deprecated.
- ``module_usage_bitmask`` (int32):  [Read-Write] Use property in struct returned from GetScriptData() instead
  deprecated: Property 'ModuleUsageBitmask' is deprecated.
- ``note_message`` (Text):  [Read-Write] Use property in struct returned from GetScriptData() instead
  deprecated: Property 'NoteMessage' is deprecated.
- ``numeric_output_type_selection_mode`` (NiagaraNumericOutputTypeSelectionMode):  [Read-Write] Use property in struct returned from GetScriptData() instead
  deprecated: Property 'NumericOutputTypeSelectionMode' is deprecated.
- ``provided_dependencies`` (Array[Name]):  [Read-Write] Use property in struct returned from GetScriptData() instead
  deprecated: Property 'ProvidedDependencies' is deprecated.
- ``required_dependencies`` (Array[NiagaraModuleDependency]):  [Read-Write] Use property in struct returned from GetScriptData() instead
  deprecated: Property 'RequiredDependencies' is deprecated.
- ``script_meta_data`` (Map[Name, str]):  [Read-Write] Deprecated, use LibraryVisibility instead.
  deprecated: Property 'ScriptMetaData' is deprecated.
- ``source`` (NiagaraScriptSourceBase):  [Read-Write] 'Source' data/graphs for this script
  deprecated: Property 'Source' is deprecated.
- ``validation_rules`` (Array[NiagaraValidationRule]):  [Read-Write] A set of rules to apply when this script is used in the stack. To create your own rules, write a custom class that extends UNiagaraValidationRule.

<a id="unreal.NiagaraScript.module_usage_bitmask"></a>

#### module_usage_bitmask

```python
@property
def module_usage_bitmask() -> int
```

(int32):  [Read-Write] Use property in struct returned from GetScriptData() instead
deprecated: Property 'ModuleUsageBitmask' is deprecated.

<a id="unreal.NiagaraScript.module_usage_bitmask"></a>

#### module_usage_bitmask

```python
@module_usage_bitmask.setter
def module_usage_bitmask(value: int) -> None
```

<a id="unreal.NiagaraScript.category"></a>

#### category

```python
@property
def category() -> Text
```

(Text):  [Read-Write] Use property in struct returned from GetScriptData() instead
deprecated: Property 'Category' is deprecated.

<a id="unreal.NiagaraScript.category"></a>

#### category

```python
@category.setter
def category(value: Text) -> None
```

<a id="unreal.NiagaraScript.provided_dependencies"></a>

#### provided_dependencies

```python
@property
def provided_dependencies() -> Array[Name]
```

(Array[Name]):  [Read-Write] Use property in struct returned from GetScriptData() instead
deprecated: Property 'ProvidedDependencies' is deprecated.

<a id="unreal.NiagaraScript.provided_dependencies"></a>

#### provided_dependencies

```python
@provided_dependencies.setter
def provided_dependencies(value: Array[Name]) -> None
```

<a id="unreal.NiagaraScript.required_dependencies"></a>

#### required_dependencies

```python
@property
def required_dependencies() -> Array[NiagaraModuleDependency]
```

(Array[NiagaraModuleDependency]):  [Read-Write] Use property in struct returned from GetScriptData() instead
deprecated: Property 'RequiredDependencies' is deprecated.

<a id="unreal.NiagaraScript.required_dependencies"></a>

#### required_dependencies

```python
@required_dependencies.setter
def required_dependencies(value: Array[NiagaraModuleDependency]) -> None
```

<a id="unreal.NiagaraScript.deprecated"></a>

#### deprecated

```python
@property
def deprecated() -> bool
```

(bool):  [Read-Write] Use property in struct returned from GetScriptData() instead
deprecated: Property 'bDeprecated' is deprecated.

<a id="unreal.NiagaraScript.deprecated"></a>

#### deprecated

```python
@deprecated.setter
def deprecated(value: bool) -> None
```

<a id="unreal.NiagaraScript.deprecation_message"></a>

#### deprecation_message

```python
@property
def deprecation_message() -> Text
```

(Text):  [Read-Write] Use property in struct returned from GetScriptData() instead
deprecated: Property 'DeprecationMessage' is deprecated.

<a id="unreal.NiagaraScript.deprecation_message"></a>

#### deprecation_message

```python
@deprecation_message.setter
def deprecation_message(value: Text) -> None
```

<a id="unreal.NiagaraScript.deprecation_recommendation"></a>

#### deprecation_recommendation

```python
@property
def deprecation_recommendation() -> NiagaraScript
```

(NiagaraScript):  [Read-Write] Use property in struct returned from GetScriptData() instead
deprecated: Property 'DeprecationRecommendation' is deprecated.

<a id="unreal.NiagaraScript.deprecation_recommendation"></a>

#### deprecation_recommendation

```python
@deprecation_recommendation.setter
def deprecation_recommendation(value: NiagaraScript) -> None
```

<a id="unreal.NiagaraScript.conversion_utility"></a>

#### conversion_utility

```python
@property
def conversion_utility() -> Class
```

(type(Class)):  [Read-Write] Use property in struct returned from GetScriptData() instead
deprecated: Property 'ConversionUtility' is deprecated.

<a id="unreal.NiagaraScript.conversion_utility"></a>

#### conversion_utility

```python
@conversion_utility.setter
def conversion_utility(value: Class) -> None
```

<a id="unreal.NiagaraScript.experimental"></a>

#### experimental

```python
@property
def experimental() -> bool
```

(bool):  [Read-Write] Use property in struct returned from GetScriptData() instead
deprecated: Property 'bExperimental' is deprecated.

<a id="unreal.NiagaraScript.experimental"></a>

#### experimental

```python
@experimental.setter
def experimental(value: bool) -> None
```

<a id="unreal.NiagaraScript.experimental_message"></a>

#### experimental_message

```python
@property
def experimental_message() -> Text
```

(Text):  [Read-Write] Use property in struct returned from GetScriptData() instead
deprecated: Property 'ExperimentalMessage' is deprecated.

<a id="unreal.NiagaraScript.experimental_message"></a>

#### experimental_message

```python
@experimental_message.setter
def experimental_message(value: Text) -> None
```

<a id="unreal.NiagaraScript.note_message"></a>

#### note_message

```python
@property
def note_message() -> Text
```

(Text):  [Read-Write] Use property in struct returned from GetScriptData() instead
deprecated: Property 'NoteMessage' is deprecated.

<a id="unreal.NiagaraScript.note_message"></a>

#### note_message

```python
@note_message.setter
def note_message(value: Text) -> None
```

<a id="unreal.NiagaraScript.expose_to_library"></a>

#### expose_to_library

```python
@property
def expose_to_library() -> bool
```

(bool):  [Read-Write] Deprecated, use LibraryVisibility instead.
deprecated: Property 'bExposeToLibrary' is deprecated.

<a id="unreal.NiagaraScript.expose_to_library"></a>

#### expose_to_library

```python
@expose_to_library.setter
def expose_to_library(value: bool) -> None
```

<a id="unreal.NiagaraScript.library_visibility"></a>

#### library_visibility

```python
@property
def library_visibility() -> NiagaraScriptLibraryVisibility
```

(NiagaraScriptLibraryVisibility):  [Read-Write] Use property in struct returned from GetScriptData() instead
deprecated: Property 'LibraryVisibility' is deprecated.

<a id="unreal.NiagaraScript.library_visibility"></a>

#### library_visibility

```python
@library_visibility.setter
def library_visibility(value: NiagaraScriptLibraryVisibility) -> None
```

<a id="unreal.NiagaraScript.numeric_output_type_selection_mode"></a>

#### numeric_output_type_selection_mode

```python
@property
def numeric_output_type_selection_mode(
) -> NiagaraNumericOutputTypeSelectionMode
```

(NiagaraNumericOutputTypeSelectionMode):  [Read-Write] Use property in struct returned from GetScriptData() instead
deprecated: Property 'NumericOutputTypeSelectionMode' is deprecated.

<a id="unreal.NiagaraScript.numeric_output_type_selection_mode"></a>

#### numeric_output_type_selection_mode

```python
@numeric_output_type_selection_mode.setter
def numeric_output_type_selection_mode(
        value: NiagaraNumericOutputTypeSelectionMode) -> None
```

<a id="unreal.NiagaraScript.description"></a>

#### description

```python
@property
def description() -> Text
```

(Text):  [Read-Write] Use property in struct returned from GetScriptData() instead
deprecated: Property 'Description' is deprecated.

<a id="unreal.NiagaraScript.description"></a>

#### description

```python
@description.setter
def description(value: Text) -> None
```

<a id="unreal.NiagaraScript.keywords"></a>

#### keywords

```python
@property
def keywords() -> Text
```

(Text):  [Read-Write] Use property in struct returned from GetScriptData() instead
deprecated: Property 'Keywords' is deprecated.

<a id="unreal.NiagaraScript.keywords"></a>

#### keywords

```python
@keywords.setter
def keywords(value: Text) -> None
```

<a id="unreal.NiagaraScript.collapsed_view_format"></a>

#### collapsed_view_format

```python
@property
def collapsed_view_format() -> Text
```

(Text):  [Read-Write] Deprecated, use LibraryVisibility instead.
deprecated: Property 'CollapsedViewFormat' is deprecated.

<a id="unreal.NiagaraScript.collapsed_view_format"></a>

#### collapsed_view_format

```python
@collapsed_view_format.setter
def collapsed_view_format(value: Text) -> None
```

<a id="unreal.NiagaraScript.script_meta_data"></a>

#### script_meta_data

```python
@property
def script_meta_data() -> Map[Name, str]
```

(Map[Name, str]):  [Read-Write] Deprecated, use LibraryVisibility instead.
deprecated: Property 'ScriptMetaData' is deprecated.

<a id="unreal.NiagaraScript.script_meta_data"></a>

#### script_meta_data

```python
@script_meta_data.setter
def script_meta_data(value: Map[Name, str]) -> None
```

<a id="unreal.NiagaraScript.source"></a>

#### source

```python
@property
def source() -> NiagaraScriptSourceBase
```

(NiagaraScriptSourceBase):  [Read-Write] 'Source' data/graphs for this script
deprecated: Property 'Source' is deprecated.

<a id="unreal.NiagaraScript.source"></a>

#### source

```python
@source.setter
def source(value: NiagaraScriptSourceBase) -> None
```

<a id="unreal.NiagaraStackEntry"></a>