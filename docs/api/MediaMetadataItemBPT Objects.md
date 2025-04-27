## MediaMetadataItemBPT Objects

```python
class MediaMetadataItemBPT(StructBase)
```

Media Metadata Item BPT

**C++ Source:**

- **Module**: MediaAssets
- **File**: MediaPlayer.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``binary_data`` (Array[uint8]):  [Read-Write]
- ``language_code`` (str):  [Read-Write]
- ``mime_type`` (str):  [Read-Write]
- ``string_data`` (str):  [Read-Write]

<a id="unreal.MediaMetadataItemBPT.__init__"></a>

#### __init__

```python
def __init__(language_code: str = "",
             mime_type: str = "",
             string_data: str = "",
             binary_data: Array[int] = []) -> None
```

<a id="unreal.MediaMetadataItemBPT.language_code"></a>

#### language_code

```python
@property
def language_code() -> str
```

(str):  [Read-Only]

<a id="unreal.MediaMetadataItemBPT.mime_type"></a>

#### mime_type

```python
@property
def mime_type() -> str
```

(str):  [Read-Only]

<a id="unreal.MediaMetadataItemBPT.string_data"></a>

#### string_data

```python
@property
def string_data() -> str
```

(str):  [Read-Only]

<a id="unreal.MediaMetadataItemBPT.binary_data"></a>

#### binary_data

```python
@property
def binary_data() -> Array[int]
```

(Array[uint8]):  [Read-Only]

<a id="unreal.MediaMetadataItemsBPT"></a>