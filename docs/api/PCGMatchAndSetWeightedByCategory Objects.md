## PCGMatchAndSetWeightedByCategory Objects

```python
class PCGMatchAndSetWeightedByCategory(PCGMatchAndSetBase)
```

PCGMatch and Set Weighted by Category

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGMatchAndSetWeightedByCategory.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``categories`` (Array[PCGMatchAndSetWeightedByCategoryEntryList]):  [Read-Write] Lookup entries (key -> weighted list)
- ``category_attribute`` (Name):  [Read-Write] Attribute to match against
- ``category_type`` (PCGMetadataTypes):  [Read-Write] Type of the attribute to match against.
- ``should_mutate_seed`` (bool):  [Read-Write] Controls whether the output data should mutate its seed - prevents issues when doing multiple random processes in a row

<a id="unreal.PCGMatchAndSetWeightedByCategory.category_attribute"></a>

#### category_attribute

```python
@property
def category_attribute() -> Name
```

(Name):  [Read-Write] Attribute to match against

<a id="unreal.PCGMatchAndSetWeightedByCategory.category_attribute"></a>

#### category_attribute

```python
@category_attribute.setter
def category_attribute(value: Name) -> None
```

<a id="unreal.PCGMatchAndSetWeightedByCategory.category_type"></a>

#### category_type

```python
@property
def category_type() -> PCGMetadataTypes
```

(PCGMetadataTypes):  [Read-Write] Type of the attribute to match against.

<a id="unreal.PCGMatchAndSetWeightedByCategory.category_type"></a>

#### category_type

```python
@category_type.setter
def category_type(value: PCGMetadataTypes) -> None
```

<a id="unreal.PCGMatchAndSetWeightedByCategory.categories"></a>

#### categories

```python
@property
def categories() -> Array[PCGMatchAndSetWeightedByCategoryEntryList]
```

(Array[PCGMatchAndSetWeightedByCategoryEntryList]):  [Read-Write] Lookup entries (key -> weighted list)

<a id="unreal.PCGMatchAndSetWeightedByCategory.categories"></a>

#### categories

```python
@categories.setter
def categories(
        value: Array[PCGMatchAndSetWeightedByCategoryEntryList]) -> None
```

<a id="unreal.PCGMatchAndSetWeightedByCategory.should_mutate_seed"></a>

#### should_mutate_seed

```python
@property
def should_mutate_seed() -> bool
```

(bool):  [Read-Write] Controls whether the output data should mutate its seed - prevents issues when doing multiple random processes in a row

<a id="unreal.PCGMatchAndSetWeightedByCategory.should_mutate_seed"></a>

#### should_mutate_seed

```python
@should_mutate_seed.setter
def should_mutate_seed(value: bool) -> None
```

<a id="unreal.PCGMeshSelectorBase"></a>