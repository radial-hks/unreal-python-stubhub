## Cesium3DTilesetLoadFailureDetails Objects

```python
class Cesium3DTilesetLoadFailureDetails(StructBase)
```

Cesium 3DTileset Load Failure Details

**C++ Source:**

- **Plugin**: CesiumForUnreal
- **Module**: CesiumRuntime
- **File**: Cesium3DTilesetLoadFailureDetails.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``http_status_code`` (int32):  [Read-Only] The HTTP status code of the response that led to the failure.

  If there was no response or the failure did not follow from a request, then
  the value of this property will be 0.
- ``message`` (str):  [Read-Only] A human-readable explanation of what failed.
- ``tileset`` (Cesium3DTileset):  [Read-Only] The tileset that encountered the load failure.
- ``type`` (Cesium3DTilesetLoadType):  [Read-Only] The type of request that failed to load.

<a id="unreal.Cesium3DTilesetLoadFailureDetails.__init__"></a>

#### \_\_init\_\_

```python
def __init__(tileset: Cesium3DTileset = None,
             type: Cesium3DTilesetLoadType = Cesium3DTilesetLoadType.UNKNOWN,
             http_status_code: int = 0,
             message: str = "") -> None
```

<a id="unreal.Cesium3DTilesetLoadFailureDetails.tileset"></a>

#### tileset

```python
@property
def tileset() -> Cesium3DTileset
```

(Cesium3DTileset):  [Read-Only] The tileset that encountered the load failure.

<a id="unreal.Cesium3DTilesetLoadFailureDetails.type"></a>

#### type

```python
@property
def type() -> Cesium3DTilesetLoadType
```

(Cesium3DTilesetLoadType):  [Read-Only] The type of request that failed to load.

<a id="unreal.Cesium3DTilesetLoadFailureDetails.http_status_code"></a>

#### http\_status\_code

```python
@property
def http_status_code() -> int
```

(int32):  [Read-Only] The HTTP status code of the response that led to the failure.

If there was no response or the failure did not follow from a request, then
the value of this property will be 0.

<a id="unreal.Cesium3DTilesetLoadFailureDetails.message"></a>

#### message

```python
@property
def message() -> str
```

(str):  [Read-Only] A human-readable explanation of what failed.

<a id="unreal.CesiumCamera"></a>