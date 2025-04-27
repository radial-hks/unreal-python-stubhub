## LandmassLandscapeInfo Objects

```python
class LandmassLandscapeInfo(StructBase)
```

Landmass Landscape Info

**C++ Source:**

- **Plugin**: Landmass
- **Module**: LandmassEditor
- **File**: LandmassManagerBase.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``landscape_quads`` (IntPoint):  [Read-Write]
- ``landscape_transform`` (Transform):  [Read-Write]
- ``render_target_resolution`` (IntPoint):  [Read-Write]

<a id="unreal.LandmassLandscapeInfo.__init__"></a>

#### __init__

```python
def __init__(landscape_transform: Transform = [[0.000000, 0.000000, 0.000000],
                                               [-0.000000, 0.000000, 0.000000],
                                               [1.000000, 1.000000, 1.000000]],
             landscape_quads: IntPoint = [0, 0],
             render_target_resolution: IntPoint = [0, 0]) -> None
```

<a id="unreal.LandmassLandscapeInfo.landscape_transform"></a>

#### landscape_transform

```python
@property
def landscape_transform() -> Transform
```

(Transform):  [Read-Write]

<a id="unreal.LandmassLandscapeInfo.landscape_transform"></a>

#### landscape_transform

```python
@landscape_transform.setter
def landscape_transform(value: Transform) -> None
```

<a id="unreal.LandmassLandscapeInfo.landscape_quads"></a>

#### landscape_quads

```python
@property
def landscape_quads() -> IntPoint
```

(IntPoint):  [Read-Write]

<a id="unreal.LandmassLandscapeInfo.landscape_quads"></a>

#### landscape_quads

```python
@landscape_quads.setter
def landscape_quads(value: IntPoint) -> None
```

<a id="unreal.LandmassLandscapeInfo.render_target_resolution"></a>

#### render_target_resolution

```python
@property
def render_target_resolution() -> IntPoint
```

(IntPoint):  [Read-Write]

<a id="unreal.LandmassLandscapeInfo.render_target_resolution"></a>

#### render_target_resolution

```python
@render_target_resolution.setter
def render_target_resolution(value: IntPoint) -> None
```

<a id="unreal.MirrorOptions"></a>