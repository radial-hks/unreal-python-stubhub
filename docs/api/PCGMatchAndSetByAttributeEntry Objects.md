## PCGMatchAndSetByAttributeEntry Objects

```python
class PCGMatchAndSetByAttributeEntry(StructBase)
```

PCGMatch and Set by Attribute Entry

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGMatchAndSetByAttribute.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``value`` (PCGMetadataTypesConstantStruct):  [Read-Write]
- ``value_to_match`` (PCGMetadataTypesConstantStruct):  [Read-Write]

<a id="unreal.PCGMatchAndSetByAttributeEntry.__init__"></a>

#### __init__

```python
def __init__(
    value_to_match: PCGMetadataTypesConstantStruct = [
        PCGMetadataTypes.DOUBLE, 0.000000, 0, 0.000000, 0,
        [0.000000, 0.000000], [0.000000, 0.000000, 0.000000],
        [0.000000, 0.000000, 0.000000, 0.000000],
        [0.000000, 0.000000, 0.000000, 1.000000],
        [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000],
         [1.000000, 1.000000, 1.000000]], "", False,
        [0.000000, 0.000000, 0.000000], "None", [""], [""]
    ],
    value: PCGMetadataTypesConstantStruct = [
        PCGMetadataTypes.DOUBLE, 0.000000, 0, 0.000000, 0,
        [0.000000, 0.000000], [0.000000, 0.000000, 0.000000],
        [0.000000, 0.000000, 0.000000, 0.000000],
        [0.000000, 0.000000, 0.000000, 1.000000],
        [[0.000000, 0.000000, 0.000000], [-0.000000, 0.000000, 0.000000],
         [1.000000, 1.000000, 1.000000]], "", False,
        [0.000000, 0.000000, 0.000000], "None", [""], [""]
    ]
) -> None
```

<a id="unreal.PCGMatchAndSetByAttributeEntry.value_to_match"></a>

#### value_to_match

```python
@property
def value_to_match() -> PCGMetadataTypesConstantStruct
```

(PCGMetadataTypesConstantStruct):  [Read-Write]

<a id="unreal.PCGMatchAndSetByAttributeEntry.value_to_match"></a>

#### value_to_match

```python
@value_to_match.setter
def value_to_match(value: PCGMetadataTypesConstantStruct) -> None
```

<a id="unreal.PCGMatchAndSetByAttributeEntry.value"></a>

#### value

```python
@property
def value() -> PCGMetadataTypesConstantStruct
```

(PCGMetadataTypesConstantStruct):  [Read-Write]

<a id="unreal.PCGMatchAndSetByAttributeEntry.value"></a>

#### value

```python
@value.setter
def value(value: PCGMetadataTypesConstantStruct) -> None
```

<a id="unreal.PCGMatchAndSetWeightedEntry"></a>