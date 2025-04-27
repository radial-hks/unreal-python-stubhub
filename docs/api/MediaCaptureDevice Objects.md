## MediaCaptureDevice Objects

```python
class MediaCaptureDevice(StructBase)
```

Information about a capture device.

**C++ Source:**

- **Module**: MediaAssets
- **File**: MediaBlueprintFunctionLibrary.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``display_name`` (Text):  [Read-Write] Human readable display name.
- ``url`` (str):  [Read-Write] Media URL string for use with media players.

<a id="unreal.MediaCaptureDevice.__init__"></a>

#### __init__

```python
def __init__(display_name: Text = "", url: str = "") -> None
```

<a id="unreal.MediaCaptureDevice.display_name"></a>

#### display_name

```python
@property
def display_name() -> Text
```

(Text):  [Read-Only] Human readable display name.

<a id="unreal.MediaCaptureDevice.url"></a>

#### url

```python
@property
def url() -> str
```

(str):  [Read-Only] Media URL string for use with media players.

<a id="unreal.ActorDataLayer"></a>