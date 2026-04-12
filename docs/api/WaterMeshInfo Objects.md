## WaterMeshInfo Objects

```python
class WaterMeshInfo(StructBase)
```

Water Mesh Info

**C++ Source:**

- **Plugin**: AesRuntimeModeler
- **Module**: AesRuntimeModeler
- **File**: AesRuntimeModelerMeshStruct.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``local_to_parent_transform`` (Transform):  [Read-Write]
- ``ways`` (Array[WaterWayInfo]):  [Read-Write]

<a id="unreal.WaterMeshInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(local_to_parent_transform: Transform = [[
    0.000000, 0.000000, 0.000000
], [-0.000000, 0.000000, 0.000000], [1.000000, 1.000000, 1.000000]],
             ways: Array[WaterWayInfo] = []) -> None
```

<a id="unreal.WaterMeshInfo.local_to_parent_transform"></a>

#### local\_to\_parent\_transform

```python
@property
def local_to_parent_transform() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.WaterMeshInfo.local_to_parent_transform"></a>

#### local\_to\_parent\_transform

```python
@local_to_parent_transform.setter
def local_to_parent_transform(value: Transform) -> None
```

<a id="unreal.WaterMeshInfo.ways"></a>

#### ways

```python
@property
def ways() -> Array[WaterWayInfo]
```

(Array[WaterWayInfo]):  [Read-Write]

<a id="unreal.WaterMeshInfo.ways"></a>

#### ways

```python
@ways.setter
def ways(value: Array[WaterWayInfo]) -> None
```

<a id="unreal.EmbankNodeInfo"></a>