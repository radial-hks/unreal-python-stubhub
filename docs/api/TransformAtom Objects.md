## TransformAtom Objects

```python
class TransformAtom(TransformAtomBase)
```

Transform Atom

**C++ Source:**

- **Plugin**: WdpDataModel
- **Module**: WdpBasicAtoms
- **File**: TransformAtom.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``location`` (Vector):  [Read-Write]
- ``pivot_offset`` (Vector):  [Read-Write]
- ``rotator`` (Rotator):  [Read-Write]
- ``scale3d`` (Vector):  [Read-Write]

<a id="unreal.TransformAtom.location"></a>

#### location

```python
@property
def location() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.TransformAtom.rotator"></a>

#### rotator

```python
@property
def rotator() -> Rotator
```

(Rotator):  [Read-Only]

<a id="unreal.TransformAtom.scale3d"></a>

#### scale3d

```python
@property
def scale3d() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.TransformAtom.pivot_offset"></a>

#### pivot\_offset

```python
@property
def pivot_offset() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.AssetAtom"></a>