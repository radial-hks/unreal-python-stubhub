## CameraRotationLimitationData Objects

```python
class CameraRotationLimitationData(StructBase)
```

旋转限制参数

**C++ Source:**

- **Plugin**: WdpCamera
- **Module**: WdpCamera
- **File**: WdpDataSource.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``max_pitch`` (float):  [Read-Write] 最大Pitch，抬头角度
- ``max_yaw`` (float):  [Read-Write] 最大Yaw，向右看的角度
- ``min_pitch`` (float):  [Read-Write] 最小pitch，低头角度
- ``min_yaw`` (float):  [Read-Write] 最小Yaw，向左看的角度
- ``use_local_space`` (bool):  [Read-Write] 最小Roll，向左转的角度
  UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Data")
         float MinRoll;
  最大Roll，向右转的角度
  UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Data")
         float MaxRoll;
  是否使用本地空间，如果启用则以相机自身的transform为准(废弃)

<a id="unreal.CameraRotationLimitationData.__init__"></a>

#### \_\_init\_\_

```python
def __init__(min_pitch: float = 0.000000,
             max_pitch: float = 0.000000,
             min_yaw: float = 0.000000,
             max_yaw: float = 0.000000,
             use_local_space: bool = False) -> None
```

<a id="unreal.CameraRotationLimitationData.min_pitch"></a>

#### min\_pitch

```python
@property
def min_pitch() -> float
```

(float):  [Read-Write] 最小pitch，低头角度

<a id="unreal.CameraRotationLimitationData.min_pitch"></a>

#### min\_pitch

```python
@min_pitch.setter
def min_pitch(value: float) -> None
```

<a id="unreal.CameraRotationLimitationData.max_pitch"></a>

#### max\_pitch

```python
@property
def max_pitch() -> float
```

(float):  [Read-Write] 最大Pitch，抬头角度

<a id="unreal.CameraRotationLimitationData.max_pitch"></a>

#### max\_pitch

```python
@max_pitch.setter
def max_pitch(value: float) -> None
```

<a id="unreal.CameraRotationLimitationData.min_yaw"></a>

#### min\_yaw

```python
@property
def min_yaw() -> float
```

(float):  [Read-Write] 最小Yaw，向左看的角度

<a id="unreal.CameraRotationLimitationData.min_yaw"></a>

#### min\_yaw

```python
@min_yaw.setter
def min_yaw(value: float) -> None
```

<a id="unreal.CameraRotationLimitationData.max_yaw"></a>

#### max\_yaw

```python
@property
def max_yaw() -> float
```

(float):  [Read-Write] 最大Yaw，向右看的角度

<a id="unreal.CameraRotationLimitationData.max_yaw"></a>

#### max\_yaw

```python
@max_yaw.setter
def max_yaw(value: float) -> None
```

<a id="unreal.CameraRotationLimitationData.use_local_space"></a>

#### use\_local\_space

```python
@property
def use_local_space() -> bool
```

(bool):  [Read-Write] 最小Roll，向左转的角度
UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Data")
       float MinRoll;
最大Roll，向右转的角度
UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Data")
       float MaxRoll;
是否使用本地空间，如果启用则以相机自身的transform为准(废弃)

<a id="unreal.CameraRotationLimitationData.use_local_space"></a>

#### use\_local\_space

```python
@use_local_space.setter
def use_local_space(value: bool) -> None
```

<a id="unreal.CoreCameraData"></a>