## SectionEntityAtom Objects

```python
class SectionEntityAtom(EntityAtomBase)
```

Section Entity Atom

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIEntity
- **File**: SectionEntityAtom.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``coord_z_ref`` (str):  [Read-Write]
- ``invert`` (bool):  [Read-Write]
- ``location`` (Vector):  [Read-Write]
- ``original_location`` (Vector):  [Read-Write]
- ``rotator`` (Rotator):  [Read-Write]
- ``scale3d`` (Vector):  [Read-Write]
- ``stroke_color`` (str):  [Read-Write]
- ``stroke_weight`` (float):  [Read-Write]

<a id="unreal.SectionEntityAtom.coord_z_ref"></a>

#### coord\_z\_ref

```python
@property
def coord_z_ref() -> str
```

(str):  [Read-Write]

<a id="unreal.SectionEntityAtom.coord_z_ref"></a>

#### coord\_z\_ref

```python
@coord_z_ref.setter
def coord_z_ref(value: str) -> None
```

<a id="unreal.SectionEntityAtom.original_location"></a>

#### original\_location

```python
@property
def original_location() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.SectionEntityAtom.original_location"></a>

#### original\_location

```python
@original_location.setter
def original_location(value: Vector) -> None
```

<a id="unreal.SectionEntityAtom.stroke_color"></a>

#### stroke\_color

```python
@property
def stroke_color() -> str
```

(str):  [Read-Write]

<a id="unreal.SectionEntityAtom.stroke_color"></a>

#### stroke\_color

```python
@stroke_color.setter
def stroke_color(value: str) -> None
```

<a id="unreal.SectionEntityAtom.stroke_weight"></a>

#### stroke\_weight

```python
@property
def stroke_weight() -> float
```

(float):  [Read-Write]

<a id="unreal.SectionEntityAtom.stroke_weight"></a>

#### stroke\_weight

```python
@stroke_weight.setter
def stroke_weight(value: float) -> None
```

<a id="unreal.SectionEntityAtom.invert"></a>

#### invert

```python
@property
def invert() -> bool
```

(bool):  [Read-Write]

<a id="unreal.SectionEntityAtom.invert"></a>

#### invert

```python
@invert.setter
def invert(value: bool) -> None
```

<a id="unreal.SectionEntityAtom.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.SectionEntityAtom.rotator"></a>

#### rotator

```python
@property
def rotator() -> Rotator
```

(Rotator):  [Read-Only]

<a id="unreal.SectionEntityAtom.scale3d"></a>

#### scale3d

```python
@property
def scale3d() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.SectionEntityAtom.set_stroke_weight"></a>

#### set\_stroke\_weight

```python
def set_stroke_weight(new_stroke_weight: float) -> bool
```

x.set_stroke_weight(new_stroke_weight) -> bool
Set Stroke Weight

Args:
    new_stroke_weight (float): 

Returns:
    bool:

<a id="unreal.SectionEntityAtom.set_stroke_color"></a>

#### set\_stroke\_color

```python
def set_stroke_color(new_stroke_color: str) -> bool
```

x.set_stroke_color(new_stroke_color) -> bool
UFUNCTION(BlueprintCallable, Category = "SectionEntityAtom")
               bool SetPointEntityEid(const FString& NewPointEntityEid);

Args:
    new_stroke_color (str): 

Returns:
    bool:

<a id="unreal.SectionEntityAtom.set_invert"></a>

#### set\_invert

```python
def set_invert(new_invert: bool) -> bool
```

x.set_invert(new_invert) -> bool
Set Invert

Args:
    new_invert (bool): 

Returns:
    bool:

<a id="unreal.SectionEntityAtom.set_coord_z_ref"></a>

#### set\_coord\_z\_ref

```python
def set_coord_z_ref(new_coord_z_ref: str) -> bool
```

x.set_coord_z_ref(new_coord_z_ref) -> bool
Set Coord ZRef

Args:
    new_coord_z_ref (str): 

Returns:
    bool:

<a id="unreal.SectionEntityAtom.get_point_vector_by_point_entity_eid"></a>

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

<a id="unreal.SectionTransformAtom"></a>