## LiveLinkTransformStaticData Objects

```python
class LiveLinkTransformStaticData(LiveLinkBaseStaticData)
```

Static data for Transform data.

**C++ Source:**

- **Module**: LiveLinkInterface
- **File**: LiveLinkTransformTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``is_location_supported`` (bool):  [Read-Write] Whether location in frame data should be used
- ``is_rotation_supported`` (bool):  [Read-Write] Whether rotation in frame data should be used
- ``is_scale_supported`` (bool):  [Read-Write] Whether scale in frame data should be used
- ``property_names`` (Array[Name]):  [Read-Write] Names for each curve values that will be sent for each frame

<a id="unreal.LiveLinkTransformStaticData.__init__"></a>

#### __init__

```python
def __init__(property_names: Array[Name] = [],
             is_location_supported: bool = False,
             is_rotation_supported: bool = False,
             is_scale_supported: bool = False) -> None
```

<a id="unreal.LiveLinkTransformStaticData.is_location_supported"></a>

#### is_location_supported

```python
@property
def is_location_supported() -> bool
```

(bool):  [Read-Write] Whether location in frame data should be used

<a id="unreal.LiveLinkTransformStaticData.is_location_supported"></a>

#### is_location_supported

```python
@is_location_supported.setter
def is_location_supported(value: bool) -> None
```

<a id="unreal.LiveLinkTransformStaticData.is_rotation_supported"></a>

#### is_rotation_supported

```python
@property
def is_rotation_supported() -> bool
```

(bool):  [Read-Write] Whether rotation in frame data should be used

<a id="unreal.LiveLinkTransformStaticData.is_rotation_supported"></a>

#### is_rotation_supported

```python
@is_rotation_supported.setter
def is_rotation_supported(value: bool) -> None
```

<a id="unreal.LiveLinkTransformStaticData.is_scale_supported"></a>

#### is_scale_supported

```python
@property
def is_scale_supported() -> bool
```

(bool):  [Read-Write] Whether scale in frame data should be used

<a id="unreal.LiveLinkTransformStaticData.is_scale_supported"></a>

#### is_scale_supported

```python
@is_scale_supported.setter
def is_scale_supported(value: bool) -> None
```

<a id="unreal.LiveLinkCameraStaticData"></a>