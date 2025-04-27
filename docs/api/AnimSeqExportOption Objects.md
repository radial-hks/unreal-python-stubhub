## AnimSeqExportOption Objects

```python
class AnimSeqExportOption(Object)
```

Anim Seq Export Option

**C++ Source:**

- **Module**: UnrealEd
- **File**: AnimSeqExportOption.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``curve_interpolation`` (RichCurveInterpMode):  [Read-Write] This defines how values between keys are calculated for curves
- ``custom_display_rate`` (FrameRate):  [Read-Write] Custom display rate, should be set from the movie scene/sequencer display rate
- ``custom_end_frame`` (FrameNumber):  [Read-Write] Custom end frame in custom display rate
- ``custom_start_frame`` (FrameNumber):  [Read-Write] Custom start frame in custom display rate
- ``delay_before_start`` (FrameNumber):  [Read-Write] Number of Display Rate frames to delay at the same frame before doing the export. It will evalaute first, then any warm up, then the export. Use it if there is some post anim BP effects you want to ran repeatedly at the start.
- ``evaluate_all_skeletal_mesh_components`` (bool):  [Read-Write] If true we evaluate all other skeletal mesh components under the same actor, this may be needed for example, to get physics to get baked
- ``exclude_animation_names`` (Array[str]):  [Read-Write] Exclude all animation bones/curves that match this list
- ``export_attribute_curves`` (bool):  [Read-Write] If enabled, export the attribute curves from the animation
- ``export_material_curves`` (bool):  [Read-Write] If enabled, export the material curves from the animation
- ``export_morph_targets`` (bool):  [Read-Write] If enabled, export the morph targets from the animation
- ``export_transforms`` (bool):  [Read-Write] If enabled, export the transforms from the animation
- ``include_animation_names`` (Array[str]):  [Read-Write] Include only the animation bones/curves that match this list
- ``interpolation`` (AnimInterpolationType):  [Read-Write] This defines how values between keys are calculated for transforms
- ``record_in_world_space`` (bool):  [Read-Write] If enabled we record in World Space otherwise we record from 0,0,0
- ``transact_recording`` (bool):  [Read-Write] Whether or not to transact the animation sequence data recording
- ``use_custom_time_range`` (bool):  [Read-Write] Whether or not to use custom time range
- ``warm_up_frames`` (FrameNumber):  [Read-Write] Number of Display Rate frames to evaluate before doing the export. It will evaluate after any Delay. This will use frames before the start frame. Use it if there is some post anim BP effects you want to run before export start time.

<a id="unreal.AnimSeqExportOption.export_transforms"></a>

#### export_transforms

```python
@property
def export_transforms() -> bool
```

(bool):  [Read-Write] If enabled, export the transforms from the animation

<a id="unreal.AnimSeqExportOption.export_transforms"></a>

#### export_transforms

```python
@export_transforms.setter
def export_transforms(value: bool) -> None
```

<a id="unreal.AnimSeqExportOption.export_morph_targets"></a>

#### export_morph_targets

```python
@property
def export_morph_targets() -> bool
```

(bool):  [Read-Write] If enabled, export the morph targets from the animation

<a id="unreal.AnimSeqExportOption.export_morph_targets"></a>

#### export_morph_targets

```python
@export_morph_targets.setter
def export_morph_targets(value: bool) -> None
```

<a id="unreal.AnimSeqExportOption.export_attribute_curves"></a>

#### export_attribute_curves

```python
@property
def export_attribute_curves() -> bool
```

(bool):  [Read-Write] If enabled, export the attribute curves from the animation

<a id="unreal.AnimSeqExportOption.export_attribute_curves"></a>

#### export_attribute_curves

```python
@export_attribute_curves.setter
def export_attribute_curves(value: bool) -> None
```

<a id="unreal.AnimSeqExportOption.export_material_curves"></a>

#### export_material_curves

```python
@property
def export_material_curves() -> bool
```

(bool):  [Read-Write] If enabled, export the material curves from the animation

<a id="unreal.AnimSeqExportOption.export_material_curves"></a>

#### export_material_curves

```python
@export_material_curves.setter
def export_material_curves(value: bool) -> None
```

<a id="unreal.AnimSeqExportOption.record_in_world_space"></a>

#### record_in_world_space

```python
@property
def record_in_world_space() -> bool
```

(bool):  [Read-Write] If enabled we record in World Space otherwise we record from 0,0,0

<a id="unreal.AnimSeqExportOption.record_in_world_space"></a>

#### record_in_world_space

```python
@record_in_world_space.setter
def record_in_world_space(value: bool) -> None
```

<a id="unreal.AnimSeqExportOption.evaluate_all_skeletal_mesh_components"></a>

#### evaluate_all_skeletal_mesh_components

```python
@property
def evaluate_all_skeletal_mesh_components() -> bool
```

(bool):  [Read-Write] If true we evaluate all other skeletal mesh components under the same actor, this may be needed for example, to get physics to get baked

<a id="unreal.AnimSeqExportOption.evaluate_all_skeletal_mesh_components"></a>

#### evaluate_all_skeletal_mesh_components

```python
@evaluate_all_skeletal_mesh_components.setter
def evaluate_all_skeletal_mesh_components(value: bool) -> None
```

<a id="unreal.AnimSeqExportOption.interpolation"></a>

#### interpolation

```python
@property
def interpolation() -> AnimInterpolationType
```

(AnimInterpolationType):  [Read-Write] This defines how values between keys are calculated for transforms

<a id="unreal.AnimSeqExportOption.interpolation"></a>

#### interpolation

```python
@interpolation.setter
def interpolation(value: AnimInterpolationType) -> None
```

<a id="unreal.AnimSeqExportOption.curve_interpolation"></a>

#### curve_interpolation

```python
@property
def curve_interpolation() -> RichCurveInterpMode
```

(RichCurveInterpMode):  [Read-Write] This defines how values between keys are calculated for curves

<a id="unreal.AnimSeqExportOption.curve_interpolation"></a>

#### curve_interpolation

```python
@curve_interpolation.setter
def curve_interpolation(value: RichCurveInterpMode) -> None
```

<a id="unreal.AnimSeqExportOption.include_animation_names"></a>

#### include_animation_names

```python
@property
def include_animation_names() -> Array[str]
```

(Array[str]):  [Read-Write] Include only the animation bones/curves that match this list

<a id="unreal.AnimSeqExportOption.include_animation_names"></a>

#### include_animation_names

```python
@include_animation_names.setter
def include_animation_names(value: Array[str]) -> None
```

<a id="unreal.AnimSeqExportOption.exclude_animation_names"></a>

#### exclude_animation_names

```python
@property
def exclude_animation_names() -> Array[str]
```

(Array[str]):  [Read-Write] Exclude all animation bones/curves that match this list

<a id="unreal.AnimSeqExportOption.exclude_animation_names"></a>

#### exclude_animation_names

```python
@exclude_animation_names.setter
def exclude_animation_names(value: Array[str]) -> None
```

<a id="unreal.AnimSeqExportOption.warm_up_frames"></a>

#### warm_up_frames

```python
@property
def warm_up_frames() -> FrameNumber
```

(FrameNumber):  [Read-Write] Number of Display Rate frames to evaluate before doing the export. It will evaluate after any Delay. This will use frames before the start frame. Use it if there is some post anim BP effects you want to run before export start time.

<a id="unreal.AnimSeqExportOption.warm_up_frames"></a>

#### warm_up_frames

```python
@warm_up_frames.setter
def warm_up_frames(value: FrameNumber) -> None
```

<a id="unreal.AnimSeqExportOption.delay_before_start"></a>

#### delay_before_start

```python
@property
def delay_before_start() -> FrameNumber
```

(FrameNumber):  [Read-Write] Number of Display Rate frames to delay at the same frame before doing the export. It will evalaute first, then any warm up, then the export. Use it if there is some post anim BP effects you want to ran repeatedly at the start.

<a id="unreal.AnimSeqExportOption.delay_before_start"></a>

#### delay_before_start

```python
@delay_before_start.setter
def delay_before_start(value: FrameNumber) -> None
```

<a id="unreal.AnimSeqExportOption.transact_recording"></a>

#### transact_recording

```python
@property
def transact_recording() -> bool
```

(bool):  [Read-Write] Whether or not to transact the animation sequence data recording

<a id="unreal.AnimSeqExportOption.transact_recording"></a>

#### transact_recording

```python
@transact_recording.setter
def transact_recording(value: bool) -> None
```

<a id="unreal.AnimSeqExportOption.use_custom_time_range"></a>

#### use_custom_time_range

```python
@property
def use_custom_time_range() -> bool
```

(bool):  [Read-Write] Whether or not to use custom time range

<a id="unreal.AnimSeqExportOption.use_custom_time_range"></a>

#### use_custom_time_range

```python
@use_custom_time_range.setter
def use_custom_time_range(value: bool) -> None
```

<a id="unreal.AnimSeqExportOption.custom_start_frame"></a>

#### custom_start_frame

```python
@property
def custom_start_frame() -> FrameNumber
```

(FrameNumber):  [Read-Write] Custom start frame in custom display rate

<a id="unreal.AnimSeqExportOption.custom_start_frame"></a>

#### custom_start_frame

```python
@custom_start_frame.setter
def custom_start_frame(value: FrameNumber) -> None
```

<a id="unreal.AnimSeqExportOption.custom_end_frame"></a>

#### custom_end_frame

```python
@property
def custom_end_frame() -> FrameNumber
```

(FrameNumber):  [Read-Write] Custom end frame in custom display rate

<a id="unreal.AnimSeqExportOption.custom_end_frame"></a>

#### custom_end_frame

```python
@custom_end_frame.setter
def custom_end_frame(value: FrameNumber) -> None
```

<a id="unreal.AnimSeqExportOption.custom_display_rate"></a>

#### custom_display_rate

```python
@property
def custom_display_rate() -> FrameRate
```

(FrameRate):  [Read-Write] Custom display rate, should be set from the movie scene/sequencer display rate

<a id="unreal.AnimSeqExportOption.custom_display_rate"></a>

#### custom_display_rate

```python
@custom_display_rate.setter
def custom_display_rate(value: FrameRate) -> None
```

<a id="unreal.ExporterFBX"></a>