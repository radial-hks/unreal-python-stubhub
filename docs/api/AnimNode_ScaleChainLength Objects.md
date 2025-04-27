## AnimNode_ScaleChainLength Objects

```python
class AnimNode_ScaleChainLength(AnimNode_Base)
```

Scale the length of a chain of bones.

**C++ Source:**

- **Module**: AnimGraphRuntime
- **File**: AnimNode_ScaleChainLength.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``alpha`` (float):  [Read-Write]
- ``alpha_scale_bias`` (InputScaleBias):  [Read-Write]
- ``chain_end_bone`` (BoneReference):  [Read-Write]
- ``chain_initial_length`` (ScaleChainInitialLength):  [Read-Write]
- ``chain_start_bone`` (BoneReference):  [Read-Write]
- ``default_chain_length`` (float):  [Read-Write] Default chain length, as animated.
- ``input_pose`` (PoseLink):  [Read-Write]
- ``target_location`` (Vector):  [Read-Write]

<a id="unreal.AnimNode_ScaleChainLength.__init__"></a>

#### __init__

```python
def __init__(default_chain_length: float = 0.000000,
             target_location: Vector = [0.000000, 0.000000, 0.000000],
             alpha: float = 0.000000) -> None
```

<a id="unreal.AnimNode_ScaleChainLength.default_chain_length"></a>

#### default_chain_length

```python
@property
def default_chain_length() -> float
```

(float):  [Read-Write] Default chain length, as animated.

<a id="unreal.AnimNode_ScaleChainLength.default_chain_length"></a>

#### default_chain_length

```python
@default_chain_length.setter
def default_chain_length(value: float) -> None
```

<a id="unreal.AnimNode_ScaleChainLength.target_location"></a>

#### target_location

```python
@property
def target_location() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.AnimNode_ScaleChainLength.target_location"></a>

#### target_location

```python
@target_location.setter
def target_location(value: Vector) -> None
```

<a id="unreal.AnimNode_ScaleChainLength.alpha"></a>

#### alpha

```python
@property
def alpha() -> float
```

(float):  [Read-Write]

<a id="unreal.AnimNode_ScaleChainLength.alpha"></a>

#### alpha

```python
@alpha.setter
def alpha(value: float) -> None
```

<a id="unreal.AnimNode_SplineIK"></a>