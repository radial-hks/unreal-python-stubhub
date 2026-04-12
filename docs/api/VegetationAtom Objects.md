## VegetationAtom Objects

```python
class VegetationAtom(EntityAtomBase)
```

Vegetation Atom

**C++ Source:**

- **Plugin**: AesRuntimeModeler
- **Module**: WdpModelerEntity
- **File**: VegetationAtom.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cluster_ratio`` (double):  [Read-Only]
- ``column_num`` (int32):  [Read-Only]
- ``column_space`` (double):  [Read-Only]
- ``cull_regions`` (Array[VegetationCullRegion]):  [Read-Only]
- ``density`` (double):  [Read-Only]
- ``grid_type`` (WdpVegetationGridType):  [Read-Only]
- ``line_space`` (double):  [Read-Only]
- ``point_zs`` (Array[float]):  [Read-Only]
- ``random_seed`` (int32):  [Read-Only]
- ``randomness`` (double):  [Read-Only]
- ``row_num`` (int32):  [Read-Only]
- ``row_space`` (double):  [Read-Only]
- ``sampler_type`` (WdpVegetationSamplerType):  [Read-Only]
- ``snap_mode`` (WdpSnapGroundMode):  [Read-Only]
- ``z_offset`` (double):  [Read-Only]

<a id="unreal.VegetationAtom.random_seed"></a>

#### random\_seed

```python
@property
def random_seed() -> int
```

(int32):  [Read-Only]

<a id="unreal.VegetationAtom.snap_mode"></a>

#### snap\_mode

```python
@property
def snap_mode() -> WdpSnapGroundMode
```

(WdpSnapGroundMode):  [Read-Only]

<a id="unreal.VegetationAtom.z_offset"></a>

#### z\_offset

```python
@property
def z_offset() -> float
```

(double):  [Read-Only]

<a id="unreal.VegetationAtom.sampler_type"></a>

#### sampler\_type

```python
@property
def sampler_type() -> WdpVegetationSamplerType
```

(WdpVegetationSamplerType):  [Read-Only]

<a id="unreal.VegetationAtom.line_space"></a>

#### line\_space

```python
@property
def line_space() -> float
```

(double):  [Read-Only]

<a id="unreal.VegetationAtom.randomness"></a>

#### randomness

```python
@property
def randomness() -> float
```

(double):  [Read-Only]

<a id="unreal.VegetationAtom.grid_type"></a>

#### grid\_type

```python
@property
def grid_type() -> WdpVegetationGridType
```

(WdpVegetationGridType):  [Read-Only]

<a id="unreal.VegetationAtom.row_num"></a>

#### row\_num

```python
@property
def row_num() -> int
```

(int32):  [Read-Only]

<a id="unreal.VegetationAtom.column_num"></a>

#### column\_num

```python
@property
def column_num() -> int
```

(int32):  [Read-Only]

<a id="unreal.VegetationAtom.row_space"></a>

#### row\_space

```python
@property
def row_space() -> float
```

(double):  [Read-Only]

<a id="unreal.VegetationAtom.column_space"></a>

#### column\_space

```python
@property
def column_space() -> float
```

(double):  [Read-Only]

<a id="unreal.VegetationAtom.density"></a>

#### density

```python
@property
def density() -> float
```

(double):  [Read-Only]

<a id="unreal.VegetationAtom.cluster_ratio"></a>

#### cluster\_ratio

```python
@property
def cluster_ratio() -> float
```

(double):  [Read-Only]

<a id="unreal.VegetationAtom.point_zs"></a>

#### point\_zs

```python
@property
def point_zs() -> Array[float]
```

(Array[float]):  [Read-Only]

<a id="unreal.VegetationAtom.cull_regions"></a>

#### cull\_regions

```python
@property
def cull_regions() -> Array[VegetationCullRegion]
```

(Array[VegetationCullRegion]):  [Read-Only]

<a id="unreal.ModelerEmbankPolylineAtom"></a>