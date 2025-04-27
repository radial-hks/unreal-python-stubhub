## SoundAttenuationSettings Objects

```python
class SoundAttenuationSettings(BaseAttenuationSettings)
```

The settings for attenuating.

**C++ Source:**

- **Module**: Engine
- **File**: SoundAttenuation.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``absorption_method`` (AirAbsorptionMethod):  [Read-Write] What method to use to map distance values to frequency absorption values.
- ``apply_normalization_to_stereo_sounds`` (bool):  [Read-Write] Enables applying a -6 dB attenuation to stereo assets which are 3d spatialized. Avoids clipping when assets have spread of 0.0 due to channel summing.
- ``attenuate`` (bool):  [Read-Write] Allows distance-based volume attenuation.
- ``attenuate_with_lpf`` (bool):  [Read-Write] Allows simulation of air absorption by applying a filter with a cutoff frequency as a function of distance.
- ``attenuation_shape`` (AttenuationShape):  [Read-Write] The shape of the non-custom attenuation method.
- ``attenuation_shape_extents`` (Vector):  [Read-Write] The dimensions to use for the attenuation shape. Interpretation of the values differ per shape.
           Sphere  - X is Sphere Radius. Y and Z are unused
           Capsule - X is Capsule Half Height, Y is Capsule Radius, Z is unused
           Box     - X, Y, and Z are the Box's dimensions
           Cone    - X is Cone Radius, Y is Cone Angle, Z is Cone Falloff Angle
- ``audio_link_settings_override`` (AudioLinkSettingsAbstract):  [Read-Write] AudioLink Setting Overrides
- ``binaural_radius`` (float):  [Read-Write] What min radius to use to swap to non-binaural audio when a sound starts playing.
- ``cone_offset`` (float):  [Read-Write] The distance back from the sound's origin to begin the cone when using the cone attenuation shape.
- ``cone_sphere_falloff_distance`` (float):  [Read-Write] The distance over which volume attenuation occurs for the optional sphere shape.
- ``cone_sphere_radius`` (float):  [Read-Write] An optional attenuation radius (sphere) that extends from the cone origin.
- ``custom_attenuation_curve`` (RuntimeFloatCurve):  [Read-Write] The custom volume attenuation curve to use.
- ``custom_highpass_air_absorption_curve`` (RuntimeFloatCurve):  [Read-Write] The normalized custom curve to use for the air absorption highpass frequency values. Does a mapping from defined distance values (x-axis) and defined frequency values (y-axis)
- ``custom_lowpass_air_absorption_curve`` (RuntimeFloatCurve):  [Read-Write] The normalized custom curve to use for the air absorption lowpass frequency values. Does a mapping from defined distance values (x-axis) and defined frequency values (y-axis)
- ``custom_priority_attenuation_curve`` (RuntimeFloatCurve):  [Read-Write] The custom curve to use for distance-based priority attenuation.
- ``custom_reverb_send_curve`` (RuntimeFloatCurve):  [Read-Write] The custom reverb send curve to use for distance-based send level.
- ``d_b_attenuation_at_max`` (float):  [Read-Write] The attenuation volume at the falloff distance in decibels (Only for 'Natural Sound' Distance Algorithm).
- ``distance_algorithm`` (AttenuationDistanceModel):  [Read-Write] The type of attenuation as a function of distance to use.
- ``enable_focus_interpolation`` (bool):  [Read-Write] Enables focus interpolation to smooth transition in and and of focus.
- ``enable_listener_focus`` (bool):  [Read-Write] Enable listener focus-based adjustments.
- ``enable_log_frequency_scaling`` (bool):  [Read-Write] Enables applying a log scale to frequency values (so frequency sweeping is perceptually linear).
- ``enable_occlusion`` (bool):  [Read-Write] Enables realtime occlusion tracing.
- ``enable_priority_attenuation`` (bool):  [Read-Write] Enables attenuation of sound priority based off distance.
- ``enable_reverb_send`` (bool):  [Read-Write] Enables adjusting reverb sends based on distance.
- ``enable_send_to_audio_link`` (bool):  [Read-Write] Enables/Disables AudioLink on all sources using this attenuation
- ``enable_source_data_override`` (bool):  [Read-Write] Enables overriding WaveInstance data using source data override plugin
- ``enable_submix_sends`` (bool):  [Read-Write] Enables submix sends based on distance.
- ``falloff_distance`` (float):  [Read-Write] The distance over which volume attenuation occurs.
- ``falloff_mode`` (NaturalSoundFalloffMode):  [Read-Write] Whether to continue attenuating, go silent, or hold last volume value when beyond falloff bounds and
  'Attenuation At Max (dB)' is set to a value greater than -60dB.
  (Only for 'Natural Sound' Distance Algorithm). */
- ``focus_attack_interp_speed`` (float):  [Read-Write] Scalar used to increase interpolation speed upwards to the target Focus value
- ``focus_azimuth`` (float):  [Read-Write] Azimuth angle (in degrees) relative to the listener forward vector which defines the focus region of sounds. Sounds playing at an angle less than this will be in focus.
- ``focus_distance_scale`` (float):  [Read-Write] Amount to scale the distance calculation of sounds that are in-focus. Can be used to make in-focus sounds appear to be closer or further away than they actually are.
- ``focus_priority_scale`` (float):  [Read-Write] Amount to scale the priority of sounds that are in focus. Can be used to boost the priority of sounds that are in focus.
- ``focus_release_interp_speed`` (float):  [Read-Write] Scalar used to increase interpolation speed downwards to the target Focus value
- ``focus_volume_attenuation`` (float):  [Read-Write] Amount to attenuate sounds that are in focus. Can be overridden at the sound-level.
- ``hpf_frequency_at_max`` (float):  [Read-Write] The range of the cutoff frequency (in Hz) of the highpass absorption filter.
- ``hpf_frequency_at_min`` (float):  [Read-Write] The range of the cutoff frequency (in Hz) of the highpass absorption filter.
- ``lpf_frequency_at_max`` (float):  [Read-Write] The range of the cutoff frequency (in Hz) of the lowpass absorption filter.
- ``lpf_frequency_at_min`` (float):  [Read-Write] The range of the cutoff frequency (in Hz) of the lowpass absorption filter.
- ``lpf_radius_max`` (float):  [Read-Write] The max distance range at which to apply an absorption LPF filter. Absorption freq cutoff interpolates between filter frequency ranges between these distance values.
- ``lpf_radius_min`` (float):  [Read-Write] The distance min range at which to apply an absorption LPF filter.
- ``manual_priority_attenuation`` (float):  [Read-Write] Static priority scalar to use (doesn't change as a function of distance).
- ``manual_reverb_send_level`` (float):  [Read-Write] The manual master reverb send level to use. Doesn't change as a function of distance.
- ``non_focus_azimuth`` (float):  [Read-Write] Azimuth angle (in degrees) relative to the listener forward vector which defines the non-focus region of sounds. Sounds playing at an angle greater than this will be out of focus.
- ``non_focus_distance_scale`` (float):  [Read-Write] Amount to scale the distance calculation of sounds that are not in-focus. Can be used to make in-focus sounds appear to be closer or further away than they actually are.
- ``non_focus_priority_scale`` (float):  [Read-Write] Amount to scale the priority of sounds that are not in-focus. Can be used to reduce the priority of sounds that are not in focus.
- ``non_focus_volume_attenuation`` (float):  [Read-Write] Amount to attenuate sounds that are not in focus. Can be overridden at the sound-level.
- ``non_spatialized_radius_end`` (float):  [Read-Write] The distance below which a sound is fully non-spatialized (2D). See "Non Spatialized Radius Start" to define the start of the interpolation and the "Non Spatialized Radius Mode" for the mode of the interpolation.
- ``non_spatialized_radius_mode`` (NonSpatializedRadiusSpeakerMapMode):  [Read-Write] Defines how to interpolate a 3D sound towards a 2D sound when using the non-spatialized radius start and end properties.
- ``non_spatialized_radius_start`` (float):  [Read-Write] The distance below which a sound begins to linearly interpolate towards being non-spatialized (2D). See "Non Spatialized Radius End" to define the end of the interpolation and the "Non Spatialized Radius Mode" for the mode of the interpolation. Note: this does not apply when using a 3rd party binaural plugin (audio will remain spatialized).
- ``occlusion_interpolation_time`` (float):  [Read-Write] The amount of time in seconds to interpolate to the target OcclusionLowPassFilterFrequency when a sound is occluded.
- ``occlusion_low_pass_filter_frequency`` (float):  [Read-Write] The low pass filter frequency (in Hz) to apply if the sound playing in this audio component is occluded. This will override the frequency set in LowPassFilterFrequency. A frequency of 0.0 is the device sample rate and will bypass the filter.
- ``occlusion_trace_channel`` (CollisionChannel):  [Read-Write] Which trace channel to use for audio occlusion checks.
- ``occlusion_volume_attenuation`` (float):  [Read-Write] The amount of volume attenuation to apply to sounds which are occluded.
- ``plugin_settings`` (SoundAttenuationPluginSettings):  [Read-Write] Sound attenuation plugin settings to use with sounds that play with this attenuation setting.
- ``priority_attenuation_distance_max`` (float):  [Read-Write] The max distance to attenuate priority.
- ``priority_attenuation_distance_min`` (float):  [Read-Write] The min distance to attenuate priority.
- ``priority_attenuation_max`` (float):  [Read-Write] Interpolated value to scale priority against when the sound is at the maximum priority attenuation distance from the closest listener.
- ``priority_attenuation_method`` (PriorityAttenuationMethod):  [Read-Write] What method to use to control priority attenuation
- ``priority_attenuation_min`` (float):  [Read-Write] Interpolated value to scale priority against when the sound is at the minimum priority attenuation distance from the closest listener.
- ``reverb_distance_max`` (float):  [Read-Write] The max distance to send to the master reverb.
- ``reverb_distance_min`` (float):  [Read-Write] The min distance to send to the master reverb.
- ``reverb_send_method`` (ReverbSendMethod):  [Read-Write] What method to use to control master reverb sends
- ``reverb_wet_level_max`` (float):  [Read-Write] The amount to send to master reverb when sound is located at a distance equal to value specified in the reverb max send distance.
- ``reverb_wet_level_min`` (float):  [Read-Write] The amount to send to master reverb when sound is located at a distance equal to value specified in the reverb min send distance.
- ``spatialization_algorithm`` (SoundSpatializationAlgorithm):  [Read-Write] What method we use to spatialize the sound.
- ``spatialize`` (bool):  [Read-Write] Allows the source to be 3D spatialized.
- ``stereo_spread`` (float):  [Read-Write] The world-space distance between left and right stereo channels when stereo assets are 3D spatialized.
- ``submix_send_settings`` (Array[AttenuationSubmixSendSettings]):  [Read-Write] Set of submix send settings to use to send audio to submixes as a function of distance.
- ``use_complex_collision_for_occlusion`` (bool):  [Read-Write] Enables tracing against complex collision when doing occlusion traces.

<a id="unreal.SoundAttenuationSettings.__init__"></a>

#### __init__

```python
def __init__(
    distance_algorithm: AttenuationDistanceModel = AttenuationDistanceModel.
    LINEAR,
    attenuation_shape: AttenuationShape = AttenuationShape.SPHERE,
    falloff_mode: NaturalSoundFalloffMode = NaturalSoundFalloffMode.CONTINUES,
    d_b_attenuation_at_max: float = 0.000000,
    attenuation_shape_extents: Vector = [0.000000, 0.000000, 0.000000],
    cone_offset: float = 0.000000,
    falloff_distance: float = 0.000000,
    cone_sphere_radius: float = 0.000000,
    cone_sphere_falloff_distance: float = 0.000000,
    custom_attenuation_curve: RuntimeFloatCurve = [],
    attenuate: bool = False,
    spatialize: bool = False,
    attenuate_with_lpf: bool = False,
    enable_listener_focus: bool = False,
    enable_focus_interpolation: bool = False,
    enable_occlusion: bool = False,
    use_complex_collision_for_occlusion: bool = False,
    enable_reverb_send: bool = False,
    enable_priority_attenuation: bool = False,
    apply_normalization_to_stereo_sounds: bool = False,
    enable_log_frequency_scaling: bool = False,
    enable_submix_sends: bool = False,
    enable_source_data_override: bool = False,
    enable_send_to_audio_link: bool = False,
    spatialization_algorithm:
    SoundSpatializationAlgorithm = SoundSpatializationAlgorithm.
    SPATIALIZATION_DEFAULT,
    audio_link_settings_override: AudioLinkSettingsAbstract = None,
    binaural_radius: float = 0.000000,
    custom_lowpass_air_absorption_curve: RuntimeFloatCurve = [],
    custom_highpass_air_absorption_curve: RuntimeFloatCurve = [],
    absorption_method: AirAbsorptionMethod = AirAbsorptionMethod.LINEAR,
    occlusion_trace_channel: CollisionChannel = CollisionChannel.
    ECC_WORLD_STATIC,
    reverb_send_method: ReverbSendMethod = ReverbSendMethod.LINEAR,
    priority_attenuation_method:
    PriorityAttenuationMethod = PriorityAttenuationMethod.LINEAR,
    non_spatialized_radius_start: float = 0.000000,
    non_spatialized_radius_end: float = 0.000000,
    non_spatialized_radius_mode:
    NonSpatializedRadiusSpeakerMapMode = NonSpatializedRadiusSpeakerMapMode.
    OMNI_DIRECTIONAL,
    stereo_spread: float = 0.000000,
    lpf_radius_min: float = 0.000000,
    lpf_radius_max: float = 0.000000,
    lpf_frequency_at_min: float = 0.000000,
    lpf_frequency_at_max: float = 0.000000,
    hpf_frequency_at_min: float = 0.000000,
    hpf_frequency_at_max: float = 0.000000,
    focus_azimuth: float = 0.000000,
    non_focus_azimuth: float = 0.000000,
    focus_distance_scale: float = 0.000000,
    non_focus_distance_scale: float = 0.000000,
    focus_priority_scale: float = 0.000000,
    non_focus_priority_scale: float = 0.000000,
    focus_volume_attenuation: float = 0.000000,
    non_focus_volume_attenuation: float = 0.000000,
    focus_attack_interp_speed: float = 0.000000,
    focus_release_interp_speed: float = 0.000000,
    occlusion_low_pass_filter_frequency: float = 0.000000,
    occlusion_volume_attenuation: float = 0.000000,
    occlusion_interpolation_time: float = 0.000000,
    reverb_wet_level_min: float = 0.000000,
    reverb_wet_level_max: float = 0.000000,
    reverb_distance_min: float = 0.000000,
    reverb_distance_max: float = 0.000000,
    manual_reverb_send_level: float = 0.000000,
    priority_attenuation_min: float = 0.000000,
    priority_attenuation_max: float = 0.000000,
    priority_attenuation_distance_min: float = 0.000000,
    priority_attenuation_distance_max: float = 0.000000,
    manual_priority_attenuation: float = 0.000000,
    custom_reverb_send_curve: RuntimeFloatCurve = [],
    submix_send_settings: Array[AttenuationSubmixSendSettings] = [],
    custom_priority_attenuation_curve: RuntimeFloatCurve = [],
    plugin_settings: SoundAttenuationPluginSettings = [[], [], [],
                                                       []]) -> None
```

<a id="unreal.SoundAttenuationSettings.attenuate"></a>

#### attenuate

```python
@property
def attenuate() -> bool
```

(bool):  [Read-Write] Allows distance-based volume attenuation.

<a id="unreal.SoundAttenuationSettings.attenuate"></a>

#### attenuate

```python
@attenuate.setter
def attenuate(value: bool) -> None
```

<a id="unreal.SoundAttenuationSettings.spatialize"></a>

#### spatialize

```python
@property
def spatialize() -> bool
```

(bool):  [Read-Write] Allows the source to be 3D spatialized.

<a id="unreal.SoundAttenuationSettings.spatialize"></a>

#### spatialize

```python
@spatialize.setter
def spatialize(value: bool) -> None
```

<a id="unreal.SoundAttenuationSettings.attenuate_with_lpf"></a>

#### attenuate_with_lpf

```python
@property
def attenuate_with_lpf() -> bool
```

(bool):  [Read-Write] Allows simulation of air absorption by applying a filter with a cutoff frequency as a function of distance.

<a id="unreal.SoundAttenuationSettings.attenuate_with_lpf"></a>

#### attenuate_with_lpf

```python
@attenuate_with_lpf.setter
def attenuate_with_lpf(value: bool) -> None
```

<a id="unreal.SoundAttenuationSettings.enable_listener_focus"></a>

#### enable_listener_focus

```python
@property
def enable_listener_focus() -> bool
```

(bool):  [Read-Write] Enable listener focus-based adjustments.

<a id="unreal.SoundAttenuationSettings.enable_listener_focus"></a>

#### enable_listener_focus

```python
@enable_listener_focus.setter
def enable_listener_focus(value: bool) -> None
```

<a id="unreal.SoundAttenuationSettings.enable_focus_interpolation"></a>

#### enable_focus_interpolation

```python
@property
def enable_focus_interpolation() -> bool
```

(bool):  [Read-Write] Enables focus interpolation to smooth transition in and and of focus.

<a id="unreal.SoundAttenuationSettings.enable_focus_interpolation"></a>

#### enable_focus_interpolation

```python
@enable_focus_interpolation.setter
def enable_focus_interpolation(value: bool) -> None
```

<a id="unreal.SoundAttenuationSettings.enable_occlusion"></a>

#### enable_occlusion

```python
@property
def enable_occlusion() -> bool
```

(bool):  [Read-Write] Enables realtime occlusion tracing.

<a id="unreal.SoundAttenuationSettings.enable_occlusion"></a>

#### enable_occlusion

```python
@enable_occlusion.setter
def enable_occlusion(value: bool) -> None
```

<a id="unreal.SoundAttenuationSettings.use_complex_collision_for_occlusion"></a>

#### use_complex_collision_for_occlusion

```python
@property
def use_complex_collision_for_occlusion() -> bool
```

(bool):  [Read-Write] Enables tracing against complex collision when doing occlusion traces.

<a id="unreal.SoundAttenuationSettings.use_complex_collision_for_occlusion"></a>

#### use_complex_collision_for_occlusion

```python
@use_complex_collision_for_occlusion.setter
def use_complex_collision_for_occlusion(value: bool) -> None
```

<a id="unreal.SoundAttenuationSettings.enable_reverb_send"></a>

#### enable_reverb_send

```python
@property
def enable_reverb_send() -> bool
```

(bool):  [Read-Write] Enables adjusting reverb sends based on distance.

<a id="unreal.SoundAttenuationSettings.enable_reverb_send"></a>

#### enable_reverb_send

```python
@enable_reverb_send.setter
def enable_reverb_send(value: bool) -> None
```

<a id="unreal.SoundAttenuationSettings.enable_priority_attenuation"></a>

#### enable_priority_attenuation

```python
@property
def enable_priority_attenuation() -> bool
```

(bool):  [Read-Write] Enables attenuation of sound priority based off distance.

<a id="unreal.SoundAttenuationSettings.enable_priority_attenuation"></a>

#### enable_priority_attenuation

```python
@enable_priority_attenuation.setter
def enable_priority_attenuation(value: bool) -> None
```

<a id="unreal.SoundAttenuationSettings.apply_normalization_to_stereo_sounds"></a>

#### apply_normalization_to_stereo_sounds

```python
@property
def apply_normalization_to_stereo_sounds() -> bool
```

(bool):  [Read-Write] Enables applying a -6 dB attenuation to stereo assets which are 3d spatialized. Avoids clipping when assets have spread of 0.0 due to channel summing.

<a id="unreal.SoundAttenuationSettings.apply_normalization_to_stereo_sounds"></a>

#### apply_normalization_to_stereo_sounds

```python
@apply_normalization_to_stereo_sounds.setter
def apply_normalization_to_stereo_sounds(value: bool) -> None
```

<a id="unreal.SoundAttenuationSettings.enable_log_frequency_scaling"></a>

#### enable_log_frequency_scaling

```python
@property
def enable_log_frequency_scaling() -> bool
```

(bool):  [Read-Write] Enables applying a log scale to frequency values (so frequency sweeping is perceptually linear).

<a id="unreal.SoundAttenuationSettings.enable_log_frequency_scaling"></a>

#### enable_log_frequency_scaling

```python
@enable_log_frequency_scaling.setter
def enable_log_frequency_scaling(value: bool) -> None
```

<a id="unreal.SoundAttenuationSettings.enable_submix_sends"></a>

#### enable_submix_sends

```python
@property
def enable_submix_sends() -> bool
```

(bool):  [Read-Write] Enables submix sends based on distance.

<a id="unreal.SoundAttenuationSettings.enable_submix_sends"></a>

#### enable_submix_sends

```python
@enable_submix_sends.setter
def enable_submix_sends(value: bool) -> None
```

<a id="unreal.SoundAttenuationSettings.enable_source_data_override"></a>

#### enable_source_data_override

```python
@property
def enable_source_data_override() -> bool
```

(bool):  [Read-Write] Enables overriding WaveInstance data using source data override plugin

<a id="unreal.SoundAttenuationSettings.enable_source_data_override"></a>

#### enable_source_data_override

```python
@enable_source_data_override.setter
def enable_source_data_override(value: bool) -> None
```

<a id="unreal.SoundAttenuationSettings.enable_send_to_audio_link"></a>

#### enable_send_to_audio_link

```python
@property
def enable_send_to_audio_link() -> bool
```

(bool):  [Read-Write] Enables/Disables AudioLink on all sources using this attenuation

<a id="unreal.SoundAttenuationSettings.enable_send_to_audio_link"></a>

#### enable_send_to_audio_link

```python
@enable_send_to_audio_link.setter
def enable_send_to_audio_link(value: bool) -> None
```

<a id="unreal.SoundAttenuationSettings.spatialization_algorithm"></a>

#### spatialization_algorithm

```python
@property
def spatialization_algorithm() -> SoundSpatializationAlgorithm
```

(SoundSpatializationAlgorithm):  [Read-Write] What method we use to spatialize the sound.

<a id="unreal.SoundAttenuationSettings.spatialization_algorithm"></a>

#### spatialization_algorithm

```python
@spatialization_algorithm.setter
def spatialization_algorithm(value: SoundSpatializationAlgorithm) -> None
```

<a id="unreal.SoundAttenuationSettings.audio_link_settings_override"></a>

#### audio_link_settings_override

```python
@property
def audio_link_settings_override() -> AudioLinkSettingsAbstract
```

(AudioLinkSettingsAbstract):  [Read-Write] AudioLink Setting Overrides

<a id="unreal.SoundAttenuationSettings.audio_link_settings_override"></a>

#### audio_link_settings_override

```python
@audio_link_settings_override.setter
def audio_link_settings_override(value: AudioLinkSettingsAbstract) -> None
```

<a id="unreal.SoundAttenuationSettings.binaural_radius"></a>

#### binaural_radius

```python
@property
def binaural_radius() -> float
```

(float):  [Read-Write] What min radius to use to swap to non-binaural audio when a sound starts playing.

<a id="unreal.SoundAttenuationSettings.binaural_radius"></a>

#### binaural_radius

```python
@binaural_radius.setter
def binaural_radius(value: float) -> None
```

<a id="unreal.SoundAttenuationSettings.custom_lowpass_air_absorption_curve"></a>

#### custom_lowpass_air_absorption_curve

```python
@property
def custom_lowpass_air_absorption_curve() -> RuntimeFloatCurve
```

(RuntimeFloatCurve):  [Read-Write] The normalized custom curve to use for the air absorption lowpass frequency values. Does a mapping from defined distance values (x-axis) and defined frequency values (y-axis)

<a id="unreal.SoundAttenuationSettings.custom_lowpass_air_absorption_curve"></a>

#### custom_lowpass_air_absorption_curve

```python
@custom_lowpass_air_absorption_curve.setter
def custom_lowpass_air_absorption_curve(value: RuntimeFloatCurve) -> None
```

<a id="unreal.SoundAttenuationSettings.custom_highpass_air_absorption_curve"></a>

#### custom_highpass_air_absorption_curve

```python
@property
def custom_highpass_air_absorption_curve() -> RuntimeFloatCurve
```

(RuntimeFloatCurve):  [Read-Write] The normalized custom curve to use for the air absorption highpass frequency values. Does a mapping from defined distance values (x-axis) and defined frequency values (y-axis)

<a id="unreal.SoundAttenuationSettings.custom_highpass_air_absorption_curve"></a>

#### custom_highpass_air_absorption_curve

```python
@custom_highpass_air_absorption_curve.setter
def custom_highpass_air_absorption_curve(value: RuntimeFloatCurve) -> None
```

<a id="unreal.SoundAttenuationSettings.absorption_method"></a>

#### absorption_method

```python
@property
def absorption_method() -> AirAbsorptionMethod
```

(AirAbsorptionMethod):  [Read-Write] What method to use to map distance values to frequency absorption values.

<a id="unreal.SoundAttenuationSettings.absorption_method"></a>

#### absorption_method

```python
@absorption_method.setter
def absorption_method(value: AirAbsorptionMethod) -> None
```

<a id="unreal.SoundAttenuationSettings.occlusion_trace_channel"></a>

#### occlusion_trace_channel

```python
@property
def occlusion_trace_channel() -> CollisionChannel
```

(CollisionChannel):  [Read-Write] Which trace channel to use for audio occlusion checks.

<a id="unreal.SoundAttenuationSettings.occlusion_trace_channel"></a>

#### occlusion_trace_channel

```python
@occlusion_trace_channel.setter
def occlusion_trace_channel(value: CollisionChannel) -> None
```

<a id="unreal.SoundAttenuationSettings.reverb_send_method"></a>

#### reverb_send_method

```python
@property
def reverb_send_method() -> ReverbSendMethod
```

(ReverbSendMethod):  [Read-Write] What method to use to control master reverb sends

<a id="unreal.SoundAttenuationSettings.reverb_send_method"></a>

#### reverb_send_method

```python
@reverb_send_method.setter
def reverb_send_method(value: ReverbSendMethod) -> None
```

<a id="unreal.SoundAttenuationSettings.priority_attenuation_method"></a>

#### priority_attenuation_method

```python
@property
def priority_attenuation_method() -> PriorityAttenuationMethod
```

(PriorityAttenuationMethod):  [Read-Write] What method to use to control priority attenuation

<a id="unreal.SoundAttenuationSettings.priority_attenuation_method"></a>

#### priority_attenuation_method

```python
@priority_attenuation_method.setter
def priority_attenuation_method(value: PriorityAttenuationMethod) -> None
```

<a id="unreal.SoundAttenuationSettings.non_spatialized_radius_start"></a>

#### non_spatialized_radius_start

```python
@property
def non_spatialized_radius_start() -> float
```

(float):  [Read-Write] The distance below which a sound begins to linearly interpolate towards being non-spatialized (2D). See "Non Spatialized Radius End" to define the end of the interpolation and the "Non Spatialized Radius Mode" for the mode of the interpolation. Note: this does not apply when using a 3rd party binaural plugin (audio will remain spatialized).

<a id="unreal.SoundAttenuationSettings.non_spatialized_radius_start"></a>

#### non_spatialized_radius_start

```python
@non_spatialized_radius_start.setter
def non_spatialized_radius_start(value: float) -> None
```

<a id="unreal.SoundAttenuationSettings.omni_radius"></a>

#### omni_radius

```python
@property
def omni_radius() -> float
```

deprecated: 'omni_radius' was renamed to 'non_spatialized_radius_start'.

<a id="unreal.SoundAttenuationSettings.omni_radius"></a>

#### omni_radius

```python
@omni_radius.setter
def omni_radius(value: float) -> None
```

<a id="unreal.SoundAttenuationSettings.non_spatialized_radius_end"></a>

#### non_spatialized_radius_end

```python
@property
def non_spatialized_radius_end() -> float
```

(float):  [Read-Write] The distance below which a sound is fully non-spatialized (2D). See "Non Spatialized Radius Start" to define the start of the interpolation and the "Non Spatialized Radius Mode" for the mode of the interpolation.

<a id="unreal.SoundAttenuationSettings.non_spatialized_radius_end"></a>

#### non_spatialized_radius_end

```python
@non_spatialized_radius_end.setter
def non_spatialized_radius_end(value: float) -> None
```

<a id="unreal.SoundAttenuationSettings.non_spatialized_radius_mode"></a>

#### non_spatialized_radius_mode

```python
@property
def non_spatialized_radius_mode() -> NonSpatializedRadiusSpeakerMapMode
```

(NonSpatializedRadiusSpeakerMapMode):  [Read-Write] Defines how to interpolate a 3D sound towards a 2D sound when using the non-spatialized radius start and end properties.

<a id="unreal.SoundAttenuationSettings.non_spatialized_radius_mode"></a>

#### non_spatialized_radius_mode

```python
@non_spatialized_radius_mode.setter
def non_spatialized_radius_mode(
        value: NonSpatializedRadiusSpeakerMapMode) -> None
```

<a id="unreal.SoundAttenuationSettings.stereo_spread"></a>

#### stereo_spread

```python
@property
def stereo_spread() -> float
```

(float):  [Read-Write] The world-space distance between left and right stereo channels when stereo assets are 3D spatialized.

<a id="unreal.SoundAttenuationSettings.stereo_spread"></a>

#### stereo_spread

```python
@stereo_spread.setter
def stereo_spread(value: float) -> None
```

<a id="unreal.SoundAttenuationSettings.lpf_radius_min"></a>

#### lpf_radius_min

```python
@property
def lpf_radius_min() -> float
```

(float):  [Read-Write] The distance min range at which to apply an absorption LPF filter.

<a id="unreal.SoundAttenuationSettings.lpf_radius_min"></a>

#### lpf_radius_min

```python
@lpf_radius_min.setter
def lpf_radius_min(value: float) -> None
```

<a id="unreal.SoundAttenuationSettings.lpf_radius_max"></a>

#### lpf_radius_max

```python
@property
def lpf_radius_max() -> float
```

(float):  [Read-Write] The max distance range at which to apply an absorption LPF filter. Absorption freq cutoff interpolates between filter frequency ranges between these distance values.

<a id="unreal.SoundAttenuationSettings.lpf_radius_max"></a>

#### lpf_radius_max

```python
@lpf_radius_max.setter
def lpf_radius_max(value: float) -> None
```

<a id="unreal.SoundAttenuationSettings.lpf_frequency_at_min"></a>

#### lpf_frequency_at_min

```python
@property
def lpf_frequency_at_min() -> float
```

(float):  [Read-Write] The range of the cutoff frequency (in Hz) of the lowpass absorption filter.

<a id="unreal.SoundAttenuationSettings.lpf_frequency_at_min"></a>

#### lpf_frequency_at_min

```python
@lpf_frequency_at_min.setter
def lpf_frequency_at_min(value: float) -> None
```

<a id="unreal.SoundAttenuationSettings.lpf_frequency_at_max"></a>

#### lpf_frequency_at_max

```python
@property
def lpf_frequency_at_max() -> float
```

(float):  [Read-Write] The range of the cutoff frequency (in Hz) of the lowpass absorption filter.

<a id="unreal.SoundAttenuationSettings.lpf_frequency_at_max"></a>

#### lpf_frequency_at_max

```python
@lpf_frequency_at_max.setter
def lpf_frequency_at_max(value: float) -> None
```

<a id="unreal.SoundAttenuationSettings.hpf_frequency_at_min"></a>

#### hpf_frequency_at_min

```python
@property
def hpf_frequency_at_min() -> float
```

(float):  [Read-Write] The range of the cutoff frequency (in Hz) of the highpass absorption filter.

<a id="unreal.SoundAttenuationSettings.hpf_frequency_at_min"></a>

#### hpf_frequency_at_min

```python
@hpf_frequency_at_min.setter
def hpf_frequency_at_min(value: float) -> None
```

<a id="unreal.SoundAttenuationSettings.hpf_frequency_at_max"></a>

#### hpf_frequency_at_max

```python
@property
def hpf_frequency_at_max() -> float
```

(float):  [Read-Write] The range of the cutoff frequency (in Hz) of the highpass absorption filter.

<a id="unreal.SoundAttenuationSettings.hpf_frequency_at_max"></a>

#### hpf_frequency_at_max

```python
@hpf_frequency_at_max.setter
def hpf_frequency_at_max(value: float) -> None
```

<a id="unreal.SoundAttenuationSettings.focus_azimuth"></a>

#### focus_azimuth

```python
@property
def focus_azimuth() -> float
```

(float):  [Read-Write] Azimuth angle (in degrees) relative to the listener forward vector which defines the focus region of sounds. Sounds playing at an angle less than this will be in focus.

<a id="unreal.SoundAttenuationSettings.focus_azimuth"></a>

#### focus_azimuth

```python
@focus_azimuth.setter
def focus_azimuth(value: float) -> None
```

<a id="unreal.SoundAttenuationSettings.non_focus_azimuth"></a>

#### non_focus_azimuth

```python
@property
def non_focus_azimuth() -> float
```

(float):  [Read-Write] Azimuth angle (in degrees) relative to the listener forward vector which defines the non-focus region of sounds. Sounds playing at an angle greater than this will be out of focus.

<a id="unreal.SoundAttenuationSettings.non_focus_azimuth"></a>

#### non_focus_azimuth

```python
@non_focus_azimuth.setter
def non_focus_azimuth(value: float) -> None
```

<a id="unreal.SoundAttenuationSettings.focus_distance_scale"></a>

#### focus_distance_scale

```python
@property
def focus_distance_scale() -> float
```

(float):  [Read-Write] Amount to scale the distance calculation of sounds that are in-focus. Can be used to make in-focus sounds appear to be closer or further away than they actually are.

<a id="unreal.SoundAttenuationSettings.focus_distance_scale"></a>

#### focus_distance_scale

```python
@focus_distance_scale.setter
def focus_distance_scale(value: float) -> None
```

<a id="unreal.SoundAttenuationSettings.non_focus_distance_scale"></a>

#### non_focus_distance_scale

```python
@property
def non_focus_distance_scale() -> float
```

(float):  [Read-Write] Amount to scale the distance calculation of sounds that are not in-focus. Can be used to make in-focus sounds appear to be closer or further away than they actually are.

<a id="unreal.SoundAttenuationSettings.non_focus_distance_scale"></a>

#### non_focus_distance_scale

```python
@non_focus_distance_scale.setter
def non_focus_distance_scale(value: float) -> None
```

<a id="unreal.SoundAttenuationSettings.focus_priority_scale"></a>

#### focus_priority_scale

```python
@property
def focus_priority_scale() -> float
```

(float):  [Read-Write] Amount to scale the priority of sounds that are in focus. Can be used to boost the priority of sounds that are in focus.

<a id="unreal.SoundAttenuationSettings.focus_priority_scale"></a>

#### focus_priority_scale

```python
@focus_priority_scale.setter
def focus_priority_scale(value: float) -> None
```

<a id="unreal.SoundAttenuationSettings.non_focus_priority_scale"></a>

#### non_focus_priority_scale

```python
@property
def non_focus_priority_scale() -> float
```

(float):  [Read-Write] Amount to scale the priority of sounds that are not in-focus. Can be used to reduce the priority of sounds that are not in focus.

<a id="unreal.SoundAttenuationSettings.non_focus_priority_scale"></a>

#### non_focus_priority_scale

```python
@non_focus_priority_scale.setter
def non_focus_priority_scale(value: float) -> None
```

<a id="unreal.SoundAttenuationSettings.focus_volume_attenuation"></a>

#### focus_volume_attenuation

```python
@property
def focus_volume_attenuation() -> float
```

(float):  [Read-Write] Amount to attenuate sounds that are in focus. Can be overridden at the sound-level.

<a id="unreal.SoundAttenuationSettings.focus_volume_attenuation"></a>

#### focus_volume_attenuation

```python
@focus_volume_attenuation.setter
def focus_volume_attenuation(value: float) -> None
```

<a id="unreal.SoundAttenuationSettings.non_focus_volume_attenuation"></a>

#### non_focus_volume_attenuation

```python
@property
def non_focus_volume_attenuation() -> float
```

(float):  [Read-Write] Amount to attenuate sounds that are not in focus. Can be overridden at the sound-level.

<a id="unreal.SoundAttenuationSettings.non_focus_volume_attenuation"></a>

#### non_focus_volume_attenuation

```python
@non_focus_volume_attenuation.setter
def non_focus_volume_attenuation(value: float) -> None
```

<a id="unreal.SoundAttenuationSettings.focus_attack_interp_speed"></a>

#### focus_attack_interp_speed

```python
@property
def focus_attack_interp_speed() -> float
```

(float):  [Read-Write] Scalar used to increase interpolation speed upwards to the target Focus value

<a id="unreal.SoundAttenuationSettings.focus_attack_interp_speed"></a>

#### focus_attack_interp_speed

```python
@focus_attack_interp_speed.setter
def focus_attack_interp_speed(value: float) -> None
```

<a id="unreal.SoundAttenuationSettings.focus_release_interp_speed"></a>

#### focus_release_interp_speed

```python
@property
def focus_release_interp_speed() -> float
```

(float):  [Read-Write] Scalar used to increase interpolation speed downwards to the target Focus value

<a id="unreal.SoundAttenuationSettings.focus_release_interp_speed"></a>

#### focus_release_interp_speed

```python
@focus_release_interp_speed.setter
def focus_release_interp_speed(value: float) -> None
```

<a id="unreal.SoundAttenuationSettings.occlusion_low_pass_filter_frequency"></a>

#### occlusion_low_pass_filter_frequency

```python
@property
def occlusion_low_pass_filter_frequency() -> float
```

(float):  [Read-Write] The low pass filter frequency (in Hz) to apply if the sound playing in this audio component is occluded. This will override the frequency set in LowPassFilterFrequency. A frequency of 0.0 is the device sample rate and will bypass the filter.

<a id="unreal.SoundAttenuationSettings.occlusion_low_pass_filter_frequency"></a>

#### occlusion_low_pass_filter_frequency

```python
@occlusion_low_pass_filter_frequency.setter
def occlusion_low_pass_filter_frequency(value: float) -> None
```

<a id="unreal.SoundAttenuationSettings.occlusion_volume_attenuation"></a>

#### occlusion_volume_attenuation

```python
@property
def occlusion_volume_attenuation() -> float
```

(float):  [Read-Write] The amount of volume attenuation to apply to sounds which are occluded.

<a id="unreal.SoundAttenuationSettings.occlusion_volume_attenuation"></a>

#### occlusion_volume_attenuation

```python
@occlusion_volume_attenuation.setter
def occlusion_volume_attenuation(value: float) -> None
```

<a id="unreal.SoundAttenuationSettings.occlusion_interpolation_time"></a>

#### occlusion_interpolation_time

```python
@property
def occlusion_interpolation_time() -> float
```

(float):  [Read-Write] The amount of time in seconds to interpolate to the target OcclusionLowPassFilterFrequency when a sound is occluded.

<a id="unreal.SoundAttenuationSettings.occlusion_interpolation_time"></a>

#### occlusion_interpolation_time

```python
@occlusion_interpolation_time.setter
def occlusion_interpolation_time(value: float) -> None
```

<a id="unreal.SoundAttenuationSettings.reverb_wet_level_min"></a>

#### reverb_wet_level_min

```python
@property
def reverb_wet_level_min() -> float
```

(float):  [Read-Write] The amount to send to master reverb when sound is located at a distance equal to value specified in the reverb min send distance.

<a id="unreal.SoundAttenuationSettings.reverb_wet_level_min"></a>

#### reverb_wet_level_min

```python
@reverb_wet_level_min.setter
def reverb_wet_level_min(value: float) -> None
```

<a id="unreal.SoundAttenuationSettings.reverb_wet_level_max"></a>

#### reverb_wet_level_max

```python
@property
def reverb_wet_level_max() -> float
```

(float):  [Read-Write] The amount to send to master reverb when sound is located at a distance equal to value specified in the reverb max send distance.

<a id="unreal.SoundAttenuationSettings.reverb_wet_level_max"></a>

#### reverb_wet_level_max

```python
@reverb_wet_level_max.setter
def reverb_wet_level_max(value: float) -> None
```

<a id="unreal.SoundAttenuationSettings.reverb_distance_min"></a>

#### reverb_distance_min

```python
@property
def reverb_distance_min() -> float
```

(float):  [Read-Write] The min distance to send to the master reverb.

<a id="unreal.SoundAttenuationSettings.reverb_distance_min"></a>

#### reverb_distance_min

```python
@reverb_distance_min.setter
def reverb_distance_min(value: float) -> None
```

<a id="unreal.SoundAttenuationSettings.reverb_distance_max"></a>

#### reverb_distance_max

```python
@property
def reverb_distance_max() -> float
```

(float):  [Read-Write] The max distance to send to the master reverb.

<a id="unreal.SoundAttenuationSettings.reverb_distance_max"></a>

#### reverb_distance_max

```python
@reverb_distance_max.setter
def reverb_distance_max(value: float) -> None
```

<a id="unreal.SoundAttenuationSettings.manual_reverb_send_level"></a>

#### manual_reverb_send_level

```python
@property
def manual_reverb_send_level() -> float
```

(float):  [Read-Write] The manual master reverb send level to use. Doesn't change as a function of distance.

<a id="unreal.SoundAttenuationSettings.manual_reverb_send_level"></a>

#### manual_reverb_send_level

```python
@manual_reverb_send_level.setter
def manual_reverb_send_level(value: float) -> None
```

<a id="unreal.SoundAttenuationSettings.priority_attenuation_min"></a>

#### priority_attenuation_min

```python
@property
def priority_attenuation_min() -> float
```

(float):  [Read-Write] Interpolated value to scale priority against when the sound is at the minimum priority attenuation distance from the closest listener.

<a id="unreal.SoundAttenuationSettings.priority_attenuation_min"></a>

#### priority_attenuation_min

```python
@priority_attenuation_min.setter
def priority_attenuation_min(value: float) -> None
```

<a id="unreal.SoundAttenuationSettings.priority_attenuation_max"></a>

#### priority_attenuation_max

```python
@property
def priority_attenuation_max() -> float
```

(float):  [Read-Write] Interpolated value to scale priority against when the sound is at the maximum priority attenuation distance from the closest listener.

<a id="unreal.SoundAttenuationSettings.priority_attenuation_max"></a>

#### priority_attenuation_max

```python
@priority_attenuation_max.setter
def priority_attenuation_max(value: float) -> None
```

<a id="unreal.SoundAttenuationSettings.priority_attenuation_distance_min"></a>

#### priority_attenuation_distance_min

```python
@property
def priority_attenuation_distance_min() -> float
```

(float):  [Read-Write] The min distance to attenuate priority.

<a id="unreal.SoundAttenuationSettings.priority_attenuation_distance_min"></a>

#### priority_attenuation_distance_min

```python
@priority_attenuation_distance_min.setter
def priority_attenuation_distance_min(value: float) -> None
```

<a id="unreal.SoundAttenuationSettings.priority_attenuation_distance_max"></a>

#### priority_attenuation_distance_max

```python
@property
def priority_attenuation_distance_max() -> float
```

(float):  [Read-Write] The max distance to attenuate priority.

<a id="unreal.SoundAttenuationSettings.priority_attenuation_distance_max"></a>

#### priority_attenuation_distance_max

```python
@priority_attenuation_distance_max.setter
def priority_attenuation_distance_max(value: float) -> None
```

<a id="unreal.SoundAttenuationSettings.manual_priority_attenuation"></a>

#### manual_priority_attenuation

```python
@property
def manual_priority_attenuation() -> float
```

(float):  [Read-Write] Static priority scalar to use (doesn't change as a function of distance).

<a id="unreal.SoundAttenuationSettings.manual_priority_attenuation"></a>

#### manual_priority_attenuation

```python
@manual_priority_attenuation.setter
def manual_priority_attenuation(value: float) -> None
```

<a id="unreal.SoundAttenuationSettings.custom_reverb_send_curve"></a>

#### custom_reverb_send_curve

```python
@property
def custom_reverb_send_curve() -> RuntimeFloatCurve
```

(RuntimeFloatCurve):  [Read-Write] The custom reverb send curve to use for distance-based send level.

<a id="unreal.SoundAttenuationSettings.custom_reverb_send_curve"></a>

#### custom_reverb_send_curve

```python
@custom_reverb_send_curve.setter
def custom_reverb_send_curve(value: RuntimeFloatCurve) -> None
```

<a id="unreal.SoundAttenuationSettings.submix_send_settings"></a>

#### submix_send_settings

```python
@property
def submix_send_settings() -> Array[AttenuationSubmixSendSettings]
```

(Array[AttenuationSubmixSendSettings]):  [Read-Write] Set of submix send settings to use to send audio to submixes as a function of distance.

<a id="unreal.SoundAttenuationSettings.submix_send_settings"></a>

#### submix_send_settings

```python
@submix_send_settings.setter
def submix_send_settings(value: Array[AttenuationSubmixSendSettings]) -> None
```

<a id="unreal.SoundAttenuationSettings.custom_priority_attenuation_curve"></a>

#### custom_priority_attenuation_curve

```python
@property
def custom_priority_attenuation_curve() -> RuntimeFloatCurve
```

(RuntimeFloatCurve):  [Read-Write] The custom curve to use for distance-based priority attenuation.

<a id="unreal.SoundAttenuationSettings.custom_priority_attenuation_curve"></a>

#### custom_priority_attenuation_curve

```python
@custom_priority_attenuation_curve.setter
def custom_priority_attenuation_curve(value: RuntimeFloatCurve) -> None
```

<a id="unreal.SoundAttenuationSettings.plugin_settings"></a>

#### plugin_settings

```python
@property
def plugin_settings() -> SoundAttenuationPluginSettings
```

(SoundAttenuationPluginSettings):  [Read-Write] Sound attenuation plugin settings to use with sounds that play with this attenuation setting.

<a id="unreal.SoundAttenuationSettings.plugin_settings"></a>

#### plugin_settings

```python
@plugin_settings.setter
def plugin_settings(value: SoundAttenuationPluginSettings) -> None
```

<a id="unreal.AttenuationSettings"></a>