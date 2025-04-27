## PCGMatchAndSetWeightedByCategoryEntryList Objects

```python
class PCGMatchAndSetWeightedByCategoryEntryList(StructBase)
```

PCGMatch and Set Weighted by Category Entry List

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGMatchAndSetWeightedByCategory.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``category_value`` (PCGMetadataTypesConstantStruct):  [Read-Write]
- ``is_default`` (bool):  [Read-Write] If the category is the default, if the input does not match to anything, it will use this category.
- ``weighted_entries`` (Array[PCGMatchAndSetWeightedEntry]):  [Read-Write] Values and their weights

<a id="unreal.PCGMatchAndSetWeightedByCategoryEntryList.__init__"></a>

#### __init__

```python
def __init__(
        category_value: PCGMetadataTypesConstantStruct = [
            PCGMetadataTypes.DOUBLE, 0.000000, 0, 0.000000, 0,
            [0.000000, 0.000000], [0.000000, 0.000000, 0.000000],
            [0.000000, 0.000000, 0.000000, 0.000000],
            [0.000000, 0.000000, 0.000000, 1.000000],
            [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000],
             [1.000000, 1.000000, 1.000000]], "", False,
            [0.000000, 0.000000, 0.000000], "None", [""], [""]
        ],
        is_default: bool = False,
        weighted_entries: Array[PCGMatchAndSetWeightedEntry] = []) -> None
```

<a id="unreal.PCGMatchAndSetWeightedByCategoryEntryList.category_value"></a>

#### category_value

```python
@property
def category_value() -> PCGMetadataTypesConstantStruct
```

(PCGMetadataTypesConstantStruct):  [Read-Write]

<a id="unreal.PCGMatchAndSetWeightedByCategoryEntryList.category_value"></a>

#### category_value

```python
@category_value.setter
def category_value(value: PCGMetadataTypesConstantStruct) -> None
```

<a id="unreal.PCGMatchAndSetWeightedByCategoryEntryList.is_default"></a>

#### is_default

```python
@property
def is_default() -> bool
```

(bool):  [Read-Write] If the category is the default, if the input does not match to anything, it will use this category.

<a id="unreal.PCGMatchAndSetWeightedByCategoryEntryList.is_default"></a>

#### is_default

```python
@is_default.setter
def is_default(value: bool) -> None
```

<a id="unreal.PCGMatchAndSetWeightedByCategoryEntryList.weighted_entries"></a>

#### weighted_entries

```python
@property
def weighted_entries() -> Array[PCGMatchAndSetWeightedEntry]
```

(Array[PCGMatchAndSetWeightedEntry]):  [Read-Write] Values and their weights

<a id="unreal.PCGMatchAndSetWeightedByCategoryEntryList.weighted_entries"></a>

#### weighted_entries

```python
@weighted_entries.setter
def weighted_entries(value: Array[PCGMatchAndSetWeightedEntry]) -> None
```

<a id="unreal.PCGMeshInstanceList"></a>