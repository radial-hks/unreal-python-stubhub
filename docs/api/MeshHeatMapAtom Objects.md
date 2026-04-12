## MeshHeatMapAtom Objects

```python
class MeshHeatMapAtom(EntityAtomBase)
```

Mesh Heat Map Atom

**C++ Source:**

- **Plugin**: WdpRuntimeAPI
- **Module**: WdpDataV
- **File**: MeshHeatMapAtom.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``gradient_setting`` (Array[str]):  [Read-Write]
- ``mapping_height_range`` (Vector2D):  [Read-Write]
- ``mapping_value_range`` (Vector2D):  [Read-Write]
- ``mesh_boundary`` (Array[Vector2D]):  [Read-Write]
- ``mesh_grid_space`` (float):  [Read-Write]
- ``opacity`` (float):  [Read-Write]
- ``point_coord_z`` (float):  [Read-Write]
- ``point_data`` (Array[MeshHeatMapPointData]):  [Read-Write]

<a id="unreal.MeshHeatMapAtom.point_data"></a>

#### point\_data

```python
@property
def point_data() -> Array[MeshHeatMapPointData]
```

(Array[MeshHeatMapPointData]):  [Read-Write]

<a id="unreal.MeshHeatMapAtom.point_data"></a>

#### point\_data

```python
@point_data.setter
def point_data(value: Array[MeshHeatMapPointData]) -> None
```

<a id="unreal.MeshHeatMapAtom.mesh_boundary"></a>

#### mesh\_boundary

```python
@property
def mesh_boundary() -> Array[Vector2D]
```

(Array[Vector2D]):  [Read-Write]

<a id="unreal.MeshHeatMapAtom.mesh_boundary"></a>

#### mesh\_boundary

```python
@mesh_boundary.setter
def mesh_boundary(value: Array[Vector2D]) -> None
```

<a id="unreal.MeshHeatMapAtom.point_coord_z"></a>

#### point\_coord\_z

```python
@property
def point_coord_z() -> float
```

(float):  [Read-Write]

<a id="unreal.MeshHeatMapAtom.point_coord_z"></a>

#### point\_coord\_z

```python
@point_coord_z.setter
def point_coord_z(value: float) -> None
```

<a id="unreal.MeshHeatMapAtom.mesh_grid_space"></a>

#### mesh\_grid\_space

```python
@property
def mesh_grid_space() -> float
```

(float):  [Read-Write]

<a id="unreal.MeshHeatMapAtom.mesh_grid_space"></a>

#### mesh\_grid\_space

```python
@mesh_grid_space.setter
def mesh_grid_space(value: float) -> None
```

<a id="unreal.MeshHeatMapAtom.mapping_value_range"></a>

#### mapping\_value\_range

```python
@property
def mapping_value_range() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.MeshHeatMapAtom.mapping_value_range"></a>

#### mapping\_value\_range

```python
@mapping_value_range.setter
def mapping_value_range(value: Vector2D) -> None
```

<a id="unreal.MeshHeatMapAtom.mapping_height_range"></a>

#### mapping\_height\_range

```python
@property
def mapping_height_range() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.MeshHeatMapAtom.mapping_height_range"></a>

#### mapping\_height\_range

```python
@mapping_height_range.setter
def mapping_height_range(value: Vector2D) -> None
```

<a id="unreal.MeshHeatMapAtom.gradient_setting"></a>

#### gradient\_setting

```python
@property
def gradient_setting() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.MeshHeatMapAtom.gradient_setting"></a>

#### gradient\_setting

```python
@gradient_setting.setter
def gradient_setting(value: Array[str]) -> None
```

<a id="unreal.MeshHeatMapAtom.opacity"></a>

#### opacity

```python
@property
def opacity() -> float
```

(float):  [Read-Write]

<a id="unreal.MeshHeatMapAtom.opacity"></a>

#### opacity

```python
@opacity.setter
def opacity(value: float) -> None
```

<a id="unreal.MeshHeatMapEntity"></a>