## TextureArea Objects

```python
class TextureArea(StructBase)
```

Texture Area

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: SuperAPI_Raster
- **File**: SuperAPI_RasterCommon.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``center`` (Vector):  [Read-Write]
- ``rotator`` (Rotator):  [Read-Write]
- ``scale`` (Vector):  [Read-Write]

<a id="unreal.TextureArea.__init__"></a>

#### \_\_init\_\_

```python
def __init__(center: Vector = [0.000000, 0.000000, 0.000000],
             scale: Vector = [0.000000, 0.000000, 0.000000],
             rotator: Rotator = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.TextureArea.center"></a>

#### center

```python
@property
def center() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.TextureArea.scale"></a>

#### scale

```python
@property
def scale() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.TextureArea.rotator"></a>

#### rotator

```python
@property
def rotator() -> Rotator
```

(Rotator):  [Read-Only]

<a id="unreal.TextureBound"></a>