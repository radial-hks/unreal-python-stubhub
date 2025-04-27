## CanvasIcon Objects

```python
class CanvasIcon(StructBase)
```

Holds texture information with UV coordinates as well.

**C++ Source:**

- **Module**: Engine
- **File**: Canvas.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``texture`` (Texture):  [Read-Write] Source texture
- ``u`` (float):  [Read-Write] UV coords
- ``ul`` (float):  [Read-Write]
- ``v`` (float):  [Read-Write]
- ``vl`` (float):  [Read-Write]

<a id="unreal.CanvasIcon.__init__"></a>

#### __init__

```python
def __init__(texture: Texture = None,
             u: float = 0.000000,
             v: float = 0.000000,
             ul: float = 0.000000,
             vl: float = 0.000000) -> None
```

<a id="unreal.CanvasIcon.texture"></a>

#### texture

```python
@property
def texture() -> Texture
```

(Texture):  [Read-Write] Source texture

<a id="unreal.CanvasIcon.texture"></a>

#### texture

```python
@texture.setter
def texture(value: Texture) -> None
```

<a id="unreal.CanvasIcon.u"></a>

#### u

```python
@property
def u() -> float
```

(float):  [Read-Write] UV coords

<a id="unreal.CanvasIcon.u"></a>

#### u

```python
@u.setter
def u(value: float) -> None
```

<a id="unreal.CanvasIcon.v"></a>

#### v

```python
@property
def v() -> float
```

(float):  [Read-Write]

<a id="unreal.CanvasIcon.v"></a>

#### v

```python
@v.setter
def v(value: float) -> None
```

<a id="unreal.CanvasIcon.ul"></a>

#### ul

```python
@property
def ul() -> float
```

(float):  [Read-Write]

<a id="unreal.CanvasIcon.ul"></a>

#### ul

```python
@ul.setter
def ul(value: float) -> None
```

<a id="unreal.CanvasIcon.vl"></a>

#### vl

```python
@property
def vl() -> float
```

(float):  [Read-Write]

<a id="unreal.CanvasIcon.vl"></a>

#### vl

```python
@vl.setter
def vl(value: float) -> None
```

<a id="unreal.InputActionKeyMapping"></a>