## AnimationCurveIdentifierExtensions Objects

```python
class AnimationCurveIdentifierExtensions(BlueprintFunctionLibrary)
```

Script-exposed functionality for wrapping native functionality and constructing valid FAnimationCurveIdentifier instances

**C++ Source:**

- **Module**: Engine
- **File**: CurveIdentifier.h

<a id="unreal.AnimationCurveIdentifierExtensions.set_curve_identifier"></a>

#### set_curve_identifier

```python
@classmethod
def set_curve_identifier(
        cls, out_identifier: AnimationCurveIdentifier, name: Name,
        curve_type: RawCurveTrackTypes) -> AnimationCurveIdentifier
```

X.set_curve_identifier(out_identifier, name, curve_type) -> AnimationCurveIdentifier
Constructs a valid FAnimationCurveIdentifier instance.

Args:
    out_identifier (AnimationCurveIdentifier): The identifier to set up
    name (Name): Name of the curve to find or add
    curve_type (RawCurveTrackTypes): Type of the curve to find or add

Returns:
    AnimationCurveIdentifier: 

    out_identifier (AnimationCurveIdentifier): The identifier to set up

<a id="unreal.AnimationCurveIdentifierExtensions.is_valid"></a>

#### is_valid

```python
@classmethod
def is_valid(
    cls, identifier: AnimationCurveIdentifier
) -> Optional[AnimationCurveIdentifier]
```

X.is_valid(identifier) -> AnimationCurveIdentifier or None


Args:
    identifier (AnimationCurveIdentifier): 

Returns:
    AnimationCurveIdentifier or None: Whether or not the Curve Identifier is valid

    identifier (AnimationCurveIdentifier):

<a id="unreal.AnimationCurveIdentifierExtensions.get_type"></a>

#### get_type

```python
@classmethod
def get_type(
    cls, identifier: AnimationCurveIdentifier
) -> Tuple[RawCurveTrackTypes, AnimationCurveIdentifier]
```

X.get_type(identifier) -> (RawCurveTrackTypes, identifier=AnimationCurveIdentifier)


Args:
    identifier (AnimationCurveIdentifier): 

Returns:
    AnimationCurveIdentifier: The animation curve type for the curve represented by the Curve Identifier

    identifier (AnimationCurveIdentifier):

<a id="unreal.AnimationCurveIdentifierExtensions.get_transform_child_curve_identifier"></a>

#### get_transform_child_curve_identifier

```python
@classmethod
def get_transform_child_curve_identifier(
        cls, out_identifier: AnimationCurveIdentifier,
        channel: TransformCurveChannel,
        axis: VectorCurveChannel) -> Optional[AnimationCurveIdentifier]
```

X.get_transform_child_curve_identifier(out_identifier, channel, axis) -> AnimationCurveIdentifier or None
Converts a valid FAnimationCurveIdentifier instance with RCT_Transform curve type to target a child curve.

Args:
    out_identifier (AnimationCurveIdentifier): [out] Identifier to be converted
    channel (TransformCurveChannel): Channel to target
    axis (VectorCurveChannel): Axis within channel to target

Returns:
    AnimationCurveIdentifier or None: Valid FAnimationCurveIdentifier if the operation was successful

    out_identifier (AnimationCurveIdentifier): [out] Identifier to be converted

<a id="unreal.AnimationCurveIdentifierExtensions.get_name"></a>

#### get_name

```python
@classmethod
def get_name(
    cls, identifier: AnimationCurveIdentifier
) -> Tuple[Name, AnimationCurveIdentifier]
```

X.get_name(identifier) -> (Name, identifier=AnimationCurveIdentifier)


Args:
    identifier (AnimationCurveIdentifier): 

Returns:
    AnimationCurveIdentifier: The name used for displaying the Curve Identifier

    identifier (AnimationCurveIdentifier):

<a id="unreal.AnimationCurveIdentifierExtensions.get_curve_identifiers"></a>

#### get_curve_identifiers

```python
@classmethod
def get_curve_identifiers(
        cls, skeleton: Skeleton,
        curve_type: RawCurveTrackTypes) -> Array[AnimationCurveIdentifier]
```

X.get_curve_identifiers(skeleton, curve_type) -> Array[AnimationCurveIdentifier]
Retrieves all curve identifiers for a specific curve types from the provided Skeleton
deprecated: Curve identifiers are no longer retrievable globally from the skeleton, they are specified per-animation.

Args:
    skeleton (Skeleton): Skeleton from which to retrieve the curve identifiers
    curve_type (RawCurveTrackTypes): Type of the curve identifers to retrieve

Returns:
    Array[AnimationCurveIdentifier]: Array of FAnimationCurveIdentifier instances each representing a unique curve if the operation was successful, empyty array otherwise

<a id="unreal.AnimationCurveIdentifierExtensions.get_curve_identifier"></a>

#### get_curve_identifier

```python
@classmethod
def get_curve_identifier(
        cls, skeleton: Skeleton, name: Name,
        curve_type: RawCurveTrackTypes) -> AnimationCurveIdentifier
```

X.get_curve_identifier(skeleton, name, curve_type) -> AnimationCurveIdentifier
Get Curve Identifier
deprecated: Please use SetCurveIdentifier.

Args:
    skeleton (Skeleton): 
    name (Name): 
    curve_type (RawCurveTrackTypes): 

Returns:
    AnimationCurveIdentifier:

<a id="unreal.AnimationCurveIdentifierExtensions.find_curve_identifier"></a>

#### find_curve_identifier

```python
@classmethod
def find_curve_identifier(
        cls, skeleton: Skeleton, name: Name,
        curve_type: RawCurveTrackTypes) -> AnimationCurveIdentifier
```

X.find_curve_identifier(skeleton, name, curve_type) -> AnimationCurveIdentifier
Tries to construct a valid FAnimationCurveIdentifier instance. It tries to find the underlying SmartName on the provided Skeleton for the provided curve type.
deprecated: Curve identifiers are no longer retrievable globally from the skeleton, they are specified per-animation.

Args:
    skeleton (Skeleton): Skeleton on which to look for the curve name
    name (Name): Name of the curve to find
    curve_type (RawCurveTrackTypes): Type of the curve to find

Returns:
    AnimationCurveIdentifier: Valid FAnimationCurveIdentifier if the name exists on the skeleton and the operation was successful, invalid otherwise

<a id="unreal.CurveSourceInterface"></a>