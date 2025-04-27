## GroomConversionSettings Objects

```python
class GroomConversionSettings(StructBase)
```

Groom Conversion Settings

**C++ Source:**

- **Plugin**: HairStrands
- **Module**: HairStrandsCore
- **File**: GroomSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``rotation`` (Vector):  [Read-Write] Rotation in Euler angles in degrees to fix up or front axes
- ``scale`` (Vector):  [Read-Write] Scale value to convert file unit into centimeters

<a id="unreal.GroomConversionSettings.__init__"></a>

#### __init__

```python
def __init__(rotation: Vector = [0.000000, 0.000000, 0.000000],
             scale: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.GroomConversionSettings.rotation"></a>

#### rotation

```python
@property
def rotation() -> Vector
```

(Vector):  [Read-Write] Rotation in Euler angles in degrees to fix up or front axes

<a id="unreal.GroomConversionSettings.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: Vector) -> None
```

<a id="unreal.GroomConversionSettings.scale"></a>

#### scale

```python
@property
def scale() -> Vector
```

(Vector):  [Read-Write] Scale value to convert file unit into centimeters

<a id="unreal.GroomConversionSettings.scale"></a>

#### scale

```python
@scale.setter
def scale(value: Vector) -> None
```

<a id="unreal.HairGroupDesc"></a>