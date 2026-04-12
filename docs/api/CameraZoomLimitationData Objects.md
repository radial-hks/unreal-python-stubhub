## CameraZoomLimitationData Objects

```python
class CameraZoomLimitationData(StructBase)
```

缩放操作的限制参数

**C++ Source:**

- **Plugin**: WdpCamera
- **Module**: WdpCamera
- **File**: WdpDataSource.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``max_fov`` (float):  [Read-Write] 如果滚轮是在操作FOV，最大的FOV数值
- ``max_zoom_distance`` (double):  [Read-Write] 最大的缩放距离，使用滚轮缩放时会保持的最大距离，如果当前距离超过了不会进行修正
- ``min_fov`` (float):  [Read-Write] 如果滚轮是在操作FOV，最小的FOV数值（FOV越小，视野越大）
- ``min_zoom_distance`` (double):  [Read-Write] 最小的缩放距离，使用滚轮缩放时会保持的最小距离

<a id="unreal.CameraZoomLimitationData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(min_zoom_distance: float = 0.000000,
             max_zoom_distance: float = 0.000000,
             min_fov: float = 0.000000,
             max_fov: float = 0.000000) -> None
```

<a id="unreal.CameraZoomLimitationData.min_zoom_distance"></a>

#### min\_zoom\_distance

```python
@property
def min_zoom_distance() -> float
```

(double):  [Read-Write] 最小的缩放距离，使用滚轮缩放时会保持的最小距离

<a id="unreal.CameraZoomLimitationData.min_zoom_distance"></a>

#### min\_zoom\_distance

```python
@min_zoom_distance.setter
def min_zoom_distance(value: float) -> None
```

<a id="unreal.CameraZoomLimitationData.max_zoom_distance"></a>

#### max\_zoom\_distance

```python
@property
def max_zoom_distance() -> float
```

(double):  [Read-Write] 最大的缩放距离，使用滚轮缩放时会保持的最大距离，如果当前距离超过了不会进行修正

<a id="unreal.CameraZoomLimitationData.max_zoom_distance"></a>

#### max\_zoom\_distance

```python
@max_zoom_distance.setter
def max_zoom_distance(value: float) -> None
```

<a id="unreal.CameraZoomLimitationData.min_fov"></a>

#### min\_fov

```python
@property
def min_fov() -> float
```

(float):  [Read-Write] 如果滚轮是在操作FOV，最小的FOV数值（FOV越小，视野越大）

<a id="unreal.CameraZoomLimitationData.min_fov"></a>

#### min\_fov

```python
@min_fov.setter
def min_fov(value: float) -> None
```

<a id="unreal.CameraZoomLimitationData.max_fov"></a>

#### max\_fov

```python
@property
def max_fov() -> float
```

(float):  [Read-Write] 如果滚轮是在操作FOV，最大的FOV数值

<a id="unreal.CameraZoomLimitationData.max_fov"></a>

#### max\_fov

```python
@max_fov.setter
def max_fov(value: float) -> None
```

<a id="unreal.CameraRotationLimitationData"></a>