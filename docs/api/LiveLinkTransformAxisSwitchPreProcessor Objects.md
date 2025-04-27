## LiveLinkTransformAxisSwitchPreProcessor Objects

```python
class LiveLinkTransformAxisSwitchPreProcessor(LiveLinkFramePreProcessor)
```

Allows to switch any axis of an incoming transform with another axis.
note: For example the Z-Axis of an incoming transform can be set to the (optionally negated) Y-Axis of the transform in UE.
note: This implies that translation, rotation and scale will be affected by switching an axis.

**C++ Source:**

- **Plugin**: LiveLink
- **Module**: LiveLink
- **File**: LiveLinkAxisSwitchPreProcessor.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``front_axis`` (LiveLinkAxis):  [Read-Write]
- ``offset_orientation`` (Rotator):  [Read-Write]
- ``offset_position`` (Vector):  [Read-Write]
- ``orientation_axis_x`` (LiveLinkAxis):  [Read-Write]
  deprecated: Use FrontAxis, RightAxis, UpAxis instead
- ``orientation_axis_y`` (LiveLinkAxis):  [Read-Write]
  deprecated: Use FrontAxis, RightAxis, UpAxis instead
- ``orientation_axis_z`` (LiveLinkAxis):  [Read-Write]
  deprecated: Use FrontAxis, RightAxis, UpAxis instead
- ``right_axis`` (LiveLinkAxis):  [Read-Write]
- ``translation_axis_x`` (LiveLinkAxis):  [Read-Write]
  deprecated: Use FrontAxis, RightAxis, UpAxis instead
- ``translation_axis_y`` (LiveLinkAxis):  [Read-Write]
  deprecated: Use FrontAxis, RightAxis, UpAxis instead
- ``translation_axis_z`` (LiveLinkAxis):  [Read-Write]
  deprecated: Use FrontAxis, RightAxis, UpAxis instead
- ``up_axis`` (LiveLinkAxis):  [Read-Write]
- ``use_offset_orientation`` (bool):  [Read-Write]
- ``use_offset_position`` (bool):  [Read-Write]

<a id="unreal.LiveLinkTransformAxisSwitchPreProcessor.orientation_axis_x"></a>

#### orientation_axis_x

```python
@property
def orientation_axis_x() -> LiveLinkAxis
```

(LiveLinkAxis):  [Read-Write]
deprecated: Use FrontAxis, RightAxis, UpAxis instead

<a id="unreal.LiveLinkTransformAxisSwitchPreProcessor.orientation_axis_x"></a>

#### orientation_axis_x

```python
@orientation_axis_x.setter
def orientation_axis_x(value: LiveLinkAxis) -> None
```

<a id="unreal.LiveLinkTransformAxisSwitchPreProcessor.axis_x"></a>

#### axis_x

```python
@property
def axis_x() -> LiveLinkAxis
```

deprecated: 'axis_x' was renamed to 'orientation_axis_x'.

<a id="unreal.LiveLinkTransformAxisSwitchPreProcessor.axis_x"></a>

#### axis_x

```python
@axis_x.setter
def axis_x(value: LiveLinkAxis) -> None
```

<a id="unreal.LiveLinkTransformAxisSwitchPreProcessor.orientation_axis_y"></a>

#### orientation_axis_y

```python
@property
def orientation_axis_y() -> LiveLinkAxis
```

(LiveLinkAxis):  [Read-Write]
deprecated: Use FrontAxis, RightAxis, UpAxis instead

<a id="unreal.LiveLinkTransformAxisSwitchPreProcessor.orientation_axis_y"></a>

#### orientation_axis_y

```python
@orientation_axis_y.setter
def orientation_axis_y(value: LiveLinkAxis) -> None
```

<a id="unreal.LiveLinkTransformAxisSwitchPreProcessor.axis_y"></a>

#### axis_y

```python
@property
def axis_y() -> LiveLinkAxis
```

deprecated: 'axis_y' was renamed to 'orientation_axis_y'.

<a id="unreal.LiveLinkTransformAxisSwitchPreProcessor.axis_y"></a>

#### axis_y

```python
@axis_y.setter
def axis_y(value: LiveLinkAxis) -> None
```

<a id="unreal.LiveLinkTransformAxisSwitchPreProcessor.orientation_axis_z"></a>

#### orientation_axis_z

```python
@property
def orientation_axis_z() -> LiveLinkAxis
```

(LiveLinkAxis):  [Read-Write]
deprecated: Use FrontAxis, RightAxis, UpAxis instead

<a id="unreal.LiveLinkTransformAxisSwitchPreProcessor.orientation_axis_z"></a>

#### orientation_axis_z

```python
@orientation_axis_z.setter
def orientation_axis_z(value: LiveLinkAxis) -> None
```

<a id="unreal.LiveLinkTransformAxisSwitchPreProcessor.axis_z"></a>

#### axis_z

```python
@property
def axis_z() -> LiveLinkAxis
```

deprecated: 'axis_z' was renamed to 'orientation_axis_z'.

<a id="unreal.LiveLinkTransformAxisSwitchPreProcessor.axis_z"></a>

#### axis_z

```python
@axis_z.setter
def axis_z(value: LiveLinkAxis) -> None
```

<a id="unreal.LiveLinkTransformAxisSwitchPreProcessor.translation_axis_x"></a>

#### translation_axis_x

```python
@property
def translation_axis_x() -> LiveLinkAxis
```

(LiveLinkAxis):  [Read-Write]
deprecated: Use FrontAxis, RightAxis, UpAxis instead

<a id="unreal.LiveLinkTransformAxisSwitchPreProcessor.translation_axis_x"></a>

#### translation_axis_x

```python
@translation_axis_x.setter
def translation_axis_x(value: LiveLinkAxis) -> None
```

<a id="unreal.LiveLinkTransformAxisSwitchPreProcessor.translation_axis_y"></a>

#### translation_axis_y

```python
@property
def translation_axis_y() -> LiveLinkAxis
```

(LiveLinkAxis):  [Read-Write]
deprecated: Use FrontAxis, RightAxis, UpAxis instead

<a id="unreal.LiveLinkTransformAxisSwitchPreProcessor.translation_axis_y"></a>

#### translation_axis_y

```python
@translation_axis_y.setter
def translation_axis_y(value: LiveLinkAxis) -> None
```

<a id="unreal.LiveLinkTransformAxisSwitchPreProcessor.translation_axis_z"></a>

#### translation_axis_z

```python
@property
def translation_axis_z() -> LiveLinkAxis
```

(LiveLinkAxis):  [Read-Write]
deprecated: Use FrontAxis, RightAxis, UpAxis instead

<a id="unreal.LiveLinkTransformAxisSwitchPreProcessor.translation_axis_z"></a>

#### translation_axis_z

```python
@translation_axis_z.setter
def translation_axis_z(value: LiveLinkAxis) -> None
```

<a id="unreal.LiveLinkAxisSwitchPreProcessor"></a>