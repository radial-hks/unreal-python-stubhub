## AvaAnchorAlignment Objects

```python
class AvaAnchorAlignment(StructBase)
```

Specifies a set of anchor alignments, one for each 3D axis.

**C++ Source:**

- **Plugin**: Avalanche
- **Module**: Avalanche
- **File**: AvaDefs.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``depth`` (AvaDepthAlignment):  [Read-Write]
- ``horizontal`` (AvaHorizontalAlignment):  [Read-Write]
- ``vertical`` (AvaVerticalAlignment):  [Read-Write]

<a id="unreal.AvaAnchorAlignment.__init__"></a>

#### __init__

```python
def __init__(horizontal: AvaHorizontalAlignment = AvaHorizontalAlignment.LEFT,
             vertical: AvaVerticalAlignment = AvaVerticalAlignment.TOP,
             depth: AvaDepthAlignment = AvaDepthAlignment.FRONT) -> None
```

<a id="unreal.AvaAnchorAlignment.horizontal"></a>

#### horizontal

```python
@property
def horizontal() -> AvaHorizontalAlignment
```

(AvaHorizontalAlignment):  [Read-Write]

<a id="unreal.AvaAnchorAlignment.horizontal"></a>

#### horizontal

```python
@horizontal.setter
def horizontal(value: AvaHorizontalAlignment) -> None
```

<a id="unreal.AvaAnchorAlignment.vertical"></a>

#### vertical

```python
@property
def vertical() -> AvaVerticalAlignment
```

(AvaVerticalAlignment):  [Read-Write]

<a id="unreal.AvaAnchorAlignment.vertical"></a>

#### vertical

```python
@vertical.setter
def vertical(value: AvaVerticalAlignment) -> None
```

<a id="unreal.AvaAnchorAlignment.depth"></a>

#### depth

```python
@property
def depth() -> AvaDepthAlignment
```

(AvaDepthAlignment):  [Read-Write]

<a id="unreal.AvaAnchorAlignment.depth"></a>

#### depth

```python
@depth.setter
def depth(value: AvaDepthAlignment) -> None
```

<a id="unreal.AvaViewportQualitySettingsFeature"></a>