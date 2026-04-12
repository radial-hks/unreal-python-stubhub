## WdpGlobalSettingsManager Objects

```python
class WdpGlobalSettingsManager(WorldSubsystem)
```

Wdp Global Settings Manager

**C++ Source:**

- **Plugin**: WdpApplication
- **Module**: WdpGlobalSettings
- **File**: WdpGlobalSettingsManager.h

<a id="unreal.WdpGlobalSettingsManager.set_resolution"></a>

#### set\_resolution

```python
def set_resolution(size_x: int, size_y: int) -> bool
```

x.set_resolution(size_x, size_y) -> bool
设置分辨率

Args:
    size_x (int32): 
    size_y (int32): 

Returns:
    bool:

<a id="unreal.WdpGlobalSettingsManager.set_frame_rate_limit"></a>

#### set\_frame\_rate\_limit

```python
def set_frame_rate_limit(max_fps: int) -> bool
```

x.set_frame_rate_limit(max_fps) -> bool
设置帧率

Args:
    max_fps (int32): 

Returns:
    bool:

<a id="unreal.WdpGlobalSettingsManager.set_coord_z_ref"></a>

#### set\_coord\_z\_ref

```python
def set_coord_z_ref(coord_z_type_value: Coord_Z_Ref) -> None
```

x.set_coord_z_ref(coord_z_type_value) -> None
设置坐标高度类型

Args:
    coord_z_type_value (Coord_Z_Ref):

<a id="unreal.WdpGlobalSettingsManager.set_audio_volume"></a>

#### set\_audio\_volume

```python
def set_audio_volume(volume: float) -> bool
```

x.set_audio_volume(volume) -> bool
设置是否静音

Args:
    volume (float): 

Returns:
    bool:

<a id="unreal.WdpGlobalSettingsManager.get_resolution"></a>

#### get\_resolution

```python
def get_resolution() -> Vector2D
```

x.get_resolution() -> Vector2D
获取分辨率

Returns:
    Vector2D:

<a id="unreal.WdpGlobalSettingsManager.get_frame_rate_limit"></a>

#### get\_frame\_rate\_limit

```python
def get_frame_rate_limit() -> float
```

x.get_frame_rate_limit() -> float
获取帧率

Returns:
    float:

<a id="unreal.WdpGlobalSettingsManager.get_coord_z_ref"></a>

#### get\_coord\_z\_ref

```python
def get_coord_z_ref() -> Coord_Z_Ref
```

x.get_coord_z_ref() -> Coord_Z_Ref
获取坐标高度类型

Returns:
    Coord_Z_Ref:

<a id="unreal.WdpGlobalSettingsManager.get"></a>

#### get

```python
@classmethod
def get(cls) -> WdpGlobalSettingsManager
```

X.get() -> WdpGlobalSettingsManager
Get

Returns:
    WdpGlobalSettingsManager:

<a id="unreal.PixelStreaming51CloudAudioComponent"></a>