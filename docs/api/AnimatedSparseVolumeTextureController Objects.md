## AnimatedSparseVolumeTextureController Objects

```python
class AnimatedSparseVolumeTextureController(Object)
```

Utility (blueprint) class for controlling SparseVolumeTexture playback.

**C++ Source:**

- **Module**: Engine
- **File**: SparseVolumeTexture.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blocking_streaming_requests`` (bool):  [Read-Write]
- ``frame_rate`` (float):  [Read-Write]
- ``is_playing`` (bool):  [Read-Write]
- ``mip_level`` (int32):  [Read-Write]
- ``sparse_volume_texture`` (SparseVolumeTexture):  [Read-Write]
- ``time`` (float):  [Read-Write]

<a id="unreal.AnimatedSparseVolumeTextureController.sparse_volume_texture"></a>

#### sparse_volume_texture

```python
@property
def sparse_volume_texture() -> SparseVolumeTexture
```

(SparseVolumeTexture):  [Read-Write]

<a id="unreal.AnimatedSparseVolumeTextureController.sparse_volume_texture"></a>

#### sparse_volume_texture

```python
@sparse_volume_texture.setter
def sparse_volume_texture(value: SparseVolumeTexture) -> None
```

<a id="unreal.AnimatedSparseVolumeTextureController.time"></a>

#### time

```python
@property
def time() -> float
```

(float):  [Read-Write]

<a id="unreal.AnimatedSparseVolumeTextureController.time"></a>

#### time

```python
@time.setter
def time(value: float) -> None
```

<a id="unreal.AnimatedSparseVolumeTextureController.is_playing"></a>

#### is_playing

```python
@property
def is_playing() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AnimatedSparseVolumeTextureController.is_playing"></a>

#### is_playing

```python
@is_playing.setter
def is_playing(value: bool) -> None
```

<a id="unreal.AnimatedSparseVolumeTextureController.frame_rate"></a>

#### frame_rate

```python
@property
def frame_rate() -> float
```

(float):  [Read-Write]

<a id="unreal.AnimatedSparseVolumeTextureController.frame_rate"></a>

#### frame_rate

```python
@frame_rate.setter
def frame_rate(value: float) -> None
```

<a id="unreal.AnimatedSparseVolumeTextureController.mip_level"></a>

#### mip_level

```python
@property
def mip_level() -> int
```

(int32):  [Read-Write]

<a id="unreal.AnimatedSparseVolumeTextureController.mip_level"></a>

#### mip_level

```python
@mip_level.setter
def mip_level(value: int) -> None
```

<a id="unreal.AnimatedSparseVolumeTextureController.blocking_streaming_requests"></a>

#### blocking_streaming_requests

```python
@property
def blocking_streaming_requests() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AnimatedSparseVolumeTextureController.blocking_streaming_requests"></a>

#### blocking_streaming_requests

```python
@blocking_streaming_requests.setter
def blocking_streaming_requests(value: bool) -> None
```

<a id="unreal.AnimatedSparseVolumeTextureController.update"></a>

#### update

```python
def update(delta_time: float) -> None
```

x.update(delta_time) -> None
Update

Args:
    delta_time (float):

<a id="unreal.AnimatedSparseVolumeTextureController.stop"></a>

#### stop

```python
def stop() -> None
```

x.stop() -> None
Stop

<a id="unreal.AnimatedSparseVolumeTextureController.play"></a>

#### play

```python
def play() -> None
```

x.play() -> None
Play

<a id="unreal.AnimatedSparseVolumeTextureController.pause"></a>

#### pause

```python
def pause() -> None
```

x.pause() -> None
Pause

<a id="unreal.AnimatedSparseVolumeTextureController.get_frame_by_index"></a>

#### get_frame_by_index

```python
def get_frame_by_index(frame_index: int) -> SparseVolumeTextureFrame
```

x.get_frame_by_index(frame_index) -> SparseVolumeTextureFrame
Get Frame by Index

Args:
    frame_index (int32): 

Returns:
    SparseVolumeTextureFrame:

<a id="unreal.AnimatedSparseVolumeTextureController.get_fractional_frame_index"></a>

#### get_fractional_frame_index

```python
def get_fractional_frame_index() -> float
```

x.get_fractional_frame_index() -> float
Get Fractional Frame Index

Returns:
    float:

<a id="unreal.AnimatedSparseVolumeTextureController.get_duration"></a>

#### get_duration

```python
def get_duration() -> float
```

x.get_duration() -> float
Get Duration

Returns:
    float:

<a id="unreal.AnimatedSparseVolumeTextureController.get_current_frames_for_interpolation"></a>

#### get_current_frames_for_interpolation

```python
def get_current_frames_for_interpolation(
) -> Tuple[SparseVolumeTextureFrame, SparseVolumeTextureFrame, float]
```

x.get_current_frames_for_interpolation() -> (frame0=SparseVolumeTextureFrame, frame1=SparseVolumeTextureFrame, lerp_alpha=float)
Get Current Frames for Interpolation

Returns:
    tuple: 

    frame0 (SparseVolumeTextureFrame): 

    frame1 (SparseVolumeTextureFrame): 

    lerp_alpha (float):

<a id="unreal.AnimatedSparseVolumeTextureController.get_current_frame"></a>

#### get_current_frame

```python
def get_current_frame() -> SparseVolumeTextureFrame
```

x.get_current_frame() -> SparseVolumeTextureFrame
Get Current Frame

Returns:
    SparseVolumeTextureFrame:

<a id="unreal.SphereReflectionCapture"></a>