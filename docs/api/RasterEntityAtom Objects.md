## RasterEntityAtom Objects

```python
class RasterEntityAtom(EntityAtomBase)
```

Raster Entity Atom

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIEntity
- **File**: RasterEntityAtom.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``gradient_setting`` (Array[str]):  [Read-Write]
- ``path`` (str):  [Read-Write] UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "RasterEntityAtom")
                 int CoordZRef = 0;
         UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "RasterEntityAtom")
                 double CoordZ = 0;
- ``type`` (str):  [Read-Write]

<a id="unreal.RasterEntityAtom.path"></a>

#### path

```python
@property
def path() -> str
```

(str):  [Read-Write] UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "RasterEntityAtom")
               int CoordZRef = 0;
       UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "RasterEntityAtom")
               double CoordZ = 0;

<a id="unreal.RasterEntityAtom.path"></a>

#### path

```python
@path.setter
def path(value: str) -> None
```

<a id="unreal.RasterEntityAtom.type"></a>

#### type

```python
@property
def type() -> str
```

(str):  [Read-Write]

<a id="unreal.RasterEntityAtom.type"></a>

#### type

```python
@type.setter
def type(value: str) -> None
```

<a id="unreal.RasterEntityAtom.gradient_setting"></a>

#### gradient\_setting

```python
@property
def gradient_setting() -> Array[str]
```

(Array[str]):  [Read-Write]

<a id="unreal.RasterEntityAtom.gradient_setting"></a>

#### gradient\_setting

```python
@gradient_setting.setter
def gradient_setting(value: Array[str]) -> None
```

<a id="unreal.RasterEntityAtom.set_type"></a>

#### set\_type

```python
def set_type(new_type: str, need_re_create: bool = False) -> bool
```

x.set_type(new_type, need_re_create=False) -> bool
Set Type

Args:
    new_type (str): 
    need_re_create (bool): 

Returns:
    bool:

<a id="unreal.RasterEntityAtom.set_path"></a>

#### set\_path

```python
def set_path(new_path: str) -> bool
```

x.set_path(new_path) -> bool
UFUNCTION(BlueprintCallable, Category = "RasterEntityAtom")
       bool Set_CoordZRef(const int& NewCoordZRef);
UFUNCTION(BlueprintCallable, Category = "RasterEntityAtom")
       bool SetCoordZ(const double& NewCoordZ);

Args:
    new_path (str): 

Returns:
    bool:

<a id="unreal.RasterEntityAtom.set_gradient_setting"></a>

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

<a id="unreal.RasterEntityAtom.get_point_vector_by_point_entity_eid"></a>

#### get\_point\_vector\_by\_point\_entity\_eid

```python
def get_point_vector_by_point_entity_eid(
        point_entity_eid: str) -> Optional[Vector]
```

x.get_point_vector_by_point_entity_eid(point_entity_eid) -> Vector or None
Get Point Vector by Point Entity Eid

Args:
    point_entity_eid (str): 

Returns:
    Vector or None: 

    out_point (Vector):

<a id="unreal.RealTimeVideoEntityAtom"></a>