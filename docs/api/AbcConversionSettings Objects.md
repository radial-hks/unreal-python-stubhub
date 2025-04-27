## AbcConversionSettings Objects

```python
class AbcConversionSettings(StructBase)
```

Abc Conversion Settings

**C++ Source:**

- **Plugin**: AlembicImporter
- **Module**: AlembicLibrary
- **File**: AbcImportSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``flip_u`` (bool):  [Read-Write] Flag whether or not to flip the U channel in the Texture Coordinates
- ``flip_v`` (bool):  [Read-Write] Flag whether or not to flip the V channel in the Texture Coordinates
- ``preset`` (AbcConversionPreset):  [Read-Write] Currently preset that should be applied
- ``rotation`` (Vector):  [Read-Write] Rotation in Euler angles that should be applied
- ``scale`` (Vector):  [Read-Write] Scale value that should be applied

<a id="unreal.AbcConversionSettings.__init__"></a>

#### __init__

```python
def __init__(preset: AbcConversionPreset = AbcConversionPreset.MAYA,
             flip_u: bool = False,
             flip_v: bool = False,
             scale: Vector = [0.000000, 0.000000, 0.000000],
             rotation: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.AbcConversionSettings.preset"></a>

#### preset

```python
@property
def preset() -> AbcConversionPreset
```

(AbcConversionPreset):  [Read-Write] Currently preset that should be applied

<a id="unreal.AbcConversionSettings.preset"></a>

#### preset

```python
@preset.setter
def preset(value: AbcConversionPreset) -> None
```

<a id="unreal.AbcConversionSettings.flip_u"></a>

#### flip_u

```python
@property
def flip_u() -> bool
```

(bool):  [Read-Write] Flag whether or not to flip the U channel in the Texture Coordinates

<a id="unreal.AbcConversionSettings.flip_u"></a>

#### flip_u

```python
@flip_u.setter
def flip_u(value: bool) -> None
```

<a id="unreal.AbcConversionSettings.flip_v"></a>

#### flip_v

```python
@property
def flip_v() -> bool
```

(bool):  [Read-Write] Flag whether or not to flip the V channel in the Texture Coordinates

<a id="unreal.AbcConversionSettings.flip_v"></a>

#### flip_v

```python
@flip_v.setter
def flip_v(value: bool) -> None
```

<a id="unreal.AbcConversionSettings.scale"></a>

#### scale

```python
@property
def scale() -> Vector
```

(Vector):  [Read-Write] Scale value that should be applied

<a id="unreal.AbcConversionSettings.scale"></a>

#### scale

```python
@scale.setter
def scale(value: Vector) -> None
```

<a id="unreal.AbcConversionSettings.rotation"></a>

#### rotation

```python
@property
def rotation() -> Vector
```

(Vector):  [Read-Write] Rotation in Euler angles that should be applied

<a id="unreal.AbcConversionSettings.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: Vector) -> None
```

<a id="unreal.AbcGeometryCacheSettings"></a>