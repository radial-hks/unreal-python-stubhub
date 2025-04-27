## PoseSearchAssetSamplerInput Objects

```python
class PoseSearchAssetSamplerInput(StructBase)
```

Pose Search Asset Sampler Input

**C++ Source:**

- **Plugin**: PoseSearch
- **Module**: PoseSearch
- **File**: PoseSearchAssetSamplerLibrary.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``animation`` (AnimationAsset):  [Read-Write] Animation to sample
- ``animation_time`` (float):  [Read-Write] Sampling time for Animation
- ``blend_parameters`` (Vector):  [Read-Write] blend parameters if Animation is a blend space
- ``mirror_data_table`` (MirrorDataTable):  [Read-Write]
- ``mirrored`` (bool):  [Read-Write]
- ``root_transform_origin`` (Transform):  [Read-Write] origin used to start sampling Animation at time of zero
- ``root_transform_sampling_rate`` (int32):  [Read-Write] frequency of sampling while sampling the root transform of blend spaces

<a id="unreal.PoseSearchAssetSamplerInput.__init__"></a>

#### __init__

```python
def __init__(animation: AnimationAsset = None,
             animation_time: float = 0.000000,
             root_transform_origin: Transform = [[
                 0.000000, 0.000000, 0.000000
             ], [-0.000000, 0.000000,
                 0.000000], [1.000000, 1.000000, 1.000000]],
             mirrored: bool = False,
             mirror_data_table: MirrorDataTable = None,
             blend_parameters: Vector = [0.000000, 0.000000, 0.000000],
             root_transform_sampling_rate: int = 0) -> None
```

<a id="unreal.PoseSearchAssetSamplerInput.animation"></a>

#### animation

```python
@property
def animation() -> AnimationAsset
```

(AnimationAsset):  [Read-Write] Animation to sample

<a id="unreal.PoseSearchAssetSamplerInput.animation"></a>

#### animation

```python
@animation.setter
def animation(value: AnimationAsset) -> None
```

<a id="unreal.PoseSearchAssetSamplerInput.animation_time"></a>

#### animation_time

```python
@property
def animation_time() -> float
```

(float):  [Read-Write] Sampling time for Animation

<a id="unreal.PoseSearchAssetSamplerInput.animation_time"></a>

#### animation_time

```python
@animation_time.setter
def animation_time(value: float) -> None
```

<a id="unreal.PoseSearchAssetSamplerInput.root_transform_origin"></a>

#### root_transform_origin

```python
@property
def root_transform_origin() -> Transform
```

(Transform):  [Read-Write] origin used to start sampling Animation at time of zero

<a id="unreal.PoseSearchAssetSamplerInput.root_transform_origin"></a>

#### root_transform_origin

```python
@root_transform_origin.setter
def root_transform_origin(value: Transform) -> None
```

<a id="unreal.PoseSearchAssetSamplerInput.mirrored"></a>

#### mirrored

```python
@property
def mirrored() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PoseSearchAssetSamplerInput.mirrored"></a>

#### mirrored

```python
@mirrored.setter
def mirrored(value: bool) -> None
```

<a id="unreal.PoseSearchAssetSamplerInput.mirror_data_table"></a>

#### mirror_data_table

```python
@property
def mirror_data_table() -> MirrorDataTable
```

(MirrorDataTable):  [Read-Write]

<a id="unreal.PoseSearchAssetSamplerInput.mirror_data_table"></a>

#### mirror_data_table

```python
@mirror_data_table.setter
def mirror_data_table(value: MirrorDataTable) -> None
```

<a id="unreal.PoseSearchAssetSamplerInput.blend_parameters"></a>

#### blend_parameters

```python
@property
def blend_parameters() -> Vector
```

(Vector):  [Read-Write] blend parameters if Animation is a blend space

<a id="unreal.PoseSearchAssetSamplerInput.blend_parameters"></a>

#### blend_parameters

```python
@blend_parameters.setter
def blend_parameters(value: Vector) -> None
```

<a id="unreal.PoseSearchAssetSamplerInput.root_transform_sampling_rate"></a>

#### root_transform_sampling_rate

```python
@property
def root_transform_sampling_rate() -> int
```

(int32):  [Read-Write] frequency of sampling while sampling the root transform of blend spaces

<a id="unreal.PoseSearchAssetSamplerInput.root_transform_sampling_rate"></a>

#### root_transform_sampling_rate

```python
@root_transform_sampling_rate.setter
def root_transform_sampling_rate(value: int) -> None
```

<a id="unreal.PoseSearchAssetSamplerPose"></a>