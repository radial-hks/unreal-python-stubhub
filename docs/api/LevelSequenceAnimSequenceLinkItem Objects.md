## LevelSequenceAnimSequenceLinkItem Objects

```python
class LevelSequenceAnimSequenceLinkItem(StructBase)
```

Link To Anim Sequence that we are linked too.

**C++ Source:**

- **Module**: LevelSequence
- **File**: LevelSequenceAnimSequenceLink.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``curve_interpolation`` (RichCurveInterpMode):  [Read-Write]
- ``custom_display_rate`` (FrameRate):  [Read-Write] Custom display rate, should be set from the movie scene/sequencer display rate
- ``custom_end_frame`` (FrameNumber):  [Read-Write] Custom end frame in display rate
- ``custom_start_frame`` (FrameNumber):  [Read-Write] Custom start frame in display rate
- ``delay_before_start`` (FrameNumber):  [Read-Write] Number of Display Rate frames to delay at the same frame before doing the export. It will evalaute first, then any warm up, then the export. Use it if there is some post anim BP effects you want to ran repeatedly at the start.
- ``evaluate_all_skeletal_mesh_components`` (bool):  [Read-Write]
- ``exclude_animation_names`` (Array[str]):  [Read-Write] Exclude all animation bones/curves that match this list
- ``export_attribute_curves`` (bool):  [Read-Write]
- ``export_material_curves`` (bool):  [Read-Write]
- ``export_morph_targets`` (bool):  [Read-Write]
- ``export_transforms`` (bool):  [Read-Write] From Editor Only UAnimSeqExportOption we cache this since we can re-import dynamically
- ``include_animation_names`` (Array[str]):  [Read-Write] Include only the animation bones/curves that match this list
- ``interpolation`` (AnimInterpolationType):  [Read-Write]
- ``path_to_anim_sequence`` (SoftObjectPath):  [Read-Write]
- ``record_in_world_space`` (bool):  [Read-Write]
- ``skel_track_guid`` (Guid):  [Read-Write]
- ``use_custom_time_range`` (bool):  [Read-Write] Whether or not to use custom time range
- ``warm_up_frames`` (FrameNumber):  [Read-Write] Number of Display Rate frames to evaluate before doing the export. It will evaluate after any Delay. This will use frames before the start frame. Use it if there is some post anim BP effects you want to run before export start time.

<a id="unreal.LevelSequenceAnimSequenceLinkItem.__init__"></a>

#### \_\_init\_\_

```python
def __init__(
        skel_track_guid: Guid = [],
        path_to_anim_sequence: SoftObjectPath = [""],
        export_transforms: bool = False,
        export_morph_targets: bool = False,
        export_attribute_curves: bool = False,
        export_material_curves: bool = False,
        interpolation: AnimInterpolationType = AnimInterpolationType.LINEAR,
        curve_interpolation: RichCurveInterpMode = RichCurveInterpMode.
    RCIM_LINEAR,
        record_in_world_space: bool = False,
        evaluate_all_skeletal_mesh_components: bool = False,
        include_animation_names: Array[str] = [],
        exclude_animation_names: Array[str] = [],
        warm_up_frames: FrameNumber = [0],
        delay_before_start: FrameNumber = [0],
        use_custom_time_range: bool = False,
        custom_start_frame: FrameNumber = [0],
        custom_end_frame: FrameNumber = [0],
        custom_display_rate: FrameRate = [60000, 1]) -> None
```

<a id="unreal.LevelSequenceAnimSequenceLinkItem.skel_track_guid"></a>

#### skel\_track\_guid

```python
@property
def skel_track_guid() -> Guid
```

(Guid):  [Read-Write]

<a id="unreal.LevelSequenceAnimSequenceLinkItem.skel_track_guid"></a>

#### skel\_track\_guid

```python
@skel_track_guid.setter
def skel_track_guid(value: Guid) -> None
```

<a id="unreal.LevelSequenceAnimSequenceLinkItem.path_to_anim_sequence"></a>

#### path\_to\_anim\_sequence

```python
@property
def path_to_anim_sequence() -> SoftObjectPath
```

(SoftObjectPath):  [Read-Write]

<a id="unreal.LevelSequenceAnimSequenceLinkItem.path_to_anim_sequence"></a>

#### path\_to\_anim\_sequence

```python
@path_to_anim_sequence.setter
def path_to_anim_sequence(value: SoftObjectPath) -> None
```

<a id="unreal.LevelSequenceAnimSequenceLinkItem.export_transforms"></a>

#### export\_transforms

```python
@property
def export_transforms() -> bool
```

(bool):  [Read-Write] From Editor Only UAnimSeqExportOption we cache this since we can re-import dynamically

<a id="unreal.LevelSequenceAnimSequenceLinkItem.export_transforms"></a>

#### export\_transforms

```python
@export_transforms.setter
def export_transforms(value: bool) -> None
```

<a id="unreal.LevelSequenceAnimSequenceLinkItem.export_morph_targets"></a>

#### export\_morph\_targets

```python
@property
def export_morph_targets() -> bool
```

(bool):  [Read-Write]

<a id="unreal.LevelSequenceAnimSequenceLinkItem.export_morph_targets"></a>

#### export\_morph\_targets

```python
@export_morph_targets.setter
def export_morph_targets(value: bool) -> None
```

<a id="unreal.LevelSequenceAnimSequenceLinkItem.export_attribute_curves"></a>

#### export\_attribute\_curves

```python
@property
def export_attribute_curves() -> bool
```

(bool):  [Read-Write]

<a id="unreal.LevelSequenceAnimSequenceLinkItem.export_attribute_curves"></a>

#### export\_attribute\_curves

```python
@export_attribute_curves.setter
def export_attribute_curves(value: bool) -> None
```

<a id="unreal.LevelSequenceAnimSequenceLinkItem.export_material_curves"></a>

#### export\_material\_curves

```python
@property
def export_material_curves() -> bool
```

(bool):  [Read-Write]

<a id="unreal.LevelSequenceAnimSequenceLinkItem.export_material_curves"></a>

#### export\_material\_curves

```python
@export_material_curves.setter
def export_material_curves(value: bool) -> None
```

<a id="unreal.LevelSequenceAnimSequenceLinkItem.interpolation"></a>

#### interpolation

```python
@property
def interpolation() -> AnimInterpolationType
```

(AnimInterpolationType):  [Read-Write]

<a id="unreal.LevelSequenceAnimSequenceLinkItem.interpolation"></a>

#### interpolation

```python
@interpolation.setter
def interpolation(value: AnimInterpolationType) -> None
```

<a id="unreal.LevelSequenceAnimSequenceLinkItem.curve_interpolation"></a>

#### curve\_interpolation

```python
@property
def curve_interpolation() -> RichCurveInterpMode
```

(RichCurveInterpMode):  [Read-Write]

<a id="unreal.LevelSequenceAnimSequenceLinkItem.curve_interpolation"></a>

#### curve\_interpolation

```python
@curve_interpolation.setter
def curve_interpolation(value: RichCurveInterpMode) -> None
```

<a id="unreal.LevelSequenceAnimSequenceLinkItem.record_in_world_space"></a>

#### record\_in\_world\_space

```python
@property
def record_in_world_space() -> bool
```

(bool):  [Read-Write]

<a id="unreal.LevelSequenceAnimSequenceLinkItem.record_in_world_space"></a>

#### record\_in\_world\_space

```python
@record_in_world_space.setter
def record_in_world_space(value: bool) -> None
```

<a id="unreal.LevelSequenceAnimSequenceLinkItem.evaluate_all_skeletal_mesh_components"></a>

#### evaluate\_all\_skeletal\_mesh\_components

```python
@property
def evaluate_all_skeletal_mesh_components() -> bool
```

(bool):  [Read-Write]

<a id="unreal.LevelSequenceAnimSequenceLinkItem.evaluate_all_skeletal_mesh_components"></a>

#### evaluate\_all\_skeletal\_mesh\_components

```python
@evaluate_all_skeletal_mesh_components.setter
def evaluate_all_skeletal_mesh_components(value: bool) -> None
```

<a id="unreal.LevelSequenceAnimSequenceLinkItem.include_animation_names"></a>

#### include\_animation\_names

```python
@property
def include_animation_names() -> Array[str]
```

(Array[str]):  [Read-Write] Include only the animation bones/curves that match this list

<a id="unreal.LevelSequenceAnimSequenceLinkItem.include_animation_names"></a>

#### include\_animation\_names

```python
@include_animation_names.setter
def include_animation_names(value: Array[str]) -> None
```

<a id="unreal.LevelSequenceAnimSequenceLinkItem.exclude_animation_names"></a>

#### exclude\_animation\_names

```python
@property
def exclude_animation_names() -> Array[str]
```

(Array[str]):  [Read-Write] Exclude all animation bones/curves that match this list

<a id="unreal.LevelSequenceAnimSequenceLinkItem.exclude_animation_names"></a>

#### exclude\_animation\_names

```python
@exclude_animation_names.setter
def exclude_animation_names(value: Array[str]) -> None
```

<a id="unreal.LevelSequenceAnimSequenceLinkItem.warm_up_frames"></a>

#### warm\_up\_frames

```python
@property
def warm_up_frames() -> FrameNumber
```

(FrameNumber):  [Read-Write] Number of Display Rate frames to evaluate before doing the export. It will evaluate after any Delay. This will use frames before the start frame. Use it if there is some post anim BP effects you want to run before export start time.

<a id="unreal.LevelSequenceAnimSequenceLinkItem.warm_up_frames"></a>

#### warm\_up\_frames

```python
@warm_up_frames.setter
def warm_up_frames(value: FrameNumber) -> None
```

<a id="unreal.LevelSequenceAnimSequenceLinkItem.delay_before_start"></a>

#### delay\_before\_start

```python
@property
def delay_before_start() -> FrameNumber
```

(FrameNumber):  [Read-Write] Number of Display Rate frames to delay at the same frame before doing the export. It will evalaute first, then any warm up, then the export. Use it if there is some post anim BP effects you want to ran repeatedly at the start.

<a id="unreal.LevelSequenceAnimSequenceLinkItem.delay_before_start"></a>

#### delay\_before\_start

```python
@delay_before_start.setter
def delay_before_start(value: FrameNumber) -> None
```

<a id="unreal.LevelSequenceAnimSequenceLinkItem.use_custom_time_range"></a>

#### use\_custom\_time\_range

```python
@property
def use_custom_time_range() -> bool
```

(bool):  [Read-Write] Whether or not to use custom time range

<a id="unreal.LevelSequenceAnimSequenceLinkItem.use_custom_time_range"></a>

#### use\_custom\_time\_range

```python
@use_custom_time_range.setter
def use_custom_time_range(value: bool) -> None
```

<a id="unreal.LevelSequenceAnimSequenceLinkItem.custom_start_frame"></a>

#### custom\_start\_frame

```python
@property
def custom_start_frame() -> FrameNumber
```

(FrameNumber):  [Read-Write] Custom start frame in display rate

<a id="unreal.LevelSequenceAnimSequenceLinkItem.custom_start_frame"></a>

#### custom\_start\_frame

```python
@custom_start_frame.setter
def custom_start_frame(value: FrameNumber) -> None
```

<a id="unreal.LevelSequenceAnimSequenceLinkItem.custom_end_frame"></a>

#### custom\_end\_frame

```python
@property
def custom_end_frame() -> FrameNumber
```

(FrameNumber):  [Read-Write] Custom end frame in display rate

<a id="unreal.LevelSequenceAnimSequenceLinkItem.custom_end_frame"></a>

#### custom\_end\_frame

```python
@custom_end_frame.setter
def custom_end_frame(value: FrameNumber) -> None
```

<a id="unreal.LevelSequenceAnimSequenceLinkItem.custom_display_rate"></a>

#### custom\_display\_rate

```python
@property
def custom_display_rate() -> FrameRate
```

(FrameRate):  [Read-Write] Custom display rate, should be set from the movie scene/sequencer display rate

<a id="unreal.LevelSequenceAnimSequenceLinkItem.custom_display_rate"></a>

#### custom\_display\_rate

```python
@custom_display_rate.setter
def custom_display_rate(value: FrameRate) -> None
```

<a id="unreal.LevelSequencePlayerSnapshot"></a>