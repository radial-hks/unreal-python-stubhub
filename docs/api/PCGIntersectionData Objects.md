## PCGIntersectionData Objects

```python
class PCGIntersectionData(PCGSpatialDataWithPointCache)
```

Generic intersection class that delays operations as long as possible.

**C++ Source:**

- **Plugin**: PCG
- **Module**: PCG
- **File**: PCGIntersectionData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``a`` (PCGSpatialData):  [Read-Only]
- ``b`` (PCGSpatialData):  [Read-Only]
- ``density_function`` (PCGIntersectionDensityFunction):  [Read-Write]
- ``keep_zero_density_points`` (bool):  [Read-Write]
- ``metadata`` (PCGMetadata):  [Read-Only] Not accessible through blueprint to make sure the constness is preserved
- ``target_actor`` (Actor):  [Read-Write] Recipient of any artifacts generated using this data.

<a id="unreal.PCGIntersectionData.density_function"></a>

#### density_function

```python
@property
def density_function() -> PCGIntersectionDensityFunction
```

(PCGIntersectionDensityFunction):  [Read-Write]

<a id="unreal.PCGIntersectionData.density_function"></a>

#### density_function

```python
@density_function.setter
def density_function(value: PCGIntersectionDensityFunction) -> None
```

<a id="unreal.PCGIntersectionData.a"></a>

#### a

```python
@property
def a() -> PCGSpatialData
```

(PCGSpatialData):  [Read-Only]

<a id="unreal.PCGIntersectionData.b"></a>

#### b

```python
@property
def b() -> PCGSpatialData
```

(PCGSpatialData):  [Read-Only]

<a id="unreal.PCGIntersectionData.initialize"></a>

#### initialize

```python
def initialize(a: PCGSpatialData, b: PCGSpatialData) -> None
```

x.initialize(a, b) -> None
Initialize

Args:
    a (PCGSpatialData): 
    b (PCGSpatialData):

<a id="unreal.PCGSurfaceData"></a>