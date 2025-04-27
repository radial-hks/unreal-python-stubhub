## GLTFMaterialBakeSize Objects

```python
class GLTFMaterialBakeSize(StructBase)
```

GLTFMaterial Bake Size

**C++ Source:**

- **Plugin**: GLTFExporter
- **Module**: GLTFExporter
- **File**: GLTFMaterialUserData.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``auto_detect`` (bool):  [Read-Write] If enabled, bake size is based on the largest texture used in the material input's expression graph. If none found, bake size will fall back to the explicit dimensions.
- ``x`` (int32):  [Read-Write]
- ``y`` (int32):  [Read-Write]

<a id="unreal.GLTFMaterialBakeSize.__init__"></a>

#### __init__

```python
def __init__(x: int = 0, y: int = 0, auto_detect: bool = False) -> None
```

<a id="unreal.GLTFMaterialBakeSize.x"></a>

#### x

```python
@property
def x() -> int
```

(int32):  [Read-Write]

<a id="unreal.GLTFMaterialBakeSize.x"></a>

#### x

```python
@x.setter
def x(value: int) -> None
```

<a id="unreal.GLTFMaterialBakeSize.y"></a>

#### y

```python
@property
def y() -> int
```

(int32):  [Read-Write]

<a id="unreal.GLTFMaterialBakeSize.y"></a>

#### y

```python
@y.setter
def y(value: int) -> None
```

<a id="unreal.GLTFMaterialBakeSize.auto_detect"></a>

#### auto_detect

```python
@property
def auto_detect() -> bool
```

(bool):  [Read-Write] If enabled, bake size is based on the largest texture used in the material input's expression graph. If none found, bake size will fall back to the explicit dimensions.

<a id="unreal.GLTFMaterialBakeSize.auto_detect"></a>

#### auto_detect

```python
@auto_detect.setter
def auto_detect(value: bool) -> None
```

<a id="unreal.GLTFOverrideMaterialBakeSettings"></a>