## PCGUnionData Objects

```python
class PCGUnionData(PCGSpatialDataWithPointCache)
```

PCGUnion Data

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGUnionData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``data`` (Array[PCGSpatialData]):  [Read-Only]
- ``density_function`` (PCGUnionDensityFunction):  [Read-Write]
- ``keep_zero_density_points`` (bool):  [Read-Write]
- ``metadata`` (PCGMetadata):  [Read-Only] Not accessible through blueprint to make sure the constness is preserved
- ``target_actor`` (Actor):  [Read-Write] Recipient of any artifacts generated using this data.
- ``union_type`` (PCGUnionType):  [Read-Write]

<a id="unreal.PCGUnionData.data"></a>

#### data

```python
@property
def data() -> Array[PCGSpatialData]
```

(Array[PCGSpatialData]):  [Read-Only]

<a id="unreal.PCGUnionData.union_type"></a>

#### union_type

```python
@property
def union_type() -> PCGUnionType
```

(PCGUnionType):  [Read-Write]

<a id="unreal.PCGUnionData.union_type"></a>

#### union_type

```python
@union_type.setter
def union_type(value: PCGUnionType) -> None
```

<a id="unreal.PCGUnionData.density_function"></a>

#### density_function

```python
@property
def density_function() -> PCGUnionDensityFunction
```

(PCGUnionDensityFunction):  [Read-Write]

<a id="unreal.PCGUnionData.density_function"></a>

#### density_function

```python
@density_function.setter
def density_function(value: PCGUnionDensityFunction) -> None
```

<a id="unreal.PCGUnionData.initialize"></a>

#### initialize

```python
def initialize(a: PCGSpatialData, b: PCGSpatialData) -> None
```

x.initialize(a, b) -> None
Initialize

Args:
    a (PCGSpatialData): 
    b (PCGSpatialData):

<a id="unreal.PCGUnionData.add_data"></a>

#### add_data

```python
def add_data(data: PCGSpatialData) -> None
```

x.add_data(data) -> None
Add Data

Args:
    data (PCGSpatialData):

<a id="unreal.PCGVolumeData"></a>