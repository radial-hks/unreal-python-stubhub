## PCGMatchAndSetWeighted Objects

```python
class PCGMatchAndSetWeighted(PCGMatchAndSetBase)
```

This Match & Set object assigns randomly a value based on weighted ratios,
provided in the entries.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGMatchAndSetWeighted.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``entries`` (Array[PCGMatchAndSetWeightedEntry]):  [Read-Write] Values and their respective weights
- ``should_mutate_seed`` (bool):  [Read-Write] Controls whether the output data should mutate its seed - prevents issues when doing multiple random processes in a row

<a id="unreal.PCGMatchAndSetWeighted.entries"></a>

#### entries

```python
@property
def entries() -> Array[PCGMatchAndSetWeightedEntry]
```

(Array[PCGMatchAndSetWeightedEntry]):  [Read-Write] Values and their respective weights

<a id="unreal.PCGMatchAndSetWeighted.entries"></a>

#### entries

```python
@entries.setter
def entries(value: Array[PCGMatchAndSetWeightedEntry]) -> None
```

<a id="unreal.PCGMatchAndSetWeighted.should_mutate_seed"></a>

#### should_mutate_seed

```python
@property
def should_mutate_seed() -> bool
```

(bool):  [Read-Write] Controls whether the output data should mutate its seed - prevents issues when doing multiple random processes in a row

<a id="unreal.PCGMatchAndSetWeighted.should_mutate_seed"></a>

#### should_mutate_seed

```python
@should_mutate_seed.setter
def should_mutate_seed(value: bool) -> None
```

<a id="unreal.PCGMatchAndSetWeightedByCategory"></a>