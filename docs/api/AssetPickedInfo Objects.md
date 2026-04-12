## AssetPickedInfo Objects

```python
class AssetPickedInfo(StructBase)
```

Asset Picked Info

**C++ Source:**

- **Plugin**: WdpAssetLoader
- **Module**: BimAssetLoader
- **File**: HierarchyMeshEntity.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``entity_id`` (int64):  [Read-Write]
- ``hit_result`` (HitResult):  [Read-Write]
- ``node_id`` (int32):  [Read-Write]

<a id="unreal.AssetPickedInfo.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
    entity_id: int = 0,
    node_id: int = 0,
    hit_result: HitResult = [
        False, False, 1.000000, 0.000000, [0.000000, 0.000000, 0.000000],
        [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000],
        [0.000000, 0.000000, 0.000000], None, None, None, "None", "None", 0, 0,
        0, [0.000000, 0.000000, 0.000000], [0.000000, 0.000000, 0.000000]
    ]
) -> None
```

<a id="unreal.AssetPickedInfo.entity_id"></a>

#### entity\_id

```python
@property
def entity_id() -> int
```

(int64):  [Read-Write]

<a id="unreal.AssetPickedInfo.entity_id"></a>

#### entity\_id

```python
@entity_id.setter
def entity_id(value: int) -> None
```

<a id="unreal.AssetPickedInfo.node_id"></a>

#### node\_id

```python
@property
def node_id() -> int
```

(int32):  [Read-Write]

<a id="unreal.AssetPickedInfo.node_id"></a>

#### node\_id

```python
@node_id.setter
def node_id(value: int) -> None
```

<a id="unreal.AssetPickedInfo.hit_result"></a>

#### hit\_result

```python
@property
def hit_result() -> HitResult
```

(HitResult):  [Read-Write]

<a id="unreal.AssetPickedInfo.hit_result"></a>

#### hit\_result

```python
@hit_result.setter
def hit_result(value: HitResult) -> None
```

<a id="unreal.NodeIdGroup"></a>