## PCGDifferenceData Objects

```python
class PCGDifferenceData(PCGSpatialDataWithPointCache)
```

PCGDifference Data

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGDifferenceData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``density_function`` (PCGDifferenceDensityFunction):  [Read-Write]
- ``diff_metadata`` (bool):  [Read-Only]
- ``difference`` (PCGSpatialData):  [Read-Only]
- ``keep_zero_density_points`` (bool):  [Read-Write]
- ``metadata`` (PCGMetadata):  [Read-Only] Not accessible through blueprint to make sure the constness is preserved
- ``source`` (PCGSpatialData):  [Read-Only]
- ``target_actor`` (Actor):  [Read-Write] Recipient of any artifacts generated using this data.

<a id="unreal.PCGDifferenceData.diff_metadata"></a>

#### diff_metadata

```python
@property
def diff_metadata() -> bool
```

(bool):  [Read-Only]

<a id="unreal.PCGDifferenceData.source"></a>

#### source

```python
@property
def source() -> PCGSpatialData
```

(PCGSpatialData):  [Read-Only]

<a id="unreal.PCGDifferenceData.difference"></a>

#### difference

```python
@property
def difference() -> PCGSpatialData
```

(PCGSpatialData):  [Read-Only]

<a id="unreal.PCGDifferenceData.density_function"></a>

#### density_function

```python
@property
def density_function() -> PCGDifferenceDensityFunction
```

(PCGDifferenceDensityFunction):  [Read-Write]

<a id="unreal.PCGDifferenceData.density_function"></a>

#### density_function

```python
@density_function.setter
def density_function(value: PCGDifferenceDensityFunction) -> None
```

<a id="unreal.PCGDifferenceData.set_density_function"></a>

#### set_density_function

```python
def set_density_function(
        density_function: PCGDifferenceDensityFunction) -> None
```

x.set_density_function(density_function) -> None
Set Density Function

Args:
    density_function (PCGDifferenceDensityFunction):

<a id="unreal.PCGDifferenceData.k2_add_difference"></a>

#### k2_add_difference

```python
def k2_add_difference(difference: PCGSpatialData) -> None
```

x.k2_add_difference(difference) -> None
K2 Add Difference

Args:
    difference (PCGSpatialData):

<a id="unreal.PCGDifferenceData.add_difference"></a>

#### add_difference

```python
def add_difference(difference: PCGSpatialData) -> None
```

deprecated: 'add_difference' was renamed to 'k2_add_difference'.

<a id="unreal.PCGDifferenceData.initialize"></a>

#### initialize

```python
def initialize(data: PCGSpatialData) -> None
```

x.initialize(data) -> None
Initialize

Args:
    data (PCGSpatialData):

<a id="unreal.PCGIntersectionData"></a>