## PCGAttributeFilterThresholdSettings Objects

```python
class PCGAttributeFilterThresholdSettings(StructBase)
```

PCGAttribute Filter Threshold Settings

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGAttributeFilter.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``attribute_types`` (PCGMetadataTypesConstantStruct):  [Read-Write]
- ``inclusive`` (bool):  [Read-Write] If the threshold in included or excluded from the range.
- ``threshold_attribute`` (PCGAttributePropertyInputSelector):  [Read-Write]
- ``use_constant_threshold`` (bool):  [Read-Write]
- ``use_spatial_query`` (bool):  [Read-Write] For Point Data, enabling this option will use sampling rather than comparing points 1 to 1 directly. For other spatial data, this is always true, and for attribute sets, always false.

<a id="unreal.PCGAttributeFilterThresholdSettings.__init__"></a>

#### __init__

```python
def __init__(
    inclusive: bool = False,
    use_constant_threshold: bool = False,
    threshold_attribute: PCGAttributePropertyInputSelector = [],
    use_spatial_query: bool = False,
    attribute_types: PCGMetadataTypesConstantStruct = [
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

<a id="unreal.PCGAttributeFilterThresholdSettings.inclusive"></a>

#### inclusive

```python
@property
def inclusive() -> bool
```

(bool):  [Read-Write] If the threshold in included or excluded from the range.

<a id="unreal.PCGAttributeFilterThresholdSettings.inclusive"></a>

#### inclusive

```python
@inclusive.setter
def inclusive(value: bool) -> None
```

<a id="unreal.PCGAttributeFilterThresholdSettings.use_constant_threshold"></a>

#### use_constant_threshold

```python
@property
def use_constant_threshold() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PCGAttributeFilterThresholdSettings.use_constant_threshold"></a>

#### use_constant_threshold

```python
@use_constant_threshold.setter
def use_constant_threshold(value: bool) -> None
```

<a id="unreal.PCGAttributeFilterThresholdSettings.threshold_attribute"></a>

#### threshold_attribute

```python
@property
def threshold_attribute() -> PCGAttributePropertyInputSelector
```

(PCGAttributePropertyInputSelector):  [Read-Write]

<a id="unreal.PCGAttributeFilterThresholdSettings.threshold_attribute"></a>

#### threshold_attribute

```python
@threshold_attribute.setter
def threshold_attribute(value: PCGAttributePropertyInputSelector) -> None
```

<a id="unreal.PCGAttributeFilterThresholdSettings.use_spatial_query"></a>

#### use_spatial_query

```python
@property
def use_spatial_query() -> bool
```

(bool):  [Read-Write] For Point Data, enabling this option will use sampling rather than comparing points 1 to 1 directly. For other spatial data, this is always true, and for attribute sets, always false.

<a id="unreal.PCGAttributeFilterThresholdSettings.use_spatial_query"></a>

#### use_spatial_query

```python
@use_spatial_query.setter
def use_spatial_query(value: bool) -> None
```

<a id="unreal.PCGAttributeFilterThresholdSettings.attribute_types"></a>

#### attribute_types

```python
@property
def attribute_types() -> PCGMetadataTypesConstantStruct
```

(PCGMetadataTypesConstantStruct):  [Read-Write]

<a id="unreal.PCGAttributeFilterThresholdSettings.attribute_types"></a>

#### attribute_types

```python
@attribute_types.setter
def attribute_types(value: PCGMetadataTypesConstantStruct) -> None
```

<a id="unreal.PCGPointFilterThresholdSettings"></a>