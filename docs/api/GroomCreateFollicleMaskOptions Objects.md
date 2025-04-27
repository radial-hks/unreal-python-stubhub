## GroomCreateFollicleMaskOptions Objects

```python
class GroomCreateFollicleMaskOptions(Object)
```

Groom Create Follicle Mask Options

**C++ Source:**

- **Plugin**: HairStrands
- **Module**: HairStrandsCore
- **File**: GroomCreateFollicleMaskOptions.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``grooms`` (Array[FollicleMaskOptions]):  [Read-Write] Grooms which will be use to create the follicle texture
- ``resolution`` (int32):  [Read-Write] Follicle mask texture resolution. The resolution will be rounded to the closest power of two.
- ``root_radius`` (int32):  [Read-Write] Size of the root in the follicle mask (in pixels)

<a id="unreal.GroomCreateFollicleMaskOptions.resolution"></a>

#### resolution

```python
@property
def resolution() -> int
```

(int32):  [Read-Write] Follicle mask texture resolution. The resolution will be rounded to the closest power of two.

<a id="unreal.GroomCreateFollicleMaskOptions.resolution"></a>

#### resolution

```python
@resolution.setter
def resolution(value: int) -> None
```

<a id="unreal.GroomCreateFollicleMaskOptions.root_radius"></a>

#### root_radius

```python
@property
def root_radius() -> int
```

(int32):  [Read-Write] Size of the root in the follicle mask (in pixels)

<a id="unreal.GroomCreateFollicleMaskOptions.root_radius"></a>

#### root_radius

```python
@root_radius.setter
def root_radius(value: int) -> None
```

<a id="unreal.GroomCreateFollicleMaskOptions.grooms"></a>

#### grooms

```python
@property
def grooms() -> Array[FollicleMaskOptions]
```

(Array[FollicleMaskOptions]):  [Read-Write] Grooms which will be use to create the follicle texture

<a id="unreal.GroomCreateFollicleMaskOptions.grooms"></a>

#### grooms

```python
@grooms.setter
def grooms(value: Array[FollicleMaskOptions]) -> None
```

<a id="unreal.GroomCreateStrandsTexturesOptions"></a>