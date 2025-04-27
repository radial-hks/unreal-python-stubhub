## AnimationAttributeIdentifierExtensions Objects

```python
class AnimationAttributeIdentifierExtensions(BlueprintFunctionLibrary)
```

Script-exposed functionality for wrapping native functionality and constructing valid FAnimationAttributeIdentifier instances

**C++ Source:**

- **Module**: Engine
- **File**: AttributeIdentifier.h

<a id="unreal.AnimationAttributeIdentifierExtensions.is_valid"></a>

#### is_valid

```python
@classmethod
def is_valid(
    cls, identifier: AnimationAttributeIdentifier
) -> Optional[AnimationAttributeIdentifier]
```

X.is_valid(identifier) -> AnimationAttributeIdentifier or None


Args:
    identifier (AnimationAttributeIdentifier): 

Returns:
    AnimationAttributeIdentifier or None: Whether or not the Attribute Identifier is valid

    identifier (AnimationAttributeIdentifier):

<a id="unreal.AnimationAttributeIdentifierExtensions.create_attribute_identifier"></a>

#### create_attribute_identifier

```python
@classmethod
def create_attribute_identifier(
        cls,
        animation_asset: AnimationAsset,
        attribute_name: Name,
        bone_name: Name,
        attribute_type: ScriptStruct,
        validate_exists_on_asset: bool = False
) -> AnimationAttributeIdentifier
```

X.create_attribute_identifier(animation_asset, attribute_name, bone_name, attribute_type, validate_exists_on_asset=False) -> AnimationAttributeIdentifier
Constructs a valid FAnimationAttributeIdentifier instance. Ensuring that the underlying BoneName exists on the Skeleton for the provided AnimationAsset.

Args:
    animation_asset (AnimationAsset): Animation asset to retrieve Skeleton from
    attribute_name (Name): Name of the attribute
    bone_name (Name): Name of the bone this attribute should be attributed to
    attribute_type (ScriptStruct): Type of the underlying data (to-be) stored by this attribute
    validate_exists_on_asset (bool): Whether or not the attribute should exist on the AnimationAsset. False by default.

Returns:
    AnimationAttributeIdentifier: Valid FAnimationCurveIdentifier if the operation was successful

<a id="unreal.BlendProfile"></a>