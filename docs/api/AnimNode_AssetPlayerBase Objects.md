## AnimNode_AssetPlayerBase Objects

```python
class AnimNode_AssetPlayerBase(AnimNode_AssetPlayerRelevancyBase)
```

Base class for any asset playing anim node

**C++ Source:**

- **Module**: Engine
- **File**: AnimNode_AssetPlayerBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blend_weight`` (float):  [Read-Write] Last encountered blendweight for this node
- ``internal_time_accumulator`` (float):  [Read-Write] Accumulated time used to reference the asset in this node

<a id="unreal.AnimNode_AssetPlayerBase.__init__"></a>

#### __init__

```python
def __init__(blend_weight: float = 0.000000,
             internal_time_accumulator: float = 0.000000) -> None
```

<a id="unreal.AnimNode_AssetPlayerBase.blend_weight"></a>

#### blend_weight

```python
@property
def blend_weight() -> float
```

(float):  [Read-Write] Last encountered blendweight for this node

<a id="unreal.AnimNode_AssetPlayerBase.blend_weight"></a>

#### blend_weight

```python
@blend_weight.setter
def blend_weight(value: float) -> None
```

<a id="unreal.AnimNode_AssetPlayerBase.internal_time_accumulator"></a>

#### internal_time_accumulator

```python
@property
def internal_time_accumulator() -> float
```

(float):  [Read-Write] Accumulated time used to reference the asset in this node

<a id="unreal.AnimNode_AssetPlayerBase.internal_time_accumulator"></a>

#### internal_time_accumulator

```python
@internal_time_accumulator.setter
def internal_time_accumulator(value: float) -> None
```

<a id="unreal.AnimNode_BlendSpacePlayerBase"></a>