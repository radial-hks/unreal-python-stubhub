## Visible2DParam Objects

```python
class Visible2DParam(ParamsBase)
```

Visible 2DParam

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIDefine
- **File**: Visible2DAtomAPI.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``camera`` (Visible2DCamera):  [Read-Write]
- ``eids`` (Array[int64]):  [Read-Write]
- ``guid`` (str):  [Read-Write]
- ``hit_keys`` (Set[Name]):  [Read-Write]
- ``interaction`` (Visible2DInteraction):  [Read-Write]

<a id="unreal.Visible2DParam.__init__"></a>

#### \_\_init\_\_

```python
def __init__(eids: Array[int] = [],
             camera: Visible2DCamera = [500.000000, "none", "2D"],
             interaction: Visible2DInteraction = [True, True]) -> None
```

<a id="unreal.Visible2DParam.eids"></a>

#### eids

```python
@property
def eids() -> Array[int]
```

(Array[int64]):  [Read-Write]

<a id="unreal.Visible2DParam.eids"></a>

#### eids

```python
@eids.setter
def eids(value: Array[int]) -> None
```

<a id="unreal.Visible2DParam.camera"></a>

#### camera

```python
@property
def camera() -> Visible2DCamera
```

(Visible2DCamera):  [Read-Write]

<a id="unreal.Visible2DParam.camera"></a>

#### camera

```python
@camera.setter
def camera(value: Visible2DCamera) -> None
```

<a id="unreal.Visible2DParam.interaction"></a>

#### interaction

```python
@property
def interaction() -> Visible2DInteraction
```

(Visible2DInteraction):  [Read-Write]

<a id="unreal.Visible2DParam.interaction"></a>

#### interaction

```python
@interaction.setter
def interaction(value: Visible2DInteraction) -> None
```

<a id="unreal.CoverWindowStyle"></a>