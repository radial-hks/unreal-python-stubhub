## AesBuildingPropertyManager Objects

```python
class AesBuildingPropertyManager(WorldSubsystem)
```

Aes Building Property Manager

**C++ Source:**

- **Plugin**: AesWorld
- **Module**: AesEditorMode
- **File**: AesBuildingPropertyManager.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``advanced_properties`` (Array[Name]):  [Read-Write]
- ``color`` (Color):  [Read-Write]
- ``enable_properties`` (Set[Name]):  [Read-Write]
- ``group_id`` (int32):  [Read-Write]
- ``height`` (double):  [Read-Write] normal property
- ``hide`` (bool):  [Read-Write]
- ``land_cover`` (str):  [Read-Write]
- ``land_use`` (Name):  [Read-Write]
- ``levels`` (int32):  [Read-Write] advanced property
- ``min_height`` (double):  [Read-Write]
- ``min_levels`` (int32):  [Read-Write]
- ``normal_properties`` (Array[Name]):  [Read-Write]
- ``on_building_property_changed`` (AesBuildingPropertyChangedEvent):  [Read-Write]
- ``prefab_id`` (str):  [Read-Write]
- ``roof_color`` (Color):  [Read-Write]
- ``roof_height`` (double):  [Read-Write]
- ``roof_levels`` (int32):  [Read-Write]
- ``roof_shape`` (Name):  [Read-Write]
- ``type`` (str):  [Read-Write]

<a id="unreal.AesBuildingPropertyManager.height"></a>

#### height

```python
@property
def height() -> float
```

(double):  [Read-Write] normal property

<a id="unreal.AesBuildingPropertyManager.height"></a>

#### height

```python
@height.setter
def height(value: float) -> None
```

<a id="unreal.AesBuildingPropertyManager.min_height"></a>

#### min\_height

```python
@property
def min_height() -> float
```

(double):  [Read-Write]

<a id="unreal.AesBuildingPropertyManager.min_height"></a>

#### min\_height

```python
@min_height.setter
def min_height(value: float) -> None
```

<a id="unreal.AesBuildingPropertyManager.type"></a>

#### type

```python
@property
def type() -> str
```

(str):  [Read-Write]

<a id="unreal.AesBuildingPropertyManager.type"></a>

#### type

```python
@type.setter
def type(value: str) -> None
```

<a id="unreal.AesBuildingPropertyManager.color"></a>

#### color

```python
@property
def color() -> Color
```

(Color):  [Read-Write]

<a id="unreal.AesBuildingPropertyManager.color"></a>

#### color

```python
@color.setter
def color(value: Color) -> None
```

<a id="unreal.AesBuildingPropertyManager.roof_color"></a>

#### roof\_color

```python
@property
def roof_color() -> Color
```

(Color):  [Read-Write]

<a id="unreal.AesBuildingPropertyManager.roof_color"></a>

#### roof\_color

```python
@roof_color.setter
def roof_color(value: Color) -> None
```

<a id="unreal.AesBuildingPropertyManager.prefab_id"></a>

#### prefab\_id

```python
@property
def prefab_id() -> str
```

(str):  [Read-Write]

<a id="unreal.AesBuildingPropertyManager.prefab_id"></a>

#### prefab\_id

```python
@prefab_id.setter
def prefab_id(value: str) -> None
```

<a id="unreal.AesBuildingPropertyManager.group_id"></a>

#### group\_id

```python
@property
def group_id() -> int
```

(int32):  [Read-Write]

<a id="unreal.AesBuildingPropertyManager.group_id"></a>

#### group\_id

```python
@group_id.setter
def group_id(value: int) -> None
```

<a id="unreal.AesBuildingPropertyManager.land_cover"></a>

#### land\_cover

```python
@property
def land_cover() -> str
```

(str):  [Read-Write]

<a id="unreal.AesBuildingPropertyManager.land_cover"></a>

#### land\_cover

```python
@land_cover.setter
def land_cover(value: str) -> None
```

<a id="unreal.AesBuildingPropertyManager.land_use"></a>

#### land\_use

```python
@property
def land_use() -> Name
```

(Name):  [Read-Write]

<a id="unreal.AesBuildingPropertyManager.land_use"></a>

#### land\_use

```python
@land_use.setter
def land_use(value: Name) -> None
```

<a id="unreal.AesBuildingPropertyManager.hide"></a>

#### hide

```python
@property
def hide() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AesBuildingPropertyManager.hide"></a>

#### hide

```python
@hide.setter
def hide(value: bool) -> None
```

<a id="unreal.AesBuildingPropertyManager.levels"></a>

#### levels

```python
@property
def levels() -> int
```

(int32):  [Read-Write] advanced property

<a id="unreal.AesBuildingPropertyManager.levels"></a>

#### levels

```python
@levels.setter
def levels(value: int) -> None
```

<a id="unreal.AesBuildingPropertyManager.min_levels"></a>

#### min\_levels

```python
@property
def min_levels() -> int
```

(int32):  [Read-Write]

<a id="unreal.AesBuildingPropertyManager.min_levels"></a>

#### min\_levels

```python
@min_levels.setter
def min_levels(value: int) -> None
```

<a id="unreal.AesBuildingPropertyManager.roof_height"></a>

#### roof\_height

```python
@property
def roof_height() -> float
```

(double):  [Read-Write]

<a id="unreal.AesBuildingPropertyManager.roof_height"></a>

#### roof\_height

```python
@roof_height.setter
def roof_height(value: float) -> None
```

<a id="unreal.AesBuildingPropertyManager.roof_levels"></a>

#### roof\_levels

```python
@property
def roof_levels() -> int
```

(int32):  [Read-Write]

<a id="unreal.AesBuildingPropertyManager.roof_levels"></a>

#### roof\_levels

```python
@roof_levels.setter
def roof_levels(value: int) -> None
```

<a id="unreal.AesBuildingPropertyManager.roof_shape"></a>

#### roof\_shape

```python
@property
def roof_shape() -> Name
```

(Name):  [Read-Write]

<a id="unreal.AesBuildingPropertyManager.roof_shape"></a>

#### roof\_shape

```python
@roof_shape.setter
def roof_shape(value: Name) -> None
```

<a id="unreal.AesBuildingPropertyManager.normal_properties"></a>

#### normal\_properties

```python
@property
def normal_properties() -> Array[Name]
```

(Array[Name]):  [Read-Only]

<a id="unreal.AesBuildingPropertyManager.advanced_properties"></a>

#### advanced\_properties

```python
@property
def advanced_properties() -> Array[Name]
```

(Array[Name]):  [Read-Only]

<a id="unreal.AesBuildingPropertyManager.enable_properties"></a>

#### enable\_properties

```python
@property
def enable_properties() -> Set[Name]
```

(Set[Name]):  [Read-Write]

<a id="unreal.AesBuildingPropertyManager.enable_properties"></a>

#### enable\_properties

```python
@enable_properties.setter
def enable_properties(value: Set[Name]) -> None
```

<a id="unreal.AesBuildingPropertyManager.on_building_property_changed"></a>

#### on\_building\_property\_changed

```python
@property
def on_building_property_changed() -> AesBuildingPropertyChangedEvent
```

(AesBuildingPropertyChangedEvent):  [Read-Write]

<a id="unreal.AesBuildingPropertyManager.on_building_property_changed"></a>

#### on\_building\_property\_changed

```python
@on_building_property_changed.setter
def on_building_property_changed(
        value: AesBuildingPropertyChangedEvent) -> None
```

<a id="unreal.AesBuildingPropertyManager.get_building_types"></a>

#### get\_building\_types

```python
def get_building_types() -> Array[str]
```

x.get_building_types() -> Array[str]
Get Building Types

Returns:
    Array[str]:

<a id="unreal.AesDomManager"></a>