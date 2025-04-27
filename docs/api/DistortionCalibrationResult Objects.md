## DistortionCalibrationResult Objects

```python
class DistortionCalibrationResult(StructBase)
```

Results from a distortion calibration, including camera intrinsics and either the parameters to an analytical model or an ST Map

**C++ Source:**

- **Plugin**: CameraCalibrationCore
- **Module**: CameraCalibrationCore
- **File**: CameraCalibrationTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``camera_poses`` (Array[Transform]):  [Read-Write] Calibrated camera pose for each input image
- ``error_message`` (Text):  [Read-Write] Error text to be written by a solver to provide the reason why the solve may have failed. No error message implies that the solve was successful and the result is valid.
- ``evaluated_focus`` (float):  [Read-Write] Nominal focus distance of the lens associated with this result
- ``evaluated_zoom`` (float):  [Read-Write] Nominal focal length of the lens associated with this result
- ``focal_length`` (FocalLengthInfo):  [Read-Write] Calibrated focal length result
- ``image_center`` (ImageCenterInfo):  [Read-Write] Calibrated image center result
- ``nodal_offset`` (NodalPointOffset):  [Read-Write] Calibrated nodal offset result
- ``parameters`` (DistortionInfo):  [Read-Write] Distortion parameters for the model specified by the lens file. And empty parameter array implies that there is a valid ST Map instead.
- ``reprojection_error`` (double):  [Read-Write] Final reprojection error produced using this result
- ``st_map`` (STMapInfo):  [Read-Write] ST Map that represents the UV displacements for this result. If the ST Map UTexture is not imported by the solver, a path string should be provided so that the lens distortion tool can import it.
- ``st_map_full_path`` (str):  [Read-Write] Absolute path to an ST Map file on disk that should be imported when this result is processed.

<a id="unreal.DistortionCalibrationResult.__init__"></a>

#### __init__

```python
def __init__(evaluated_focus: float = 0.000000,
             evaluated_zoom: float = 0.000000,
             reprojection_error: float = 0.000000,
             focal_length: FocalLengthInfo = [[1.000000, 1.777778]],
             image_center: ImageCenterInfo = [[0.500000, 0.500000]],
             camera_poses: Array[Transform] = [],
             nodal_offset: NodalPointOffset = [[0.000000, 0.000000, 0.000000],
                                               [
                                                   0.000000, 0.000000,
                                                   0.000000, 1.000000
                                               ]],
             parameters: DistortionInfo = [[]],
             st_map: STMapInfo = [None],
             st_map_full_path: str = "",
             error_message: Text = "") -> None
```

<a id="unreal.DistortionCalibrationResult.evaluated_focus"></a>

#### evaluated_focus

```python
@property
def evaluated_focus() -> float
```

(float):  [Read-Write] Nominal focus distance of the lens associated with this result

<a id="unreal.DistortionCalibrationResult.evaluated_focus"></a>

#### evaluated_focus

```python
@evaluated_focus.setter
def evaluated_focus(value: float) -> None
```

<a id="unreal.DistortionCalibrationResult.evaluated_zoom"></a>

#### evaluated_zoom

```python
@property
def evaluated_zoom() -> float
```

(float):  [Read-Write] Nominal focal length of the lens associated with this result

<a id="unreal.DistortionCalibrationResult.evaluated_zoom"></a>

#### evaluated_zoom

```python
@evaluated_zoom.setter
def evaluated_zoom(value: float) -> None
```

<a id="unreal.DistortionCalibrationResult.reprojection_error"></a>

#### reprojection_error

```python
@property
def reprojection_error() -> float
```

(double):  [Read-Write] Final reprojection error produced using this result

<a id="unreal.DistortionCalibrationResult.reprojection_error"></a>

#### reprojection_error

```python
@reprojection_error.setter
def reprojection_error(value: float) -> None
```

<a id="unreal.DistortionCalibrationResult.focal_length"></a>

#### focal_length

```python
@property
def focal_length() -> FocalLengthInfo
```

(FocalLengthInfo):  [Read-Write] Calibrated focal length result

<a id="unreal.DistortionCalibrationResult.focal_length"></a>

#### focal_length

```python
@focal_length.setter
def focal_length(value: FocalLengthInfo) -> None
```

<a id="unreal.DistortionCalibrationResult.image_center"></a>

#### image_center

```python
@property
def image_center() -> ImageCenterInfo
```

(ImageCenterInfo):  [Read-Write] Calibrated image center result

<a id="unreal.DistortionCalibrationResult.image_center"></a>

#### image_center

```python
@image_center.setter
def image_center(value: ImageCenterInfo) -> None
```

<a id="unreal.DistortionCalibrationResult.camera_poses"></a>

#### camera_poses

```python
@property
def camera_poses() -> Array[Transform]
```

(Array[Transform]):  [Read-Write] Calibrated camera pose for each input image

<a id="unreal.DistortionCalibrationResult.camera_poses"></a>

#### camera_poses

```python
@camera_poses.setter
def camera_poses(value: Array[Transform]) -> None
```

<a id="unreal.DistortionCalibrationResult.nodal_offset"></a>

#### nodal_offset

```python
@property
def nodal_offset() -> NodalPointOffset
```

(NodalPointOffset):  [Read-Write] Calibrated nodal offset result

<a id="unreal.DistortionCalibrationResult.nodal_offset"></a>

#### nodal_offset

```python
@nodal_offset.setter
def nodal_offset(value: NodalPointOffset) -> None
```

<a id="unreal.DistortionCalibrationResult.parameters"></a>

#### parameters

```python
@property
def parameters() -> DistortionInfo
```

(DistortionInfo):  [Read-Write] Distortion parameters for the model specified by the lens file. And empty parameter array implies that there is a valid ST Map instead.

<a id="unreal.DistortionCalibrationResult.parameters"></a>

#### parameters

```python
@parameters.setter
def parameters(value: DistortionInfo) -> None
```

<a id="unreal.DistortionCalibrationResult.st_map"></a>

#### st_map

```python
@property
def st_map() -> STMapInfo
```

(STMapInfo):  [Read-Write] ST Map that represents the UV displacements for this result. If the ST Map UTexture is not imported by the solver, a path string should be provided so that the lens distortion tool can import it.

<a id="unreal.DistortionCalibrationResult.st_map"></a>

#### st_map

```python
@st_map.setter
def st_map(value: STMapInfo) -> None
```

<a id="unreal.DistortionCalibrationResult.st_map_full_path"></a>

#### st_map_full_path

```python
@property
def st_map_full_path() -> str
```

(str):  [Read-Write] Absolute path to an ST Map file on disk that should be imported when this result is processed.

<a id="unreal.DistortionCalibrationResult.st_map_full_path"></a>

#### st_map_full_path

```python
@st_map_full_path.setter
def st_map_full_path(value: str) -> None
```

<a id="unreal.DistortionCalibrationResult.error_message"></a>

#### error_message

```python
@property
def error_message() -> Text
```

(Text):  [Read-Write] Error text to be written by a solver to provide the reason why the solve may have failed. No error message implies that the solve was successful and the result is valid.

<a id="unreal.DistortionCalibrationResult.error_message"></a>

#### error_message

```python
@error_message.setter
def error_message(value: Text) -> None
```

<a id="unreal.STMapInfo"></a>