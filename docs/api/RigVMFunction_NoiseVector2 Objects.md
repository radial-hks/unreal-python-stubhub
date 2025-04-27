## RigVMFunction_NoiseVector2 Objects

```python
class RigVMFunction_NoiseVector2(RigVMFunction_MathBase)
```

Generates a vector through a noise fluctuation process between a min and a max through speed

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_Noise.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``frequency`` (Vector):  [Read-Write]
- ``maximum`` (double):  [Read-Write]
- ``minimum`` (double):  [Read-Write]
- ``result`` (Vector):  [Read-Write]
- ``speed`` (Vector):  [Read-Write]
- ``value`` (Vector):  [Read-Write]

<a id="unreal.RigVMFunction_NoiseVector2.__init__"></a>

#### __init__

```python
def __init__(value: Vector = [0.000000, 0.000000, 0.000000],
             speed: Vector = [0.000000, 0.000000, 0.000000],
             frequency: Vector = [0.000000, 0.000000, 0.000000],
             minimum: float = 0.000000,
             maximum: float = 0.000000,
             result: Vector = [0.000000, 0.000000, 0.000000]) -> None
```

<a id="unreal.RigVMFunction_NoiseVector2.value"></a>

#### value

```python
@property
def value() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_NoiseVector2.value"></a>

#### value

```python
@value.setter
def value(value: Vector) -> None
```

<a id="unreal.RigVMFunction_NoiseVector2.speed"></a>

#### speed

```python
@property
def speed() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_NoiseVector2.speed"></a>

#### speed

```python
@speed.setter
def speed(value: Vector) -> None
```

<a id="unreal.RigVMFunction_NoiseVector2.frequency"></a>

#### frequency

```python
@property
def frequency() -> Vector
```

(Vector):  [Read-Write]

<a id="unreal.RigVMFunction_NoiseVector2.frequency"></a>

#### frequency

```python
@frequency.setter
def frequency(value: Vector) -> None
```

<a id="unreal.RigVMFunction_NoiseVector2.minimum"></a>

#### minimum

```python
@property
def minimum() -> float
```

(double):  [Read-Write]

<a id="unreal.RigVMFunction_NoiseVector2.minimum"></a>

#### minimum

```python
@minimum.setter
def minimum(value: float) -> None
```

<a id="unreal.RigVMFunction_NoiseVector2.maximum"></a>

#### maximum

```python
@property
def maximum() -> float
```

(double):  [Read-Write]

<a id="unreal.RigVMFunction_NoiseVector2.maximum"></a>

#### maximum

```python
@maximum.setter
def maximum(value: float) -> None
```

<a id="unreal.RigVMFunction_NoiseVector2.result"></a>

#### result

```python
@property
def result() -> Vector
```

(Vector):  [Read-Only]

<a id="unreal.RigUnit_NoiseVector2"></a>