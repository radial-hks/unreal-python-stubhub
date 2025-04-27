## AvaMaterialMaskSettings Objects

```python
class AvaMaterialMaskSettings(StructBase)
```

TODO: use this for UAvaText3DComponent in place of separate mask settings
Main Blocker from using this now is that it needs custom tracks/sections/property track editor to be keyable for Sequencer

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheText
- **File**: AvaTextDefs.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``offset`` (float):  [Read-Write]
- ``orientation`` (AvaMaterialMaskOrientation):  [Read-Write]
- ``rotation`` (float):  [Read-Write]
- ``smoothness`` (float):  [Read-Write]

<a id="unreal.AvaMaterialMaskSettings.__init__"></a>

#### __init__

```python
def __init__(
        orientation: AvaMaterialMaskOrientation = AvaMaterialMaskOrientation.
    LEFT_RIGHT,
        smoothness: float = 0.000000,
        offset: float = 0.000000,
        rotation: float = 0.000000) -> None
```

<a id="unreal.AvaMaterialMaskSettings.orientation"></a>

#### orientation

```python
@property
def orientation() -> AvaMaterialMaskOrientation
```

(AvaMaterialMaskOrientation):  [Read-Write]

<a id="unreal.AvaMaterialMaskSettings.orientation"></a>

#### orientation

```python
@orientation.setter
def orientation(value: AvaMaterialMaskOrientation) -> None
```

<a id="unreal.AvaMaterialMaskSettings.smoothness"></a>

#### smoothness

```python
@property
def smoothness() -> float
```

(float):  [Read-Write]

<a id="unreal.AvaMaterialMaskSettings.smoothness"></a>

#### smoothness

```python
@smoothness.setter
def smoothness(value: float) -> None
```

<a id="unreal.AvaMaterialMaskSettings.offset"></a>

#### offset

```python
@property
def offset() -> float
```

(float):  [Read-Write]

<a id="unreal.AvaMaterialMaskSettings.offset"></a>

#### offset

```python
@offset.setter
def offset(value: float) -> None
```

<a id="unreal.AvaMaterialMaskSettings.rotation"></a>

#### rotation

```python
@property
def rotation() -> float
```

(float):  [Read-Write]

<a id="unreal.AvaMaterialMaskSettings.rotation"></a>

#### rotation

```python
@rotation.setter
def rotation(value: float) -> None
```

<a id="unreal.AvaTextField"></a>