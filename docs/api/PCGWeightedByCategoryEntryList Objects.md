## PCGWeightedByCategoryEntryList Objects

```python
class PCGWeightedByCategoryEntryList(StructBase)
```

PCGWeighted by Category Entry List

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGMeshSelectorWeightedByCategory.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``category_entry`` (str):  [Read-Write]
- ``is_default`` (bool):  [Read-Write]
- ``weighted_mesh_entries`` (Array[PCGMeshSelectorWeightedEntry]):  [Read-Write]

<a id="unreal.PCGWeightedByCategoryEntryList.__init__"></a>

#### __init__

```python
def __init__(
        category_entry: str = "",
        is_default: bool = False,
        weighted_mesh_entries: Array[PCGMeshSelectorWeightedEntry] = []
) -> None
```

<a id="unreal.PCGWeightedByCategoryEntryList.category_entry"></a>

#### category_entry

```python
@property
def category_entry() -> str
```

(str):  [Read-Write]

<a id="unreal.PCGWeightedByCategoryEntryList.category_entry"></a>

#### category_entry

```python
@category_entry.setter
def category_entry(value: str) -> None
```

<a id="unreal.PCGWeightedByCategoryEntryList.is_default"></a>

#### is_default

```python
@property
def is_default() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGWeightedByCategoryEntryList.is_default"></a>

#### is_default

```python
@is_default.setter
def is_default(value: bool) -> None
```

<a id="unreal.PCGWeightedByCategoryEntryList.weighted_mesh_entries"></a>

#### weighted_mesh_entries

```python
@property
def weighted_mesh_entries() -> Array[PCGMeshSelectorWeightedEntry]
```

(Array[PCGMeshSelectorWeightedEntry]):  [Read-Write]

<a id="unreal.PCGWeightedByCategoryEntryList.weighted_mesh_entries"></a>

#### weighted_mesh_entries

```python
@weighted_mesh_entries.setter
def weighted_mesh_entries(value: Array[PCGMeshSelectorWeightedEntry]) -> None
```

<a id="unreal.PCGDebugVisualizationSettings"></a>