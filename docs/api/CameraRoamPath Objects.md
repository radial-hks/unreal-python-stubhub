## CameraRoamPath Objects

```python
class CameraRoamPath(StructBase)
```

Camera Roam Path

**C++ Source:**

- **Plugin**: WdpApplication
- **Module**: WdpCameraPreset
- **File**: CameraRoamEntity.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``duration`` (float):  [Read-Write]
- ``length`` (double):  [Read-Write]
- ``location`` (RuntimeVectorCurve):  [Read-Write]
- ``rotation`` (RuntimeVectorCurve):  [Read-Write]

<a id="unreal.CameraRoamPath.__init__"></a>

#### \_\_init\_\_

```python
def __init__(location: RuntimeVectorCurve = [],
             rotation: RuntimeVectorCurve = [],
             duration: float = 0.000000,
             length: float = 0.000000) -> None
```

<a id="unreal.CameraRoamPath.location"></a>

#### location

```python
@property
def location() -> RuntimeVectorCurve
```

(RuntimeVectorCurve):  [Read-Write]

<a id="unreal.CameraRoamPath.location"></a>

#### location

```python
@location.setter
def location(value: RuntimeVectorCurve) -> None
```

<a id="unreal.CameraRoamPath.rotation"></a>

#### rotation

```python
@property
def rotation() -> RuntimeVectorCurve
```

(RuntimeVectorCurve):  [Read-Write]

<a id="unreal.CameraRoamPath.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: RuntimeVectorCurve) -> None
```

<a id="unreal.CameraRoamPath.duration"></a>

#### duration

```python
@property
def duration() -> float
```

(float):  [Read-Write]

<a id="unreal.CameraRoamPath.duration"></a>

#### duration

```python
@duration.setter
def duration(value: float) -> None
```

<a id="unreal.CameraRoamPath.length"></a>

#### length

```python
@property
def length() -> float
```

(double):  [Read-Write]

<a id="unreal.CameraRoamPath.length"></a>

#### length

```python
@length.setter
def length(value: float) -> None
```

<a id="unreal.ChangedMaterialInfo"></a>