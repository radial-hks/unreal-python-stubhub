## LensDistortionState Objects

```python
class LensDistortionState(StructBase)
```

Lens Distortion State

**C++ Source:**

- **Plugin**: CameraCalibrationCore
- **Module**: CameraCalibrationCore
- **File**: LensDistortionModelHandlerBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``distortion_info`` (DistortionInfo):  [Read-Write] Generic array of distortion parameters
- ``focal_length_info`` (FocalLengthInfo):  [Read-Write] Normalized focal fength in both dimensions
- ``image_center`` (ImageCenterInfo):  [Read-Write] Normalized center of the image, in the range [0.0f, 1.0f]

<a id="unreal.LensDistortionState.__init__"></a>

#### __init__

```python
def __init__(distortion_info: DistortionInfo = [[]],
             focal_length_info: FocalLengthInfo = [[1.000000, 1.777778]],
             image_center: ImageCenterInfo = [[0.500000, 0.500000]]) -> None
```

<a id="unreal.LensDistortionState.distortion_info"></a>

#### distortion_info

```python
@property
def distortion_info() -> DistortionInfo
```

(DistortionInfo):  [Read-Write] Generic array of distortion parameters

<a id="unreal.LensDistortionState.distortion_info"></a>

#### distortion_info

```python
@distortion_info.setter
def distortion_info(value: DistortionInfo) -> None
```

<a id="unreal.LensDistortionState.focal_length_info"></a>

#### focal_length_info

```python
@property
def focal_length_info() -> FocalLengthInfo
```

(FocalLengthInfo):  [Read-Write] Normalized focal fength in both dimensions

<a id="unreal.LensDistortionState.focal_length_info"></a>

#### focal_length_info

```python
@focal_length_info.setter
def focal_length_info(value: FocalLengthInfo) -> None
```

<a id="unreal.LensDistortionState.image_center"></a>

#### image_center

```python
@property
def image_center() -> ImageCenterInfo
```

(ImageCenterInfo):  [Read-Write] Normalized center of the image, in the range [0.0f, 1.0f]

<a id="unreal.LensDistortionState.image_center"></a>

#### image_center

```python
@image_center.setter
def image_center(value: ImageCenterInfo) -> None
```

<a id="unreal.LensFilePicker"></a>