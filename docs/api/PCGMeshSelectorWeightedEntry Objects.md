## PCGMeshSelectorWeightedEntry Objects

```python
class PCGMeshSelectorWeightedEntry(StructBase)
```

PCGMesh Selector Weighted Entry

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGMeshSelectorWeighted.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``descriptor`` (PCGSoftISMComponentDescriptor):  [Read-Write]
- ``display_name`` (Name):  [Read-Only]
- ``weight`` (int32):  [Read-Write]

<a id="unreal.PCGMeshSelectorWeightedEntry.__init__"></a>

#### __init__

```python
def __init__(weight: int = 0) -> None
```

<a id="unreal.PCGMeshSelectorWeightedEntry.weight"></a>

#### weight

```python
@property
def weight() -> int
```

(int32):  [Read-Write]

<a id="unreal.PCGMeshSelectorWeightedEntry.weight"></a>

#### weight

```python
@weight.setter
def weight(value: int) -> None
```

<a id="unreal.PCGWeightedByCategoryEntryList"></a>