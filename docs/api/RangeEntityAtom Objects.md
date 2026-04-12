## RangeEntityAtom Objects

```python
class RangeEntityAtom(EntityAtomBase)
```

Range Entity Atom

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIEntity
- **File**: RangeEntityAtom.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``blocked`` (bool):  [Read-Write]
- ``color`` (str):  [Read-Write]
- ``fill_area_color`` (str):  [Read-Write]
- ``fill_area_type`` (str):  [Read-Write]
- ``height`` (float):  [Read-Write]
- ``shape`` (str):  [Read-Write] UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "RangeEntityAtom")
                 int CoordZRef = 0;
         UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "RangeEntityAtom")
                 double CoordZ = 0;
- ``stroke_weight`` (float):  [Read-Write]
- ``type`` (str):  [Read-Write]

<a id="unreal.RangeEntityAtom.shape"></a>

#### shape

```python
@property
def shape() -> str
```

(str):  [Read-Write] UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "RangeEntityAtom")
               int CoordZRef = 0;
       UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "RangeEntityAtom")
               double CoordZ = 0;

<a id="unreal.RangeEntityAtom.shape"></a>

#### shape

```python
@shape.setter
def shape(value: str) -> None
```

<a id="unreal.RangeEntityAtom.type"></a>

#### type

```python
@property
def type() -> str
```

(str):  [Read-Write]

<a id="unreal.RangeEntityAtom.type"></a>

#### type

```python
@type.setter
def type(value: str) -> None
```

<a id="unreal.RangeEntityAtom.fill_area_type"></a>

#### fill\_area\_type

```python
@property
def fill_area_type() -> str
```

(str):  [Read-Write]

<a id="unreal.RangeEntityAtom.fill_area_type"></a>

#### fill\_area\_type

```python
@fill_area_type.setter
def fill_area_type(value: str) -> None
```

<a id="unreal.RangeEntityAtom.height"></a>

#### height

```python
@property
def height() -> float
```

(float):  [Read-Write]

<a id="unreal.RangeEntityAtom.height"></a>

#### height

```python
@height.setter
def height(value: float) -> None
```

<a id="unreal.RangeEntityAtom.stroke_weight"></a>

#### stroke\_weight

```python
@property
def stroke_weight() -> float
```

(float):  [Read-Write]

<a id="unreal.RangeEntityAtom.stroke_weight"></a>

#### stroke\_weight

```python
@stroke_weight.setter
def stroke_weight(value: float) -> None
```

<a id="unreal.RangeEntityAtom.color"></a>

#### color

```python
@property
def color() -> str
```

(str):  [Read-Write]

<a id="unreal.RangeEntityAtom.color"></a>

#### color

```python
@color.setter
def color(value: str) -> None
```

<a id="unreal.RangeEntityAtom.fill_area_color"></a>

#### fill\_area\_color

```python
@property
def fill_area_color() -> str
```

(str):  [Read-Write]

<a id="unreal.RangeEntityAtom.fill_area_color"></a>

#### fill\_area\_color

```python
@fill_area_color.setter
def fill_area_color(value: str) -> None
```

<a id="unreal.RangeEntityAtom.blocked"></a>

#### blocked

```python
@property
def blocked() -> bool
```

(bool):  [Read-Write]

<a id="unreal.RangeEntityAtom.blocked"></a>

#### blocked

```python
@blocked.setter
def blocked(value: bool) -> None
```

<a id="unreal.RangeEntityAtom.set_type"></a>

#### set\_type

```python
def set_type(new_type: str) -> bool
```

x.set_type(new_type) -> bool
UFUNCTION(BlueprintCallable, Category = "RangeEntityAtom")
               bool Set_CoordZRef(const int& NewCoordZRef);
       UFUNCTION(BlueprintCallable, Category = "PathEntityAtom")
               bool SetCoordZ(const double& NewCoordZ);

Args:
    new_type (str): 

Returns:
    bool:

<a id="unreal.RangeEntityAtom.set_stroke_weight"></a>

#### set\_stroke\_weight

```python
def set_stroke_weight(new_stroke_weight: float,
                      need_re_create: bool = False) -> bool
```

x.set_stroke_weight(new_stroke_weight, need_re_create=False) -> bool
Set Stroke Weight

Args:
    new_stroke_weight (float): 
    need_re_create (bool): 

Returns:
    bool:

<a id="unreal.RangeEntityAtom.set_height"></a>

#### set\_height

```python
def set_height(new_height: float) -> bool
```

x.set_height(new_height) -> bool
Set Height

Args:
    new_height (float): 

Returns:
    bool:

<a id="unreal.RangeEntityAtom.set_fill_area_type"></a>

#### set\_fill\_area\_type

```python
def set_fill_area_type(new_fill_area_type: str,
                       need_re_create: bool = False) -> bool
```

x.set_fill_area_type(new_fill_area_type, need_re_create=False) -> bool
Set Fill Area Type

Args:
    new_fill_area_type (str): 
    need_re_create (bool): 

Returns:
    bool:

<a id="unreal.RangeEntityAtom.set_color"></a>

#### set\_color

```python
def set_color(new_color: str, need_re_create: bool = False) -> bool
```

x.set_color(new_color, need_re_create=False) -> bool
Set Color

Args:
    new_color (str): 
    need_re_create (bool): 

Returns:
    bool:

<a id="unreal.RasterEntityAtom"></a>