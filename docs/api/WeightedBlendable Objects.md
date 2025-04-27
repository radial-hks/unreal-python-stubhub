## WeightedBlendable Objects

```python
class WeightedBlendable(StructBase)
```

Weighted Blendable

**C++ Source:**

- **Module**: Engine
- **File**: Scene.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``object`` (Object):  [Read-Write] should be of the IBlendableInterface* type but UProperties cannot express that
- ``weight`` (float):  [Read-Write] 0:no effect .. 1:full effect

<a id="unreal.WeightedBlendable.__init__"></a>

#### __init__

```python
def __init__(weight: float = 0.000000, object: Object = None) -> None
```

<a id="unreal.WeightedBlendable.weight"></a>

#### weight

```python
@property
def weight() -> float
```

(float):  [Read-Write] 0:no effect .. 1:full effect

<a id="unreal.WeightedBlendable.weight"></a>

#### weight

```python
@weight.setter
def weight(value: float) -> None
```

<a id="unreal.WeightedBlendable.object"></a>

#### object

```python
@property
def object() -> Object
```

(Object):  [Read-Write] should be of the IBlendableInterface* type but UProperties cannot express that

<a id="unreal.WeightedBlendable.object"></a>

#### object

```python
@object.setter
def object(value: Object) -> None
```

<a id="unreal.GameplayTagQuery"></a>