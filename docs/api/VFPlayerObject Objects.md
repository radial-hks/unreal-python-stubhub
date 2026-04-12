## VFPlayerObject Objects

```python
class VFPlayerObject(Object)
```

VFPlayer Object

**C++ Source:**

- **Plugin**: VFVideoPlayer
- **Module**: VFVideoPlayer
- **File**: VFPlayerObject.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``url`` (str):  [Read-Write]

<a id="unreal.VFPlayerObject.stop"></a>

#### stop

```python
def stop() -> None
```

x.stop() -> None
停止

<a id="unreal.VFPlayerObject.scrub"></a>

#### scrub

```python
def scrub(time_sec: float) -> None
```

x.scrub(time_sec) -> None
跳到某个时间播放

Args:
    time_sec (float): 时间（秒）

<a id="unreal.VFPlayerObject.play"></a>

#### play

```python
def play() -> None
```

x.play() -> None
播放

<a id="unreal.VFPlayerObject.pause"></a>

#### pause

```python
def pause() -> None
```

x.pause() -> None
暂停

<a id="unreal.VFPlayerObject.initialize_without_delegate"></a>

#### initialize\_without\_delegate

```python
def initialize_without_delegate(url: str) -> bool
```

x.initialize_without_delegate(url) -> bool
初始化播放器不从外部传入Delegate

Args:
    url (str): 视频资源的Url，可以是本地文件，也可以是视频流地址等。

Returns:
    bool: 成功返回true

<a id="unreal.VFPlayerObject.initialize"></a>

#### initialize

```python
def initialize(url: str,
               on_video_loaded_callback: OnVideoLoadedDelegate) -> bool
```

x.initialize(url, on_video_loaded_callback) -> bool
初始化播放器

Args:
    url (str): 视频资源的Url，可以是本地文件，也可以是视频流地址等。
    on_video_loaded_callback (OnVideoLoadedDelegate): 视频初始化完成并且生成了Texture2D成功回调

Returns:
    bool: 成功返回true

<a id="unreal.VFPlayerObject.get_texture"></a>

#### get\_texture

```python
def get_texture() -> Texture2D
```

x.get_texture() -> Texture2D
获取当前视频Texture

Returns:
    Texture2D:

<a id="unreal.VFPlayerObject.get_length"></a>

#### get\_length

```python
def get_length() -> float
```

x.get_length() -> float
获取视频总时长（秒）

Returns:
    float:

<a id="unreal.VFVideoLog"></a>