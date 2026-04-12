## glTFRuntimeSkeletalAnimationConfig Objects

```python
class glTFRuntimeSkeletalAnimationConfig(StructBase)
```

Gl TFRuntime Skeletal Animation Config

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: glTFRuntime
- **File**: glTFRuntimeParser.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cache_mode`` (EglTFRuntimeCacheMode):  [Read-Write]
- ``curve_remapper`` (glTFRuntimeSkeletalAnimationCurveRemapperHook):  [Read-Write]
- ``curves_name_map`` (Map[str, str]):  [Read-Write]
- ``fill_all_curves`` (bool):  [Read-Write]
- ``frame_rotation_remapper`` (glTFRuntimeSkeletalAnimationFrameRotationRemapperHook):  [Read-Write]
- ``frame_translation_remapper`` (glTFRuntimeSkeletalAnimationFrameTranslationRemapperHook):  [Read-Write]
- ``frames_per_second`` (float):  [Read-Write]
- ``override_track_name_from_extension`` (Array[glTFRuntimePathItem]):  [Read-Write]
- ``pose_for_retargeting`` (PoseAsset):  [Read-Write]
- ``remove_morph_targets`` (bool):  [Read-Write]
- ``remove_root_motion`` (bool):  [Read-Write]
- ``remove_rotations`` (bool):  [Read-Write]
- ``remove_scales`` (bool):  [Read-Write]
- ``remove_tracks`` (Array[str]):  [Read-Write]
- ``remove_translations`` (bool):  [Read-Write]
- ``retarget_skin_index`` (int32):  [Read-Write]
- ``retarget_to`` (Skeleton):  [Read-Write]
- ``retarget_to_skeletal_mesh`` (SkeletalMesh):  [Read-Write]
- ``root_motion`` (bool):  [Read-Write]
- ``root_motion_root_lock`` (RootMotionRootLock):  [Read-Write]
- ``root_node_index`` (int32):  [Read-Write]
- ``transform_pose`` (Map[str, Transform]):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalAnimationConfig.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        cache_mode: EglTFRuntimeCacheMode = EglTFRuntimeCacheMode.READ_WRITE,
        root_node_index: int = 0,
        root_motion: bool = False,
        remove_root_motion: bool = False,
        root_motion_root_lock: RootMotionRootLock = RootMotionRootLock.
    REF_POSE,
        remove_translations: bool = False,
        remove_rotations: bool = False,
        remove_scales: bool = False,
        remove_morph_targets: bool = False,
        override_track_name_from_extension: Array[glTFRuntimePathItem] = [],
        remove_tracks: Array[str] = [],
        curve_remapper: glTFRuntimeSkeletalAnimationCurveRemapperHook = [
            glTFRuntimeAnimationCurveRemapper(), None
        ],
        retarget_to: Skeleton = None,
        retarget_to_skeletal_mesh: SkeletalMesh = None,
        transform_pose: Map[str, Transform] = {},
        frame_translation_remapper:
    glTFRuntimeSkeletalAnimationFrameTranslationRemapperHook = [
        glTFRuntimeAnimationFrameTranslationRemapper(), None
    ],
        frame_rotation_remapper:
    glTFRuntimeSkeletalAnimationFrameRotationRemapperHook = [
        glTFRuntimeAnimationFrameRotationRemapper(), None
    ],
        frames_per_second: float = 0.000000,
        fill_all_curves: bool = False,
        curves_name_map: Map[str, str] = {},
        retarget_skin_index: int = 0,
        pose_for_retargeting: PoseAsset = None) -> None
```

<a id="unreal.glTFRuntimeSkeletalAnimationConfig.cache_mode"></a>

#### cache\_mode

```python
@property
def cache_mode() -> EglTFRuntimeCacheMode
```

(EglTFRuntimeCacheMode):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalAnimationConfig.cache_mode"></a>

#### cache\_mode

```python
@cache_mode.setter
def cache_mode(value: EglTFRuntimeCacheMode) -> None
```

<a id="unreal.glTFRuntimeSkeletalAnimationConfig.root_node_index"></a>

#### root\_node\_index

```python
@property
def root_node_index() -> int
```

(int32):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalAnimationConfig.root_node_index"></a>

#### root\_node\_index

```python
@root_node_index.setter
def root_node_index(value: int) -> None
```

<a id="unreal.glTFRuntimeSkeletalAnimationConfig.root_motion"></a>

#### root\_motion

```python
@property
def root_motion() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalAnimationConfig.root_motion"></a>

#### root\_motion

```python
@root_motion.setter
def root_motion(value: bool) -> None
```

<a id="unreal.glTFRuntimeSkeletalAnimationConfig.remove_root_motion"></a>

#### remove\_root\_motion

```python
@property
def remove_root_motion() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalAnimationConfig.remove_root_motion"></a>

#### remove\_root\_motion

```python
@remove_root_motion.setter
def remove_root_motion(value: bool) -> None
```

<a id="unreal.glTFRuntimeSkeletalAnimationConfig.root_motion_root_lock"></a>

#### root\_motion\_root\_lock

```python
@property
def root_motion_root_lock() -> RootMotionRootLock
```

(RootMotionRootLock):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalAnimationConfig.root_motion_root_lock"></a>

#### root\_motion\_root\_lock

```python
@root_motion_root_lock.setter
def root_motion_root_lock(value: RootMotionRootLock) -> None
```

<a id="unreal.glTFRuntimeSkeletalAnimationConfig.remove_translations"></a>

#### remove\_translations

```python
@property
def remove_translations() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalAnimationConfig.remove_translations"></a>

#### remove\_translations

```python
@remove_translations.setter
def remove_translations(value: bool) -> None
```

<a id="unreal.glTFRuntimeSkeletalAnimationConfig.remove_rotations"></a>

#### remove\_rotations

```python
@property
def remove_rotations() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalAnimationConfig.remove_rotations"></a>

#### remove\_rotations

```python
@remove_rotations.setter
def remove_rotations(value: bool) -> None
```

<a id="unreal.glTFRuntimeSkeletalAnimationConfig.remove_scales"></a>

#### remove\_scales

```python
@property
def remove_scales() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalAnimationConfig.remove_scales"></a>

#### remove\_scales

```python
@remove_scales.setter
def remove_scales(value: bool) -> None
```

<a id="unreal.glTFRuntimeSkeletalAnimationConfig.remove_morph_targets"></a>

#### remove\_morph\_targets

```python
@property
def remove_morph_targets() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalAnimationConfig.remove_morph_targets"></a>

#### remove\_morph\_targets

```python
@remove_morph_targets.setter
def remove_morph_targets(value: bool) -> None
```

<a id="unreal.glTFRuntimeSkeletalAnimationConfig.override_track_name_from_extension"></a>

#### override\_track\_name\_from\_extension

```python
@property
def override_track_name_from_extension() -> Array[glTFRuntimePathItem]
```

(Array[glTFRuntimePathItem]):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalAnimationConfig.override_track_name_from_extension"></a>

#### override\_track\_name\_from\_extension

```python
@override_track_name_from_extension.setter
def override_track_name_from_extension(
        value: Array[glTFRuntimePathItem]) -> None
```

<a id="unreal.glTFRuntimeSkeletalAnimationConfig.remove_tracks"></a>

#### remove\_tracks

```python
@property
def remove_tracks() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalAnimationConfig.remove_tracks"></a>

#### remove\_tracks

```python
@remove_tracks.setter
def remove_tracks(value: Array[str]) -> None
```

<a id="unreal.glTFRuntimeSkeletalAnimationConfig.curve_remapper"></a>

#### curve\_remapper

```python
@property
def curve_remapper() -> glTFRuntimeSkeletalAnimationCurveRemapperHook
```

(glTFRuntimeSkeletalAnimationCurveRemapperHook):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalAnimationConfig.curve_remapper"></a>

#### curve\_remapper

```python
@curve_remapper.setter
def curve_remapper(
        value: glTFRuntimeSkeletalAnimationCurveRemapperHook) -> None
```

<a id="unreal.glTFRuntimeSkeletalAnimationConfig.retarget_to"></a>

#### retarget\_to

```python
@property
def retarget_to() -> Skeleton
```

(Skeleton):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalAnimationConfig.retarget_to"></a>

#### retarget\_to

```python
@retarget_to.setter
def retarget_to(value: Skeleton) -> None
```

<a id="unreal.glTFRuntimeSkeletalAnimationConfig.retarget_to_skeletal_mesh"></a>

#### retarget\_to\_skeletal\_mesh

```python
@property
def retarget_to_skeletal_mesh() -> SkeletalMesh
```

(SkeletalMesh):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalAnimationConfig.retarget_to_skeletal_mesh"></a>

#### retarget\_to\_skeletal\_mesh

```python
@retarget_to_skeletal_mesh.setter
def retarget_to_skeletal_mesh(value: SkeletalMesh) -> None
```

<a id="unreal.glTFRuntimeSkeletalAnimationConfig.transform_pose"></a>

#### transform\_pose

```python
@property
def transform_pose() -> Map[str, Transform]
```

(Map[str, Transform]):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalAnimationConfig.transform_pose"></a>

#### transform\_pose

```python
@transform_pose.setter
def transform_pose(value: Map[str, Transform]) -> None
```

<a id="unreal.glTFRuntimeSkeletalAnimationConfig.frame_translation_remapper"></a>

#### frame\_translation\_remapper

```python
@property
def frame_translation_remapper(
) -> glTFRuntimeSkeletalAnimationFrameTranslationRemapperHook
```

(glTFRuntimeSkeletalAnimationFrameTranslationRemapperHook):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalAnimationConfig.frame_translation_remapper"></a>

#### frame\_translation\_remapper

```python
@frame_translation_remapper.setter
def frame_translation_remapper(
        value: glTFRuntimeSkeletalAnimationFrameTranslationRemapperHook
) -> None
```

<a id="unreal.glTFRuntimeSkeletalAnimationConfig.frame_rotation_remapper"></a>

#### frame\_rotation\_remapper

```python
@property
def frame_rotation_remapper(
) -> glTFRuntimeSkeletalAnimationFrameRotationRemapperHook
```

(glTFRuntimeSkeletalAnimationFrameRotationRemapperHook):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalAnimationConfig.frame_rotation_remapper"></a>

#### frame\_rotation\_remapper

```python
@frame_rotation_remapper.setter
def frame_rotation_remapper(
        value: glTFRuntimeSkeletalAnimationFrameRotationRemapperHook) -> None
```

<a id="unreal.glTFRuntimeSkeletalAnimationConfig.frames_per_second"></a>

#### frames\_per\_second

```python
@property
def frames_per_second() -> float
```

(float):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalAnimationConfig.frames_per_second"></a>

#### frames\_per\_second

```python
@frames_per_second.setter
def frames_per_second(value: float) -> None
```

<a id="unreal.glTFRuntimeSkeletalAnimationConfig.fill_all_curves"></a>

#### fill\_all\_curves

```python
@property
def fill_all_curves() -> bool
```

(bool):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalAnimationConfig.fill_all_curves"></a>

#### fill\_all\_curves

```python
@fill_all_curves.setter
def fill_all_curves(value: bool) -> None
```

<a id="unreal.glTFRuntimeSkeletalAnimationConfig.curves_name_map"></a>

#### curves\_name\_map

```python
@property
def curves_name_map() -> Map[str, str]
```

(Map[str, str]):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalAnimationConfig.curves_name_map"></a>

#### curves\_name\_map

```python
@curves_name_map.setter
def curves_name_map(value: Map[str, str]) -> None
```

<a id="unreal.glTFRuntimeSkeletalAnimationConfig.retarget_skin_index"></a>

#### retarget\_skin\_index

```python
@property
def retarget_skin_index() -> int
```

(int32):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalAnimationConfig.retarget_skin_index"></a>

#### retarget\_skin\_index

```python
@retarget_skin_index.setter
def retarget_skin_index(value: int) -> None
```

<a id="unreal.glTFRuntimeSkeletalAnimationConfig.pose_for_retargeting"></a>

#### pose\_for\_retargeting

```python
@property
def pose_for_retargeting() -> PoseAsset
```

(PoseAsset):  [Read-Write]

<a id="unreal.glTFRuntimeSkeletalAnimationConfig.pose_for_retargeting"></a>

#### pose\_for\_retargeting

```python
@pose_for_retargeting.setter
def pose_for_retargeting(value: PoseAsset) -> None
```

<a id="unreal.glTFRuntimeAudioEmitter"></a>