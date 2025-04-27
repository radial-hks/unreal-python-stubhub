## ControlRigSnapSettings Objects

```python
class ControlRigSnapSettings(Object)
```

Control Rig Snap Settings

**C++ Source:**

- **Plugin**: ControlRig
- **Module**: ControlRigEditor
- **File**: ControlRigSnapSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``baking_key_settings`` (BakingKeySettings):  [Read-Write]
- ``frame_increment`` (int32):  [Read-Write]
- ``keep_offset`` (bool):  [Read-Write] When snapping keep offset, if false snap completely
- ``reduce_keys`` (bool):  [Read-Write]
- ``snap_position`` (bool):  [Read-Write] When snapping, also snap position
- ``snap_rotation`` (bool):  [Read-Write] When snapping, also snap rotation
- ``snap_scale`` (bool):  [Read-Write] When snapping, also snap scale
- ``tolerance`` (float):  [Read-Write]

<a id="unreal.ControlRigSnapSettings.keep_offset"></a>

#### keep_offset

```python
@property
def keep_offset() -> bool
```

(bool):  [Read-Write] When snapping keep offset, if false snap completely

<a id="unreal.ControlRigSnapSettings.keep_offset"></a>

#### keep_offset

```python
@keep_offset.setter
def keep_offset(value: bool) -> None
```

<a id="unreal.ControlRigSnapSettings.snap_position"></a>

#### snap_position

```python
@property
def snap_position() -> bool
```

(bool):  [Read-Write] When snapping, also snap position

<a id="unreal.ControlRigSnapSettings.snap_position"></a>

#### snap_position

```python
@snap_position.setter
def snap_position(value: bool) -> None
```

<a id="unreal.ControlRigSnapSettings.snap_rotation"></a>

#### snap_rotation

```python
@property
def snap_rotation() -> bool
```

(bool):  [Read-Write] When snapping, also snap rotation

<a id="unreal.ControlRigSnapSettings.snap_rotation"></a>

#### snap_rotation

```python
@snap_rotation.setter
def snap_rotation(value: bool) -> None
```

<a id="unreal.ControlRigSnapSettings.snap_scale"></a>

#### snap_scale

```python
@property
def snap_scale() -> bool
```

(bool):  [Read-Write] When snapping, also snap scale

<a id="unreal.ControlRigSnapSettings.snap_scale"></a>

#### snap_scale

```python
@snap_scale.setter
def snap_scale(value: bool) -> None
```

<a id="unreal.ControlRigSnapSettings.baking_key_settings"></a>

#### baking_key_settings

```python
@property
def baking_key_settings() -> BakingKeySettings
```

(BakingKeySettings):  [Read-Write]

<a id="unreal.ControlRigSnapSettings.baking_key_settings"></a>

#### baking_key_settings

```python
@baking_key_settings.setter
def baking_key_settings(value: BakingKeySettings) -> None
```

<a id="unreal.ControlRigSnapSettings.frame_increment"></a>

#### frame_increment

```python
@property
def frame_increment() -> int
```

(int32):  [Read-Write]

<a id="unreal.ControlRigSnapSettings.frame_increment"></a>

#### frame_increment

```python
@frame_increment.setter
def frame_increment(value: int) -> None
```

<a id="unreal.ControlRigSnapSettings.reduce_keys"></a>

#### reduce_keys

```python
@property
def reduce_keys() -> bool
```

(bool):  [Read-Write]

<a id="unreal.ControlRigSnapSettings.reduce_keys"></a>

#### reduce_keys

```python
@reduce_keys.setter
def reduce_keys(value: bool) -> None
```

<a id="unreal.ControlRigSnapSettings.tolerance"></a>

#### tolerance

```python
@property
def tolerance() -> float
```

(float):  [Read-Write]

<a id="unreal.ControlRigSnapSettings.tolerance"></a>

#### tolerance

```python
@tolerance.setter
def tolerance(value: float) -> None
```

<a id="unreal.CreateControlPoseAssetRigSettings"></a>