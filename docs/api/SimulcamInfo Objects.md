## SimulcamInfo Objects

```python
class SimulcamInfo(StructBase)
```

Information about the simulcam composition

**C++ Source:**

- **Plugin**: CameraCalibrationCore
- **Module**: CameraCalibrationCore
- **File**: LensData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``cg_layer_aspect_ratio`` (float):  [Read-Write] Aspect ratio of the CG layer in the simulcam composition, which was set to match the aspect ratio of the selected Camera Actor
- ``media_plate_aspect_ratio`` (float):  [Read-Write] Aspect ratio of the media plate in the simulcam composition, which was set to match the aspect ratio of the selected Media Source
- ``media_resolution`` (IntPoint):  [Read-Write] Resolution of the selected Media Source

<a id="unreal.SimulcamInfo.__init__"></a>

#### __init__

```python
def __init__(media_resolution: IntPoint = [0, 0],
             media_plate_aspect_ratio: float = 0.000000,
             cg_layer_aspect_ratio: float = 0.000000) -> None
```

<a id="unreal.SimulcamInfo.media_resolution"></a>

#### media_resolution

```python
@property
def media_resolution() -> IntPoint
```

(IntPoint):  [Read-Write] Resolution of the selected Media Source

<a id="unreal.SimulcamInfo.media_resolution"></a>

#### media_resolution

```python
@media_resolution.setter
def media_resolution(value: IntPoint) -> None
```

<a id="unreal.SimulcamInfo.media_plate_aspect_ratio"></a>

#### media_plate_aspect_ratio

```python
@property
def media_plate_aspect_ratio() -> float
```

(float):  [Read-Write] Aspect ratio of the media plate in the simulcam composition, which was set to match the aspect ratio of the selected Media Source

<a id="unreal.SimulcamInfo.media_plate_aspect_ratio"></a>

#### media_plate_aspect_ratio

```python
@media_plate_aspect_ratio.setter
def media_plate_aspect_ratio(value: float) -> None
```

<a id="unreal.SimulcamInfo.cg_layer_aspect_ratio"></a>

#### cg_layer_aspect_ratio

```python
@property
def cg_layer_aspect_ratio() -> float
```

(float):  [Read-Write] Aspect ratio of the CG layer in the simulcam composition, which was set to match the aspect ratio of the selected Camera Actor

<a id="unreal.SimulcamInfo.cg_layer_aspect_ratio"></a>

#### cg_layer_aspect_ratio

```python
@cg_layer_aspect_ratio.setter
def cg_layer_aspect_ratio(value: float) -> None
```

<a id="unreal.DistortionData"></a>