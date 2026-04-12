## TreeSamplerWayInfo Objects

```python
class TreeSamplerWayInfo(StructBase)
```

Tree Sampler Way Info

**C++ Source:**

- **Plugin**: AesRuntimeModeler
- **Module**: AesRuntimeModeler
- **File**: AesRuntimeModelerMeshStruct.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cluster_ratio`` (float):  [Read-Write]
- ``col_row_num`` (Vector):  [Read-Write] PatternWithColRowNumber
- ``col_row_space`` (Vector):  [Read-Write] PatternWithColRowSpacing
- ``hole_lists`` (Array[PointsArray]):  [Read-Write]
- ``local_to_parent_transform`` (Transform):  [Read-Write]
- ``mesh_density`` (float):  [Read-Write] scatter
- ``mesh_list`` (Array[SamplerMeshSettingInfo]):  [Read-Write]
- ``nodes`` (Array[TreeSamplerNodeInfo]):  [Read-Write]
- ``random_ratio`` (float):  [Read-Write]
- ``sampler_type`` (SamplerType):  [Read-Write] UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "ParaInfo")
                 FString SamplerType;
- ``seed`` (int32):  [Read-Write]
- ``trace_object`` (TraceObjectType):  [Read-Write]
- ``z_offset`` (float):  [Read-Write] x Col y row

<a id="unreal.TreeSamplerWayInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(local_to_parent_transform: Transform = [[
    0.000000, 0.000000, 0.000000
], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]],
             seed: int = 0,
             sampler_type: SamplerType = SamplerType.DEFAULT,
             trace_object: TraceObjectType = TraceObjectType.LANDSCAPE,
             random_ratio: float = 0.000000,
             cluster_ratio: float = 0.000000,
             mesh_density: float = 0.000000,
             col_row_num: Vector = [0.000000, 0.000000, 0.000000],
             col_row_space: Vector = [0.000000, 0.000000, 0.000000],
             z_offset: float = 0.000000,
             mesh_list: Array[SamplerMeshSettingInfo] = [],
             nodes: Array[TreeSamplerNodeInfo] = [],
             hole_lists: Array[PointsArray] = []) -> None
```

<a id="unreal.TreeSamplerWayInfo.local_to_parent_transform"></a>

#### local\_to\_parent\_transform

```python
@property
def local_to_parent_transform() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.TreeSamplerWayInfo.local_to_parent_transform"></a>

#### local\_to\_parent\_transform

```python
@local_to_parent_transform.setter
def local_to_parent_transform(value: Transform) -> None
```

<a id="unreal.TreeSamplerWayInfo.seed"></a>

#### seed

```python
@property
def seed() -> int
```

(int32):  [Read-Write]

<a id="unreal.TreeSamplerWayInfo.seed"></a>

#### seed

```python
@seed.setter
def seed(value: int) -> None
```

<a id="unreal.TreeSamplerWayInfo.sampler_type"></a>

#### sampler\_type

```python
@property
def sampler_type() -> SamplerType
```

(SamplerType):  [Read-Write] UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "ParaInfo")
               FString SamplerType;

<a id="unreal.TreeSamplerWayInfo.sampler_type"></a>

#### sampler\_type

```python
@sampler_type.setter
def sampler_type(value: SamplerType) -> None
```

<a id="unreal.TreeSamplerWayInfo.trace_object"></a>

#### trace\_object

```python
@property
def trace_object() -> TraceObjectType
```

(TraceObjectType):  [Read-Write]

<a id="unreal.TreeSamplerWayInfo.trace_object"></a>

#### trace\_object

```python
@trace_object.setter
def trace_object(value: TraceObjectType) -> None
```

<a id="unreal.TreeSamplerWayInfo.random_ratio"></a>

#### random\_ratio

```python
@property
def random_ratio() -> float
```

(float):  [Read-Write]

<a id="unreal.TreeSamplerWayInfo.random_ratio"></a>

#### random\_ratio

```python
@random_ratio.setter
def random_ratio(value: float) -> None
```

<a id="unreal.TreeSamplerWayInfo.cluster_ratio"></a>

#### cluster\_ratio

```python
@property
def cluster_ratio() -> float
```

(float):  [Read-Write]

<a id="unreal.TreeSamplerWayInfo.cluster_ratio"></a>

#### cluster\_ratio

```python
@cluster_ratio.setter
def cluster_ratio(value: float) -> None
```

<a id="unreal.TreeSamplerWayInfo.mesh_density"></a>

#### mesh\_density

```python
@property
def mesh_density() -> float
```

(float):  [Read-Write] scatter

<a id="unreal.TreeSamplerWayInfo.mesh_density"></a>

#### mesh\_density

```python
@mesh_density.setter
def mesh_density(value: float) -> None
```

<a id="unreal.TreeSamplerWayInfo.col_row_num"></a>

#### col\_row\_num

```python
@property
def col_row_num() -> Vector
```

(Vector):  [Read-Write] PatternWithColRowNumber

<a id="unreal.TreeSamplerWayInfo.col_row_num"></a>

#### col\_row\_num

```python
@col_row_num.setter
def col_row_num(value: Vector) -> None
```

<a id="unreal.TreeSamplerWayInfo.col_row_space"></a>

#### col\_row\_space

```python
@property
def col_row_space() -> Vector
```

(Vector):  [Read-Write] PatternWithColRowSpacing

<a id="unreal.TreeSamplerWayInfo.col_row_space"></a>

#### col\_row\_space

```python
@col_row_space.setter
def col_row_space(value: Vector) -> None
```

<a id="unreal.TreeSamplerWayInfo.z_offset"></a>

#### z\_offset

```python
@property
def z_offset() -> float
```

(float):  [Read-Write] x Col y row

<a id="unreal.TreeSamplerWayInfo.z_offset"></a>

#### z\_offset

```python
@z_offset.setter
def z_offset(value: float) -> None
```

<a id="unreal.TreeSamplerWayInfo.mesh_list"></a>

#### mesh\_list

```python
@property
def mesh_list() -> Array[SamplerMeshSettingInfo]
```

(Array[SamplerMeshSettingInfo]):  [Read-Write]

<a id="unreal.TreeSamplerWayInfo.mesh_list"></a>

#### mesh\_list

```python
@mesh_list.setter
def mesh_list(value: Array[SamplerMeshSettingInfo]) -> None
```

<a id="unreal.TreeSamplerWayInfo.nodes"></a>

#### nodes

```python
@property
def nodes() -> Array[TreeSamplerNodeInfo]
```

(Array[TreeSamplerNodeInfo]):  [Read-Write]

<a id="unreal.TreeSamplerWayInfo.nodes"></a>

#### nodes

```python
@nodes.setter
def nodes(value: Array[TreeSamplerNodeInfo]) -> None
```

<a id="unreal.TreeSamplerWayInfo.hole_lists"></a>

#### hole\_lists

```python
@property
def hole_lists() -> Array[PointsArray]
```

(Array[PointsArray]):  [Read-Write]

<a id="unreal.TreeSamplerWayInfo.hole_lists"></a>

#### hole\_lists

```python
@hole_lists.setter
def hole_lists(value: Array[PointsArray]) -> None
```

<a id="unreal.TreeSamplerEntityInfo"></a>