## CesiumRasterOverlayLoadFailureDetails Objects

```python
class CesiumRasterOverlayLoadFailureDetails(StructBase)
```

Cesium Raster Overlay Load Failure Details

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: CesiumRasterOverlayLoadFailureDetails.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``http_status_code`` (int32):  [Read-Only] The HTTP status code of the response that led to the failure.

  If there was no response or the failure did not follow from a request, then
  the value of this property will be 0.
- ``message`` (str):  [Read-Only] A human-readable explanation of what failed.
- ``overlay`` (CesiumRasterOverlay):  [Read-Only] The overlay that encountered the load failure.
- ``type`` (CesiumRasterOverlayLoadType):  [Read-Only] The type of request that failed to load.

<a id="unreal.CesiumRasterOverlayLoadFailureDetails.__init__"></a>

#### \_\_init\_\_

```python
def __init__(overlay: CesiumRasterOverlay = None,
             type: CesiumRasterOverlayLoadType = CesiumRasterOverlayLoadType.
             UNKNOWN,
             http_status_code: int = 0,
             message: str = "") -> None
```

<a id="unreal.CesiumRasterOverlayLoadFailureDetails.overlay"></a>

#### overlay

```python
@property
def overlay() -> CesiumRasterOverlay
```

(CesiumRasterOverlay):  [Read-Only] The overlay that encountered the load failure.

<a id="unreal.CesiumRasterOverlayLoadFailureDetails.type"></a>

#### type

```python
@property
def type() -> CesiumRasterOverlayLoadType
```

(CesiumRasterOverlayLoadType):  [Read-Only] The type of request that failed to load.

<a id="unreal.CesiumRasterOverlayLoadFailureDetails.http_status_code"></a>

#### http\_status\_code

```python
@property
def http_status_code() -> int
```

(int32):  [Read-Only] The HTTP status code of the response that led to the failure.

If there was no response or the failure did not follow from a request, then
the value of this property will be 0.

<a id="unreal.CesiumRasterOverlayLoadFailureDetails.message"></a>

#### message

```python
@property
def message() -> str
```

(str):  [Read-Only] A human-readable explanation of what failed.

<a id="unreal.CustomDepthParameters"></a>