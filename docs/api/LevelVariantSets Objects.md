## LevelVariantSets Objects

```python
class LevelVariantSets(Object)
```

Level Variant Sets

**C++ Source:**

- **Plugin**: VariantManagerContent
- **Module**: VariantManagerContent
- **File**: LevelVariantSets.h

<a id="unreal.LevelVariantSets.get_variant_set_by_name"></a>

#### get_variant_set_by_name

```python
def get_variant_set_by_name(variant_set_name: str) -> VariantSet
```

x.get_variant_set_by_name(variant_set_name) -> VariantSet
Get Variant Set by Name

Args:
    variant_set_name (str): 

Returns:
    VariantSet:

<a id="unreal.LevelVariantSets.get_variant_set"></a>

#### get_variant_set

```python
def get_variant_set(variant_set_index: int) -> VariantSet
```

x.get_variant_set(variant_set_index) -> VariantSet
Get Variant Set

Args:
    variant_set_index (int32): 

Returns:
    VariantSet:

<a id="unreal.LevelVariantSets.get_num_variant_sets"></a>

#### get_num_variant_sets

```python
def get_num_variant_sets() -> int
```

x.get_num_variant_sets() -> int32
Get Num Variant Sets

Returns:
    int32:

<a id="unreal.LevelVariantSets.remove_variant_set_by_name"></a>

#### remove_variant_set_by_name

```python
def remove_variant_set_by_name(variant_set_name: str) -> None
```

x.remove_variant_set_by_name(variant_set_name) -> None
Looks for a variant set with VariantSetName within LevelVariantSets and removes it, if it exists

Args:
    variant_set_name (str):

<a id="unreal.LevelVariantSets.remove_variant_set"></a>

#### remove_variant_set

```python
def remove_variant_set(variant_set: VariantSet) -> None
```

x.remove_variant_set(variant_set) -> None
Removes VariantSet from LevelVariantSets, if that is its parent

Args:
    variant_set (VariantSet):

<a id="unreal.LevelVariantSets.add_variant_set"></a>

#### add_variant_set

```python
def add_variant_set(variant_set: VariantSet) -> None
```

x.add_variant_set(variant_set) -> None
Adds VariantSet to the LevelVariantSets' list of VariantSets

Args:
    variant_set (VariantSet):

<a id="unreal.LevelVariantSetsActor"></a>