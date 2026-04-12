## DCPBuildingLayerNodeIds Objects

```python
class DCPBuildingLayerNodeIds(StructBase)
```

DCPBuilding Layer Node Ids

**C++ Source:**

- **Plugin**: WdpAssetLoader
- **Module**: BimAssetLoader
- **File**: DCPBuildingLayerAtom.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``direction`` (Vector):  [Read-Write]
- ``distance`` (float):  [Read-Write]
- ``height`` (float):  [Read-Write]
- ``move_time`` (float):  [Read-Write]
- ``node_ids`` (Array[int32]):  [Read-Write]

<a id="unreal.DCPBuildingLayerNodeIds.__init__"></a>

#### \_\_init\_\_

```python
def __init__(direction: Vector = [0.000000, 0.000000, 0.000000],
             move_time: float = 0.000000,
             distance: float = 0.000000,
             height: float = 0.000000,
             node_ids: Array[int] = []) -> None
```

<a id="unreal.DCPBuildingLayerNodeIds.direction"></a>

#### direction

```python
@property
def direction() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.DCPBuildingLayerNodeIds.direction"></a>

#### direction

```python
@direction.setter
def direction(value: Vector) -> None
```

<a id="unreal.DCPBuildingLayerNodeIds.move_time"></a>

#### move\_time

```python
@property
def move_time() -> float
```

(float):  [Read-Write]

<a id="unreal.DCPBuildingLayerNodeIds.move_time"></a>

#### move\_time

```python
@move_time.setter
def move_time(value: float) -> None
```

<a id="unreal.DCPBuildingLayerNodeIds.distance"></a>

#### distance

```python
@property
def distance() -> float
```

(float):  [Read-Write]

<a id="unreal.DCPBuildingLayerNodeIds.distance"></a>

#### distance

```python
@distance.setter
def distance(value: float) -> None
```

<a id="unreal.DCPBuildingLayerNodeIds.height"></a>

#### height

```python
@property
def height() -> float
```

(float):  [Read-Write]

<a id="unreal.DCPBuildingLayerNodeIds.height"></a>

#### height

```python
@height.setter
def height(value: float) -> None
```

<a id="unreal.DCPBuildingLayerNodeIds.node_ids"></a>

#### node\_ids

```python
@property
def node_ids() -> Array[int]
```

(Array[int32]):  [Read-Write]

<a id="unreal.DCPBuildingLayerNodeIds.node_ids"></a>

#### node\_ids

```python
@node_ids.setter
def node_ids(value: Array[int]) -> None
```

<a id="unreal.DCPBuildingLayers"></a>