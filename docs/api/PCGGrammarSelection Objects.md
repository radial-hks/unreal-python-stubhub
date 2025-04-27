## PCGGrammarSelection Objects

```python
class PCGGrammarSelection(StructBase)
```

PCGGrammar Selection

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGGrammar.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``grammar_as_attribute`` (bool):  [Read-Write] Read the grammar as an attribute rather than directly from the settings.
  Grammar syntax:
  - Each symbol can have multiple characters
  - Modules are defined in '[]', multiple symbols in a module are separated with ','
  - Modules can be repeated a fixed number of times, by adding a number after it (like [A,B]3 will produce ABABAB)
  - Modules can be marked repeated an indefinite number of times, with '*'. (like [A,B]* will produce ABABABAB... while it fits the allowed size).
- ``grammar_attribute`` (PCGAttributePropertyInputSelector):  [Read-Write] Attribute to be taken from the input spline containing the grammar to use.
- ``grammar_string`` (str):  [Read-Write] An encoded string that represents how to apply a set of rules to a series of defined modules.

<a id="unreal.PCGGrammarSelection.__init__"></a>

#### __init__

```python
def __init__(
        grammar_as_attribute: bool = False,
        grammar_string: str = "",
        grammar_attribute: PCGAttributePropertyInputSelector = []) -> None
```

<a id="unreal.PCGGrammarSelection.grammar_as_attribute"></a>

#### grammar_as_attribute

```python
@property
def grammar_as_attribute() -> bool
```

(bool):  [Read-Write] Read the grammar as an attribute rather than directly from the settings.
Grammar syntax:
- Each symbol can have multiple characters
- Modules are defined in '[]', multiple symbols in a module are separated with ','
- Modules can be repeated a fixed number of times, by adding a number after it (like [A,B]3 will produce ABABAB)
- Modules can be marked repeated an indefinite number of times, with '*'. (like [A,B]* will produce ABABABAB... while it fits the allowed size).

<a id="unreal.PCGGrammarSelection.grammar_as_attribute"></a>

#### grammar_as_attribute

```python
@grammar_as_attribute.setter
def grammar_as_attribute(value: bool) -> None
```

<a id="unreal.PCGGrammarSelection.grammar_string"></a>

#### grammar_string

```python
@property
def grammar_string() -> str
```

(str):  [Read-Write] An encoded string that represents how to apply a set of rules to a series of defined modules.

<a id="unreal.PCGGrammarSelection.grammar_string"></a>

#### grammar_string

```python
@grammar_string.setter
def grammar_string(value: str) -> None
```

<a id="unreal.PCGGrammarSelection.grammar_attribute"></a>

#### grammar_attribute

```python
@property
def grammar_attribute() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write] Attribute to be taken from the input spline containing the grammar to use.

<a id="unreal.PCGGrammarSelection.grammar_attribute"></a>

#### grammar_attribute

```python
@grammar_attribute.setter
def grammar_attribute(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGPinProperties"></a>