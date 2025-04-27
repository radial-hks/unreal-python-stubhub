## PCGMatchAndSetWeightedEntry Objects

```python
class PCGMatchAndSetWeightedEntry(StructBase)
```

PCGMatch and Set Weighted Entry

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGMatchAndSetWeighted.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``value`` (PCGMetadataTypesConstantStruct):  [Read-Write]
- ``weight`` (int32):  [Read-Write] Relative weight of this entry

<a id="unreal.PCGMatchAndSetWeightedEntry.__init__"></a>

#### __init__

```python
def __init__(value: PCGMetadataTypesConstantStruct = [
    PCGMetadataTypes.DOUBLE, 0.000000, 0, 0.000000, 0, [0.000000, 0.000000],
    [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000, 0.000000],
    [0.000000, 0.000000, 0.000000, 1.000000],
    [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000],
     [1.000000, 1.000000, 1.000000]], "", False,
    [0.000000, 0.000000, 0.000000], "None", [""], [""]
],
             weight: int = 0) -> None
```

<a id="unreal.PCGMatchAndSetWeightedEntry.value"></a>

#### value

```python
@property
def value() -> PCGMetadataTypesConstantStruct
```

(PCGMetadataTypesConstantStruct):  [Read-Write]

<a id="unreal.PCGMatchAndSetWeightedEntry.value"></a>

#### value

```python
@value.setter
def value(value: PCGMetadataTypesConstantStruct) -> None
```

<a id="unreal.PCGMatchAndSetWeightedEntry.weight"></a>

#### weight

```python
@property
def weight() -> int
```

(int32):  [Read-Write] Relative weight of this entry

<a id="unreal.PCGMatchAndSetWeightedEntry.weight"></a>

#### weight

```python
@weight.setter
def weight(value: int) -> None
```

<a id="unreal.PCGMatchAndSetWeightedByCategoryEntryList"></a>