## OpenCVBlueprintFunctionLibrary Objects

```python
class OpenCVBlueprintFunctionLibrary(BlueprintFunctionLibrary)
```

Open CVBlueprint Function Library

**C++ Source:**

- **Plugin**: OpenCV
- **Module**: OpenCVHelper
- **File**: OpenCVBlueprintFunctionLibrary.h

<a id="unreal.OpenCVBlueprintFunctionLibrary.open_cv_chessboard_detect_corners"></a>

#### open_cv_chessboard_detect_corners

```python
@classmethod
def open_cv_chessboard_detect_corners(
        cls, render_target: TextureRenderTarget2D, pattern_size: IntPoint,
        debug_draw_corners: bool) -> Tuple[int, Texture2D, Array[Vector2D]]
```

X.open_cv_chessboard_detect_corners(render_target, pattern_size, debug_draw_corners) -> (int32, out_debug_texture=Texture2D, out_detected_corners=Array[Vector2D])
Detects a camera calibration chessboard in the supplied image

Args:
    render_target (TextureRenderTarget2D): Input image in which to search for a chessboard
    pattern_size (IntPoint): Number of interior corners on the physical chessboard (rows, columns)
    debug_draw_corners (bool): If true, output a Texture2D showing the detected corner debug info overlaid on the input image

Returns:
    tuple: Total number of corners detected in the input image

    out_debug_texture (Texture2D): Output debug image (required if bDebugDrawCorners is True)

    out_detected_corners (Array[Vector2D]): Output array of corners detected in the input image

<a id="unreal.OpenCVBlueprintFunctionLibrary.open_cv_aruco_detect_markers"></a>

#### open_cv_aruco_detect_markers

```python
@classmethod
def open_cv_aruco_detect_markers(
    cls, render_target: TextureRenderTarget2D,
    dictionary: OpenCVArucoDictionary,
    dictionary_size: OpenCVArucoDictionarySize, debug_draw_markers: bool,
    estimate_pose: bool, marker_length_in_meters: float,
    lens_distortion_parameters: OpenCVLensDistortionParametersBase
) -> Tuple[int, Texture2D, Array[OpenCVArucoDetectedMarker]]
```

X.open_cv_aruco_detect_markers(render_target, dictionary, dictionary_size, debug_draw_markers, estimate_pose, marker_length_in_meters, lens_distortion_parameters) -> (int32, out_debug_texture=Texture2D, out_detected_markers=Array[OpenCVArucoDetectedMarker])
Detects all ArUco markers in the supplied image

Args:
    render_target (TextureRenderTarget2D): Input image in which to search for markers
    dictionary (OpenCVArucoDictionary): Which ArUco marker dictionary to use for detection
    dictionary_size (OpenCVArucoDictionarySize): The size of the ArUco marker dictionary
    debug_draw_markers (bool): If true, output a Texture2D showing the detected marker debug info overlaid on the input image
    estimate_pose (bool): If true, return the 3D pose for each marker relative to the camera position
    marker_length_in_meters (float): Length in meters of one side of the physical marker (required if bEstimatePose is True)
    lens_distortion_parameters (OpenCVLensDistortionParametersBase): 

Returns:
    tuple: Total number of markers detected in the input image

    out_debug_texture (Texture2D): Output debug image (required if bDebugDrawMarkers is True)

    out_detected_markers (Array[OpenCVArucoDetectedMarker]): Output array of markers detected in the input image

<a id="unreal.ProceduralMeshLibrary"></a>