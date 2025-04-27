## AvaShapeRectangleCornerSettings Objects

```python
class AvaShapeRectangleCornerSettings(StructBase)
```

Ava Shape Rectangle Corner Settings

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: AvalancheShapes
- **File**: AvaShapeRectangleDynMesh.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``bevel_size`` (float):  [Read-Write]
- ``bevel_subdivisions`` (uint8):  [Read-Write]
- ``type`` (AvaShapeCornerType):  [Read-Write]

<a id="unreal.AvaShapeRectangleCornerSettings.__init__"></a>

#### __init__

```python
def __init__(type: AvaShapeCornerType = AvaShapeCornerType.POINT,
             bevel_size: float = 0.000000,
             bevel_subdivisions: int = 0) -> None
```

<a id="unreal.AvaShapeRectangleCornerSettings.type"></a>

#### type

```python
@property
def type() -> AvaShapeCornerType
```

(AvaShapeCornerType):  [Read-Write]

<a id="unreal.AvaShapeRectangleCornerSettings.type"></a>

#### type

```python
@type.setter
def type(value: AvaShapeCornerType) -> None
```

<a id="unreal.AvaShapeRectangleCornerSettings.bevel_size"></a>

#### bevel_size

```python
@property
def bevel_size() -> float
```

(float):  [Read-Write]

<a id="unreal.AvaShapeRectangleCornerSettings.bevel_size"></a>

#### bevel_size

```python
@bevel_size.setter
def bevel_size(value: float) -> None
```

<a id="unreal.AvaShapeRectangleCornerSettings.bevel_subdivisions"></a>

#### bevel_subdivisions

```python
@property
def bevel_subdivisions() -> int
```

(uint8):  [Read-Write]

<a id="unreal.AvaShapeRectangleCornerSettings.bevel_subdivisions"></a>

#### bevel_subdivisions

```python
@bevel_subdivisions.setter
def bevel_subdivisions(value: int) -> None
```

<a id="unreal.AvaToolboxRectangleCornerSettings"></a>