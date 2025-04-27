## PlayerMappableKeyProfileCreationArgs Objects

```python
class PlayerMappableKeyProfileCreationArgs(StructBase)
```

Arguments that can be used when creating a new mapping profile

**C++ Source:**

- **Plugin**: EnhancedInput
- **Module**: EnhancedInput
- **File**: EnhancedInputUserSettings.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``display_name`` (Text):  [Read-Write] The display name of this profile
- ``profile_identifier`` (GameplayTag):  [Read-Write] The uniqiue identifier that this profile should have
- ``profile_type`` (type(Class)):  [Read-Write]
- ``set_as_current_profile`` (bool):  [Read-Write]
- ``user_id`` (PlatformUserId):  [Read-Write] The user ID of the ULocalPlayer that this profile is associated with

<a id="unreal.PlayerMappableKeyProfileCreationArgs.__init__"></a>

#### __init__

```python
def __init__(profile_type: Class = None,
             profile_identifier: GameplayTag = ["None"],
             user_id: PlatformUserId = [],
             display_name: Text = "",
             set_as_current_profile: bool = False) -> None
```

<a id="unreal.PlayerMappableKeyProfileCreationArgs.profile_type"></a>

#### profile_type

```python
@property
def profile_type() -> Class
```

(type(Class)):  [Read-Write]

<a id="unreal.PlayerMappableKeyProfileCreationArgs.profile_type"></a>

#### profile_type

```python
@profile_type.setter
def profile_type(value: Class) -> None
```

<a id="unreal.PlayerMappableKeyProfileCreationArgs.profile_identifier"></a>

#### profile_identifier

```python
@property
def profile_identifier() -> GameplayTag
```

(GameplayTag):  [Read-Write] The uniqiue identifier that this profile should have

<a id="unreal.PlayerMappableKeyProfileCreationArgs.profile_identifier"></a>

#### profile_identifier

```python
@profile_identifier.setter
def profile_identifier(value: GameplayTag) -> None
```

<a id="unreal.PlayerMappableKeyProfileCreationArgs.user_id"></a>

#### user_id

```python
@property
def user_id() -> PlatformUserId
```

(PlatformUserId):  [Read-Write] The user ID of the ULocalPlayer that this profile is associated with

<a id="unreal.PlayerMappableKeyProfileCreationArgs.user_id"></a>

#### user_id

```python
@user_id.setter
def user_id(value: PlatformUserId) -> None
```

<a id="unreal.PlayerMappableKeyProfileCreationArgs.display_name"></a>

#### display_name

```python
@property
def display_name() -> Text
```

(Text):  [Read-Write] The display name of this profile

<a id="unreal.PlayerMappableKeyProfileCreationArgs.display_name"></a>

#### display_name

```python
@display_name.setter
def display_name(value: Text) -> None
```

<a id="unreal.PlayerMappableKeyProfileCreationArgs.set_as_current_profile"></a>

#### set_as_current_profile

```python
@property
def set_as_current_profile() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PlayerMappableKeyProfileCreationArgs.set_as_current_profile"></a>

#### set_as_current_profile

```python
@set_as_current_profile.setter
def set_as_current_profile(value: bool) -> None
```

<a id="unreal.GameplayTag"></a>