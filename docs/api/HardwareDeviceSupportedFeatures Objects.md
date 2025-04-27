## HardwareDeviceSupportedFeatures Objects

```python
class HardwareDeviceSupportedFeatures(EnumBase)
```

A bitmask of supported features that a hardware device has.

**C++ Source:**

- **Module**: Engine
- **File**: InputSettings.h

<a id="unreal.HardwareDeviceSupportedFeatures.UNSPECIFIED"></a>

#### UNSPECIFIED

0: A device that has not specified the type

<a id="unreal.HardwareDeviceSupportedFeatures.KEYPRESS"></a>

#### KEYPRESS

1: This device can support basic key presses

<a id="unreal.HardwareDeviceSupportedFeatures.POINTER"></a>

#### POINTER

2: This device can handle basic pointer behavior, such as a mouse

<a id="unreal.HardwareDeviceSupportedFeatures.GAMEPAD"></a>

#### GAMEPAD

4: This device has basic gamepad support

<a id="unreal.HardwareDeviceSupportedFeatures.TOUCH"></a>

#### TOUCH

8: This device supports touch in some capactiy (tablet, controller with a touch pad, etc)

<a id="unreal.HardwareDeviceSupportedFeatures.CAMERA"></a>

#### CAMERA

16: Does this device have a camera on it that we can access?

<a id="unreal.HardwareDeviceSupportedFeatures.MOTION_TRACKING"></a>

#### MOTION_TRACKING

32: Can this device track motion in a 3D space? (VR controllers, headset, etc)

<a id="unreal.HardwareDeviceSupportedFeatures.LIGHTS"></a>

#### LIGHTS

64: This hardware supports setting a light color (such as an LED light bar)

<a id="unreal.HardwareDeviceSupportedFeatures.TRIGGER_HAPTICS"></a>

#### TRIGGER_HAPTICS

128: Does this device have trigger haptics available?

<a id="unreal.HardwareDeviceSupportedFeatures.FORCE_FEEDBACK"></a>

#### FORCE_FEEDBACK

256: Flagged true if this device supports force feedback

<a id="unreal.HardwareDeviceSupportedFeatures.AUDIO_BASED_VIBRATIONS"></a>

#### AUDIO_BASED_VIBRATIONS

512: Does this device support vibrations sourced from an audio file?

<a id="unreal.HardwareDeviceSupportedFeatures.ACCELERATION"></a>

#### ACCELERATION

1024: This device can track acceleration in the users physical space

<a id="unreal.HardwareDeviceSupportedFeatures.VIRTUAL"></a>

#### VIRTUAL

2048: This is a virtual device simulating input, not a physical device

<a id="unreal.HardwareDeviceSupportedFeatures.MICROPHONE"></a>

#### MICROPHONE

4096: This device has a microphone on it that you can get audio from

<a id="unreal.HardwareDeviceSupportedFeatures.ORIENTATION"></a>

#### ORIENTATION

8192: This device can track the orientation in world space, such as a gyroscope

<a id="unreal.HardwareDeviceSupportedFeatures.GUITAR"></a>

#### GUITAR

16384: This device has the capabilities of a guitar (whammy bar, tilt, etc)

<a id="unreal.HardwareDeviceSupportedFeatures.DRUMS"></a>

#### DRUMS

32768: This device has the capabilities of drums (symbols, foot pedal, etc)

<a id="unreal.HardwareDeviceSupportedFeatures.CUSTOM_A"></a>

#### CUSTOM_A

16777216: Some custom flags that can be used in your game if you have custom hardware!

<a id="unreal.HardwareDeviceSupportedFeatures.CUSTOM_B"></a>

#### CUSTOM_B

33554432

<a id="unreal.HardwareDeviceSupportedFeatures.CUSTOM_C"></a>

#### CUSTOM_C

67108864

<a id="unreal.HardwareDeviceSupportedFeatures.CUSTOM_D"></a>

#### CUSTOM_D

134217728

<a id="unreal.HardwareDevicePrimaryType"></a>