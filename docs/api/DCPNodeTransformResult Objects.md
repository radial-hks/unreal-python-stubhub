## DCPNodeTransformResult Objects

```python
class DCPNodeTransformResult(ResultBase)
```

DCPNode Transform Result

**C++ Source:**

- **Plugin**: WdpAssetAPI
- **Module**: DcpAPI
- **File**: DCPNodeAPIParams.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``location`` (Vector):  [Read-Write]
- ``message`` (str):  [Read-Write]
- ``rotation`` (Rotator):  [Read-Write]
- ``scale`` (Vector):  [Read-Write]
- ``scene_change_info`` (WdpSceneChangeInfo):  [Read-Write]
- ``success`` (bool):  [Read-Write]

<a id="unreal.DCPNodeTransformResult.__init__"></a>

#### \_\_init\_\_

```python
def __init__(message: str = "",
             scene_change_info: WdpSceneChangeInfo = [[], [], []],
             success: bool = False,
             location: Vector = [0.000000, 0.000000, 0.000000],
             rotation: Rotator = [0.000000, 0.000000, 0.000000],
             scale: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.DCPNodeTransformResult.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.DCPNodeTransformResult.location"></a>

#### location

```python
@location.setter
def location(value: Vector) -> None
```

<a id="unreal.DCPNodeTransformResult.rotation"></a>

#### rotation

```python
@property
def rotation() -> Rotator
```

(Rotator):  [Read-Write]

<a id="unreal.DCPNodeTransformResult.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: Rotator) -> None
```

<a id="unreal.DCPNodeTransformResult.scale"></a>

#### scale

```python
@property
def scale() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.DCPNodeTransformResult.scale"></a>

#### scale

```python
@scale.setter
def scale(value: Vector) -> None
```

<a id="unreal.DCPNodePickResult"></a>