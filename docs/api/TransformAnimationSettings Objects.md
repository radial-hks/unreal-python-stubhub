## TransformAnimationSettings Objects

```python
class TransformAnimationSettings(StructBase)
```

brief: BIM模型节点移动动画相关设置

**C++ Source:**

- **Plugin**: WdpAssetLoader
- **Module**: BimAssetLoader
- **File**: HierarchyMeshTypes.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``ease_in`` (bool):  [Read-Write]
- ``ease_out`` (bool):  [Read-Write]
- ``force_shortest_rotation_path`` (bool):  [Read-Write]
- ``over_time`` (float):  [Read-Write]
- ``target_relative_location`` (Vector):  [Read-Write]
- ``target_relative_rotation`` (Rotator):  [Read-Write]

<a id="unreal.TransformAnimationSettings.__init__"></a>

#### \_\_init\_\_

```python
def __init__(target_relative_location: Vector = [0.000000, 0.000000, 0.000000],
             target_relative_rotation: Rotator = [
                 0.000000, 0.000000, 0.000000
             ],
             ease_out: bool = False,
             ease_in: bool = False,
             over_time: float = 0.000000,
             force_shortest_rotation_path: bool = False) -> None
```

<a id="unreal.TransformAnimationSettings.target_relative_location"></a>

#### target\_relative\_location

```python
@property
def target_relative_location() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.TransformAnimationSettings.target_relative_location"></a>

#### target\_relative\_location

```python
@target_relative_location.setter
def target_relative_location(value: Vector) -> None
```

<a id="unreal.TransformAnimationSettings.target_relative_rotation"></a>

#### target\_relative\_rotation

```python
@property
def target_relative_rotation() -> Rotator
```

(Rotator):  [Read-Write]

<a id="unreal.TransformAnimationSettings.target_relative_rotation"></a>

#### target\_relative\_rotation

```python
@target_relative_rotation.setter
def target_relative_rotation(value: Rotator) -> None
```

<a id="unreal.TransformAnimationSettings.ease_out"></a>

#### ease\_out

```python
@property
def ease_out() -> bool
```

(bool):  [Read-Write]

<a id="unreal.TransformAnimationSettings.ease_out"></a>

#### ease\_out

```python
@ease_out.setter
def ease_out(value: bool) -> None
```

<a id="unreal.TransformAnimationSettings.ease_in"></a>

#### ease\_in

```python
@property
def ease_in() -> bool
```

(bool):  [Read-Write]

<a id="unreal.TransformAnimationSettings.ease_in"></a>

#### ease\_in

```python
@ease_in.setter
def ease_in(value: bool) -> None
```

<a id="unreal.TransformAnimationSettings.over_time"></a>

#### over\_time

```python
@property
def over_time() -> float
```

(float):  [Read-Write]

<a id="unreal.TransformAnimationSettings.over_time"></a>

#### over\_time

```python
@over_time.setter
def over_time(value: float) -> None
```

<a id="unreal.TransformAnimationSettings.force_shortest_rotation_path"></a>

#### force\_shortest\_rotation\_path

```python
@property
def force_shortest_rotation_path() -> bool
```

(bool):  [Read-Write]

<a id="unreal.TransformAnimationSettings.force_shortest_rotation_path"></a>

#### force\_shortest\_rotation\_path

```python
@force_shortest_rotation_path.setter
def force_shortest_rotation_path(value: bool) -> None
```

<a id="unreal.WdpLoadAssetByIdParams"></a>