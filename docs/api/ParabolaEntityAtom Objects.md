## ParabolaEntityAtom Objects

```python
class ParabolaEntityAtom(EntityAtomBase)
```

Parabola Entity Atom

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIEntity
- **File**: ParabolaEntityAtom.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``color`` (str):  [Read-Write]
- ``gather`` (bool):  [Read-Write]
- ``top_height`` (float):  [Read-Write]
- ``top_scale`` (float):  [Read-Write]
- ``type`` (str):  [Read-Write] UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "ParabolaEntityAtom")
                 FVector startOriginalLocation;
         UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "ParabolaEntityAtom")
                 FVector endOriginalLocation;
- ``width`` (float):  [Read-Write]

<a id="unreal.ParabolaEntityAtom.type"></a>

#### type

```python
@property
def type() -> str
```

(str):  [Read-Write] UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "ParabolaEntityAtom")
               FVector startOriginalLocation;
       UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "ParabolaEntityAtom")
               FVector endOriginalLocation;

<a id="unreal.ParabolaEntityAtom.type"></a>

#### type

```python
@type.setter
def type(value: str) -> None
```

<a id="unreal.ParabolaEntityAtom.top_height"></a>

#### top\_height

```python
@property
def top_height() -> float
```

(float):  [Read-Write]

<a id="unreal.ParabolaEntityAtom.top_height"></a>

#### top\_height

```python
@top_height.setter
def top_height(value: float) -> None
```

<a id="unreal.ParabolaEntityAtom.top_scale"></a>

#### top\_scale

```python
@property
def top_scale() -> float
```

(float):  [Read-Write]

<a id="unreal.ParabolaEntityAtom.top_scale"></a>

#### top\_scale

```python
@top_scale.setter
def top_scale(value: float) -> None
```

<a id="unreal.ParabolaEntityAtom.width"></a>

#### width

```python
@property
def width() -> float
```

(float):  [Read-Write]

<a id="unreal.ParabolaEntityAtom.width"></a>

#### width

```python
@width.setter
def width(value: float) -> None
```

<a id="unreal.ParabolaEntityAtom.color"></a>

#### color

```python
@property
def color() -> str
```

(str):  [Read-Write]

<a id="unreal.ParabolaEntityAtom.color"></a>

#### color

```python
@color.setter
def color(value: str) -> None
```

<a id="unreal.ParabolaEntityAtom.gather"></a>

#### gather

```python
@property
def gather() -> bool
```

(bool):  [Read-Write]

<a id="unreal.ParabolaEntityAtom.gather"></a>

#### gather

```python
@gather.setter
def gather(value: bool) -> None
```

<a id="unreal.ParabolaEntityAtom.set_width"></a>

#### set\_width

```python
def set_width(new_width: float, need_re_create: bool = False) -> bool
```

x.set_width(new_width, need_re_create=False) -> bool
Set Width

Args:
    new_width (float): 
    need_re_create (bool): 

Returns:
    bool:

<a id="unreal.ParabolaEntityAtom.set_type"></a>

#### set\_type

```python
def set_type(new_type: str) -> bool
```

x.set_type(new_type) -> bool
UFUNCTION(BlueprintCallable, Category = "ParabolaEntityAtom")
               bool SetstartOriginalLocation(const FVector& NewStartPoint);
       UFUNCTION(BlueprintCallable, Category = "ParabolaEntityAtom")
               bool SetendOriginalLocation(const FVector& NewEndPoint);

Args:
    new_type (str): 

Returns:
    bool:

<a id="unreal.ParabolaEntityAtom.set_top_scale"></a>

#### set\_top\_scale

```python
def set_top_scale(new_top_scale: float, need_re_create: bool = False) -> bool
```

x.set_top_scale(new_top_scale, need_re_create=False) -> bool
Set Top Scale

Args:
    new_top_scale (float): 
    need_re_create (bool): 

Returns:
    bool:

<a id="unreal.ParabolaEntityAtom.set_top_height"></a>

#### set\_top\_height

```python
def set_top_height(new_top_height: float,
                   need_re_create: bool = False) -> bool
```

x.set_top_height(new_top_height, need_re_create=False) -> bool
Set Top Height

Args:
    new_top_height (float): 
    need_re_create (bool): 

Returns:
    bool:

<a id="unreal.ParabolaEntityAtom.set_gather"></a>

#### set\_gather

```python
def set_gather(new_gather: bool, need_re_create: bool = False) -> bool
```

x.set_gather(new_gather, need_re_create=False) -> bool
Set Gather

Args:
    new_gather (bool): 
    need_re_create (bool): 

Returns:
    bool:

<a id="unreal.ParabolaEntityAtom.set_color"></a>

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

<a id="unreal.ParabolaEntityAtom.get_point_vector_by_point_entity_eid"></a>

#### get\_point\_vector\_by\_point\_entity\_eid

```python
def get_point_vector_by_point_entity_eid(
        point_entity_eid: str) -> Optional[Vector]
```

x.get_point_vector_by_point_entity_eid(point_entity_eid) -> Vector or None
UFUNCTION(BlueprintCallable, Category = "ParabolaEntityAtom")
               bool Set_CoordZRef(const int& NewCoordZRef);

Args:
    point_entity_eid (str): 

Returns:
    Vector or None: 

    out_point (Vector):

<a id="unreal.ParticleEntityAtom"></a>