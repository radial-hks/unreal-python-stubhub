## ZoneLaneDesc Objects

```python
class ZoneLaneDesc(StructBase)
```

Describes single lane.

**C++ Source:**

- **Plugin**: ZoneGraph
- **Module**: ZoneGraph
- **File**: ZoneGraphTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``direction`` (ZoneLaneDirection):  [Read-Write] Direction of the lane
- ``tags`` (ZoneGraphTagMask):  [Read-Write] Lane tags
- ``width`` (float):  [Read-Write] Width of the lane

<a id="unreal.ZoneLaneDesc.__init__"></a>

#### \_\_init\_\_

```python
def __init__(width: float = 0.000000,
             direction: ZoneLaneDirection = ZoneLaneDirection.NONE,
             tags: ZoneGraphTagMask = []) -> None
```

<a id="unreal.ZoneLaneDesc.width"></a>

#### width

```python
@property
def width() -> float
```

(float):  [Read-Only] Width of the lane

<a id="unreal.ZoneLaneDesc.direction"></a>

#### direction

```python
@property
def direction() -> ZoneLaneDirection
```

(ZoneLaneDirection):  [Read-Only] Direction of the lane

<a id="unreal.ZoneLaneDesc.tags"></a>

#### tags

```python
@property
def tags() -> ZoneGraphTagMask
```

(ZoneGraphTagMask):  [Read-Only] Lane tags

<a id="unreal.ZoneLaneProfileRef"></a>