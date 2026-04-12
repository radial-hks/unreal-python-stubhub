## FollowActorInterface Objects

```python
class FollowActorInterface(Interface)
```

Follow Actor Interface

**C++ Source:**

- **Plugin**: WdpCamera
- **Module**: WdpCamera
- **File**: FollowActorInterface.h

<a id="unreal.FollowActorInterface.bpi_on_following_start"></a>

#### bpi\_on\_following\_start

```python
def bpi_on_following_start() -> None
```

x.bpi_on_following_start() -> None
跟踪开始事件

<a id="unreal.FollowActorInterface.bpi_on_following_end"></a>

#### bpi\_on\_following\_end

```python
def bpi_on_following_end() -> None
```

x.bpi_on_following_end() -> None
跟踪结束事件

<a id="unreal.FollowActorInterface.bpi_get_follow_camera_settings"></a>

#### bpi\_get\_follow\_camera\_settings

```python
def bpi_get_follow_camera_settings() -> Optional[FollowCameraSettings]
```

x.bpi_get_follow_camera_settings() -> FollowCameraSettings or None
获取跟踪数据

Returns:
    FollowCameraSettings or None: 

    camera_settings (FollowCameraSettings):

<a id="unreal.TouchInputComponent"></a>