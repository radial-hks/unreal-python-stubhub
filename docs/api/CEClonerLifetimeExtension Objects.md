## CEClonerLifetimeExtension Objects

```python
class CEClonerLifetimeExtension(CEClonerExtensionBase)
```

Extension dealing with clones lifetime options

**C++ Source:**

- **Plugin**: ClonerEffector
- **Module**: ClonerEffector
- **File**: CEClonerLifetimeExtension.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``lifetime_enabled`` (bool):  [Read-Write] Do we destroy the clones after a specific duration
- ``lifetime_max`` (float):  [Read-Write] Maximum lifetime for a clone
- ``lifetime_min`` (float):  [Read-Write] Minimum lifetime for a clone
- ``lifetime_scale_enabled`` (bool):  [Read-Write] Enable scale by lifetime

<a id="unreal.CEClonerLifetimeExtension.set_lifetime_scale_enabled"></a>

#### set_lifetime_scale_enabled

```python
def set_lifetime_scale_enabled(enabled: bool) -> None
```

x.set_lifetime_scale_enabled(enabled) -> None
Set Lifetime Scale Enabled

Args:
    enabled (bool):

<a id="unreal.CEClonerLifetimeExtension.set_lifetime_scale_curve"></a>

#### set_lifetime_scale_curve

```python
def set_lifetime_scale_curve(curve: CurveFloat) -> None
```

x.set_lifetime_scale_curve(curve) -> None
Set Lifetime Scale Curve

Args:
    curve (CurveFloat):

<a id="unreal.CEClonerLifetimeExtension.set_lifetime_min"></a>

#### set_lifetime_min

```python
def set_lifetime_min(min: float) -> None
```

x.set_lifetime_min(min) -> None
Set Lifetime Min

Args:
    min (float):

<a id="unreal.CEClonerLifetimeExtension.set_lifetime_max"></a>

#### set_lifetime_max

```python
def set_lifetime_max(max: float) -> None
```

x.set_lifetime_max(max) -> None
Set Lifetime Max

Args:
    max (float):

<a id="unreal.CEClonerLifetimeExtension.set_lifetime_enabled"></a>

#### set_lifetime_enabled

```python
def set_lifetime_enabled(enabled: bool) -> None
```

x.set_lifetime_enabled(enabled) -> None
Set Lifetime Enabled

Args:
    enabled (bool):

<a id="unreal.CEClonerLifetimeExtension.get_lifetime_scale_enabled"></a>

#### get_lifetime_scale_enabled

```python
def get_lifetime_scale_enabled() -> bool
```

x.get_lifetime_scale_enabled() -> bool
Get Lifetime Scale Enabled

Returns:
    bool:

<a id="unreal.CEClonerLifetimeExtension.get_lifetime_min"></a>

#### get_lifetime_min

```python
def get_lifetime_min() -> float
```

x.get_lifetime_min() -> float
Get Lifetime Min

Returns:
    float:

<a id="unreal.CEClonerLifetimeExtension.get_lifetime_max"></a>

#### get_lifetime_max

```python
def get_lifetime_max() -> float
```

x.get_lifetime_max() -> float
Get Lifetime Max

Returns:
    float:

<a id="unreal.CEClonerLifetimeExtension.get_lifetime_enabled"></a>

#### get_lifetime_enabled

```python
def get_lifetime_enabled() -> bool
```

x.get_lifetime_enabled() -> bool
Get Lifetime Enabled

Returns:
    bool:

<a id="unreal.CEClonerLineLayout"></a>