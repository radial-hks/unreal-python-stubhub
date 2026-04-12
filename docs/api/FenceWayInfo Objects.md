## FenceWayInfo Objects

```python
class FenceWayInfo(StructBase)
```

Fence Way Info

**C++ Source:**

- **Plugin**: AesRuntimeModeler
- **Module**: AesRuntimeModeler
- **File**: AesRuntimeModelerMeshStruct.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``closed`` (bool):  [Read-Write]
- ``corner_radius`` (float):  [Read-Write]
- ``fence_mesh_type_name`` (AssetName):  [Read-Write]
- ``fence_scale`` (float):  [Read-Write]
- ``local_to_parent_transform`` (Transform):  [Read-Write]
- ``nodes`` (Array[FenceNodeInfo]):  [Read-Write]
- ``rot_col`` (bool):  [Read-Write]
- ``use_global_rounded_corner`` (bool):  [Read-Write]

<a id="unreal.FenceWayInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(local_to_parent_transform: Transform = [[
    0.000000, 0.000000, 0.000000
], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]],
             closed: bool = False,
             use_global_rounded_corner: bool = False,
             rot_col: bool = False,
             fence_mesh_type_name: AssetName = AssetName.SM_EMBANKMENT_ASPHALT,
             corner_radius: float = 0.000000,
             fence_scale: float = 0.000000,
             nodes: Array[FenceNodeInfo] = []) -> None
```

<a id="unreal.FenceWayInfo.local_to_parent_transform"></a>

#### local\_to\_parent\_transform

```python
@property
def local_to_parent_transform() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.FenceWayInfo.local_to_parent_transform"></a>

#### local\_to\_parent\_transform

```python
@local_to_parent_transform.setter
def local_to_parent_transform(value: Transform) -> None
```

<a id="unreal.FenceWayInfo.closed"></a>

#### closed

```python
@property
def closed() -> bool
```

(bool):  [Read-Write]

<a id="unreal.FenceWayInfo.closed"></a>

#### closed

```python
@closed.setter
def closed(value: bool) -> None
```

<a id="unreal.FenceWayInfo.use_global_rounded_corner"></a>

#### use\_global\_rounded\_corner

```python
@property
def use_global_rounded_corner() -> bool
```

(bool):  [Read-Write]

<a id="unreal.FenceWayInfo.use_global_rounded_corner"></a>

#### use\_global\_rounded\_corner

```python
@use_global_rounded_corner.setter
def use_global_rounded_corner(value: bool) -> None
```

<a id="unreal.FenceWayInfo.rot_col"></a>

#### rot\_col

```python
@property
def rot_col() -> bool
```

(bool):  [Read-Write]

<a id="unreal.FenceWayInfo.rot_col"></a>

#### rot\_col

```python
@rot_col.setter
def rot_col(value: bool) -> None
```

<a id="unreal.FenceWayInfo.fence_mesh_type_name"></a>

#### fence\_mesh\_type\_name

```python
@property
def fence_mesh_type_name() -> AssetName
```

(AssetName):  [Read-Write]

<a id="unreal.FenceWayInfo.fence_mesh_type_name"></a>

#### fence\_mesh\_type\_name

```python
@fence_mesh_type_name.setter
def fence_mesh_type_name(value: AssetName) -> None
```

<a id="unreal.FenceWayInfo.corner_radius"></a>

#### corner\_radius

```python
@property
def corner_radius() -> float
```

(float):  [Read-Write]

<a id="unreal.FenceWayInfo.corner_radius"></a>

#### corner\_radius

```python
@corner_radius.setter
def corner_radius(value: float) -> None
```

<a id="unreal.FenceWayInfo.fence_scale"></a>

#### fence\_scale

```python
@property
def fence_scale() -> float
```

(float):  [Read-Write]

<a id="unreal.FenceWayInfo.fence_scale"></a>

#### fence\_scale

```python
@fence_scale.setter
def fence_scale(value: float) -> None
```

<a id="unreal.FenceWayInfo.nodes"></a>

#### nodes

```python
@property
def nodes() -> Array[FenceNodeInfo]
```

(Array[FenceNodeInfo]):  [Read-Write]

<a id="unreal.FenceWayInfo.nodes"></a>

#### nodes

```python
@nodes.setter
def nodes(value: Array[FenceNodeInfo]) -> None
```

<a id="unreal.FenceEntityInfo"></a>