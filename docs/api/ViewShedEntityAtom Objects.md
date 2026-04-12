## ViewShedEntityAtom Objects

```python
class ViewShedEntityAtom(EntityAtomBase)
```

View Shed Entity Atom

**C++ Source:**

- **Plugin**: CoveringAPI
- **Module**: CoveringAPIEntity
- **File**: ViewShedEntityAtom.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``field_of_view`` (float):  [Read-Write]
- ``hidden_color`` (str):  [Read-Write]
- ``outline`` (bool):  [Read-Write]
- ``radius`` (float):  [Read-Write]
- ``visible_color`` (str):  [Read-Write] UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "ViewShedEntityAtom")
         int CoordZRef = 0;

<a id="unreal.ViewShedEntityAtom.visible_color"></a>

#### visible\_color

```python
@property
def visible_color() -> str
```

(str):  [Read-Write] UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "ViewShedEntityAtom")
       int CoordZRef = 0;

<a id="unreal.ViewShedEntityAtom.visible_color"></a>

#### visible\_color

```python
@visible_color.setter
def visible_color(value: str) -> None
```

<a id="unreal.ViewShedEntityAtom.hidden_color"></a>

#### hidden\_color

```python
@property
def hidden_color() -> str
```

(str):  [Read-Write]

<a id="unreal.ViewShedEntityAtom.hidden_color"></a>

#### hidden\_color

```python
@hidden_color.setter
def hidden_color(value: str) -> None
```

<a id="unreal.ViewShedEntityAtom.outline"></a>

#### outline

```python
@property
def outline() -> bool
```

(bool):  [Read-Write]

<a id="unreal.ViewShedEntityAtom.outline"></a>

#### outline

```python
@outline.setter
def outline(value: bool) -> None
```

<a id="unreal.ViewShedEntityAtom.field_of_view"></a>

#### field\_of\_view

```python
@property
def field_of_view() -> float
```

(float):  [Read-Write]

<a id="unreal.ViewShedEntityAtom.field_of_view"></a>

#### field\_of\_view

```python
@field_of_view.setter
def field_of_view(value: float) -> None
```

<a id="unreal.ViewShedEntityAtom.radius"></a>

#### radius

```python
@property
def radius() -> float
```

(float):  [Read-Write]

<a id="unreal.ViewShedEntityAtom.radius"></a>

#### radius

```python
@radius.setter
def radius(value: float) -> None
```

<a id="unreal.ViewShedEntityAtom.setvisible_color"></a>

#### setvisible\_color

```python
def setvisible_color(newvisible_color: str) -> bool
```

x.setvisible_color(newvisible_color) -> bool
UFUNCTION(BlueprintCallable, Category = "ViewShedEntityAtom")
               bool Set_CoordZRef(const int& NewCoordZRef);

Args:
    newvisible_color (str): 

Returns:
    bool:

<a id="unreal.ViewShedEntityAtom.setradius"></a>

#### setradius

```python
def setradius(newradius: float) -> bool
```

x.setradius(newradius) -> bool
Setradius

Args:
    newradius (float): 

Returns:
    bool:

<a id="unreal.ViewShedEntityAtom.setoutline"></a>

#### setoutline

```python
def setoutline(newoutline: bool) -> bool
```

x.setoutline(newoutline) -> bool
Setoutline

Args:
    newoutline (bool): 

Returns:
    bool:

<a id="unreal.ViewShedEntityAtom.sethidden_color"></a>

#### sethidden\_color

```python
def sethidden_color(newhidden_color: str) -> bool
```

x.sethidden_color(newhidden_color) -> bool
Sethidden Color

Args:
    newhidden_color (str): 

Returns:
    bool:

<a id="unreal.ViewShedEntityAtom.set_fov"></a>

#### set\_fov

```python
def set_fov(new_fov: float) -> bool
```

x.set_fov(new_fov) -> bool
Set FOV

Args:
    new_fov (float): 

Returns:
    bool:

<a id="unreal.WindowEntityAtom"></a>