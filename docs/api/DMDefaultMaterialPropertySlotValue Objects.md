## DMDefaultMaterialPropertySlotValue Objects

```python
class DMDefaultMaterialPropertySlotValue(StructBase)
```

DMDefault Material Property Slot Value

**C++ Source:**

- **Plugin**: DynamicMaterial
- **Module**: DynamicMaterialEditor
- **File**: DynamicMaterialEditorSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color`` (LinearColor):  [Read-Write]
- ``default_type`` (DMDefaultMaterialPropertySlotValueType):  [Read-Write]
- ``texture`` (Texture):  [Read-Write]

<a id="unreal.DMDefaultMaterialPropertySlotValue.__init__"></a>

#### __init__

```python
def __init__(
        default_type:
    DMDefaultMaterialPropertySlotValueType = DMDefaultMaterialPropertySlotValueType
    .TEXTURE,
        texture: Texture = None,
        color: LinearColor = [0.000000, 0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.DMDefaultMaterialPropertySlotValue.default_type"></a>

#### default_type

```python
@property
def default_type() -> DMDefaultMaterialPropertySlotValueType
```

(DMDefaultMaterialPropertySlotValueType):  [Read-Write]

<a id="unreal.DMDefaultMaterialPropertySlotValue.default_type"></a>

#### default_type

```python
@default_type.setter
def default_type(value: DMDefaultMaterialPropertySlotValueType) -> None
```

<a id="unreal.DMDefaultMaterialPropertySlotValue.texture"></a>

#### texture

```python
@property
def texture() -> Texture
```

(Texture):  [Read-Write]

<a id="unreal.DMDefaultMaterialPropertySlotValue.texture"></a>

#### texture

```python
@texture.setter
def texture(value: Texture) -> None
```

<a id="unreal.DMDefaultMaterialPropertySlotValue.color"></a>

#### color

```python
@property
def color() -> LinearColor
```

(LinearColor):  [Read-Write]

<a id="unreal.DMDefaultMaterialPropertySlotValue.color"></a>

#### color

```python
@color.setter
def color(value: LinearColor) -> None
```

<a id="unreal.DMMaterialChannelListPreset"></a>