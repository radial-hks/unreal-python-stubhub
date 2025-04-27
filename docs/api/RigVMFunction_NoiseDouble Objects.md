## RigVMFunction_NoiseDouble Objects

```python
class RigVMFunction_NoiseDouble(RigVMFunction_MathBase)
```

Generates a float through a noise fluctuation process between a min and a max through speed

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVM
- **File**: RigVMFunction_Noise.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``frequency`` (double):  [Read-Write]
- ``maximum`` (double):  [Read-Write]
- ``minimum`` (double):  [Read-Write]
- ``result`` (double):  [Read-Write]
- ``speed`` (double):  [Read-Write]
- ``value`` (double):  [Read-Write]

<a id="unreal.RigVMFunction_NoiseDouble.__init__"></a>

#### __init__

```python
def __init__(value: float = 0.000000,
             speed: float = 0.000000,
             frequency: float = 0.000000,
             minimum: float = 0.000000,
             maximum: float = 0.000000,
             result: float = 0.000000) -> None
```

<a id="unreal.RigVMFunction_NoiseDouble.value"></a>

#### value

```python
@property
def value() -> float
```

(double):  [Read-Write]

<a id="unreal.RigVMFunction_NoiseDouble.value"></a>

#### value

```python
@value.setter
def value(value: float) -> None
```

<a id="unreal.RigVMFunction_NoiseDouble.speed"></a>

#### speed

```python
@property
def speed() -> float
```

(double):  [Read-Write]

<a id="unreal.RigVMFunction_NoiseDouble.speed"></a>

#### speed

```python
@speed.setter
def speed(value: float) -> None
```

<a id="unreal.RigVMFunction_NoiseDouble.frequency"></a>

#### frequency

```python
@property
def frequency() -> float
```

(double):  [Read-Write]

<a id="unreal.RigVMFunction_NoiseDouble.frequency"></a>

#### frequency

```python
@frequency.setter
def frequency(value: float) -> None
```

<a id="unreal.RigVMFunction_NoiseDouble.minimum"></a>

#### minimum

```python
@property
def minimum() -> float
```

(double):  [Read-Write]

<a id="unreal.RigVMFunction_NoiseDouble.minimum"></a>

#### minimum

```python
@minimum.setter
def minimum(value: float) -> None
```

<a id="unreal.RigVMFunction_NoiseDouble.maximum"></a>

#### maximum

```python
@property
def maximum() -> float
```

(double):  [Read-Write]

<a id="unreal.RigVMFunction_NoiseDouble.maximum"></a>

#### maximum

```python
@maximum.setter
def maximum(value: float) -> None
```

<a id="unreal.RigVMFunction_NoiseDouble.result"></a>

#### result

```python
@property
def result() -> float
```

(double):  [Read-Only]

<a id="unreal.RigUnit_NoiseDouble"></a>