## WdpCameraRoamFrame Objects

```python
class WdpCameraRoamFrame(StructBase)
```

Wdp Camera Roam Frame

**C++ Source:**

- **Plugin**: WdpApplication
- **Module**: WdpCameraPreset
- **File**: CameraRoamAtom.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``location`` (Vector):  [Read-Only]
- ``rotation`` (CameraPresetRotator):  [Read-Only]
- ``time`` (float):  [Read-Only]

<a id="unreal.WdpCameraRoamFrame.__init__"></a>

#### \_\_init\_\_

```python
def __init__(location: Vector = [0.000000, 0.000000, 0.000000],
             rotation: CameraPresetRotator = [0.000000, 0.000000],
             time: float = 0.000000) -> None
```

<a id="unreal.WdpCameraRoamFrame.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.WdpCameraRoamFrame.rotation"></a>

#### rotation

```python
@property
def rotation() -> CameraPresetRotator
```

(CameraPresetRotator):  [Read-Only]

<a id="unreal.WdpCameraRoamFrame.time"></a>

#### time

```python
@property
def time() -> float
```

(float):  [Read-Only]

<a id="unreal.CameraRoamPath"></a>