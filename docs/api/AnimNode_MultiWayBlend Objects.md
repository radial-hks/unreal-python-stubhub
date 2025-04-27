## AnimNode_MultiWayBlend Objects

```python
class AnimNode_MultiWayBlend(AnimNode_Base)
```

This represents a baked transition

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_MultiWayBlend.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``additive_node`` (bool):  [Read-Write]
- ``alpha_scale_bias`` (InputScaleBias):  [Read-Write]
- ``desired_alphas`` (Array[float]):  [Read-Write]
- ``normalize_alpha`` (bool):  [Read-Write]
- ``poses`` (Array[PoseLink]):  [Read-Write]

<a id="unreal.AnimNode_MultiWayBlend.__init__"></a>

#### __init__

```python
def __init__(poses: Array[PoseLink] = [],
             desired_alphas: Array[float] = [],
             alpha_scale_bias: InputScaleBias = [1.000000, 0.000000],
             additive_node: bool = False,
             normalize_alpha: bool = False) -> None
```

<a id="unreal.AnimNode_MultiWayBlend.poses"></a>

#### poses

```python
@property
def poses() -> Array[PoseLink]
```

(Array[PoseLink]):  [Read-Write]

<a id="unreal.AnimNode_MultiWayBlend.poses"></a>

#### poses

```python
@poses.setter
def poses(value: Array[PoseLink]) -> None
```

<a id="unreal.AnimNode_MultiWayBlend.desired_alphas"></a>

#### desired_alphas

```python
@property
def desired_alphas() -> Array[float]
```

(Array[float]):  [Read-Write]

<a id="unreal.AnimNode_MultiWayBlend.desired_alphas"></a>

#### desired_alphas

```python
@desired_alphas.setter
def desired_alphas(value: Array[float]) -> None
```

<a id="unreal.AnimNode_MultiWayBlend.alpha_scale_bias"></a>

#### alpha_scale_bias

```python
@property
def alpha_scale_bias() -> InputScaleBias
```

(InputScaleBias):  [Read-Write]

<a id="unreal.AnimNode_MultiWayBlend.alpha_scale_bias"></a>

#### alpha_scale_bias

```python
@alpha_scale_bias.setter
def alpha_scale_bias(value: InputScaleBias) -> None
```

<a id="unreal.AnimNode_MultiWayBlend.additive_node"></a>

#### additive_node

```python
@property
def additive_node() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AnimNode_MultiWayBlend.additive_node"></a>

#### additive_node

```python
@additive_node.setter
def additive_node(value: bool) -> None
```

<a id="unreal.AnimNode_MultiWayBlend.normalize_alpha"></a>

#### normalize_alpha

```python
@property
def normalize_alpha() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AnimNode_MultiWayBlend.normalize_alpha"></a>

#### normalize_alpha

```python
@normalize_alpha.setter
def normalize_alpha(value: bool) -> None
```

<a id="unreal.AnimNode_PoseHandler"></a>