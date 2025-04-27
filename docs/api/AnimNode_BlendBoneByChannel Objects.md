## AnimNode_BlendBoneByChannel Objects

```python
class AnimNode_BlendBoneByChannel(AnimNode_Base)
```

Anim Node Blend Bone by Channel

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_BlendBoneByChannel.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``a`` (PoseLink):  [Read-Write]
- ``alpha`` (float):  [Read-Write]
- ``alpha_scale_bias`` (InputScaleBias):  [Read-Write]
- ``b`` (PoseLink):  [Read-Write]
- ``bone_definitions`` (Array[BlendBoneByChannelEntry]):  [Read-Write]
- ``transforms_space`` (BoneControlSpace):  [Read-Write] Space to convert transforms into prior to copying channels

<a id="unreal.AnimNode_BlendBoneByChannel.__init__"></a>

#### __init__

```python
def __init__(a: PoseLink = [],
             b: PoseLink = [],
             alpha: float = 0.000000,
             alpha_scale_bias: InputScaleBias = [1.000000, 0.000000]) -> None
```

<a id="unreal.AnimNode_BlendBoneByChannel.a"></a>

#### a

```python
@property
def a() -> PoseLink
```

(PoseLink):  [Read-Write]

<a id="unreal.AnimNode_BlendBoneByChannel.a"></a>

#### a

```python
@a.setter
def a(value: PoseLink) -> None
```

<a id="unreal.AnimNode_BlendBoneByChannel.b"></a>

#### b

```python
@property
def b() -> PoseLink
```

(PoseLink):  [Read-Write]

<a id="unreal.AnimNode_BlendBoneByChannel.b"></a>

#### b

```python
@b.setter
def b(value: PoseLink) -> None
```

<a id="unreal.AnimNode_BlendBoneByChannel.alpha"></a>

#### alpha

```python
@property
def alpha() -> float
```

(float):  [Read-Write]

<a id="unreal.AnimNode_BlendBoneByChannel.alpha"></a>

#### alpha

```python
@alpha.setter
def alpha(value: float) -> None
```

<a id="unreal.AnimNode_BlendBoneByChannel.alpha_scale_bias"></a>

#### alpha_scale_bias

```python
@property
def alpha_scale_bias() -> InputScaleBias
```

(InputScaleBias):  [Read-Write]

<a id="unreal.AnimNode_BlendBoneByChannel.alpha_scale_bias"></a>

#### alpha_scale_bias

```python
@alpha_scale_bias.setter
def alpha_scale_bias(value: InputScaleBias) -> None
```

<a id="unreal.AnimNode_BlendListBase"></a>