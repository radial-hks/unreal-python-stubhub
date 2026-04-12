## RoadHeatMapEntityAtom Objects

```python
class RoadHeatMapEntityAtom(EntityAtomBase)
```

Road Heat Map Entity Atom

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIEntity
- **File**: RoadHeatMapEntityAtom.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``filter`` (Array[str]):  [Read-Write]
- ``gradient_setting`` (Array[str]):  [Read-Write]
- ``mapping_value_range`` (Vector2D):  [Read-Write]
- ``type`` (str):  [Read-Write] UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "RoadHeatMapEntityAtom")
                 int CoordZRef = 0;
- ``width`` (float):  [Read-Write]

<a id="unreal.RoadHeatMapEntityAtom.type"></a>

#### type

```python
@property
def type() -> str
```

(str):  [Read-Write] UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "RoadHeatMapEntityAtom")
               int CoordZRef = 0;

<a id="unreal.RoadHeatMapEntityAtom.type"></a>

#### type

```python
@type.setter
def type(value: str) -> None
```

<a id="unreal.RoadHeatMapEntityAtom.width"></a>

#### width

```python
@property
def width() -> float
```

(float):  [Read-Write]

<a id="unreal.RoadHeatMapEntityAtom.width"></a>

#### width

```python
@width.setter
def width(value: float) -> None
```

<a id="unreal.RoadHeatMapEntityAtom.mapping_value_range"></a>

#### mapping\_value\_range

```python
@property
def mapping_value_range() -> Vector2D
```

(Vector2D):  [Read-Write]

<a id="unreal.RoadHeatMapEntityAtom.mapping_value_range"></a>

#### mapping\_value\_range

```python
@mapping_value_range.setter
def mapping_value_range(value: Vector2D) -> None
```

<a id="unreal.RoadHeatMapEntityAtom.gradient_setting"></a>

#### gradient\_setting

```python
@property
def gradient_setting() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.RoadHeatMapEntityAtom.gradient_setting"></a>

#### gradient\_setting

```python
@gradient_setting.setter
def gradient_setting(value: Array[str]) -> None
```

<a id="unreal.RoadHeatMapEntityAtom.filter"></a>

#### filter

```python
@property
def filter() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.RoadHeatMapEntityAtom.filter"></a>

#### filter

```python
@filter.setter
def filter(value: Array[str]) -> None
```

<a id="unreal.RoadHeatMapEntityAtom.set_width"></a>

#### set\_width

```python
def set_width(new_value: float, need_re_create: bool = False) -> bool
```

x.set_width(new_value, need_re_create=False) -> bool
Set Width

Args:
    new_value (float): 
    need_re_create (bool): 

Returns:
    bool:

<a id="unreal.RoadHeatMapEntityAtom.set_type"></a>

#### set\_type

```python
def set_type(new_type: str, need_re_create: bool = False) -> bool
```

x.set_type(new_type, need_re_create=False) -> bool
UFUNCTION(BlueprintCallable, Category = "RoadHeatMapEntityAtom")
       bool Set_CoordZRef(const int& NewCoordZRef);

Args:
    new_type (str): 
    need_re_create (bool): 

Returns:
    bool:

<a id="unreal.RoadHeatMapEntityAtom.set_mapping_value_range"></a>

#### set\_mapping\_value\_range

```python
def set_mapping_value_range(new_value: Vector2D,
                            need_re_create: bool = False) -> bool
```

x.set_mapping_value_range(new_value, need_re_create=False) -> bool
Set Mapping Value Range

Args:
    new_value (Vector2D): 
    need_re_create (bool): 

Returns:
    bool:

<a id="unreal.RoadHeatMapEntityAtom.set_gradient_setting"></a>

#### set\_gradient\_setting

```python
def set_gradient_setting(new_colors: Array[str],
                         need_re_create: bool = False) -> bool
```

x.set_gradient_setting(new_colors, need_re_create=False) -> bool
Set Gradient Setting

Args:
    new_colors (Array[str]): 
    need_re_create (bool): 

Returns:
    bool:

<a id="unreal.RoadHeatMapEntityAtom.set_filter"></a>

#### set\_filter

```python
def set_filter(newfilter: Array[str]) -> bool
```

x.set_filter(newfilter) -> bool
Set Filter

Args:
    newfilter (Array[str]): 

Returns:
    bool:

<a id="unreal.RoadHeatMapEntityAtom.get_point_vector_by_point_entity_eid"></a>

#### get\_point\_vector\_by\_point\_entity\_eid

```python
def get_point_vector_by_point_entity_eid(
        point_entity_eid: str) -> Optional[Vector]
```

x.get_point_vector_by_point_entity_eid(point_entity_eid) -> Vector or None
UFUNCTION(BlueprintCallable, Category = "RoadHeatMapEntityAtom")
               bool Set_originalLocation(const TArray<FRoadHeatMapData_Atom>& NewDatas, bool NeedReCreate = false);

Args:
    point_entity_eid (str): 

Returns:
    Vector or None: 

    out_point (Vector):

<a id="unreal.SectionEntityAtom"></a>