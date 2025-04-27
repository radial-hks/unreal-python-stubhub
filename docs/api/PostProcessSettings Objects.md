## PostProcessSettings Objects

```python
class PostProcessSettings(StructBase)
```

To be able to use struct PostProcessSettings. // Each property consists of a bool to enable it (by default off),
// the variable declaration and further down the default value for it.
// The comment should include the meaning and usable range.

**C++ Source:**

- **Module**: Engine
- **File**: Scene.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``ambient_cubemap`` (TextureCube):  [Read-Write] The Ambient cubemap (Affects diffuse and specular shading), blends additively which if different from all other settings here
- ``ambient_cubemap_intensity`` (float):  [Read-Write] To scale the Ambient cubemap brightness
  >=0: off, 1(default), >1 brighter
- ``ambient_cubemap_tint`` (LinearColor):  [Read-Write] AmbientCubemap tint color
- ``ambient_occlusion_bias`` (float):  [Read-Write] >0, in unreal units, default (3.0) works well for flat surfaces but can reduce details
- ``ambient_occlusion_fade_distance`` (float):  [Read-Write] >0, in unreal units, at what distance the AO effect disppears in the distance (avoding artifacts and AO effects on huge object)
- ``ambient_occlusion_fade_radius`` (float):  [Read-Write] >0, in unreal units, how many units before AmbientOcclusionFadeOutDistance it starts fading out
- ``ambient_occlusion_intensity`` (float):  [Read-Write] 0..1 0=off/no ambient occlusion .. 1=strong ambient occlusion, defines how much it affects the non direct lighting after base pass
- ``ambient_occlusion_mip_blend`` (float):  [Read-Write] Affects the blend over the multiple mips (lower resolution versions) , 0:fully use full resolution, 1::fully use low resolution, around 0.6 seems to be a good value
- ``ambient_occlusion_mip_scale`` (float):  [Read-Write] Affects the radius AO radius scale over the multiple mips (lower resolution versions)
- ``ambient_occlusion_mip_threshold`` (float):  [Read-Write] to tweak the bilateral upsampling when using multiple mips (lower resolution versions)
- ``ambient_occlusion_power`` (float):  [Read-Write] >0, in unreal units, bigger values means even distant surfaces affect the ambient occlusion
- ``ambient_occlusion_quality`` (float):  [Read-Write] 0=lowest quality..100=maximum quality, only a few quality levels are implemented, no soft transition
- ``ambient_occlusion_radius`` (float):  [Read-Write] >0, in unreal units, bigger values means even distant surfaces affect the ambient occlusion
- ``ambient_occlusion_radius_in_ws`` (bool):  [Read-Write] true: AO radius is in world space units, false: AO radius is locked the view space in 400 units
- ``ambient_occlusion_static_fraction`` (float):  [Read-Write] 0..1 0=no effect on static lighting .. 1=AO affects the stat lighting, 0 is free meaning no extra rendering pass
- ``ambient_occlusion_temporal_blend_weight`` (float):  [Read-Write] How much to blend the current frame with previous frames when using GTAO with temporal accumulation
- ``auto_exposure_apply_physical_camera_exposure`` (bool):  [Read-Write] Only affects Manual exposure mode.
- ``auto_exposure_bias`` (float):  [Read-Write] Logarithmic adjustment for the exposure. Only used if a tonemapper is specified.
  0: no adjustment, -1:2x darker, -2:4x darker, 1:2x brighter, 2:4x brighter, ...
- ``auto_exposure_bias_curve`` (CurveFloat):  [Read-Write] Exposure compensation based on the scene EV100.
  Used to calibrate the final exposure differently depending on the average scene luminance.
  0: no adjustment, -1:2x darker, -2:4x darker, 1:2x brighter, 2:4x brighter, ...
- ``auto_exposure_high_percent`` (float):  [Read-Write] The eye adaptation will adapt to a value extracted from the luminance histogram of the scene color.
  The value is defined as having x percent below this brightness. Higher values give bright spots on the screen more priority
  but can lead to less stable results. Lower values give the medium and darker values more priority but might cause burn out of
  bright spots.
  >0, <100, good values are in the range 80 .. 95
- ``auto_exposure_low_percent`` (float):  [Read-Write] The eye adaptation will adapt to a value extracted from the luminance histogram of the scene color.
  The value is defined as having x percent below this brightness. Higher values give bright spots on the screen more priority
  but can lead to less stable results. Lower values give the medium and darker values more priority but might cause burn out of
  bright spots.
  >0, <100, good values are in the range 70 .. 80
- ``auto_exposure_max_brightness`` (float):  [Read-Write] Auto-Exposure maximum adaptation. Eye Adaptation is disabled if Min = Max.
  Auto-exposure is implemented by choosing an exposure value for which the average luminance generates a pixel brightness equal to the Constant Calibration value.
  The Min/Max are expressed in pixel luminance (cd/m2) or in EV100 when using ExtendDefaultLuminanceRange (see project settings).
- ``auto_exposure_meter_mask`` (Texture):  [Read-Write] Exposure metering mask. Bright spots on the mask will have high influence on auto-exposure metering
  and dark spots will have low influence.
- ``auto_exposure_method`` (AutoExposureMethod):  [Read-Write] Luminance computation method
- ``auto_exposure_min_brightness`` (float):  [Read-Write] Auto-Exposure minimum adaptation. Eye Adaptation is disabled if Min = Max.
  Auto-exposure is implemented by choosing an exposure value for which the average luminance generates a pixel brightness equal to the Constant Calibration value.
  The Min/Max are expressed in pixel luminance (cd/m2) or in EV100 when using ExtendDefaultLuminanceRange (see project settings).
- ``auto_exposure_speed_down`` (float):  [Read-Write] In F-stops per second, should be >0
- ``auto_exposure_speed_up`` (float):  [Read-Write] In F-stops per second, should be >0
- ``bloom1_size`` (float):  [Read-Write] Diameter size for the Bloom1 in percent of the screen width
  (is done in 1/2 resolution, larger values cost more performance, good for high frequency details)
  >=0: can be clamped because of shader limitations
- ``bloom1_tint`` (LinearColor):  [Read-Write] Bloom1 tint color
- ``bloom2_size`` (float):  [Read-Write] Diameter size for Bloom2 in percent of the screen width
  (is done in 1/4 resolution, larger values cost more performance)
  >=0: can be clamped because of shader limitations
- ``bloom2_tint`` (LinearColor):  [Read-Write] Bloom2 tint color
- ``bloom3_size`` (float):  [Read-Write] Diameter size for Bloom3 in percent of the screen width
  (is done in 1/8 resolution, larger values cost more performance)
  >=0: can be clamped because of shader limitations
- ``bloom3_tint`` (LinearColor):  [Read-Write] Bloom3 tint color
- ``bloom4_size`` (float):  [Read-Write] Diameter size for Bloom4 in percent of the screen width
  (is done in 1/16 resolution, larger values cost more performance, best for wide contributions)
  >=0: can be clamped because of shader limitations
- ``bloom4_tint`` (LinearColor):  [Read-Write] Bloom4 tint color
- ``bloom5_size`` (float):  [Read-Write] Diameter size for Bloom5 in percent of the screen width
  (is done in 1/32 resolution, larger values cost more performance, best for wide contributions)
  >=0: can be clamped because of shader limitations
- ``bloom5_tint`` (LinearColor):  [Read-Write] Bloom5 tint color
- ``bloom6_size`` (float):  [Read-Write] Diameter size for Bloom6 in percent of the screen width
  (is done in 1/64 resolution, larger values cost more performance, best for wide contributions)
  >=0: can be clamped because of shader limitations
- ``bloom6_tint`` (LinearColor):  [Read-Write] Bloom6 tint color
- ``bloom_convolution_buffer_scale`` (float):  [Read-Write] Implicit buffer region as a fraction of the screen size to insure the bloom does not wrap across the screen.  Larger sizes have perf impact.
- ``bloom_convolution_center_uv`` (Vector2D):  [Read-Write] The UV location of the center of the kernel.  Should be very close to (.5,.5)
- ``bloom_convolution_pre_filter_max`` (float):  [Read-Write] Boost intensity of select pixels  prior to computing bloom convolution (Min, Max, Multiplier).  Max < Min disables
- ``bloom_convolution_pre_filter_min`` (float):  [Read-Write] Boost intensity of select pixels  prior to computing bloom convolution (Min, Max, Multiplier).  Max < Min disables
- ``bloom_convolution_pre_filter_mult`` (float):  [Read-Write] Boost intensity of select pixels  prior to computing bloom convolution (Min, Max, Multiplier).  Max < Min disables
- ``bloom_convolution_scatter_dispersion`` (float):  [Read-Write] Intensity multiplier on the scatter dispersion energy of the kernel. 1.0 means exactly use the same energy as the kernel scatter dispersion.
- ``bloom_convolution_size`` (float):  [Read-Write] Relative size of the convolution kernel image compared to the minor axis of the viewport
- ``bloom_convolution_texture`` (Texture2D):  [Read-Write] Texture to replace default convolution bloom kernel
- ``bloom_dirt_mask`` (Texture):  [Read-Write] Texture that defines the dirt on the camera lens where the light of very bright objects is scattered.
- ``bloom_dirt_mask_intensity`` (float):  [Read-Write] BloomDirtMask intensity
- ``bloom_dirt_mask_tint`` (LinearColor):  [Read-Write] BloomDirtMask tint color
- ``bloom_intensity`` (float):  [Read-Write] Multiplier for all bloom contributions >=0: off, 1(default), >1 brighter
- ``bloom_method`` (BloomMethod):  [Read-Write] Bloom algorithm
- ``bloom_size_scale`` (float):  [Read-Write] Scale for all bloom sizes
- ``bloom_threshold`` (float):  [Read-Write] minimum brightness the bloom starts having effect
  -1:all pixels affect bloom equally (physically correct, faster as a threshold pass is omitted), 0:all pixels affect bloom brights more, 1(default), >1 brighter
- ``blue_correction`` (float):  [Read-Write] Correct for artifacts with "electric" blues due to the ACEScg color space. Bright blue desaturates instead of going to violet.
- ``camera_iso`` (float):  [Read-Write] The camera sensor sensitivity
- ``camera_shutter_speed`` (float):  [Read-Write] The camera shutter in seconds.
- ``chromatic_aberration_start_offset`` (float):  [Read-Write] A normalized distance to the center of the framebuffer where the effect takes place.
- ``color_contrast`` (Vector4):  [Read-Write] Control the range of light and dark values in your scene. Lower values will reduce the difference between bright and dark areas while higher values will increase the difference between the bright and dark areas.
- ``color_contrast_highlights`` (Vector4):  [Read-Write] Control the range of light and dark values in the highlights region. Lower values will reduce the difference between bright and dark areas while higher values will increase the difference between the bright and dark areas.
- ``color_contrast_midtones`` (Vector4):  [Read-Write] Control the range of light and dark values in the mid-tone region. Lower values will reduce the difference between bright and dark areas while higher values will increase the difference between the bright and dark areas.
- ``color_contrast_shadows`` (Vector4):  [Read-Write] Control the range of light and dark values in your scene. Lower values will reduce the difference between bright and dark areas while higher values will increase the difference between the bright and dark areas.
- ``color_correction_highlights_max`` (float):  [Read-Write] This value sets the upper threshold for what is considered to be the highlight region of the image.  This value should be larger than HighlightsMin. Default is 1.0, for backwards compatibility
- ``color_correction_highlights_min`` (float):  [Read-Write] This value sets the lower threshold for what is considered to be the highlight region of the image.
- ``color_correction_shadows_max`` (float):  [Read-Write] This value sets the threshold for what is considered to be the shadow region of the image.
- ``color_gain`` (Vector4):  [Read-Write] This value multiplies the colors of the image.  Raising or lowering this value will result in brightening or darkening the entire scene.
- ``color_gain_highlights`` (Vector4):  [Read-Write] This value multiplies the colors in the highlight region.  Raising or lowering this value will result in brightening or darkening the affected region.
- ``color_gain_midtones`` (Vector4):  [Read-Write] This value multiplies the colors in the mid-tone region of the image.  Raising or lowering this value will result in brightening or darkening the affected region.
- ``color_gain_shadows`` (Vector4):  [Read-Write] This value multiplies the colors in the shadow region.  Raising or lowering this value will result in brightening or darkening the affected region.
- ``color_gamma`` (Vector4):  [Read-Write] Control the luminance curve of the scene. Raising or lowering this value will result brightening or darkening the mid-tones of the entire image.
- ``color_gamma_highlights`` (Vector4):  [Read-Write] Control the luminance curve of the highlight region. Raising or lowering this value will result brightening or darkening the mid-tones of the highlight region.
- ``color_gamma_midtones`` (Vector4):  [Read-Write] Control the luminance curve of the mid-tone region of the image. Raising or lowering this value will result brightening or darkening the mid-tones of the image.
- ``color_gamma_shadows`` (Vector4):  [Read-Write] Control the luminance curve of the shadow region. Raising or lowering this value will result brightening or darkening the mid-tones of the shadow region.
- ``color_grading_intensity`` (float):  [Read-Write] Color grading lookup table intensity. 0 = no intensity, 1=full intensity
- ``color_grading_lut`` (Texture):  [Read-Write] Look up table texture to use or none of not used
- ``color_offset`` (Vector4):  [Read-Write] This value is added to the colors of the scene.  Raising or lowering this value will result in the image being more or less washed-out.
- ``color_offset_highlights`` (Vector4):  [Read-Write] This value is added to the colors in the highlight region.  Raising or lowering this value will result in the highlights being more or less washed-out.
- ``color_offset_midtones`` (Vector4):  [Read-Write] This value is added to the colors in the mid-tone region of the image.  Raising or lowering this value will result in the mid-tones being more or less washed-out.
- ``color_offset_shadows`` (Vector4):  [Read-Write] This value is added to the colors in the shadow region.  Raising or lowering this value will result in the shadows being more or less washed-out.
- ``color_saturation`` (Vector4):  [Read-Write] Control the intensity of the color(hue) for the entire image.Higher values will result in more vibrant colors.
- ``color_saturation_highlights`` (Vector4):  [Read-Write] Control the intensity of the color (hue) for the highlights region of the image.  Higher values will result in more vibrant colors.
- ``color_saturation_midtones`` (Vector4):  [Read-Write] Control the intensity of the colors (hue) in the mid-tone region of the image.  Higher values will result in more vibrant colors.
- ``color_saturation_shadows`` (Vector4):  [Read-Write] Control the intensity of the colors (hue) in the shadow region of the image.  Higher values will result in more vibrant colors.
- ``depth_of_field_blade_count`` (int32):  [Read-Write] Defines the number of blades of the diaphragm within the lens (between 4 and 16).
- ``depth_of_field_depth_blur_amount`` (float):  [Read-Write] CircleDOF only: Depth blur km for 50%
- ``depth_of_field_depth_blur_radius`` (float):  [Read-Write] CircleDOF only: Depth blur radius in pixels at 1920x
- ``depth_of_field_far_blur_size`` (float):  [Read-Write] Gaussian only: Maximum size of the Depth of Field blur (in percent of the view width) (note: performance cost scales with size)
- ``depth_of_field_far_transition_region`` (float):  [Read-Write] To define the width of the transition region next to the focal region on the near side (cm)
- ``depth_of_field_focal_distance`` (float):  [Read-Write] Distance in which the Depth of Field effect should be sharp, in unreal units (cm)
- ``depth_of_field_focal_region`` (float):  [Read-Write] Artificial region where all content is in focus, starting after DepthOfFieldFocalDistance, in unreal units  (cm)
- ``depth_of_field_fstop`` (float):  [Read-Write] Defines the opening of the camera lens, Aperture is 1/fstop, typical lens go down to f/1.2 (large opening), larger numbers reduce the DOF effect
- ``depth_of_field_min_fstop`` (float):  [Read-Write] Defines the maximum opening of the camera lens to control the curvature of blades of the diaphragm. Set it to 0 to get straight blades.
- ``depth_of_field_near_blur_size`` (float):  [Read-Write] Gaussian only: Maximum size of the Depth of Field blur (in percent of the view width) (note: performance cost scales with size)
- ``depth_of_field_near_transition_region`` (float):  [Read-Write] To define the width of the transition region next to the focal region on the near side (cm)
- ``depth_of_field_occlusion`` (float):  [Read-Write] Occlusion tweak factor 1 (0.18 to get natural occlusion, 0.4 to solve layer color leaking issues)
- ``depth_of_field_scale`` (float):  [Read-Write] SM5: BokehDOF only: To amplify the depth of field effect (like aperture)  0=off
            ES3_1: Used to blend DoF. 0=off
- ``depth_of_field_sensor_width`` (float):  [Read-Write] Width of the camera sensor to assume, in mm.
- ``depth_of_field_sky_focus_distance`` (float):  [Read-Write] Artificial distance to allow the skybox to be in focus (e.g. 200000), <=0 to switch the feature off, only for GaussianDOF, can cost performance
- ``depth_of_field_squeeze_factor`` (float):  [Read-Write] This is the squeeze factor for the DOF, which emulates the properties of anamorphic lenses.
- ``depth_of_field_use_hair_depth`` (bool):  [Read-Write] For depth of field to use the hair depth for computing circle of confusion size. Otherwise use an interpolated distance between the hair depth and the scene depth based on the hair coverage (default).
- ``depth_of_field_vignette_size`` (float):  [Read-Write] Artificial circular mask to (near) blur content outside the radius, only for GaussianDOF, diameter in percent of screen width, costs performance if the mask is used, keep Feather can Radius on default to keep it off
- ``dynamic_global_illumination_method`` (DynamicGlobalIlluminationMethod):  [Read-Write] Chooses the Dynamic Global Illumination method.  Not compatible with Forward Shading.
- ``expand_gamut`` (float):  [Read-Write] Expand bright saturated colors outside the sRGB gamut to fake wide gamut rendering.
- ``film_black_clip`` (float):  [Read-Write] Lowers the toe of the tonemapper curve by this amount. Increasing this value causes more of the scene to clip to black.  For most purposes, this property should remain 0
- ``film_grain_highlights_max`` (float):  [Read-Write] Sets the upper bound used for Film Grain Highlight Intensity. This value should be larger than HighlightsMin.. Default is 1.0, for backwards compatibility
- ``film_grain_highlights_min`` (float):  [Read-Write] Sets the lower bound used for Film Grain Highlight Intensity.
- ``film_grain_intensity`` (float):  [Read-Write] 0..1 Film grain intensity to apply. LinearSceneColor *= lerp(1.0, DecodedFilmGrainTexture, FilmGrainIntensity)
- ``film_grain_intensity_highlights`` (float):  [Read-Write] Control over the grain intensity in the regions of the image considered highlight areas.
- ``film_grain_intensity_midtones`` (float):  [Read-Write] Control over the grain intensity in the mid-tone region of the image.
- ``film_grain_intensity_shadows`` (float):  [Read-Write] Control over the grain intensity in the regions of the image considered shadow areas.
- ``film_grain_shadows_max`` (float):  [Read-Write] Sets the upper bound used for Film Grain Shadow Intensity.
- ``film_grain_texel_size`` (float):  [Read-Write] Controls the size of the film grain. Size of texel of FilmGrainTexture on screen.
- ``film_grain_texture`` (Texture2D):  [Read-Write] Defines film grain texture to use.
- ``film_shoulder`` (float):  [Read-Write] Sometimes referred to as highlight rolloff.  Controls the contrast of the bright end of the tonemapper curve. Larger values increase contrast and smaller values decrease contrast.
- ``film_slope`` (float):  [Read-Write] Controls the overall steepness of the tonemapper curve.  Larger values increase scene contrast and smaller values reduce contrast.
- ``film_toe`` (float):  [Read-Write] Controls the contrast of the dark end of the tonemapper curve. Larger values increase contrast and smaller values decrease contrast.
- ``film_white_clip`` (float):  [Read-Write] Controls the height of the tonemapper curve.  Raising this value can cause bright values to more quickly approach fully-saturated white.
- ``histogram_log_max`` (float):  [Read-Write] Histogram Max value. Expressed in Log2(Luminance) or in EV100 when using ExtendDefaultLuminanceRange (see project settings)
- ``histogram_log_min`` (float):  [Read-Write] Histogram Min value. Expressed in Log2(Luminance) or in EV100 when using ExtendDefaultLuminanceRange (see project settings)
- ``indirect_lighting_color`` (LinearColor):  [Read-Write] Adjusts indirect lighting color. (1,1,1) is default. (0,0,0) to disable GI. The show flag 'Global Illumination' must be enabled to use this property.
- ``indirect_lighting_intensity`` (float):  [Read-Write] Scales the indirect lighting contribution. A value of 0 disables GI. Default is 1. The show flag 'Global Illumination' must be enabled to use this property.
- ``lens_flare_bokeh_shape`` (Texture):  [Read-Write] Defines the shape of the Bokeh when the image base lens flares are blurred, cannot be blended
- ``lens_flare_bokeh_size`` (float):  [Read-Write] Size of the Lens Blur (in percent of the view width) that is done with the Bokeh texture (note: performance cost is radius*radius)
- ``lens_flare_intensity`` (float):  [Read-Write] Brightness scale of the image cased lens flares (linear)
- ``lens_flare_threshold`` (float):  [Read-Write] Minimum brightness the lens flare starts having effect (this should be as high as possible to avoid the performance cost of blurring content that is too dark too see)
- ``lens_flare_tint`` (LinearColor):  [Read-Write] Tint color for the image based lens flares.
- ``lens_flare_tints`` (LinearColor):  [Read-Write] RGB defines the lens flare color, A it's position. This is a temporary solution.
- ``local_exposure_blurred_luminance_blend`` (float):  [Read-Write] Local Exposure decomposes luminance of the frame into a base layer and a detail layer.
  Blend between bilateral filtered and blurred luminance as the base layer.
  Blurred luminance helps preserve image appearance and specular highlights, and reduce ringing.
  Good values are usually in the range 0.4 .. 0.6
- ``local_exposure_blurred_luminance_kernel_size_percent`` (float):  [Read-Write] Kernel size (percentage of screen) used to blur frame luminance.
- ``local_exposure_detail_strength`` (float):  [Read-Write] Local Exposure decomposes luminance of the frame into a base layer and a detail layer.
  Value different than 1 will enable local exposure.
  This value should be set to 1 in most cases.
- ``local_exposure_highlight_contrast_curve`` (CurveFloat):  [Read-Write] Local Exposure Highlight Contrast based on the scene EV100.
  Used to calibrate Local Exposure differently depending on the average scene luminance.
- ``local_exposure_highlight_contrast_scale`` (float):  [Read-Write] Local Exposure decomposes luminance of the frame into a base layer and a detail layer.
  Contrast of the base layer is reduced based on this value.
  Value less than 1 will enable local exposure.
  Good values are usually in the range 0.6 .. 1.0.
- ``local_exposure_highlight_threshold`` (float):  [Read-Write] Threshold used to determine which regions of the screen are considered highlights.
- ``local_exposure_method`` (LocalExposureMethod):  [Read-Write] Local Exposure algorithm
- ``local_exposure_middle_grey_bias`` (float):  [Read-Write] Logarithmic adjustment for the local exposure middle grey.
  0: no adjustment, -1:2x darker, -2:4x darker, 1:2x brighter, 2:4x brighter, ...
- ``local_exposure_shadow_contrast_curve`` (CurveFloat):  [Read-Write] Local Exposure Shadow Contrast based on the scene EV100.
  Used to calibrate Local Exposure differently depending on the average scene luminance.
- ``local_exposure_shadow_contrast_scale`` (float):  [Read-Write] Local Exposure decomposes luminance of the frame into a base layer and a detail layer.
  Contrast of the base layer is reduced based on this value.
  Value less than 1 will enable local exposure.
  Good values are usually in the range 0.6 .. 1.0.
- ``local_exposure_shadow_threshold`` (float):  [Read-Write] Threshold used to determine which regions of the screen are considered shadows.
- ``lumen_diffuse_color_boost`` (float):  [Read-Write] Allows brightening indirect lighting by calculating material diffuse color for indirect lighting as pow(DiffuseColor, 1 / DiffuseColorBoost). Values above 1 (original diffuse color) aren't physically correct, but they can be useful as an art direction knob to increase the amount of bounced light in the scene. Best to keep below 2 as it also causes reflections to be brighter than the scene.
- ``lumen_final_gather_lighting_update_speed`` (float):  [Read-Write] Controls how much Lumen Final Gather is allowed to cache lighting results to improve performance.  Larger scales cause lighting changes to propagate faster, but increase GPU cost and noise.
- ``lumen_final_gather_quality`` (float):  [Read-Write] Scales Lumen's Final Gather quality.  Larger scales reduce noise, but greatly increase GPU cost.
- ``lumen_final_gather_screen_traces`` (bool):  [Read-Write] Whether to use screen space traces for Lumen Global Illumination. Screen space traces bypass Lumen Scene and instead sample Scene Depth and Scene Color. This improves quality, as it bypasses Lumen Scene, but causes view dependent lighting.
- ``lumen_front_layer_translucency_reflections`` (bool):  [Read-Write] Whether to use high quality mirror reflections on the front layer of translucent surfaces.  Other layers will use the lower quality Radiance Cache method that can only produce glossy reflections.  Increases GPU cost when enabled.
- ``lumen_full_skylight_leaking_distance`` (float):  [Read-Write] Controls the distance from a receiving surface where skylight leaking reaches its full intensity.  Smaller values make the skylight leaking flatter, while larger values create an Ambient Occlusion effect.
- ``lumen_max_reflection_bounces`` (int32):  [Read-Write] Sets the maximum number of recursive reflection bounces. 1 means a single reflection ray (no secondary reflections in mirrors). Currently only supported by Hardware Ray Tracing with Hit Lighting.
- ``lumen_max_refraction_bounces`` (int32):  [Read-Write] The maximum count of refraction event to trace. When hit lighting is used, Translucent meshes will be traced when LumenMaxRefractionBounces > 0, making the reflection tracing more expenssive.
- ``lumen_max_roughness_to_trace_reflections`` (float):  [Read-Write] Sets the maximum roughness value for which Lumen still traces dedicated reflection rays. Higher values improve reflection quality, but greatly increase GPU cost.
- ``lumen_max_trace_distance`` (float):  [Read-Write] Controls the maximum distance that Lumen should trace while solving lighting.  Values that are too small will cause lighting to leak into large caves, while values that are large will increase GPU cost.
- ``lumen_ray_lighting_mode`` (LumenRayLightingModeOverride):  [Read-Write] Controls how Lumen rays are lit when Lumen is using Hardware Ray Tracing.  By default, Lumen uses the Surface Cache for best performance, but can be set to 'Hit Lighting' for higher quality.
- ``lumen_reflection_quality`` (float):  [Read-Write] Scales the Reflection quality.  Larger scales reduce noise in reflections, but increase GPU cost.
- ``lumen_reflections_screen_traces`` (bool):  [Read-Write] Whether to use screen space traces for Lumen Reflections. Screen space traces bypass Lumen Scene and instead sample Scene Depth and Scene Color. This improves quality, as it bypasses Lumen Scene, but causes view dependent lighting.
- ``lumen_scene_detail`` (float):  [Read-Write] Controls the size of instances that can be represented in Lumen Scene.  Larger values will ensure small objects are represented, but increase GPU cost.
- ``lumen_scene_lighting_quality`` (float):  [Read-Write] Scales Lumen Scene's quality.  Larger scales cause Lumen Scene to be calculated with a higher fidelity, which can be visible in reflections, but increase GPU cost.
- ``lumen_scene_lighting_update_speed`` (float):  [Read-Write] Controls how much Lumen Scene is allowed to cache lighting results to improve performance.  Larger scales cause lighting changes to propagate faster, but increase GPU cost.
- ``lumen_scene_view_distance`` (float):  [Read-Write] Sets the maximum view distance of the scene that Lumen maintains for ray tracing against.  Larger values will increase the effective range of sky shadowing and Global Illumination, but increase GPU cost.
- ``lumen_skylight_leaking`` (float):  [Read-Write] Controls what fraction of the skylight intensity should be allowed to leak.  This can be useful as an art direction knob (non-physically based) to keep indoor areas from going fully black.
- ``lumen_surface_cache_resolution`` (float):  [Read-Write] Scale factor for Lumen Surface Cache resolution, for Scene Capture.  Smaller values save GPU memory, at a cost in quality.  Defaults to 0.5 if not overridden.
- ``mega_lights`` (bool):  [Read-Write] Allows forcing MegaLights on or off for this volume, regardless of the project setting for MegaLights.
  MegaLights will stochastically sample lights, which allows many shadow casting lights to be rendered efficiently, with a consistent and low GPU cost.
  When MegaLights is enabled, other direct lighting algorithms like Deferred Shading will no longer be used, and other shadowing methods like Ray Traced Shadows, Distance Field Shadows and Shadow Maps will no longer be used.
  MegaLights requires Hardware Ray Tracing and Shader Model 6.
- ``mobile_hq_gaussian`` (bool):  [Read-Write] Enable HQ Gaussian on high end mobile platforms. (ES3_1)
- ``motion_blur_amount`` (float):  [Read-Write] Strength of motion blur, 0:off
- ``motion_blur_max`` (float):  [Read-Write] max distortion caused by motion blur, in percent of the screen width, 0:off
- ``motion_blur_per_object_size`` (float):  [Read-Write] The minimum projected screen radius for a primitive to be drawn in the velocity pass, percentage of screen width. smaller numbers cause more draw calls, default: 4%
- ``motion_blur_target_fps`` (int32):  [Read-Write] Defines the target FPS for motion blur. Makes motion blur independent of actual frame rate and relative
  to the specified target FPS instead. Higher target FPS results in shorter frames, which means shorter
  shutter times and less motion blur. Lower FPS means more motion blur. A value of zero makes the motion
  blur dependent on the actual frame rate.
- ``override_ambient_cubemap_intensity`` (bool):  [Read-Write]
- ``override_ambient_cubemap_tint`` (bool):  [Read-Write]
- ``override_ambient_occlusion_bias`` (bool):  [Read-Write]
- ``override_ambient_occlusion_fade_distance`` (bool):  [Read-Write]
- ``override_ambient_occlusion_fade_radius`` (bool):  [Read-Write]
- ``override_ambient_occlusion_intensity`` (bool):  [Read-Write]
- ``override_ambient_occlusion_mip_blend`` (bool):  [Read-Write]
- ``override_ambient_occlusion_mip_scale`` (bool):  [Read-Write]
- ``override_ambient_occlusion_mip_threshold`` (bool):  [Read-Write]
- ``override_ambient_occlusion_power`` (bool):  [Read-Write]
- ``override_ambient_occlusion_quality`` (bool):  [Read-Write]
- ``override_ambient_occlusion_radius`` (bool):  [Read-Write]
- ``override_ambient_occlusion_radius_in_ws`` (bool):  [Read-Write]
- ``override_ambient_occlusion_static_fraction`` (bool):  [Read-Write]
- ``override_ambient_occlusion_temporal_blend_weight`` (bool):  [Read-Write]
- ``override_auto_exposure_apply_physical_camera_exposure`` (bool):  [Read-Write]
- ``override_auto_exposure_bias`` (bool):  [Read-Write]
- ``override_auto_exposure_bias_curve`` (bool):  [Read-Write]
- ``override_auto_exposure_high_percent`` (bool):  [Read-Write]
- ``override_auto_exposure_low_percent`` (bool):  [Read-Write]
- ``override_auto_exposure_max_brightness`` (bool):  [Read-Write]
- ``override_auto_exposure_meter_mask`` (bool):  [Read-Write]
- ``override_auto_exposure_method`` (bool):  [Read-Write]
- ``override_auto_exposure_min_brightness`` (bool):  [Read-Write]
- ``override_auto_exposure_speed_down`` (bool):  [Read-Write]
- ``override_auto_exposure_speed_up`` (bool):  [Read-Write]
- ``override_b_mega_lights`` (bool):  [Read-Write]
- ``override_bloom1_size`` (bool):  [Read-Write]
- ``override_bloom1_tint`` (bool):  [Read-Write]
- ``override_bloom2_size`` (bool):  [Read-Write]
- ``override_bloom2_tint`` (bool):  [Read-Write]
- ``override_bloom3_size`` (bool):  [Read-Write]
- ``override_bloom3_tint`` (bool):  [Read-Write]
- ``override_bloom4_size`` (bool):  [Read-Write]
- ``override_bloom4_tint`` (bool):  [Read-Write]
- ``override_bloom5_size`` (bool):  [Read-Write]
- ``override_bloom5_tint`` (bool):  [Read-Write]
- ``override_bloom6_size`` (bool):  [Read-Write]
- ``override_bloom6_tint`` (bool):  [Read-Write]
- ``override_bloom_convolution_buffer_scale`` (bool):  [Read-Write]
- ``override_bloom_convolution_center_uv`` (bool):  [Read-Write]
- ``override_bloom_convolution_pre_filter_max`` (bool):  [Read-Write]
- ``override_bloom_convolution_pre_filter_min`` (bool):  [Read-Write]
- ``override_bloom_convolution_pre_filter_mult`` (bool):  [Read-Write]
- ``override_bloom_convolution_scatter_dispersion`` (bool):  [Read-Write]
- ``override_bloom_convolution_size`` (bool):  [Read-Write]
- ``override_bloom_convolution_texture`` (bool):  [Read-Write]
- ``override_bloom_dirt_mask`` (bool):  [Read-Write]
- ``override_bloom_dirt_mask_intensity`` (bool):  [Read-Write]
- ``override_bloom_dirt_mask_tint`` (bool):  [Read-Write]
- ``override_bloom_intensity`` (bool):  [Read-Write]
- ``override_bloom_method`` (bool):  [Read-Write]
- ``override_bloom_size_scale`` (bool):  [Read-Write]
- ``override_bloom_threshold`` (bool):  [Read-Write]
- ``override_blue_correction`` (bool):  [Read-Write]
- ``override_camera_iso`` (bool):  [Read-Write]
- ``override_camera_shutter_speed`` (bool):  [Read-Write]
- ``override_chromatic_aberration_start_offset`` (bool):  [Read-Write]
- ``override_color_contrast`` (bool):  [Read-Write]
- ``override_color_contrast_highlights`` (bool):  [Read-Write]
- ``override_color_contrast_midtones`` (bool):  [Read-Write]
- ``override_color_contrast_shadows`` (bool):  [Read-Write]
- ``override_color_correction_highlights_max`` (bool):  [Read-Write]
- ``override_color_correction_highlights_min`` (bool):  [Read-Write]
- ``override_color_correction_shadows_max`` (bool):  [Read-Write]
- ``override_color_gain`` (bool):  [Read-Write]
- ``override_color_gain_highlights`` (bool):  [Read-Write]
- ``override_color_gain_midtones`` (bool):  [Read-Write]
- ``override_color_gain_shadows`` (bool):  [Read-Write]
- ``override_color_gamma`` (bool):  [Read-Write]
- ``override_color_gamma_highlights`` (bool):  [Read-Write]
- ``override_color_gamma_midtones`` (bool):  [Read-Write]
- ``override_color_gamma_shadows`` (bool):  [Read-Write]
- ``override_color_grading_intensity`` (bool):  [Read-Write]
- ``override_color_grading_lut`` (bool):  [Read-Write]
- ``override_color_offset`` (bool):  [Read-Write]
- ``override_color_offset_highlights`` (bool):  [Read-Write]
- ``override_color_offset_midtones`` (bool):  [Read-Write]
- ``override_color_offset_shadows`` (bool):  [Read-Write]
- ``override_color_saturation`` (bool):  [Read-Write] Color Correction controls
- ``override_color_saturation_highlights`` (bool):  [Read-Write]
- ``override_color_saturation_midtones`` (bool):  [Read-Write]
- ``override_color_saturation_shadows`` (bool):  [Read-Write]
- ``override_depth_of_field_blade_count`` (bool):  [Read-Write]
- ``override_depth_of_field_depth_blur_amount`` (bool):  [Read-Write]
- ``override_depth_of_field_depth_blur_radius`` (bool):  [Read-Write]
- ``override_depth_of_field_far_blur_size`` (bool):  [Read-Write]
- ``override_depth_of_field_far_transition_region`` (bool):  [Read-Write]
- ``override_depth_of_field_focal_distance`` (bool):  [Read-Write]
- ``override_depth_of_field_focal_region`` (bool):  [Read-Write]
- ``override_depth_of_field_fstop`` (bool):  [Read-Write]
- ``override_depth_of_field_min_fstop`` (bool):  [Read-Write]
- ``override_depth_of_field_near_blur_size`` (bool):  [Read-Write]
- ``override_depth_of_field_near_transition_region`` (bool):  [Read-Write]
- ``override_depth_of_field_occlusion`` (bool):  [Read-Write]
- ``override_depth_of_field_scale`` (bool):  [Read-Write]
- ``override_depth_of_field_sensor_width`` (bool):  [Read-Write]
- ``override_depth_of_field_sky_focus_distance`` (bool):  [Read-Write]
- ``override_depth_of_field_squeeze_factor`` (bool):  [Read-Write]
- ``override_depth_of_field_use_hair_depth`` (bool):  [Read-Write]
- ``override_depth_of_field_vignette_size`` (bool):  [Read-Write]
- ``override_dynamic_global_illumination_method`` (bool):  [Read-Write]
- ``override_expand_gamut`` (bool):  [Read-Write]
- ``override_film_black_clip`` (bool):  [Read-Write]
- ``override_film_grain_highlights_max`` (bool):  [Read-Write]
- ``override_film_grain_highlights_min`` (bool):  [Read-Write]
- ``override_film_grain_intensity`` (bool):  [Read-Write]
- ``override_film_grain_intensity_highlights`` (bool):  [Read-Write]
- ``override_film_grain_intensity_midtones`` (bool):  [Read-Write]
- ``override_film_grain_intensity_shadows`` (bool):  [Read-Write]
- ``override_film_grain_shadows_max`` (bool):  [Read-Write]
- ``override_film_grain_texel_size`` (bool):  [Read-Write]
- ``override_film_grain_texture`` (bool):  [Read-Write]
- ``override_film_shoulder`` (bool):  [Read-Write]
- ``override_film_slope`` (bool):  [Read-Write]
- ``override_film_toe`` (bool):  [Read-Write]
- ``override_film_white_clip`` (bool):  [Read-Write]
- ``override_histogram_log_max`` (bool):  [Read-Write]
- ``override_histogram_log_min`` (bool):  [Read-Write]
- ``override_indirect_lighting_color`` (bool):  [Read-Write]
- ``override_indirect_lighting_intensity`` (bool):  [Read-Write]
- ``override_lens_flare_bokeh_shape`` (bool):  [Read-Write]
- ``override_lens_flare_bokeh_size`` (bool):  [Read-Write]
- ``override_lens_flare_intensity`` (bool):  [Read-Write]
- ``override_lens_flare_threshold`` (bool):  [Read-Write]
- ``override_lens_flare_tint`` (bool):  [Read-Write]
- ``override_lens_flare_tints`` (bool):  [Read-Write]
- ``override_local_exposure_blurred_luminance_blend`` (bool):  [Read-Write]
- ``override_local_exposure_blurred_luminance_kernel_size_percent`` (bool):  [Read-Write]
- ``override_local_exposure_detail_strength`` (bool):  [Read-Write]
- ``override_local_exposure_highlight_contrast_curve`` (bool):  [Read-Write]
- ``override_local_exposure_highlight_contrast_scale`` (bool):  [Read-Write]
- ``override_local_exposure_highlight_threshold`` (bool):  [Read-Write]
- ``override_local_exposure_method`` (bool):  [Read-Write]
- ``override_local_exposure_middle_grey_bias`` (bool):  [Read-Write]
- ``override_local_exposure_shadow_contrast_curve`` (bool):  [Read-Write]
- ``override_local_exposure_shadow_contrast_scale`` (bool):  [Read-Write]
- ``override_local_exposure_shadow_threshold`` (bool):  [Read-Write]
- ``override_lumen_diffuse_color_boost`` (bool):  [Read-Write]
- ``override_lumen_final_gather_lighting_update_speed`` (bool):  [Read-Write]
- ``override_lumen_final_gather_quality`` (bool):  [Read-Write]
- ``override_lumen_final_gather_screen_traces`` (bool):  [Read-Write]
- ``override_lumen_front_layer_translucency_reflections`` (bool):  [Read-Write]
- ``override_lumen_full_skylight_leaking_distance`` (bool):  [Read-Write]
- ``override_lumen_max_reflection_bounces`` (bool):  [Read-Write]
- ``override_lumen_max_refraction_bounces`` (bool):  [Read-Write]
- ``override_lumen_max_roughness_to_trace_reflections`` (bool):  [Read-Write]
- ``override_lumen_max_trace_distance`` (bool):  [Read-Write]
- ``override_lumen_ray_lighting_mode`` (bool):  [Read-Write]
- ``override_lumen_reflection_quality`` (bool):  [Read-Write]
- ``override_lumen_reflections_screen_traces`` (bool):  [Read-Write]
- ``override_lumen_scene_detail`` (bool):  [Read-Write]
- ``override_lumen_scene_lighting_quality`` (bool):  [Read-Write]
- ``override_lumen_scene_lighting_update_speed`` (bool):  [Read-Write]
- ``override_lumen_scene_view_distance`` (bool):  [Read-Write]
- ``override_lumen_skylight_leaking`` (bool):  [Read-Write]
- ``override_lumen_surface_cache_resolution`` (bool):  [Read-Write]
- ``override_mobile_hq_gaussian`` (bool):  [Read-Write]
- ``override_motion_blur_amount`` (bool):  [Read-Write]
- ``override_motion_blur_max`` (bool):  [Read-Write]
- ``override_motion_blur_per_object_size`` (bool):  [Read-Write]
- ``override_motion_blur_target_fps`` (bool):  [Read-Write]
- ``override_path_tracing_enable_denoiser`` (bool):  [Read-Write]
- ``override_path_tracing_enable_emissive_materials`` (bool):  [Read-Write]
- ``override_path_tracing_enable_reference_atmosphere`` (bool):  [Read-Write]
- ``override_path_tracing_enable_reference_dof`` (bool):  [Read-Write]
- ``override_path_tracing_include_diffuse`` (bool):  [Read-Write]
- ``override_path_tracing_include_emissive`` (bool):  [Read-Write]
- ``override_path_tracing_include_indirect_diffuse`` (bool):  [Read-Write]
- ``override_path_tracing_include_indirect_specular`` (bool):  [Read-Write]
- ``override_path_tracing_include_indirect_volume`` (bool):  [Read-Write]
- ``override_path_tracing_include_specular`` (bool):  [Read-Write]
- ``override_path_tracing_include_volume`` (bool):  [Read-Write]
- ``override_path_tracing_max_bounces`` (bool):  [Read-Write]
- ``override_path_tracing_max_path_intensity`` (bool):  [Read-Write]
- ``override_path_tracing_samples_per_pixel`` (bool):  [Read-Write]
- ``override_ray_tracing_ao`` (bool):  [Read-Write]
- ``override_ray_tracing_ao_intensity`` (bool):  [Read-Write]
- ``override_ray_tracing_ao_radius`` (bool):  [Read-Write]
- ``override_ray_tracing_ao_samples_per_pixel`` (bool):  [Read-Write]
- ``override_ray_tracing_gi`` (bool):  [Read-Write]
- ``override_ray_tracing_gi_max_bounces`` (bool):  [Read-Write]
- ``override_ray_tracing_gi_samples_per_pixel`` (bool):  [Read-Write]
- ``override_ray_tracing_reflections_max_bounces`` (bool):  [Read-Write]
- ``override_ray_tracing_reflections_max_roughness`` (bool):  [Read-Write]
- ``override_ray_tracing_reflections_samples_per_pixel`` (bool):  [Read-Write]
- ``override_ray_tracing_reflections_shadows`` (bool):  [Read-Write]
- ``override_ray_tracing_reflections_translucency`` (bool):  [Read-Write]
- ``override_ray_tracing_translucency_max_roughness`` (bool):  [Read-Write]
- ``override_ray_tracing_translucency_refraction`` (bool):  [Read-Write]
- ``override_ray_tracing_translucency_refraction_rays`` (bool):  [Read-Write]
- ``override_ray_tracing_translucency_samples_per_pixel`` (bool):  [Read-Write]
- ``override_ray_tracing_translucency_shadows`` (bool):  [Read-Write]
- ``override_reflection_method`` (bool):  [Read-Write]
- ``override_scene_color_tint`` (bool):  [Read-Write]
- ``override_scene_fringe_intensity`` (bool):  [Read-Write]
- ``override_screen_space_reflection_intensity`` (bool):  [Read-Write]
- ``override_screen_space_reflection_max_roughness`` (bool):  [Read-Write]
- ``override_screen_space_reflection_quality`` (bool):  [Read-Write]
- ``override_screen_space_reflection_roughness_scale`` (bool):  [Read-Write]
- ``override_sharpen`` (bool):  [Read-Write]
- ``override_temperature_type`` (bool):  [Read-Write] first all bOverride_... as they get grouped together into bitfields
- ``override_tone_curve_amount`` (bool):  [Read-Write]
- ``override_translucency_type`` (bool):  [Read-Write]
- ``override_user_flags`` (bool):  [Read-Write] TODO: look useless...
- ``override_vignette_intensity`` (bool):  [Read-Write]
- ``override_white_temp`` (bool):  [Read-Write]
- ``override_white_tint`` (bool):  [Read-Write]
- ``path_tracing_enable_denoiser`` (bool):  [Read-Write] Run the currently loaded denoiser plugin on the last sample to remove noise from the output. Has no effect if a plug-in is not loaded.
- ``path_tracing_enable_emissive_materials`` (bool):  [Read-Write] Should emissive materials contribute to scene lighting?
- ``path_tracing_enable_reference_atmosphere`` (bool):  [Read-Write] Enables path tracing in the atmosphere instead of baking the sky atmosphere contribution into a skylight. Any skylight present in the scene will be automatically ignored when this is enabled.
- ``path_tracing_enable_reference_dof`` (bool):  [Read-Write] Enables a reference quality depth-of-field which replaces the post-process effect.
- ``path_tracing_include_diffuse`` (bool):  [Read-Write] Should the render include diffuse lighting contributions?
- ``path_tracing_include_emissive`` (bool):  [Read-Write] Should the render include directly visible emissive elements?
- ``path_tracing_include_indirect_diffuse`` (bool):  [Read-Write] Should the render include indirect diffuse lighting contributions?
- ``path_tracing_include_indirect_specular`` (bool):  [Read-Write] Should the render include indirect specular lighting contributions?
- ``path_tracing_include_indirect_volume`` (bool):  [Read-Write] Should the render include volume lighting contributions?
- ``path_tracing_include_specular`` (bool):  [Read-Write] Should the render include specular lighting contributions?
- ``path_tracing_include_volume`` (bool):  [Read-Write] Should the render include volume lighting contributions?
- ``path_tracing_max_bounces`` (int32):  [Read-Write] Sets the path tracing maximum bounces
- ``path_tracing_max_path_intensity`` (float):  [Read-Write] Sets the maximum intensity of indirect samples to reduce fireflies. Lowering this value reduces noise at the expense of accuracy. Increasing it is more accurate but may lead to more noise.
- ``path_tracing_samples_per_pixel`` (int32):  [Read-Write] Sets the samples per pixel for the path tracer.
- ``ray_tracing_ao`` (bool):  [Read-Write] Enables ray tracing ambient occlusion.
- ``ray_tracing_ao_intensity`` (float):  [Read-Write] Scalar factor on the ray-tracing ambient occlusion score.
- ``ray_tracing_ao_radius`` (float):  [Read-Write] Defines the world-space search radius for occlusion rays.
- ``ray_tracing_ao_samples_per_pixel`` (int32):  [Read-Write] Sets the samples per pixel for ray tracing ambient occlusion.
- ``ray_tracing_translucency_max_roughness`` (float):  [Read-Write] Sets the maximum roughness until which ray tracing translucency will be visible (lower value is faster). Translucency contribution is smoothly faded when close to roughness threshold. This parameter behaves similarly to ScreenSpaceReflectionMaxRoughness.
- ``ray_tracing_translucency_refraction`` (bool):  [Read-Write] Sets whether refraction should be enabled or not (if not rays will not scatter and only travel in the same direction as before the intersection event).
- ``ray_tracing_translucency_refraction_rays`` (int32):  [Read-Write] Sets the maximum number of ray tracing refraction rays.
- ``ray_tracing_translucency_samples_per_pixel`` (int32):  [Read-Write] Sets the samples per pixel for ray traced translucency.
- ``ray_tracing_translucency_shadows`` (ReflectedAndRefractedRayTracedShadows):  [Read-Write] Sets the translucency shadows type.
- ``reflection_method`` (ReflectionMethod):  [Read-Write] Chooses the Reflection method. Not compatible with Forward Shading.
- ``scene_color_tint`` (LinearColor):  [Read-Write] Scene tint color
- ``scene_fringe_intensity`` (float):  [Read-Write] in percent, Scene chromatic aberration / color fringe (camera imperfection) to simulate an artifact that happens in real-world lens, mostly visible in the image corners.
- ``screen_space_reflection_intensity`` (float):  [Read-Write] Enable/Fade/disable the Screen Space Reflection feature, in percent, avoid numbers between 0 and 1 fo consistency
- ``screen_space_reflection_max_roughness`` (float):  [Read-Write] Until what roughness we fade the screen space reflections, 0.8 works well, smaller can run faster
- ``screen_space_reflection_quality`` (float):  [Read-Write] 0=lowest quality..100=maximum quality, only a few quality levels are implemented, no soft transition, 50 is the default for better performance.
- ``sharpen`` (float):  [Read-Write] Controls the strength of image sharpening applied during tonemapping.
- ``temperature_type`` (TemperatureMethod):  [Read-Write] Selects the type of temperature calculation.
  White Balance uses the Temperature value to control the virtual camera's White Balance. This is the default selection.
  Color Temperature uses the Temperature value to adjust the color temperature of the scene, which is the inverse of the White Balance operation.
- ``tone_curve_amount`` (float):  [Read-Write] Allow effect of Tone Curve to be reduced (Set ToneCurveAmount and ExpandGamut to 0.0 to fully disable tone curve)
- ``translucency_type`` (TranslucencyType):  [Read-Write] Sets the translucency type
- ``user_flags`` (int32):  [Read-Write] Per-view user flags accessible in materials via TestPostVolumeUserFlag node, allowing per-view overrides of material behavior.
- ``vignette_intensity`` (float):  [Read-Write] 0..1 0=off/no vignette .. 1=strong vignette
- ``weighted_blendables`` (WeightedBlendables):  [Read-Write] Allows custom post process materials to be defined, using a MaterialInstance with the same Material as its parent to allow blending.
  For materials this needs to be the "PostProcess" domain type. This can be used for any UObject object implementing the IBlendableInterface (e.g. could be used to fade weather settings).
- ``white_temp`` (float):  [Read-Write] Controls the color temperature or white balance in degrees Kelvin which the scene considers as white light.
- ``white_tint`` (float):  [Read-Write] Controls the color of the scene along the magenta - green axis (orthogonal to the color temperature).  This feature is equivalent to color tint in digital cameras.

<a id="unreal.PostProcessSettings.__init__"></a>

#### __init__

```python
def __init__(*args: Any, **kwargs: Any) -> None
```

<a id="unreal.PostProcessSettings.override_temperature_type"></a>

#### override_temperature_type

```python
@property
def override_temperature_type() -> bool
```

(bool):  [Read-Write] first all bOverride_... as they get grouped together into bitfields

<a id="unreal.PostProcessSettings.override_temperature_type"></a>

#### override_temperature_type

```python
@override_temperature_type.setter
def override_temperature_type(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_white_temp"></a>

#### override_white_temp

```python
@property
def override_white_temp() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_white_temp"></a>

#### override_white_temp

```python
@override_white_temp.setter
def override_white_temp(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_white_tint"></a>

#### override_white_tint

```python
@property
def override_white_tint() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_white_tint"></a>

#### override_white_tint

```python
@override_white_tint.setter
def override_white_tint(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_color_saturation"></a>

#### override_color_saturation

```python
@property
def override_color_saturation() -> bool
```

(bool):  [Read-Write] Color Correction controls

<a id="unreal.PostProcessSettings.override_color_saturation"></a>

#### override_color_saturation

```python
@override_color_saturation.setter
def override_color_saturation(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_color_contrast"></a>

#### override_color_contrast

```python
@property
def override_color_contrast() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_color_contrast"></a>

#### override_color_contrast

```python
@override_color_contrast.setter
def override_color_contrast(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_color_gamma"></a>

#### override_color_gamma

```python
@property
def override_color_gamma() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_color_gamma"></a>

#### override_color_gamma

```python
@override_color_gamma.setter
def override_color_gamma(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_color_gain"></a>

#### override_color_gain

```python
@property
def override_color_gain() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_color_gain"></a>

#### override_color_gain

```python
@override_color_gain.setter
def override_color_gain(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_color_offset"></a>

#### override_color_offset

```python
@property
def override_color_offset() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_color_offset"></a>

#### override_color_offset

```python
@override_color_offset.setter
def override_color_offset(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_color_saturation_shadows"></a>

#### override_color_saturation_shadows

```python
@property
def override_color_saturation_shadows() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_color_saturation_shadows"></a>

#### override_color_saturation_shadows

```python
@override_color_saturation_shadows.setter
def override_color_saturation_shadows(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_color_contrast_shadows"></a>

#### override_color_contrast_shadows

```python
@property
def override_color_contrast_shadows() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_color_contrast_shadows"></a>

#### override_color_contrast_shadows

```python
@override_color_contrast_shadows.setter
def override_color_contrast_shadows(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_color_gamma_shadows"></a>

#### override_color_gamma_shadows

```python
@property
def override_color_gamma_shadows() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_color_gamma_shadows"></a>

#### override_color_gamma_shadows

```python
@override_color_gamma_shadows.setter
def override_color_gamma_shadows(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_color_gain_shadows"></a>

#### override_color_gain_shadows

```python
@property
def override_color_gain_shadows() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_color_gain_shadows"></a>

#### override_color_gain_shadows

```python
@override_color_gain_shadows.setter
def override_color_gain_shadows(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_color_offset_shadows"></a>

#### override_color_offset_shadows

```python
@property
def override_color_offset_shadows() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_color_offset_shadows"></a>

#### override_color_offset_shadows

```python
@override_color_offset_shadows.setter
def override_color_offset_shadows(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_color_saturation_midtones"></a>

#### override_color_saturation_midtones

```python
@property
def override_color_saturation_midtones() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_color_saturation_midtones"></a>

#### override_color_saturation_midtones

```python
@override_color_saturation_midtones.setter
def override_color_saturation_midtones(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_color_contrast_midtones"></a>

#### override_color_contrast_midtones

```python
@property
def override_color_contrast_midtones() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_color_contrast_midtones"></a>

#### override_color_contrast_midtones

```python
@override_color_contrast_midtones.setter
def override_color_contrast_midtones(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_color_gamma_midtones"></a>

#### override_color_gamma_midtones

```python
@property
def override_color_gamma_midtones() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_color_gamma_midtones"></a>

#### override_color_gamma_midtones

```python
@override_color_gamma_midtones.setter
def override_color_gamma_midtones(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_color_gain_midtones"></a>

#### override_color_gain_midtones

```python
@property
def override_color_gain_midtones() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_color_gain_midtones"></a>

#### override_color_gain_midtones

```python
@override_color_gain_midtones.setter
def override_color_gain_midtones(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_color_offset_midtones"></a>

#### override_color_offset_midtones

```python
@property
def override_color_offset_midtones() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_color_offset_midtones"></a>

#### override_color_offset_midtones

```python
@override_color_offset_midtones.setter
def override_color_offset_midtones(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_color_saturation_highlights"></a>

#### override_color_saturation_highlights

```python
@property
def override_color_saturation_highlights() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_color_saturation_highlights"></a>

#### override_color_saturation_highlights

```python
@override_color_saturation_highlights.setter
def override_color_saturation_highlights(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_color_contrast_highlights"></a>

#### override_color_contrast_highlights

```python
@property
def override_color_contrast_highlights() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_color_contrast_highlights"></a>

#### override_color_contrast_highlights

```python
@override_color_contrast_highlights.setter
def override_color_contrast_highlights(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_color_gamma_highlights"></a>

#### override_color_gamma_highlights

```python
@property
def override_color_gamma_highlights() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_color_gamma_highlights"></a>

#### override_color_gamma_highlights

```python
@override_color_gamma_highlights.setter
def override_color_gamma_highlights(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_color_gain_highlights"></a>

#### override_color_gain_highlights

```python
@property
def override_color_gain_highlights() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_color_gain_highlights"></a>

#### override_color_gain_highlights

```python
@override_color_gain_highlights.setter
def override_color_gain_highlights(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_color_offset_highlights"></a>

#### override_color_offset_highlights

```python
@property
def override_color_offset_highlights() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_color_offset_highlights"></a>

#### override_color_offset_highlights

```python
@override_color_offset_highlights.setter
def override_color_offset_highlights(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_color_correction_shadows_max"></a>

#### override_color_correction_shadows_max

```python
@property
def override_color_correction_shadows_max() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_color_correction_shadows_max"></a>

#### override_color_correction_shadows_max

```python
@override_color_correction_shadows_max.setter
def override_color_correction_shadows_max(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_color_correction_highlights_min"></a>

#### override_color_correction_highlights_min

```python
@property
def override_color_correction_highlights_min() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_color_correction_highlights_min"></a>

#### override_color_correction_highlights_min

```python
@override_color_correction_highlights_min.setter
def override_color_correction_highlights_min(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_color_correction_highlights_max"></a>

#### override_color_correction_highlights_max

```python
@property
def override_color_correction_highlights_max() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_color_correction_highlights_max"></a>

#### override_color_correction_highlights_max

```python
@override_color_correction_highlights_max.setter
def override_color_correction_highlights_max(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_blue_correction"></a>

#### override_blue_correction

```python
@property
def override_blue_correction() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_blue_correction"></a>

#### override_blue_correction

```python
@override_blue_correction.setter
def override_blue_correction(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_expand_gamut"></a>

#### override_expand_gamut

```python
@property
def override_expand_gamut() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_expand_gamut"></a>

#### override_expand_gamut

```python
@override_expand_gamut.setter
def override_expand_gamut(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_tone_curve_amount"></a>

#### override_tone_curve_amount

```python
@property
def override_tone_curve_amount() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_tone_curve_amount"></a>

#### override_tone_curve_amount

```python
@override_tone_curve_amount.setter
def override_tone_curve_amount(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_film_slope"></a>

#### override_film_slope

```python
@property
def override_film_slope() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_film_slope"></a>

#### override_film_slope

```python
@override_film_slope.setter
def override_film_slope(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_film_toe"></a>

#### override_film_toe

```python
@property
def override_film_toe() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_film_toe"></a>

#### override_film_toe

```python
@override_film_toe.setter
def override_film_toe(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_film_shoulder"></a>

#### override_film_shoulder

```python
@property
def override_film_shoulder() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_film_shoulder"></a>

#### override_film_shoulder

```python
@override_film_shoulder.setter
def override_film_shoulder(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_film_black_clip"></a>

#### override_film_black_clip

```python
@property
def override_film_black_clip() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_film_black_clip"></a>

#### override_film_black_clip

```python
@override_film_black_clip.setter
def override_film_black_clip(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_film_white_clip"></a>

#### override_film_white_clip

```python
@property
def override_film_white_clip() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_film_white_clip"></a>

#### override_film_white_clip

```python
@override_film_white_clip.setter
def override_film_white_clip(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_scene_color_tint"></a>

#### override_scene_color_tint

```python
@property
def override_scene_color_tint() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_scene_color_tint"></a>

#### override_scene_color_tint

```python
@override_scene_color_tint.setter
def override_scene_color_tint(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_scene_fringe_intensity"></a>

#### override_scene_fringe_intensity

```python
@property
def override_scene_fringe_intensity() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_scene_fringe_intensity"></a>

#### override_scene_fringe_intensity

```python
@override_scene_fringe_intensity.setter
def override_scene_fringe_intensity(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_chromatic_aberration_start_offset"></a>

#### override_chromatic_aberration_start_offset

```python
@property
def override_chromatic_aberration_start_offset() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_chromatic_aberration_start_offset"></a>

#### override_chromatic_aberration_start_offset

```python
@override_chromatic_aberration_start_offset.setter
def override_chromatic_aberration_start_offset(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_b_mega_lights"></a>

#### override_b_mega_lights

```python
@property
def override_b_mega_lights() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_b_mega_lights"></a>

#### override_b_mega_lights

```python
@override_b_mega_lights.setter
def override_b_mega_lights(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_ambient_cubemap_tint"></a>

#### override_ambient_cubemap_tint

```python
@property
def override_ambient_cubemap_tint() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_ambient_cubemap_tint"></a>

#### override_ambient_cubemap_tint

```python
@override_ambient_cubemap_tint.setter
def override_ambient_cubemap_tint(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_ambient_cubemap_intensity"></a>

#### override_ambient_cubemap_intensity

```python
@property
def override_ambient_cubemap_intensity() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_ambient_cubemap_intensity"></a>

#### override_ambient_cubemap_intensity

```python
@override_ambient_cubemap_intensity.setter
def override_ambient_cubemap_intensity(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_bloom_method"></a>

#### override_bloom_method

```python
@property
def override_bloom_method() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_bloom_method"></a>

#### override_bloom_method

```python
@override_bloom_method.setter
def override_bloom_method(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_bloom_intensity"></a>

#### override_bloom_intensity

```python
@property
def override_bloom_intensity() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_bloom_intensity"></a>

#### override_bloom_intensity

```python
@override_bloom_intensity.setter
def override_bloom_intensity(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_bloom_threshold"></a>

#### override_bloom_threshold

```python
@property
def override_bloom_threshold() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_bloom_threshold"></a>

#### override_bloom_threshold

```python
@override_bloom_threshold.setter
def override_bloom_threshold(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_bloom1_tint"></a>

#### override_bloom1_tint

```python
@property
def override_bloom1_tint() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_bloom1_tint"></a>

#### override_bloom1_tint

```python
@override_bloom1_tint.setter
def override_bloom1_tint(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_bloom1_size"></a>

#### override_bloom1_size

```python
@property
def override_bloom1_size() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_bloom1_size"></a>

#### override_bloom1_size

```python
@override_bloom1_size.setter
def override_bloom1_size(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_bloom2_size"></a>

#### override_bloom2_size

```python
@property
def override_bloom2_size() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_bloom2_size"></a>

#### override_bloom2_size

```python
@override_bloom2_size.setter
def override_bloom2_size(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_bloom2_tint"></a>

#### override_bloom2_tint

```python
@property
def override_bloom2_tint() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_bloom2_tint"></a>

#### override_bloom2_tint

```python
@override_bloom2_tint.setter
def override_bloom2_tint(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_bloom3_tint"></a>

#### override_bloom3_tint

```python
@property
def override_bloom3_tint() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_bloom3_tint"></a>

#### override_bloom3_tint

```python
@override_bloom3_tint.setter
def override_bloom3_tint(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_bloom3_size"></a>

#### override_bloom3_size

```python
@property
def override_bloom3_size() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_bloom3_size"></a>

#### override_bloom3_size

```python
@override_bloom3_size.setter
def override_bloom3_size(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_bloom4_tint"></a>

#### override_bloom4_tint

```python
@property
def override_bloom4_tint() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_bloom4_tint"></a>

#### override_bloom4_tint

```python
@override_bloom4_tint.setter
def override_bloom4_tint(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_bloom4_size"></a>

#### override_bloom4_size

```python
@property
def override_bloom4_size() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_bloom4_size"></a>

#### override_bloom4_size

```python
@override_bloom4_size.setter
def override_bloom4_size(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_bloom5_tint"></a>

#### override_bloom5_tint

```python
@property
def override_bloom5_tint() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_bloom5_tint"></a>

#### override_bloom5_tint

```python
@override_bloom5_tint.setter
def override_bloom5_tint(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_bloom5_size"></a>

#### override_bloom5_size

```python
@property
def override_bloom5_size() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_bloom5_size"></a>

#### override_bloom5_size

```python
@override_bloom5_size.setter
def override_bloom5_size(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_bloom6_tint"></a>

#### override_bloom6_tint

```python
@property
def override_bloom6_tint() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_bloom6_tint"></a>

#### override_bloom6_tint

```python
@override_bloom6_tint.setter
def override_bloom6_tint(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_bloom6_size"></a>

#### override_bloom6_size

```python
@property
def override_bloom6_size() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_bloom6_size"></a>

#### override_bloom6_size

```python
@override_bloom6_size.setter
def override_bloom6_size(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_bloom_size_scale"></a>

#### override_bloom_size_scale

```python
@property
def override_bloom_size_scale() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_bloom_size_scale"></a>

#### override_bloom_size_scale

```python
@override_bloom_size_scale.setter
def override_bloom_size_scale(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_bloom_convolution_texture"></a>

#### override_bloom_convolution_texture

```python
@property
def override_bloom_convolution_texture() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_bloom_convolution_texture"></a>

#### override_bloom_convolution_texture

```python
@override_bloom_convolution_texture.setter
def override_bloom_convolution_texture(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_bloom_convolution_scatter_dispersion"></a>

#### override_bloom_convolution_scatter_dispersion

```python
@property
def override_bloom_convolution_scatter_dispersion() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_bloom_convolution_scatter_dispersion"></a>

#### override_bloom_convolution_scatter_dispersion

```python
@override_bloom_convolution_scatter_dispersion.setter
def override_bloom_convolution_scatter_dispersion(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_bloom_convolution_size"></a>

#### override_bloom_convolution_size

```python
@property
def override_bloom_convolution_size() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_bloom_convolution_size"></a>

#### override_bloom_convolution_size

```python
@override_bloom_convolution_size.setter
def override_bloom_convolution_size(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_bloom_convolution_center_uv"></a>

#### override_bloom_convolution_center_uv

```python
@property
def override_bloom_convolution_center_uv() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_bloom_convolution_center_uv"></a>

#### override_bloom_convolution_center_uv

```python
@override_bloom_convolution_center_uv.setter
def override_bloom_convolution_center_uv(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_bloom_convolution_pre_filter_min"></a>

#### override_bloom_convolution_pre_filter_min

```python
@property
def override_bloom_convolution_pre_filter_min() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_bloom_convolution_pre_filter_min"></a>

#### override_bloom_convolution_pre_filter_min

```python
@override_bloom_convolution_pre_filter_min.setter
def override_bloom_convolution_pre_filter_min(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_bloom_convolution_pre_filter_max"></a>

#### override_bloom_convolution_pre_filter_max

```python
@property
def override_bloom_convolution_pre_filter_max() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_bloom_convolution_pre_filter_max"></a>

#### override_bloom_convolution_pre_filter_max

```python
@override_bloom_convolution_pre_filter_max.setter
def override_bloom_convolution_pre_filter_max(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_bloom_convolution_pre_filter_mult"></a>

#### override_bloom_convolution_pre_filter_mult

```python
@property
def override_bloom_convolution_pre_filter_mult() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_bloom_convolution_pre_filter_mult"></a>

#### override_bloom_convolution_pre_filter_mult

```python
@override_bloom_convolution_pre_filter_mult.setter
def override_bloom_convolution_pre_filter_mult(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_bloom_convolution_buffer_scale"></a>

#### override_bloom_convolution_buffer_scale

```python
@property
def override_bloom_convolution_buffer_scale() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_bloom_convolution_buffer_scale"></a>

#### override_bloom_convolution_buffer_scale

```python
@override_bloom_convolution_buffer_scale.setter
def override_bloom_convolution_buffer_scale(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_bloom_dirt_mask_intensity"></a>

#### override_bloom_dirt_mask_intensity

```python
@property
def override_bloom_dirt_mask_intensity() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_bloom_dirt_mask_intensity"></a>

#### override_bloom_dirt_mask_intensity

```python
@override_bloom_dirt_mask_intensity.setter
def override_bloom_dirt_mask_intensity(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_bloom_dirt_mask_tint"></a>

#### override_bloom_dirt_mask_tint

```python
@property
def override_bloom_dirt_mask_tint() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_bloom_dirt_mask_tint"></a>

#### override_bloom_dirt_mask_tint

```python
@override_bloom_dirt_mask_tint.setter
def override_bloom_dirt_mask_tint(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_bloom_dirt_mask"></a>

#### override_bloom_dirt_mask

```python
@property
def override_bloom_dirt_mask() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_bloom_dirt_mask"></a>

#### override_bloom_dirt_mask

```python
@override_bloom_dirt_mask.setter
def override_bloom_dirt_mask(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_camera_shutter_speed"></a>

#### override_camera_shutter_speed

```python
@property
def override_camera_shutter_speed() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_camera_shutter_speed"></a>

#### override_camera_shutter_speed

```python
@override_camera_shutter_speed.setter
def override_camera_shutter_speed(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_camera_iso"></a>

#### override_camera_iso

```python
@property
def override_camera_iso() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_camera_iso"></a>

#### override_camera_iso

```python
@override_camera_iso.setter
def override_camera_iso(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_auto_exposure_method"></a>

#### override_auto_exposure_method

```python
@property
def override_auto_exposure_method() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_auto_exposure_method"></a>

#### override_auto_exposure_method

```python
@override_auto_exposure_method.setter
def override_auto_exposure_method(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_auto_exposure_low_percent"></a>

#### override_auto_exposure_low_percent

```python
@property
def override_auto_exposure_low_percent() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_auto_exposure_low_percent"></a>

#### override_auto_exposure_low_percent

```python
@override_auto_exposure_low_percent.setter
def override_auto_exposure_low_percent(value: bool) -> None
```

<a id="unreal.PostProcessSettings.b_override_eye_adaptation_low_percent"></a>

#### b_override_eye_adaptation_low_percent

```python
@property
def b_override_eye_adaptation_low_percent() -> bool
```

deprecated: 'b_override_eye_adaptation_low_percent' was renamed to 'override_auto_exposure_low_percent'.

<a id="unreal.PostProcessSettings.b_override_eye_adaptation_low_percent"></a>

#### b_override_eye_adaptation_low_percent

```python
@b_override_eye_adaptation_low_percent.setter
def b_override_eye_adaptation_low_percent(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_auto_exposure_high_percent"></a>

#### override_auto_exposure_high_percent

```python
@property
def override_auto_exposure_high_percent() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_auto_exposure_high_percent"></a>

#### override_auto_exposure_high_percent

```python
@override_auto_exposure_high_percent.setter
def override_auto_exposure_high_percent(value: bool) -> None
```

<a id="unreal.PostProcessSettings.b_override_eye_adaptation_high_percent"></a>

#### b_override_eye_adaptation_high_percent

```python
@property
def b_override_eye_adaptation_high_percent() -> bool
```

deprecated: 'b_override_eye_adaptation_high_percent' was renamed to 'override_auto_exposure_high_percent'.

<a id="unreal.PostProcessSettings.b_override_eye_adaptation_high_percent"></a>

#### b_override_eye_adaptation_high_percent

```python
@b_override_eye_adaptation_high_percent.setter
def b_override_eye_adaptation_high_percent(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_auto_exposure_min_brightness"></a>

#### override_auto_exposure_min_brightness

```python
@property
def override_auto_exposure_min_brightness() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_auto_exposure_min_brightness"></a>

#### override_auto_exposure_min_brightness

```python
@override_auto_exposure_min_brightness.setter
def override_auto_exposure_min_brightness(value: bool) -> None
```

<a id="unreal.PostProcessSettings.b_override_eye_adaptation_min_brightness"></a>

#### b_override_eye_adaptation_min_brightness

```python
@property
def b_override_eye_adaptation_min_brightness() -> bool
```

deprecated: 'b_override_eye_adaptation_min_brightness' was renamed to 'override_auto_exposure_min_brightness'.

<a id="unreal.PostProcessSettings.b_override_eye_adaptation_min_brightness"></a>

#### b_override_eye_adaptation_min_brightness

```python
@b_override_eye_adaptation_min_brightness.setter
def b_override_eye_adaptation_min_brightness(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_auto_exposure_max_brightness"></a>

#### override_auto_exposure_max_brightness

```python
@property
def override_auto_exposure_max_brightness() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_auto_exposure_max_brightness"></a>

#### override_auto_exposure_max_brightness

```python
@override_auto_exposure_max_brightness.setter
def override_auto_exposure_max_brightness(value: bool) -> None
```

<a id="unreal.PostProcessSettings.b_override_eye_adaptation_max_brightness"></a>

#### b_override_eye_adaptation_max_brightness

```python
@property
def b_override_eye_adaptation_max_brightness() -> bool
```

deprecated: 'b_override_eye_adaptation_max_brightness' was renamed to 'override_auto_exposure_max_brightness'.

<a id="unreal.PostProcessSettings.b_override_eye_adaptation_max_brightness"></a>

#### b_override_eye_adaptation_max_brightness

```python
@b_override_eye_adaptation_max_brightness.setter
def b_override_eye_adaptation_max_brightness(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_auto_exposure_speed_up"></a>

#### override_auto_exposure_speed_up

```python
@property
def override_auto_exposure_speed_up() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_auto_exposure_speed_up"></a>

#### override_auto_exposure_speed_up

```python
@override_auto_exposure_speed_up.setter
def override_auto_exposure_speed_up(value: bool) -> None
```

<a id="unreal.PostProcessSettings.b_override_eye_adaption_speed_up"></a>

#### b_override_eye_adaption_speed_up

```python
@property
def b_override_eye_adaption_speed_up() -> bool
```

deprecated: 'b_override_eye_adaption_speed_up' was renamed to 'override_auto_exposure_speed_up'.

<a id="unreal.PostProcessSettings.b_override_eye_adaption_speed_up"></a>

#### b_override_eye_adaption_speed_up

```python
@b_override_eye_adaption_speed_up.setter
def b_override_eye_adaption_speed_up(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_auto_exposure_speed_down"></a>

#### override_auto_exposure_speed_down

```python
@property
def override_auto_exposure_speed_down() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_auto_exposure_speed_down"></a>

#### override_auto_exposure_speed_down

```python
@override_auto_exposure_speed_down.setter
def override_auto_exposure_speed_down(value: bool) -> None
```

<a id="unreal.PostProcessSettings.b_override_eye_adaption_speed_down"></a>

#### b_override_eye_adaption_speed_down

```python
@property
def b_override_eye_adaption_speed_down() -> bool
```

deprecated: 'b_override_eye_adaption_speed_down' was renamed to 'override_auto_exposure_speed_down'.

<a id="unreal.PostProcessSettings.b_override_eye_adaption_speed_down"></a>

#### b_override_eye_adaption_speed_down

```python
@b_override_eye_adaption_speed_down.setter
def b_override_eye_adaption_speed_down(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_auto_exposure_bias"></a>

#### override_auto_exposure_bias

```python
@property
def override_auto_exposure_bias() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_auto_exposure_bias"></a>

#### override_auto_exposure_bias

```python
@override_auto_exposure_bias.setter
def override_auto_exposure_bias(value: bool) -> None
```

<a id="unreal.PostProcessSettings.b_override_exposure_offset"></a>

#### b_override_exposure_offset

```python
@property
def b_override_exposure_offset() -> bool
```

deprecated: 'b_override_exposure_offset' was renamed to 'override_auto_exposure_bias'.

<a id="unreal.PostProcessSettings.b_override_exposure_offset"></a>

#### b_override_exposure_offset

```python
@b_override_exposure_offset.setter
def b_override_exposure_offset(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_auto_exposure_bias_curve"></a>

#### override_auto_exposure_bias_curve

```python
@property
def override_auto_exposure_bias_curve() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_auto_exposure_bias_curve"></a>

#### override_auto_exposure_bias_curve

```python
@override_auto_exposure_bias_curve.setter
def override_auto_exposure_bias_curve(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_auto_exposure_meter_mask"></a>

#### override_auto_exposure_meter_mask

```python
@property
def override_auto_exposure_meter_mask() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_auto_exposure_meter_mask"></a>

#### override_auto_exposure_meter_mask

```python
@override_auto_exposure_meter_mask.setter
def override_auto_exposure_meter_mask(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_auto_exposure_apply_physical_camera_exposure"></a>

#### override_auto_exposure_apply_physical_camera_exposure

```python
@property
def override_auto_exposure_apply_physical_camera_exposure() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_auto_exposure_apply_physical_camera_exposure"></a>

#### override_auto_exposure_apply_physical_camera_exposure

```python
@override_auto_exposure_apply_physical_camera_exposure.setter
def override_auto_exposure_apply_physical_camera_exposure(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_histogram_log_min"></a>

#### override_histogram_log_min

```python
@property
def override_histogram_log_min() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_histogram_log_min"></a>

#### override_histogram_log_min

```python
@override_histogram_log_min.setter
def override_histogram_log_min(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_histogram_log_max"></a>

#### override_histogram_log_max

```python
@property
def override_histogram_log_max() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_histogram_log_max"></a>

#### override_histogram_log_max

```python
@override_histogram_log_max.setter
def override_histogram_log_max(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_local_exposure_method"></a>

#### override_local_exposure_method

```python
@property
def override_local_exposure_method() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_local_exposure_method"></a>

#### override_local_exposure_method

```python
@override_local_exposure_method.setter
def override_local_exposure_method(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_local_exposure_highlight_contrast_scale"></a>

#### override_local_exposure_highlight_contrast_scale

```python
@property
def override_local_exposure_highlight_contrast_scale() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_local_exposure_highlight_contrast_scale"></a>

#### override_local_exposure_highlight_contrast_scale

```python
@override_local_exposure_highlight_contrast_scale.setter
def override_local_exposure_highlight_contrast_scale(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_local_exposure_shadow_contrast_scale"></a>

#### override_local_exposure_shadow_contrast_scale

```python
@property
def override_local_exposure_shadow_contrast_scale() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_local_exposure_shadow_contrast_scale"></a>

#### override_local_exposure_shadow_contrast_scale

```python
@override_local_exposure_shadow_contrast_scale.setter
def override_local_exposure_shadow_contrast_scale(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_local_exposure_highlight_contrast_curve"></a>

#### override_local_exposure_highlight_contrast_curve

```python
@property
def override_local_exposure_highlight_contrast_curve() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_local_exposure_highlight_contrast_curve"></a>

#### override_local_exposure_highlight_contrast_curve

```python
@override_local_exposure_highlight_contrast_curve.setter
def override_local_exposure_highlight_contrast_curve(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_local_exposure_shadow_contrast_curve"></a>

#### override_local_exposure_shadow_contrast_curve

```python
@property
def override_local_exposure_shadow_contrast_curve() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_local_exposure_shadow_contrast_curve"></a>

#### override_local_exposure_shadow_contrast_curve

```python
@override_local_exposure_shadow_contrast_curve.setter
def override_local_exposure_shadow_contrast_curve(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_local_exposure_highlight_threshold"></a>

#### override_local_exposure_highlight_threshold

```python
@property
def override_local_exposure_highlight_threshold() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_local_exposure_highlight_threshold"></a>

#### override_local_exposure_highlight_threshold

```python
@override_local_exposure_highlight_threshold.setter
def override_local_exposure_highlight_threshold(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_local_exposure_shadow_threshold"></a>

#### override_local_exposure_shadow_threshold

```python
@property
def override_local_exposure_shadow_threshold() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_local_exposure_shadow_threshold"></a>

#### override_local_exposure_shadow_threshold

```python
@override_local_exposure_shadow_threshold.setter
def override_local_exposure_shadow_threshold(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_local_exposure_detail_strength"></a>

#### override_local_exposure_detail_strength

```python
@property
def override_local_exposure_detail_strength() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_local_exposure_detail_strength"></a>

#### override_local_exposure_detail_strength

```python
@override_local_exposure_detail_strength.setter
def override_local_exposure_detail_strength(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_local_exposure_blurred_luminance_blend"></a>

#### override_local_exposure_blurred_luminance_blend

```python
@property
def override_local_exposure_blurred_luminance_blend() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_local_exposure_blurred_luminance_blend"></a>

#### override_local_exposure_blurred_luminance_blend

```python
@override_local_exposure_blurred_luminance_blend.setter
def override_local_exposure_blurred_luminance_blend(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_local_exposure_blurred_luminance_kernel_size_percent"></a>

#### override_local_exposure_blurred_luminance_kernel_size_percent

```python
@property
def override_local_exposure_blurred_luminance_kernel_size_percent() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_local_exposure_blurred_luminance_kernel_size_percent"></a>

#### override_local_exposure_blurred_luminance_kernel_size_percent

```python
@override_local_exposure_blurred_luminance_kernel_size_percent.setter
def override_local_exposure_blurred_luminance_kernel_size_percent(
        value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_local_exposure_middle_grey_bias"></a>

#### override_local_exposure_middle_grey_bias

```python
@property
def override_local_exposure_middle_grey_bias() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_local_exposure_middle_grey_bias"></a>

#### override_local_exposure_middle_grey_bias

```python
@override_local_exposure_middle_grey_bias.setter
def override_local_exposure_middle_grey_bias(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_lens_flare_intensity"></a>

#### override_lens_flare_intensity

```python
@property
def override_lens_flare_intensity() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_lens_flare_intensity"></a>

#### override_lens_flare_intensity

```python
@override_lens_flare_intensity.setter
def override_lens_flare_intensity(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_lens_flare_tint"></a>

#### override_lens_flare_tint

```python
@property
def override_lens_flare_tint() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_lens_flare_tint"></a>

#### override_lens_flare_tint

```python
@override_lens_flare_tint.setter
def override_lens_flare_tint(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_lens_flare_tints"></a>

#### override_lens_flare_tints

```python
@property
def override_lens_flare_tints() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_lens_flare_tints"></a>

#### override_lens_flare_tints

```python
@override_lens_flare_tints.setter
def override_lens_flare_tints(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_lens_flare_bokeh_size"></a>

#### override_lens_flare_bokeh_size

```python
@property
def override_lens_flare_bokeh_size() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_lens_flare_bokeh_size"></a>

#### override_lens_flare_bokeh_size

```python
@override_lens_flare_bokeh_size.setter
def override_lens_flare_bokeh_size(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_lens_flare_bokeh_shape"></a>

#### override_lens_flare_bokeh_shape

```python
@property
def override_lens_flare_bokeh_shape() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_lens_flare_bokeh_shape"></a>

#### override_lens_flare_bokeh_shape

```python
@override_lens_flare_bokeh_shape.setter
def override_lens_flare_bokeh_shape(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_lens_flare_threshold"></a>

#### override_lens_flare_threshold

```python
@property
def override_lens_flare_threshold() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_lens_flare_threshold"></a>

#### override_lens_flare_threshold

```python
@override_lens_flare_threshold.setter
def override_lens_flare_threshold(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_vignette_intensity"></a>

#### override_vignette_intensity

```python
@property
def override_vignette_intensity() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_vignette_intensity"></a>

#### override_vignette_intensity

```python
@override_vignette_intensity.setter
def override_vignette_intensity(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_sharpen"></a>

#### override_sharpen

```python
@property
def override_sharpen() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_sharpen"></a>

#### override_sharpen

```python
@override_sharpen.setter
def override_sharpen(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_film_grain_intensity"></a>

#### override_film_grain_intensity

```python
@property
def override_film_grain_intensity() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_film_grain_intensity"></a>

#### override_film_grain_intensity

```python
@override_film_grain_intensity.setter
def override_film_grain_intensity(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_film_grain_intensity_shadows"></a>

#### override_film_grain_intensity_shadows

```python
@property
def override_film_grain_intensity_shadows() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_film_grain_intensity_shadows"></a>

#### override_film_grain_intensity_shadows

```python
@override_film_grain_intensity_shadows.setter
def override_film_grain_intensity_shadows(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_film_grain_intensity_midtones"></a>

#### override_film_grain_intensity_midtones

```python
@property
def override_film_grain_intensity_midtones() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_film_grain_intensity_midtones"></a>

#### override_film_grain_intensity_midtones

```python
@override_film_grain_intensity_midtones.setter
def override_film_grain_intensity_midtones(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_film_grain_intensity_highlights"></a>

#### override_film_grain_intensity_highlights

```python
@property
def override_film_grain_intensity_highlights() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_film_grain_intensity_highlights"></a>

#### override_film_grain_intensity_highlights

```python
@override_film_grain_intensity_highlights.setter
def override_film_grain_intensity_highlights(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_film_grain_shadows_max"></a>

#### override_film_grain_shadows_max

```python
@property
def override_film_grain_shadows_max() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_film_grain_shadows_max"></a>

#### override_film_grain_shadows_max

```python
@override_film_grain_shadows_max.setter
def override_film_grain_shadows_max(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_film_grain_highlights_min"></a>

#### override_film_grain_highlights_min

```python
@property
def override_film_grain_highlights_min() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_film_grain_highlights_min"></a>

#### override_film_grain_highlights_min

```python
@override_film_grain_highlights_min.setter
def override_film_grain_highlights_min(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_film_grain_highlights_max"></a>

#### override_film_grain_highlights_max

```python
@property
def override_film_grain_highlights_max() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_film_grain_highlights_max"></a>

#### override_film_grain_highlights_max

```python
@override_film_grain_highlights_max.setter
def override_film_grain_highlights_max(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_film_grain_texel_size"></a>

#### override_film_grain_texel_size

```python
@property
def override_film_grain_texel_size() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_film_grain_texel_size"></a>

#### override_film_grain_texel_size

```python
@override_film_grain_texel_size.setter
def override_film_grain_texel_size(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_film_grain_texture"></a>

#### override_film_grain_texture

```python
@property
def override_film_grain_texture() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_film_grain_texture"></a>

#### override_film_grain_texture

```python
@override_film_grain_texture.setter
def override_film_grain_texture(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_ambient_occlusion_intensity"></a>

#### override_ambient_occlusion_intensity

```python
@property
def override_ambient_occlusion_intensity() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_ambient_occlusion_intensity"></a>

#### override_ambient_occlusion_intensity

```python
@override_ambient_occlusion_intensity.setter
def override_ambient_occlusion_intensity(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_ambient_occlusion_static_fraction"></a>

#### override_ambient_occlusion_static_fraction

```python
@property
def override_ambient_occlusion_static_fraction() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_ambient_occlusion_static_fraction"></a>

#### override_ambient_occlusion_static_fraction

```python
@override_ambient_occlusion_static_fraction.setter
def override_ambient_occlusion_static_fraction(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_ambient_occlusion_radius"></a>

#### override_ambient_occlusion_radius

```python
@property
def override_ambient_occlusion_radius() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_ambient_occlusion_radius"></a>

#### override_ambient_occlusion_radius

```python
@override_ambient_occlusion_radius.setter
def override_ambient_occlusion_radius(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_ambient_occlusion_fade_distance"></a>

#### override_ambient_occlusion_fade_distance

```python
@property
def override_ambient_occlusion_fade_distance() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_ambient_occlusion_fade_distance"></a>

#### override_ambient_occlusion_fade_distance

```python
@override_ambient_occlusion_fade_distance.setter
def override_ambient_occlusion_fade_distance(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_ambient_occlusion_fade_radius"></a>

#### override_ambient_occlusion_fade_radius

```python
@property
def override_ambient_occlusion_fade_radius() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_ambient_occlusion_fade_radius"></a>

#### override_ambient_occlusion_fade_radius

```python
@override_ambient_occlusion_fade_radius.setter
def override_ambient_occlusion_fade_radius(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_ambient_occlusion_radius_in_ws"></a>

#### override_ambient_occlusion_radius_in_ws

```python
@property
def override_ambient_occlusion_radius_in_ws() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_ambient_occlusion_radius_in_ws"></a>

#### override_ambient_occlusion_radius_in_ws

```python
@override_ambient_occlusion_radius_in_ws.setter
def override_ambient_occlusion_radius_in_ws(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_ambient_occlusion_power"></a>

#### override_ambient_occlusion_power

```python
@property
def override_ambient_occlusion_power() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_ambient_occlusion_power"></a>

#### override_ambient_occlusion_power

```python
@override_ambient_occlusion_power.setter
def override_ambient_occlusion_power(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_ambient_occlusion_bias"></a>

#### override_ambient_occlusion_bias

```python
@property
def override_ambient_occlusion_bias() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_ambient_occlusion_bias"></a>

#### override_ambient_occlusion_bias

```python
@override_ambient_occlusion_bias.setter
def override_ambient_occlusion_bias(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_ambient_occlusion_quality"></a>

#### override_ambient_occlusion_quality

```python
@property
def override_ambient_occlusion_quality() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_ambient_occlusion_quality"></a>

#### override_ambient_occlusion_quality

```python
@override_ambient_occlusion_quality.setter
def override_ambient_occlusion_quality(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_ambient_occlusion_mip_blend"></a>

#### override_ambient_occlusion_mip_blend

```python
@property
def override_ambient_occlusion_mip_blend() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_ambient_occlusion_mip_blend"></a>

#### override_ambient_occlusion_mip_blend

```python
@override_ambient_occlusion_mip_blend.setter
def override_ambient_occlusion_mip_blend(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_ambient_occlusion_mip_scale"></a>

#### override_ambient_occlusion_mip_scale

```python
@property
def override_ambient_occlusion_mip_scale() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_ambient_occlusion_mip_scale"></a>

#### override_ambient_occlusion_mip_scale

```python
@override_ambient_occlusion_mip_scale.setter
def override_ambient_occlusion_mip_scale(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_ambient_occlusion_mip_threshold"></a>

#### override_ambient_occlusion_mip_threshold

```python
@property
def override_ambient_occlusion_mip_threshold() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_ambient_occlusion_mip_threshold"></a>

#### override_ambient_occlusion_mip_threshold

```python
@override_ambient_occlusion_mip_threshold.setter
def override_ambient_occlusion_mip_threshold(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_ambient_occlusion_temporal_blend_weight"></a>

#### override_ambient_occlusion_temporal_blend_weight

```python
@property
def override_ambient_occlusion_temporal_blend_weight() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_ambient_occlusion_temporal_blend_weight"></a>

#### override_ambient_occlusion_temporal_blend_weight

```python
@override_ambient_occlusion_temporal_blend_weight.setter
def override_ambient_occlusion_temporal_blend_weight(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_ray_tracing_ao"></a>

#### override_ray_tracing_ao

```python
@property
def override_ray_tracing_ao() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_ray_tracing_ao"></a>

#### override_ray_tracing_ao

```python
@override_ray_tracing_ao.setter
def override_ray_tracing_ao(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_ray_tracing_ao_samples_per_pixel"></a>

#### override_ray_tracing_ao_samples_per_pixel

```python
@property
def override_ray_tracing_ao_samples_per_pixel() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_ray_tracing_ao_samples_per_pixel"></a>

#### override_ray_tracing_ao_samples_per_pixel

```python
@override_ray_tracing_ao_samples_per_pixel.setter
def override_ray_tracing_ao_samples_per_pixel(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_ray_tracing_ao_intensity"></a>

#### override_ray_tracing_ao_intensity

```python
@property
def override_ray_tracing_ao_intensity() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_ray_tracing_ao_intensity"></a>

#### override_ray_tracing_ao_intensity

```python
@override_ray_tracing_ao_intensity.setter
def override_ray_tracing_ao_intensity(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_ray_tracing_ao_radius"></a>

#### override_ray_tracing_ao_radius

```python
@property
def override_ray_tracing_ao_radius() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_ray_tracing_ao_radius"></a>

#### override_ray_tracing_ao_radius

```python
@override_ray_tracing_ao_radius.setter
def override_ray_tracing_ao_radius(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_indirect_lighting_color"></a>

#### override_indirect_lighting_color

```python
@property
def override_indirect_lighting_color() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_indirect_lighting_color"></a>

#### override_indirect_lighting_color

```python
@override_indirect_lighting_color.setter
def override_indirect_lighting_color(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_indirect_lighting_intensity"></a>

#### override_indirect_lighting_intensity

```python
@property
def override_indirect_lighting_intensity() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_indirect_lighting_intensity"></a>

#### override_indirect_lighting_intensity

```python
@override_indirect_lighting_intensity.setter
def override_indirect_lighting_intensity(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_color_grading_intensity"></a>

#### override_color_grading_intensity

```python
@property
def override_color_grading_intensity() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_color_grading_intensity"></a>

#### override_color_grading_intensity

```python
@override_color_grading_intensity.setter
def override_color_grading_intensity(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_color_grading_lut"></a>

#### override_color_grading_lut

```python
@property
def override_color_grading_lut() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_color_grading_lut"></a>

#### override_color_grading_lut

```python
@override_color_grading_lut.setter
def override_color_grading_lut(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_depth_of_field_focal_distance"></a>

#### override_depth_of_field_focal_distance

```python
@property
def override_depth_of_field_focal_distance() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_depth_of_field_focal_distance"></a>

#### override_depth_of_field_focal_distance

```python
@override_depth_of_field_focal_distance.setter
def override_depth_of_field_focal_distance(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_depth_of_field_fstop"></a>

#### override_depth_of_field_fstop

```python
@property
def override_depth_of_field_fstop() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_depth_of_field_fstop"></a>

#### override_depth_of_field_fstop

```python
@override_depth_of_field_fstop.setter
def override_depth_of_field_fstop(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_depth_of_field_min_fstop"></a>

#### override_depth_of_field_min_fstop

```python
@property
def override_depth_of_field_min_fstop() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_depth_of_field_min_fstop"></a>

#### override_depth_of_field_min_fstop

```python
@override_depth_of_field_min_fstop.setter
def override_depth_of_field_min_fstop(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_depth_of_field_blade_count"></a>

#### override_depth_of_field_blade_count

```python
@property
def override_depth_of_field_blade_count() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_depth_of_field_blade_count"></a>

#### override_depth_of_field_blade_count

```python
@override_depth_of_field_blade_count.setter
def override_depth_of_field_blade_count(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_depth_of_field_sensor_width"></a>

#### override_depth_of_field_sensor_width

```python
@property
def override_depth_of_field_sensor_width() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_depth_of_field_sensor_width"></a>

#### override_depth_of_field_sensor_width

```python
@override_depth_of_field_sensor_width.setter
def override_depth_of_field_sensor_width(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_depth_of_field_squeeze_factor"></a>

#### override_depth_of_field_squeeze_factor

```python
@property
def override_depth_of_field_squeeze_factor() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_depth_of_field_squeeze_factor"></a>

#### override_depth_of_field_squeeze_factor

```python
@override_depth_of_field_squeeze_factor.setter
def override_depth_of_field_squeeze_factor(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_depth_of_field_depth_blur_radius"></a>

#### override_depth_of_field_depth_blur_radius

```python
@property
def override_depth_of_field_depth_blur_radius() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_depth_of_field_depth_blur_radius"></a>

#### override_depth_of_field_depth_blur_radius

```python
@override_depth_of_field_depth_blur_radius.setter
def override_depth_of_field_depth_blur_radius(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_depth_of_field_use_hair_depth"></a>

#### override_depth_of_field_use_hair_depth

```python
@property
def override_depth_of_field_use_hair_depth() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_depth_of_field_use_hair_depth"></a>

#### override_depth_of_field_use_hair_depth

```python
@override_depth_of_field_use_hair_depth.setter
def override_depth_of_field_use_hair_depth(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_depth_of_field_depth_blur_amount"></a>

#### override_depth_of_field_depth_blur_amount

```python
@property
def override_depth_of_field_depth_blur_amount() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_depth_of_field_depth_blur_amount"></a>

#### override_depth_of_field_depth_blur_amount

```python
@override_depth_of_field_depth_blur_amount.setter
def override_depth_of_field_depth_blur_amount(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_depth_of_field_focal_region"></a>

#### override_depth_of_field_focal_region

```python
@property
def override_depth_of_field_focal_region() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_depth_of_field_focal_region"></a>

#### override_depth_of_field_focal_region

```python
@override_depth_of_field_focal_region.setter
def override_depth_of_field_focal_region(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_depth_of_field_near_transition_region"></a>

#### override_depth_of_field_near_transition_region

```python
@property
def override_depth_of_field_near_transition_region() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_depth_of_field_near_transition_region"></a>

#### override_depth_of_field_near_transition_region

```python
@override_depth_of_field_near_transition_region.setter
def override_depth_of_field_near_transition_region(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_depth_of_field_far_transition_region"></a>

#### override_depth_of_field_far_transition_region

```python
@property
def override_depth_of_field_far_transition_region() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_depth_of_field_far_transition_region"></a>

#### override_depth_of_field_far_transition_region

```python
@override_depth_of_field_far_transition_region.setter
def override_depth_of_field_far_transition_region(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_depth_of_field_scale"></a>

#### override_depth_of_field_scale

```python
@property
def override_depth_of_field_scale() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_depth_of_field_scale"></a>

#### override_depth_of_field_scale

```python
@override_depth_of_field_scale.setter
def override_depth_of_field_scale(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_depth_of_field_near_blur_size"></a>

#### override_depth_of_field_near_blur_size

```python
@property
def override_depth_of_field_near_blur_size() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_depth_of_field_near_blur_size"></a>

#### override_depth_of_field_near_blur_size

```python
@override_depth_of_field_near_blur_size.setter
def override_depth_of_field_near_blur_size(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_depth_of_field_far_blur_size"></a>

#### override_depth_of_field_far_blur_size

```python
@property
def override_depth_of_field_far_blur_size() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_depth_of_field_far_blur_size"></a>

#### override_depth_of_field_far_blur_size

```python
@override_depth_of_field_far_blur_size.setter
def override_depth_of_field_far_blur_size(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_mobile_hq_gaussian"></a>

#### override_mobile_hq_gaussian

```python
@property
def override_mobile_hq_gaussian() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_mobile_hq_gaussian"></a>

#### override_mobile_hq_gaussian

```python
@override_mobile_hq_gaussian.setter
def override_mobile_hq_gaussian(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_depth_of_field_occlusion"></a>

#### override_depth_of_field_occlusion

```python
@property
def override_depth_of_field_occlusion() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_depth_of_field_occlusion"></a>

#### override_depth_of_field_occlusion

```python
@override_depth_of_field_occlusion.setter
def override_depth_of_field_occlusion(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_depth_of_field_sky_focus_distance"></a>

#### override_depth_of_field_sky_focus_distance

```python
@property
def override_depth_of_field_sky_focus_distance() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_depth_of_field_sky_focus_distance"></a>

#### override_depth_of_field_sky_focus_distance

```python
@override_depth_of_field_sky_focus_distance.setter
def override_depth_of_field_sky_focus_distance(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_depth_of_field_vignette_size"></a>

#### override_depth_of_field_vignette_size

```python
@property
def override_depth_of_field_vignette_size() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_depth_of_field_vignette_size"></a>

#### override_depth_of_field_vignette_size

```python
@override_depth_of_field_vignette_size.setter
def override_depth_of_field_vignette_size(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_motion_blur_amount"></a>

#### override_motion_blur_amount

```python
@property
def override_motion_blur_amount() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_motion_blur_amount"></a>

#### override_motion_blur_amount

```python
@override_motion_blur_amount.setter
def override_motion_blur_amount(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_motion_blur_max"></a>

#### override_motion_blur_max

```python
@property
def override_motion_blur_max() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_motion_blur_max"></a>

#### override_motion_blur_max

```python
@override_motion_blur_max.setter
def override_motion_blur_max(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_motion_blur_target_fps"></a>

#### override_motion_blur_target_fps

```python
@property
def override_motion_blur_target_fps() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_motion_blur_target_fps"></a>

#### override_motion_blur_target_fps

```python
@override_motion_blur_target_fps.setter
def override_motion_blur_target_fps(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_motion_blur_per_object_size"></a>

#### override_motion_blur_per_object_size

```python
@property
def override_motion_blur_per_object_size() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_motion_blur_per_object_size"></a>

#### override_motion_blur_per_object_size

```python
@override_motion_blur_per_object_size.setter
def override_motion_blur_per_object_size(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_reflection_method"></a>

#### override_reflection_method

```python
@property
def override_reflection_method() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_reflection_method"></a>

#### override_reflection_method

```python
@override_reflection_method.setter
def override_reflection_method(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_lumen_reflection_quality"></a>

#### override_lumen_reflection_quality

```python
@property
def override_lumen_reflection_quality() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_lumen_reflection_quality"></a>

#### override_lumen_reflection_quality

```python
@override_lumen_reflection_quality.setter
def override_lumen_reflection_quality(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_screen_space_reflection_intensity"></a>

#### override_screen_space_reflection_intensity

```python
@property
def override_screen_space_reflection_intensity() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_screen_space_reflection_intensity"></a>

#### override_screen_space_reflection_intensity

```python
@override_screen_space_reflection_intensity.setter
def override_screen_space_reflection_intensity(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_screen_space_reflection_quality"></a>

#### override_screen_space_reflection_quality

```python
@property
def override_screen_space_reflection_quality() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_screen_space_reflection_quality"></a>

#### override_screen_space_reflection_quality

```python
@override_screen_space_reflection_quality.setter
def override_screen_space_reflection_quality(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_screen_space_reflection_max_roughness"></a>

#### override_screen_space_reflection_max_roughness

```python
@property
def override_screen_space_reflection_max_roughness() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_screen_space_reflection_max_roughness"></a>

#### override_screen_space_reflection_max_roughness

```python
@override_screen_space_reflection_max_roughness.setter
def override_screen_space_reflection_max_roughness(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_screen_space_reflection_roughness_scale"></a>

#### override_screen_space_reflection_roughness_scale

```python
@property
def override_screen_space_reflection_roughness_scale() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_screen_space_reflection_roughness_scale"></a>

#### override_screen_space_reflection_roughness_scale

```python
@override_screen_space_reflection_roughness_scale.setter
def override_screen_space_reflection_roughness_scale(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_user_flags"></a>

#### override_user_flags

```python
@property
def override_user_flags() -> bool
```

(bool):  [Read-Write] TODO: look useless...

<a id="unreal.PostProcessSettings.override_user_flags"></a>

#### override_user_flags

```python
@override_user_flags.setter
def override_user_flags(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_ray_tracing_reflections_max_roughness"></a>

#### override_ray_tracing_reflections_max_roughness

```python
@property
def override_ray_tracing_reflections_max_roughness() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_ray_tracing_reflections_max_roughness"></a>

#### override_ray_tracing_reflections_max_roughness

```python
@override_ray_tracing_reflections_max_roughness.setter
def override_ray_tracing_reflections_max_roughness(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_ray_tracing_reflections_max_bounces"></a>

#### override_ray_tracing_reflections_max_bounces

```python
@property
def override_ray_tracing_reflections_max_bounces() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_ray_tracing_reflections_max_bounces"></a>

#### override_ray_tracing_reflections_max_bounces

```python
@override_ray_tracing_reflections_max_bounces.setter
def override_ray_tracing_reflections_max_bounces(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_ray_tracing_reflections_samples_per_pixel"></a>

#### override_ray_tracing_reflections_samples_per_pixel

```python
@property
def override_ray_tracing_reflections_samples_per_pixel() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_ray_tracing_reflections_samples_per_pixel"></a>

#### override_ray_tracing_reflections_samples_per_pixel

```python
@override_ray_tracing_reflections_samples_per_pixel.setter
def override_ray_tracing_reflections_samples_per_pixel(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_ray_tracing_reflections_shadows"></a>

#### override_ray_tracing_reflections_shadows

```python
@property
def override_ray_tracing_reflections_shadows() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_ray_tracing_reflections_shadows"></a>

#### override_ray_tracing_reflections_shadows

```python
@override_ray_tracing_reflections_shadows.setter
def override_ray_tracing_reflections_shadows(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_ray_tracing_reflections_translucency"></a>

#### override_ray_tracing_reflections_translucency

```python
@property
def override_ray_tracing_reflections_translucency() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_ray_tracing_reflections_translucency"></a>

#### override_ray_tracing_reflections_translucency

```python
@override_ray_tracing_reflections_translucency.setter
def override_ray_tracing_reflections_translucency(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_translucency_type"></a>

#### override_translucency_type

```python
@property
def override_translucency_type() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_translucency_type"></a>

#### override_translucency_type

```python
@override_translucency_type.setter
def override_translucency_type(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_ray_tracing_translucency_max_roughness"></a>

#### override_ray_tracing_translucency_max_roughness

```python
@property
def override_ray_tracing_translucency_max_roughness() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_ray_tracing_translucency_max_roughness"></a>

#### override_ray_tracing_translucency_max_roughness

```python
@override_ray_tracing_translucency_max_roughness.setter
def override_ray_tracing_translucency_max_roughness(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_ray_tracing_translucency_refraction_rays"></a>

#### override_ray_tracing_translucency_refraction_rays

```python
@property
def override_ray_tracing_translucency_refraction_rays() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_ray_tracing_translucency_refraction_rays"></a>

#### override_ray_tracing_translucency_refraction_rays

```python
@override_ray_tracing_translucency_refraction_rays.setter
def override_ray_tracing_translucency_refraction_rays(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_ray_tracing_translucency_samples_per_pixel"></a>

#### override_ray_tracing_translucency_samples_per_pixel

```python
@property
def override_ray_tracing_translucency_samples_per_pixel() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_ray_tracing_translucency_samples_per_pixel"></a>

#### override_ray_tracing_translucency_samples_per_pixel

```python
@override_ray_tracing_translucency_samples_per_pixel.setter
def override_ray_tracing_translucency_samples_per_pixel(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_ray_tracing_translucency_shadows"></a>

#### override_ray_tracing_translucency_shadows

```python
@property
def override_ray_tracing_translucency_shadows() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_ray_tracing_translucency_shadows"></a>

#### override_ray_tracing_translucency_shadows

```python
@override_ray_tracing_translucency_shadows.setter
def override_ray_tracing_translucency_shadows(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_ray_tracing_translucency_refraction"></a>

#### override_ray_tracing_translucency_refraction

```python
@property
def override_ray_tracing_translucency_refraction() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_ray_tracing_translucency_refraction"></a>

#### override_ray_tracing_translucency_refraction

```python
@override_ray_tracing_translucency_refraction.setter
def override_ray_tracing_translucency_refraction(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_dynamic_global_illumination_method"></a>

#### override_dynamic_global_illumination_method

```python
@property
def override_dynamic_global_illumination_method() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_dynamic_global_illumination_method"></a>

#### override_dynamic_global_illumination_method

```python
@override_dynamic_global_illumination_method.setter
def override_dynamic_global_illumination_method(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_lumen_scene_lighting_quality"></a>

#### override_lumen_scene_lighting_quality

```python
@property
def override_lumen_scene_lighting_quality() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_lumen_scene_lighting_quality"></a>

#### override_lumen_scene_lighting_quality

```python
@override_lumen_scene_lighting_quality.setter
def override_lumen_scene_lighting_quality(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_lumen_scene_detail"></a>

#### override_lumen_scene_detail

```python
@property
def override_lumen_scene_detail() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_lumen_scene_detail"></a>

#### override_lumen_scene_detail

```python
@override_lumen_scene_detail.setter
def override_lumen_scene_detail(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_lumen_scene_view_distance"></a>

#### override_lumen_scene_view_distance

```python
@property
def override_lumen_scene_view_distance() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_lumen_scene_view_distance"></a>

#### override_lumen_scene_view_distance

```python
@override_lumen_scene_view_distance.setter
def override_lumen_scene_view_distance(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_lumen_scene_lighting_update_speed"></a>

#### override_lumen_scene_lighting_update_speed

```python
@property
def override_lumen_scene_lighting_update_speed() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_lumen_scene_lighting_update_speed"></a>

#### override_lumen_scene_lighting_update_speed

```python
@override_lumen_scene_lighting_update_speed.setter
def override_lumen_scene_lighting_update_speed(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_lumen_final_gather_quality"></a>

#### override_lumen_final_gather_quality

```python
@property
def override_lumen_final_gather_quality() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_lumen_final_gather_quality"></a>

#### override_lumen_final_gather_quality

```python
@override_lumen_final_gather_quality.setter
def override_lumen_final_gather_quality(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_lumen_final_gather_lighting_update_speed"></a>

#### override_lumen_final_gather_lighting_update_speed

```python
@property
def override_lumen_final_gather_lighting_update_speed() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_lumen_final_gather_lighting_update_speed"></a>

#### override_lumen_final_gather_lighting_update_speed

```python
@override_lumen_final_gather_lighting_update_speed.setter
def override_lumen_final_gather_lighting_update_speed(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_lumen_final_gather_screen_traces"></a>

#### override_lumen_final_gather_screen_traces

```python
@property
def override_lumen_final_gather_screen_traces() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_lumen_final_gather_screen_traces"></a>

#### override_lumen_final_gather_screen_traces

```python
@override_lumen_final_gather_screen_traces.setter
def override_lumen_final_gather_screen_traces(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_lumen_max_trace_distance"></a>

#### override_lumen_max_trace_distance

```python
@property
def override_lumen_max_trace_distance() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_lumen_max_trace_distance"></a>

#### override_lumen_max_trace_distance

```python
@override_lumen_max_trace_distance.setter
def override_lumen_max_trace_distance(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_lumen_diffuse_color_boost"></a>

#### override_lumen_diffuse_color_boost

```python
@property
def override_lumen_diffuse_color_boost() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_lumen_diffuse_color_boost"></a>

#### override_lumen_diffuse_color_boost

```python
@override_lumen_diffuse_color_boost.setter
def override_lumen_diffuse_color_boost(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_lumen_skylight_leaking"></a>

#### override_lumen_skylight_leaking

```python
@property
def override_lumen_skylight_leaking() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_lumen_skylight_leaking"></a>

#### override_lumen_skylight_leaking

```python
@override_lumen_skylight_leaking.setter
def override_lumen_skylight_leaking(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_lumen_full_skylight_leaking_distance"></a>

#### override_lumen_full_skylight_leaking_distance

```python
@property
def override_lumen_full_skylight_leaking_distance() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_lumen_full_skylight_leaking_distance"></a>

#### override_lumen_full_skylight_leaking_distance

```python
@override_lumen_full_skylight_leaking_distance.setter
def override_lumen_full_skylight_leaking_distance(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_lumen_ray_lighting_mode"></a>

#### override_lumen_ray_lighting_mode

```python
@property
def override_lumen_ray_lighting_mode() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_lumen_ray_lighting_mode"></a>

#### override_lumen_ray_lighting_mode

```python
@override_lumen_ray_lighting_mode.setter
def override_lumen_ray_lighting_mode(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_lumen_reflections_screen_traces"></a>

#### override_lumen_reflections_screen_traces

```python
@property
def override_lumen_reflections_screen_traces() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_lumen_reflections_screen_traces"></a>

#### override_lumen_reflections_screen_traces

```python
@override_lumen_reflections_screen_traces.setter
def override_lumen_reflections_screen_traces(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_lumen_front_layer_translucency_reflections"></a>

#### override_lumen_front_layer_translucency_reflections

```python
@property
def override_lumen_front_layer_translucency_reflections() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_lumen_front_layer_translucency_reflections"></a>

#### override_lumen_front_layer_translucency_reflections

```python
@override_lumen_front_layer_translucency_reflections.setter
def override_lumen_front_layer_translucency_reflections(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_lumen_max_roughness_to_trace_reflections"></a>

#### override_lumen_max_roughness_to_trace_reflections

```python
@property
def override_lumen_max_roughness_to_trace_reflections() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_lumen_max_roughness_to_trace_reflections"></a>

#### override_lumen_max_roughness_to_trace_reflections

```python
@override_lumen_max_roughness_to_trace_reflections.setter
def override_lumen_max_roughness_to_trace_reflections(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_lumen_max_reflection_bounces"></a>

#### override_lumen_max_reflection_bounces

```python
@property
def override_lumen_max_reflection_bounces() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_lumen_max_reflection_bounces"></a>

#### override_lumen_max_reflection_bounces

```python
@override_lumen_max_reflection_bounces.setter
def override_lumen_max_reflection_bounces(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_lumen_max_refraction_bounces"></a>

#### override_lumen_max_refraction_bounces

```python
@property
def override_lumen_max_refraction_bounces() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_lumen_max_refraction_bounces"></a>

#### override_lumen_max_refraction_bounces

```python
@override_lumen_max_refraction_bounces.setter
def override_lumen_max_refraction_bounces(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_lumen_surface_cache_resolution"></a>

#### override_lumen_surface_cache_resolution

```python
@property
def override_lumen_surface_cache_resolution() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_lumen_surface_cache_resolution"></a>

#### override_lumen_surface_cache_resolution

```python
@override_lumen_surface_cache_resolution.setter
def override_lumen_surface_cache_resolution(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_ray_tracing_gi"></a>

#### override_ray_tracing_gi

```python
@property
def override_ray_tracing_gi() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_ray_tracing_gi"></a>

#### override_ray_tracing_gi

```python
@override_ray_tracing_gi.setter
def override_ray_tracing_gi(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_ray_tracing_gi_max_bounces"></a>

#### override_ray_tracing_gi_max_bounces

```python
@property
def override_ray_tracing_gi_max_bounces() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_ray_tracing_gi_max_bounces"></a>

#### override_ray_tracing_gi_max_bounces

```python
@override_ray_tracing_gi_max_bounces.setter
def override_ray_tracing_gi_max_bounces(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_ray_tracing_gi_samples_per_pixel"></a>

#### override_ray_tracing_gi_samples_per_pixel

```python
@property
def override_ray_tracing_gi_samples_per_pixel() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_ray_tracing_gi_samples_per_pixel"></a>

#### override_ray_tracing_gi_samples_per_pixel

```python
@override_ray_tracing_gi_samples_per_pixel.setter
def override_ray_tracing_gi_samples_per_pixel(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_path_tracing_max_bounces"></a>

#### override_path_tracing_max_bounces

```python
@property
def override_path_tracing_max_bounces() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_path_tracing_max_bounces"></a>

#### override_path_tracing_max_bounces

```python
@override_path_tracing_max_bounces.setter
def override_path_tracing_max_bounces(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_path_tracing_samples_per_pixel"></a>

#### override_path_tracing_samples_per_pixel

```python
@property
def override_path_tracing_samples_per_pixel() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_path_tracing_samples_per_pixel"></a>

#### override_path_tracing_samples_per_pixel

```python
@override_path_tracing_samples_per_pixel.setter
def override_path_tracing_samples_per_pixel(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_path_tracing_max_path_intensity"></a>

#### override_path_tracing_max_path_intensity

```python
@property
def override_path_tracing_max_path_intensity() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_path_tracing_max_path_intensity"></a>

#### override_path_tracing_max_path_intensity

```python
@override_path_tracing_max_path_intensity.setter
def override_path_tracing_max_path_intensity(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_path_tracing_enable_emissive_materials"></a>

#### override_path_tracing_enable_emissive_materials

```python
@property
def override_path_tracing_enable_emissive_materials() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_path_tracing_enable_emissive_materials"></a>

#### override_path_tracing_enable_emissive_materials

```python
@override_path_tracing_enable_emissive_materials.setter
def override_path_tracing_enable_emissive_materials(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_path_tracing_enable_reference_dof"></a>

#### override_path_tracing_enable_reference_dof

```python
@property
def override_path_tracing_enable_reference_dof() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_path_tracing_enable_reference_dof"></a>

#### override_path_tracing_enable_reference_dof

```python
@override_path_tracing_enable_reference_dof.setter
def override_path_tracing_enable_reference_dof(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_path_tracing_enable_reference_atmosphere"></a>

#### override_path_tracing_enable_reference_atmosphere

```python
@property
def override_path_tracing_enable_reference_atmosphere() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_path_tracing_enable_reference_atmosphere"></a>

#### override_path_tracing_enable_reference_atmosphere

```python
@override_path_tracing_enable_reference_atmosphere.setter
def override_path_tracing_enable_reference_atmosphere(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_path_tracing_enable_denoiser"></a>

#### override_path_tracing_enable_denoiser

```python
@property
def override_path_tracing_enable_denoiser() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_path_tracing_enable_denoiser"></a>

#### override_path_tracing_enable_denoiser

```python
@override_path_tracing_enable_denoiser.setter
def override_path_tracing_enable_denoiser(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_path_tracing_include_emissive"></a>

#### override_path_tracing_include_emissive

```python
@property
def override_path_tracing_include_emissive() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_path_tracing_include_emissive"></a>

#### override_path_tracing_include_emissive

```python
@override_path_tracing_include_emissive.setter
def override_path_tracing_include_emissive(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_path_tracing_include_diffuse"></a>

#### override_path_tracing_include_diffuse

```python
@property
def override_path_tracing_include_diffuse() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_path_tracing_include_diffuse"></a>

#### override_path_tracing_include_diffuse

```python
@override_path_tracing_include_diffuse.setter
def override_path_tracing_include_diffuse(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_path_tracing_include_indirect_diffuse"></a>

#### override_path_tracing_include_indirect_diffuse

```python
@property
def override_path_tracing_include_indirect_diffuse() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_path_tracing_include_indirect_diffuse"></a>

#### override_path_tracing_include_indirect_diffuse

```python
@override_path_tracing_include_indirect_diffuse.setter
def override_path_tracing_include_indirect_diffuse(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_path_tracing_include_specular"></a>

#### override_path_tracing_include_specular

```python
@property
def override_path_tracing_include_specular() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_path_tracing_include_specular"></a>

#### override_path_tracing_include_specular

```python
@override_path_tracing_include_specular.setter
def override_path_tracing_include_specular(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_path_tracing_include_indirect_specular"></a>

#### override_path_tracing_include_indirect_specular

```python
@property
def override_path_tracing_include_indirect_specular() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_path_tracing_include_indirect_specular"></a>

#### override_path_tracing_include_indirect_specular

```python
@override_path_tracing_include_indirect_specular.setter
def override_path_tracing_include_indirect_specular(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_path_tracing_include_volume"></a>

#### override_path_tracing_include_volume

```python
@property
def override_path_tracing_include_volume() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_path_tracing_include_volume"></a>

#### override_path_tracing_include_volume

```python
@override_path_tracing_include_volume.setter
def override_path_tracing_include_volume(value: bool) -> None
```

<a id="unreal.PostProcessSettings.override_path_tracing_include_indirect_volume"></a>

#### override_path_tracing_include_indirect_volume

```python
@property
def override_path_tracing_include_indirect_volume() -> bool
```

(bool):  [Read-Write]

<a id="unreal.PostProcessSettings.override_path_tracing_include_indirect_volume"></a>

#### override_path_tracing_include_indirect_volume

```python
@override_path_tracing_include_indirect_volume.setter
def override_path_tracing_include_indirect_volume(value: bool) -> None
```

<a id="unreal.PostProcessSettings.mobile_hq_gaussian"></a>

#### mobile_hq_gaussian

```python
@property
def mobile_hq_gaussian() -> bool
```

(bool):  [Read-Write] Enable HQ Gaussian on high end mobile platforms. (ES3_1)

<a id="unreal.PostProcessSettings.mobile_hq_gaussian"></a>

#### mobile_hq_gaussian

```python
@mobile_hq_gaussian.setter
def mobile_hq_gaussian(value: bool) -> None
```

<a id="unreal.PostProcessSettings.bloom_method"></a>

#### bloom_method

```python
@property
def bloom_method() -> BloomMethod
```

(BloomMethod):  [Read-Write] Bloom algorithm

<a id="unreal.PostProcessSettings.bloom_method"></a>

#### bloom_method

```python
@bloom_method.setter
def bloom_method(value: BloomMethod) -> None
```

<a id="unreal.PostProcessSettings.auto_exposure_method"></a>

#### auto_exposure_method

```python
@property
def auto_exposure_method() -> AutoExposureMethod
```

(AutoExposureMethod):  [Read-Write] Luminance computation method

<a id="unreal.PostProcessSettings.auto_exposure_method"></a>

#### auto_exposure_method

```python
@auto_exposure_method.setter
def auto_exposure_method(value: AutoExposureMethod) -> None
```

<a id="unreal.PostProcessSettings.temperature_type"></a>

#### temperature_type

```python
@property
def temperature_type() -> TemperatureMethod
```

(TemperatureMethod):  [Read-Write] Selects the type of temperature calculation.
White Balance uses the Temperature value to control the virtual camera's White Balance. This is the default selection.
Color Temperature uses the Temperature value to adjust the color temperature of the scene, which is the inverse of the White Balance operation.

<a id="unreal.PostProcessSettings.temperature_type"></a>

#### temperature_type

```python
@temperature_type.setter
def temperature_type(value: TemperatureMethod) -> None
```

<a id="unreal.PostProcessSettings.white_temp"></a>

#### white_temp

```python
@property
def white_temp() -> float
```

(float):  [Read-Write] Controls the color temperature or white balance in degrees Kelvin which the scene considers as white light.

<a id="unreal.PostProcessSettings.white_temp"></a>

#### white_temp

```python
@white_temp.setter
def white_temp(value: float) -> None
```

<a id="unreal.PostProcessSettings.white_tint"></a>

#### white_tint

```python
@property
def white_tint() -> float
```

(float):  [Read-Write] Controls the color of the scene along the magenta - green axis (orthogonal to the color temperature).  This feature is equivalent to color tint in digital cameras.

<a id="unreal.PostProcessSettings.white_tint"></a>

#### white_tint

```python
@white_tint.setter
def white_tint(value: float) -> None
```

<a id="unreal.PostProcessSettings.color_saturation"></a>

#### color_saturation

```python
@property
def color_saturation() -> Vector4
```

(Vector4):  [Read-Write] Control the intensity of the color(hue) for the entire image.Higher values will result in more vibrant colors.

<a id="unreal.PostProcessSettings.color_saturation"></a>

#### color_saturation

```python
@color_saturation.setter
def color_saturation(value: Vector4) -> None
```

<a id="unreal.PostProcessSettings.color_contrast"></a>

#### color_contrast

```python
@property
def color_contrast() -> Vector4
```

(Vector4):  [Read-Write] Control the range of light and dark values in your scene. Lower values will reduce the difference between bright and dark areas while higher values will increase the difference between the bright and dark areas.

<a id="unreal.PostProcessSettings.color_contrast"></a>

#### color_contrast

```python
@color_contrast.setter
def color_contrast(value: Vector4) -> None
```

<a id="unreal.PostProcessSettings.color_gamma"></a>

#### color_gamma

```python
@property
def color_gamma() -> Vector4
```

(Vector4):  [Read-Write] Control the luminance curve of the scene. Raising or lowering this value will result brightening or darkening the mid-tones of the entire image.

<a id="unreal.PostProcessSettings.color_gamma"></a>

#### color_gamma

```python
@color_gamma.setter
def color_gamma(value: Vector4) -> None
```

<a id="unreal.PostProcessSettings.color_gain"></a>

#### color_gain

```python
@property
def color_gain() -> Vector4
```

(Vector4):  [Read-Write] This value multiplies the colors of the image.  Raising or lowering this value will result in brightening or darkening the entire scene.

<a id="unreal.PostProcessSettings.color_gain"></a>

#### color_gain

```python
@color_gain.setter
def color_gain(value: Vector4) -> None
```

<a id="unreal.PostProcessSettings.color_offset"></a>

#### color_offset

```python
@property
def color_offset() -> Vector4
```

(Vector4):  [Read-Write] This value is added to the colors of the scene.  Raising or lowering this value will result in the image being more or less washed-out.

<a id="unreal.PostProcessSettings.color_offset"></a>

#### color_offset

```python
@color_offset.setter
def color_offset(value: Vector4) -> None
```

<a id="unreal.PostProcessSettings.color_saturation_shadows"></a>

#### color_saturation_shadows

```python
@property
def color_saturation_shadows() -> Vector4
```

(Vector4):  [Read-Write] Control the intensity of the colors (hue) in the shadow region of the image.  Higher values will result in more vibrant colors.

<a id="unreal.PostProcessSettings.color_saturation_shadows"></a>

#### color_saturation_shadows

```python
@color_saturation_shadows.setter
def color_saturation_shadows(value: Vector4) -> None
```

<a id="unreal.PostProcessSettings.color_contrast_shadows"></a>

#### color_contrast_shadows

```python
@property
def color_contrast_shadows() -> Vector4
```

(Vector4):  [Read-Write] Control the range of light and dark values in your scene. Lower values will reduce the difference between bright and dark areas while higher values will increase the difference between the bright and dark areas.

<a id="unreal.PostProcessSettings.color_contrast_shadows"></a>

#### color_contrast_shadows

```python
@color_contrast_shadows.setter
def color_contrast_shadows(value: Vector4) -> None
```

<a id="unreal.PostProcessSettings.color_gamma_shadows"></a>

#### color_gamma_shadows

```python
@property
def color_gamma_shadows() -> Vector4
```

(Vector4):  [Read-Write] Control the luminance curve of the shadow region. Raising or lowering this value will result brightening or darkening the mid-tones of the shadow region.

<a id="unreal.PostProcessSettings.color_gamma_shadows"></a>

#### color_gamma_shadows

```python
@color_gamma_shadows.setter
def color_gamma_shadows(value: Vector4) -> None
```

<a id="unreal.PostProcessSettings.color_gain_shadows"></a>

#### color_gain_shadows

```python
@property
def color_gain_shadows() -> Vector4
```

(Vector4):  [Read-Write] This value multiplies the colors in the shadow region.  Raising or lowering this value will result in brightening or darkening the affected region.

<a id="unreal.PostProcessSettings.color_gain_shadows"></a>

#### color_gain_shadows

```python
@color_gain_shadows.setter
def color_gain_shadows(value: Vector4) -> None
```

<a id="unreal.PostProcessSettings.color_offset_shadows"></a>

#### color_offset_shadows

```python
@property
def color_offset_shadows() -> Vector4
```

(Vector4):  [Read-Write] This value is added to the colors in the shadow region.  Raising or lowering this value will result in the shadows being more or less washed-out.

<a id="unreal.PostProcessSettings.color_offset_shadows"></a>

#### color_offset_shadows

```python
@color_offset_shadows.setter
def color_offset_shadows(value: Vector4) -> None
```

<a id="unreal.PostProcessSettings.color_saturation_midtones"></a>

#### color_saturation_midtones

```python
@property
def color_saturation_midtones() -> Vector4
```

(Vector4):  [Read-Write] Control the intensity of the colors (hue) in the mid-tone region of the image.  Higher values will result in more vibrant colors.

<a id="unreal.PostProcessSettings.color_saturation_midtones"></a>

#### color_saturation_midtones

```python
@color_saturation_midtones.setter
def color_saturation_midtones(value: Vector4) -> None
```

<a id="unreal.PostProcessSettings.color_contrast_midtones"></a>

#### color_contrast_midtones

```python
@property
def color_contrast_midtones() -> Vector4
```

(Vector4):  [Read-Write] Control the range of light and dark values in the mid-tone region. Lower values will reduce the difference between bright and dark areas while higher values will increase the difference between the bright and dark areas.

<a id="unreal.PostProcessSettings.color_contrast_midtones"></a>

#### color_contrast_midtones

```python
@color_contrast_midtones.setter
def color_contrast_midtones(value: Vector4) -> None
```

<a id="unreal.PostProcessSettings.color_gamma_midtones"></a>

#### color_gamma_midtones

```python
@property
def color_gamma_midtones() -> Vector4
```

(Vector4):  [Read-Write] Control the luminance curve of the mid-tone region of the image. Raising or lowering this value will result brightening or darkening the mid-tones of the image.

<a id="unreal.PostProcessSettings.color_gamma_midtones"></a>

#### color_gamma_midtones

```python
@color_gamma_midtones.setter
def color_gamma_midtones(value: Vector4) -> None
```

<a id="unreal.PostProcessSettings.color_gain_midtones"></a>

#### color_gain_midtones

```python
@property
def color_gain_midtones() -> Vector4
```

(Vector4):  [Read-Write] This value multiplies the colors in the mid-tone region of the image.  Raising or lowering this value will result in brightening or darkening the affected region.

<a id="unreal.PostProcessSettings.color_gain_midtones"></a>

#### color_gain_midtones

```python
@color_gain_midtones.setter
def color_gain_midtones(value: Vector4) -> None
```

<a id="unreal.PostProcessSettings.color_offset_midtones"></a>

#### color_offset_midtones

```python
@property
def color_offset_midtones() -> Vector4
```

(Vector4):  [Read-Write] This value is added to the colors in the mid-tone region of the image.  Raising or lowering this value will result in the mid-tones being more or less washed-out.

<a id="unreal.PostProcessSettings.color_offset_midtones"></a>

#### color_offset_midtones

```python
@color_offset_midtones.setter
def color_offset_midtones(value: Vector4) -> None
```

<a id="unreal.PostProcessSettings.color_saturation_highlights"></a>

#### color_saturation_highlights

```python
@property
def color_saturation_highlights() -> Vector4
```

(Vector4):  [Read-Write] Control the intensity of the color (hue) for the highlights region of the image.  Higher values will result in more vibrant colors.

<a id="unreal.PostProcessSettings.color_saturation_highlights"></a>

#### color_saturation_highlights

```python
@color_saturation_highlights.setter
def color_saturation_highlights(value: Vector4) -> None
```

<a id="unreal.PostProcessSettings.color_contrast_highlights"></a>

#### color_contrast_highlights

```python
@property
def color_contrast_highlights() -> Vector4
```

(Vector4):  [Read-Write] Control the range of light and dark values in the highlights region. Lower values will reduce the difference between bright and dark areas while higher values will increase the difference between the bright and dark areas.

<a id="unreal.PostProcessSettings.color_contrast_highlights"></a>

#### color_contrast_highlights

```python
@color_contrast_highlights.setter
def color_contrast_highlights(value: Vector4) -> None
```

<a id="unreal.PostProcessSettings.color_gamma_highlights"></a>

#### color_gamma_highlights

```python
@property
def color_gamma_highlights() -> Vector4
```

(Vector4):  [Read-Write] Control the luminance curve of the highlight region. Raising or lowering this value will result brightening or darkening the mid-tones of the highlight region.

<a id="unreal.PostProcessSettings.color_gamma_highlights"></a>

#### color_gamma_highlights

```python
@color_gamma_highlights.setter
def color_gamma_highlights(value: Vector4) -> None
```

<a id="unreal.PostProcessSettings.color_gain_highlights"></a>

#### color_gain_highlights

```python
@property
def color_gain_highlights() -> Vector4
```

(Vector4):  [Read-Write] This value multiplies the colors in the highlight region.  Raising or lowering this value will result in brightening or darkening the affected region.

<a id="unreal.PostProcessSettings.color_gain_highlights"></a>

#### color_gain_highlights

```python
@color_gain_highlights.setter
def color_gain_highlights(value: Vector4) -> None
```

<a id="unreal.PostProcessSettings.color_offset_highlights"></a>

#### color_offset_highlights

```python
@property
def color_offset_highlights() -> Vector4
```

(Vector4):  [Read-Write] This value is added to the colors in the highlight region.  Raising or lowering this value will result in the highlights being more or less washed-out.

<a id="unreal.PostProcessSettings.color_offset_highlights"></a>

#### color_offset_highlights

```python
@color_offset_highlights.setter
def color_offset_highlights(value: Vector4) -> None
```

<a id="unreal.PostProcessSettings.color_correction_highlights_min"></a>

#### color_correction_highlights_min

```python
@property
def color_correction_highlights_min() -> float
```

(float):  [Read-Write] This value sets the lower threshold for what is considered to be the highlight region of the image.

<a id="unreal.PostProcessSettings.color_correction_highlights_min"></a>

#### color_correction_highlights_min

```python
@color_correction_highlights_min.setter
def color_correction_highlights_min(value: float) -> None
```

<a id="unreal.PostProcessSettings.color_correction_highlights_max"></a>

#### color_correction_highlights_max

```python
@property
def color_correction_highlights_max() -> float
```

(float):  [Read-Write] This value sets the upper threshold for what is considered to be the highlight region of the image.  This value should be larger than HighlightsMin. Default is 1.0, for backwards compatibility

<a id="unreal.PostProcessSettings.color_correction_highlights_max"></a>

#### color_correction_highlights_max

```python
@color_correction_highlights_max.setter
def color_correction_highlights_max(value: float) -> None
```

<a id="unreal.PostProcessSettings.color_correction_shadows_max"></a>

#### color_correction_shadows_max

```python
@property
def color_correction_shadows_max() -> float
```

(float):  [Read-Write] This value sets the threshold for what is considered to be the shadow region of the image.

<a id="unreal.PostProcessSettings.color_correction_shadows_max"></a>

#### color_correction_shadows_max

```python
@color_correction_shadows_max.setter
def color_correction_shadows_max(value: float) -> None
```

<a id="unreal.PostProcessSettings.blue_correction"></a>

#### blue_correction

```python
@property
def blue_correction() -> float
```

(float):  [Read-Write] Correct for artifacts with "electric" blues due to the ACEScg color space. Bright blue desaturates instead of going to violet.

<a id="unreal.PostProcessSettings.blue_correction"></a>

#### blue_correction

```python
@blue_correction.setter
def blue_correction(value: float) -> None
```

<a id="unreal.PostProcessSettings.expand_gamut"></a>

#### expand_gamut

```python
@property
def expand_gamut() -> float
```

(float):  [Read-Write] Expand bright saturated colors outside the sRGB gamut to fake wide gamut rendering.

<a id="unreal.PostProcessSettings.expand_gamut"></a>

#### expand_gamut

```python
@expand_gamut.setter
def expand_gamut(value: float) -> None
```

<a id="unreal.PostProcessSettings.tone_curve_amount"></a>

#### tone_curve_amount

```python
@property
def tone_curve_amount() -> float
```

(float):  [Read-Write] Allow effect of Tone Curve to be reduced (Set ToneCurveAmount and ExpandGamut to 0.0 to fully disable tone curve)

<a id="unreal.PostProcessSettings.tone_curve_amount"></a>

#### tone_curve_amount

```python
@tone_curve_amount.setter
def tone_curve_amount(value: float) -> None
```

<a id="unreal.PostProcessSettings.film_slope"></a>

#### film_slope

```python
@property
def film_slope() -> float
```

(float):  [Read-Write] Controls the overall steepness of the tonemapper curve.  Larger values increase scene contrast and smaller values reduce contrast.

<a id="unreal.PostProcessSettings.film_slope"></a>

#### film_slope

```python
@film_slope.setter
def film_slope(value: float) -> None
```

<a id="unreal.PostProcessSettings.film_toe"></a>

#### film_toe

```python
@property
def film_toe() -> float
```

(float):  [Read-Write] Controls the contrast of the dark end of the tonemapper curve. Larger values increase contrast and smaller values decrease contrast.

<a id="unreal.PostProcessSettings.film_toe"></a>

#### film_toe

```python
@film_toe.setter
def film_toe(value: float) -> None
```

<a id="unreal.PostProcessSettings.film_shoulder"></a>

#### film_shoulder

```python
@property
def film_shoulder() -> float
```

(float):  [Read-Write] Sometimes referred to as highlight rolloff.  Controls the contrast of the bright end of the tonemapper curve. Larger values increase contrast and smaller values decrease contrast.

<a id="unreal.PostProcessSettings.film_shoulder"></a>

#### film_shoulder

```python
@film_shoulder.setter
def film_shoulder(value: float) -> None
```

<a id="unreal.PostProcessSettings.film_black_clip"></a>

#### film_black_clip

```python
@property
def film_black_clip() -> float
```

(float):  [Read-Write] Lowers the toe of the tonemapper curve by this amount. Increasing this value causes more of the scene to clip to black.  For most purposes, this property should remain 0

<a id="unreal.PostProcessSettings.film_black_clip"></a>

#### film_black_clip

```python
@film_black_clip.setter
def film_black_clip(value: float) -> None
```

<a id="unreal.PostProcessSettings.film_white_clip"></a>

#### film_white_clip

```python
@property
def film_white_clip() -> float
```

(float):  [Read-Write] Controls the height of the tonemapper curve.  Raising this value can cause bright values to more quickly approach fully-saturated white.

<a id="unreal.PostProcessSettings.film_white_clip"></a>

#### film_white_clip

```python
@film_white_clip.setter
def film_white_clip(value: float) -> None
```

<a id="unreal.PostProcessSettings.scene_color_tint"></a>

#### scene_color_tint

```python
@property
def scene_color_tint() -> LinearColor
```

(LinearColor):  [Read-Write] Scene tint color

<a id="unreal.PostProcessSettings.scene_color_tint"></a>

#### scene_color_tint

```python
@scene_color_tint.setter
def scene_color_tint(value: LinearColor) -> None
```

<a id="unreal.PostProcessSettings.scene_fringe_intensity"></a>

#### scene_fringe_intensity

```python
@property
def scene_fringe_intensity() -> float
```

(float):  [Read-Write] in percent, Scene chromatic aberration / color fringe (camera imperfection) to simulate an artifact that happens in real-world lens, mostly visible in the image corners.

<a id="unreal.PostProcessSettings.scene_fringe_intensity"></a>

#### scene_fringe_intensity

```python
@scene_fringe_intensity.setter
def scene_fringe_intensity(value: float) -> None
```

<a id="unreal.PostProcessSettings.chromatic_aberration_start_offset"></a>

#### chromatic_aberration_start_offset

```python
@property
def chromatic_aberration_start_offset() -> float
```

(float):  [Read-Write] A normalized distance to the center of the framebuffer where the effect takes place.

<a id="unreal.PostProcessSettings.chromatic_aberration_start_offset"></a>

#### chromatic_aberration_start_offset

```python
@chromatic_aberration_start_offset.setter
def chromatic_aberration_start_offset(value: float) -> None
```

<a id="unreal.PostProcessSettings.bloom_intensity"></a>

#### bloom_intensity

```python
@property
def bloom_intensity() -> float
```

(float):  [Read-Write] Multiplier for all bloom contributions >=0: off, 1(default), >1 brighter

<a id="unreal.PostProcessSettings.bloom_intensity"></a>

#### bloom_intensity

```python
@bloom_intensity.setter
def bloom_intensity(value: float) -> None
```

<a id="unreal.PostProcessSettings.bloom_threshold"></a>

#### bloom_threshold

```python
@property
def bloom_threshold() -> float
```

(float):  [Read-Write] minimum brightness the bloom starts having effect
-1:all pixels affect bloom equally (physically correct, faster as a threshold pass is omitted), 0:all pixels affect bloom brights more, 1(default), >1 brighter

<a id="unreal.PostProcessSettings.bloom_threshold"></a>

#### bloom_threshold

```python
@bloom_threshold.setter
def bloom_threshold(value: float) -> None
```

<a id="unreal.PostProcessSettings.bloom_size_scale"></a>

#### bloom_size_scale

```python
@property
def bloom_size_scale() -> float
```

(float):  [Read-Write] Scale for all bloom sizes

<a id="unreal.PostProcessSettings.bloom_size_scale"></a>

#### bloom_size_scale

```python
@bloom_size_scale.setter
def bloom_size_scale(value: float) -> None
```

<a id="unreal.PostProcessSettings.bloom1_size"></a>

#### bloom1_size

```python
@property
def bloom1_size() -> float
```

(float):  [Read-Write] Diameter size for the Bloom1 in percent of the screen width
(is done in 1/2 resolution, larger values cost more performance, good for high frequency details)
>=0: can be clamped because of shader limitations

<a id="unreal.PostProcessSettings.bloom1_size"></a>

#### bloom1_size

```python
@bloom1_size.setter
def bloom1_size(value: float) -> None
```

<a id="unreal.PostProcessSettings.bloom2_size"></a>

#### bloom2_size

```python
@property
def bloom2_size() -> float
```

(float):  [Read-Write] Diameter size for Bloom2 in percent of the screen width
(is done in 1/4 resolution, larger values cost more performance)
>=0: can be clamped because of shader limitations

<a id="unreal.PostProcessSettings.bloom2_size"></a>

#### bloom2_size

```python
@bloom2_size.setter
def bloom2_size(value: float) -> None
```

<a id="unreal.PostProcessSettings.bloom3_size"></a>

#### bloom3_size

```python
@property
def bloom3_size() -> float
```

(float):  [Read-Write] Diameter size for Bloom3 in percent of the screen width
(is done in 1/8 resolution, larger values cost more performance)
>=0: can be clamped because of shader limitations

<a id="unreal.PostProcessSettings.bloom3_size"></a>

#### bloom3_size

```python
@bloom3_size.setter
def bloom3_size(value: float) -> None
```

<a id="unreal.PostProcessSettings.bloom4_size"></a>

#### bloom4_size

```python
@property
def bloom4_size() -> float
```

(float):  [Read-Write] Diameter size for Bloom4 in percent of the screen width
(is done in 1/16 resolution, larger values cost more performance, best for wide contributions)
>=0: can be clamped because of shader limitations

<a id="unreal.PostProcessSettings.bloom4_size"></a>

#### bloom4_size

```python
@bloom4_size.setter
def bloom4_size(value: float) -> None
```

<a id="unreal.PostProcessSettings.bloom5_size"></a>

#### bloom5_size

```python
@property
def bloom5_size() -> float
```

(float):  [Read-Write] Diameter size for Bloom5 in percent of the screen width
(is done in 1/32 resolution, larger values cost more performance, best for wide contributions)
>=0: can be clamped because of shader limitations

<a id="unreal.PostProcessSettings.bloom5_size"></a>

#### bloom5_size

```python
@bloom5_size.setter
def bloom5_size(value: float) -> None
```

<a id="unreal.PostProcessSettings.bloom6_size"></a>

#### bloom6_size

```python
@property
def bloom6_size() -> float
```

(float):  [Read-Write] Diameter size for Bloom6 in percent of the screen width
(is done in 1/64 resolution, larger values cost more performance, best for wide contributions)
>=0: can be clamped because of shader limitations

<a id="unreal.PostProcessSettings.bloom6_size"></a>

#### bloom6_size

```python
@bloom6_size.setter
def bloom6_size(value: float) -> None
```

<a id="unreal.PostProcessSettings.bloom1_tint"></a>

#### bloom1_tint

```python
@property
def bloom1_tint() -> LinearColor
```

(LinearColor):  [Read-Write] Bloom1 tint color

<a id="unreal.PostProcessSettings.bloom1_tint"></a>

#### bloom1_tint

```python
@bloom1_tint.setter
def bloom1_tint(value: LinearColor) -> None
```

<a id="unreal.PostProcessSettings.bloom2_tint"></a>

#### bloom2_tint

```python
@property
def bloom2_tint() -> LinearColor
```

(LinearColor):  [Read-Write] Bloom2 tint color

<a id="unreal.PostProcessSettings.bloom2_tint"></a>

#### bloom2_tint

```python
@bloom2_tint.setter
def bloom2_tint(value: LinearColor) -> None
```

<a id="unreal.PostProcessSettings.bloom3_tint"></a>

#### bloom3_tint

```python
@property
def bloom3_tint() -> LinearColor
```

(LinearColor):  [Read-Write] Bloom3 tint color

<a id="unreal.PostProcessSettings.bloom3_tint"></a>

#### bloom3_tint

```python
@bloom3_tint.setter
def bloom3_tint(value: LinearColor) -> None
```

<a id="unreal.PostProcessSettings.bloom4_tint"></a>

#### bloom4_tint

```python
@property
def bloom4_tint() -> LinearColor
```

(LinearColor):  [Read-Write] Bloom4 tint color

<a id="unreal.PostProcessSettings.bloom4_tint"></a>

#### bloom4_tint

```python
@bloom4_tint.setter
def bloom4_tint(value: LinearColor) -> None
```

<a id="unreal.PostProcessSettings.bloom5_tint"></a>

#### bloom5_tint

```python
@property
def bloom5_tint() -> LinearColor
```

(LinearColor):  [Read-Write] Bloom5 tint color

<a id="unreal.PostProcessSettings.bloom5_tint"></a>

#### bloom5_tint

```python
@bloom5_tint.setter
def bloom5_tint(value: LinearColor) -> None
```

<a id="unreal.PostProcessSettings.bloom6_tint"></a>

#### bloom6_tint

```python
@property
def bloom6_tint() -> LinearColor
```

(LinearColor):  [Read-Write] Bloom6 tint color

<a id="unreal.PostProcessSettings.bloom6_tint"></a>

#### bloom6_tint

```python
@bloom6_tint.setter
def bloom6_tint(value: LinearColor) -> None
```

<a id="unreal.PostProcessSettings.bloom_convolution_scatter_dispersion"></a>

#### bloom_convolution_scatter_dispersion

```python
@property
def bloom_convolution_scatter_dispersion() -> float
```

(float):  [Read-Write] Intensity multiplier on the scatter dispersion energy of the kernel. 1.0 means exactly use the same energy as the kernel scatter dispersion.

<a id="unreal.PostProcessSettings.bloom_convolution_scatter_dispersion"></a>

#### bloom_convolution_scatter_dispersion

```python
@bloom_convolution_scatter_dispersion.setter
def bloom_convolution_scatter_dispersion(value: float) -> None
```

<a id="unreal.PostProcessSettings.bloom_convolution_size"></a>

#### bloom_convolution_size

```python
@property
def bloom_convolution_size() -> float
```

(float):  [Read-Write] Relative size of the convolution kernel image compared to the minor axis of the viewport

<a id="unreal.PostProcessSettings.bloom_convolution_size"></a>

#### bloom_convolution_size

```python
@bloom_convolution_size.setter
def bloom_convolution_size(value: float) -> None
```

<a id="unreal.PostProcessSettings.bloom_convolution_texture"></a>

#### bloom_convolution_texture

```python
@property
def bloom_convolution_texture() -> Texture2D
```

(Texture2D):  [Read-Write] Texture to replace default convolution bloom kernel

<a id="unreal.PostProcessSettings.bloom_convolution_texture"></a>

#### bloom_convolution_texture

```python
@bloom_convolution_texture.setter
def bloom_convolution_texture(value: Texture2D) -> None
```

<a id="unreal.PostProcessSettings.bloom_convolution_center_uv"></a>

#### bloom_convolution_center_uv

```python
@property
def bloom_convolution_center_uv() -> Vector2D
```

(Vector2D):  [Read-Write] The UV location of the center of the kernel.  Should be very close to (.5,.5)

<a id="unreal.PostProcessSettings.bloom_convolution_center_uv"></a>

#### bloom_convolution_center_uv

```python
@bloom_convolution_center_uv.setter
def bloom_convolution_center_uv(value: Vector2D) -> None
```

<a id="unreal.PostProcessSettings.bloom_convolution_pre_filter_min"></a>

#### bloom_convolution_pre_filter_min

```python
@property
def bloom_convolution_pre_filter_min() -> float
```

(float):  [Read-Write] Boost intensity of select pixels  prior to computing bloom convolution (Min, Max, Multiplier).  Max < Min disables

<a id="unreal.PostProcessSettings.bloom_convolution_pre_filter_min"></a>

#### bloom_convolution_pre_filter_min

```python
@bloom_convolution_pre_filter_min.setter
def bloom_convolution_pre_filter_min(value: float) -> None
```

<a id="unreal.PostProcessSettings.bloom_convolution_pre_filter_max"></a>

#### bloom_convolution_pre_filter_max

```python
@property
def bloom_convolution_pre_filter_max() -> float
```

(float):  [Read-Write] Boost intensity of select pixels  prior to computing bloom convolution (Min, Max, Multiplier).  Max < Min disables

<a id="unreal.PostProcessSettings.bloom_convolution_pre_filter_max"></a>

#### bloom_convolution_pre_filter_max

```python
@bloom_convolution_pre_filter_max.setter
def bloom_convolution_pre_filter_max(value: float) -> None
```

<a id="unreal.PostProcessSettings.bloom_convolution_pre_filter_mult"></a>

#### bloom_convolution_pre_filter_mult

```python
@property
def bloom_convolution_pre_filter_mult() -> float
```

(float):  [Read-Write] Boost intensity of select pixels  prior to computing bloom convolution (Min, Max, Multiplier).  Max < Min disables

<a id="unreal.PostProcessSettings.bloom_convolution_pre_filter_mult"></a>

#### bloom_convolution_pre_filter_mult

```python
@bloom_convolution_pre_filter_mult.setter
def bloom_convolution_pre_filter_mult(value: float) -> None
```

<a id="unreal.PostProcessSettings.bloom_convolution_buffer_scale"></a>

#### bloom_convolution_buffer_scale

```python
@property
def bloom_convolution_buffer_scale() -> float
```

(float):  [Read-Write] Implicit buffer region as a fraction of the screen size to insure the bloom does not wrap across the screen.  Larger sizes have perf impact.

<a id="unreal.PostProcessSettings.bloom_convolution_buffer_scale"></a>

#### bloom_convolution_buffer_scale

```python
@bloom_convolution_buffer_scale.setter
def bloom_convolution_buffer_scale(value: float) -> None
```

<a id="unreal.PostProcessSettings.bloom_dirt_mask"></a>

#### bloom_dirt_mask

```python
@property
def bloom_dirt_mask() -> Texture
```

(Texture):  [Read-Write] Texture that defines the dirt on the camera lens where the light of very bright objects is scattered.

<a id="unreal.PostProcessSettings.bloom_dirt_mask"></a>

#### bloom_dirt_mask

```python
@bloom_dirt_mask.setter
def bloom_dirt_mask(value: Texture) -> None
```

<a id="unreal.PostProcessSettings.bloom_dirt_mask_intensity"></a>

#### bloom_dirt_mask_intensity

```python
@property
def bloom_dirt_mask_intensity() -> float
```

(float):  [Read-Write] BloomDirtMask intensity

<a id="unreal.PostProcessSettings.bloom_dirt_mask_intensity"></a>

#### bloom_dirt_mask_intensity

```python
@bloom_dirt_mask_intensity.setter
def bloom_dirt_mask_intensity(value: float) -> None
```

<a id="unreal.PostProcessSettings.bloom_dirt_mask_tint"></a>

#### bloom_dirt_mask_tint

```python
@property
def bloom_dirt_mask_tint() -> LinearColor
```

(LinearColor):  [Read-Write] BloomDirtMask tint color

<a id="unreal.PostProcessSettings.bloom_dirt_mask_tint"></a>

#### bloom_dirt_mask_tint

```python
@bloom_dirt_mask_tint.setter
def bloom_dirt_mask_tint(value: LinearColor) -> None
```

<a id="unreal.PostProcessSettings.dynamic_global_illumination_method"></a>

#### dynamic_global_illumination_method

```python
@property
def dynamic_global_illumination_method() -> DynamicGlobalIlluminationMethod
```

(DynamicGlobalIlluminationMethod):  [Read-Write] Chooses the Dynamic Global Illumination method.  Not compatible with Forward Shading.

<a id="unreal.PostProcessSettings.dynamic_global_illumination_method"></a>

#### dynamic_global_illumination_method

```python
@dynamic_global_illumination_method.setter
def dynamic_global_illumination_method(
        value: DynamicGlobalIlluminationMethod) -> None
```

<a id="unreal.PostProcessSettings.indirect_lighting_color"></a>

#### indirect_lighting_color

```python
@property
def indirect_lighting_color() -> LinearColor
```

(LinearColor):  [Read-Write] Adjusts indirect lighting color. (1,1,1) is default. (0,0,0) to disable GI. The show flag 'Global Illumination' must be enabled to use this property.

<a id="unreal.PostProcessSettings.indirect_lighting_color"></a>

#### indirect_lighting_color

```python
@indirect_lighting_color.setter
def indirect_lighting_color(value: LinearColor) -> None
```

<a id="unreal.PostProcessSettings.indirect_lighting_intensity"></a>

#### indirect_lighting_intensity

```python
@property
def indirect_lighting_intensity() -> float
```

(float):  [Read-Write] Scales the indirect lighting contribution. A value of 0 disables GI. Default is 1. The show flag 'Global Illumination' must be enabled to use this property.

<a id="unreal.PostProcessSettings.indirect_lighting_intensity"></a>

#### indirect_lighting_intensity

```python
@indirect_lighting_intensity.setter
def indirect_lighting_intensity(value: float) -> None
```

<a id="unreal.PostProcessSettings.lumen_ray_lighting_mode"></a>

#### lumen_ray_lighting_mode

```python
@property
def lumen_ray_lighting_mode() -> LumenRayLightingModeOverride
```

(LumenRayLightingModeOverride):  [Read-Write] Controls how Lumen rays are lit when Lumen is using Hardware Ray Tracing.  By default, Lumen uses the Surface Cache for best performance, but can be set to 'Hit Lighting' for higher quality.

<a id="unreal.PostProcessSettings.lumen_ray_lighting_mode"></a>

#### lumen_ray_lighting_mode

```python
@lumen_ray_lighting_mode.setter
def lumen_ray_lighting_mode(value: LumenRayLightingModeOverride) -> None
```

<a id="unreal.PostProcessSettings.lumen_scene_lighting_quality"></a>

#### lumen_scene_lighting_quality

```python
@property
def lumen_scene_lighting_quality() -> float
```

(float):  [Read-Write] Scales Lumen Scene's quality.  Larger scales cause Lumen Scene to be calculated with a higher fidelity, which can be visible in reflections, but increase GPU cost.

<a id="unreal.PostProcessSettings.lumen_scene_lighting_quality"></a>

#### lumen_scene_lighting_quality

```python
@lumen_scene_lighting_quality.setter
def lumen_scene_lighting_quality(value: float) -> None
```

<a id="unreal.PostProcessSettings.lumen_scene_detail"></a>

#### lumen_scene_detail

```python
@property
def lumen_scene_detail() -> float
```

(float):  [Read-Write] Controls the size of instances that can be represented in Lumen Scene.  Larger values will ensure small objects are represented, but increase GPU cost.

<a id="unreal.PostProcessSettings.lumen_scene_detail"></a>

#### lumen_scene_detail

```python
@lumen_scene_detail.setter
def lumen_scene_detail(value: float) -> None
```

<a id="unreal.PostProcessSettings.lumen_scene_view_distance"></a>

#### lumen_scene_view_distance

```python
@property
def lumen_scene_view_distance() -> float
```

(float):  [Read-Write] Sets the maximum view distance of the scene that Lumen maintains for ray tracing against.  Larger values will increase the effective range of sky shadowing and Global Illumination, but increase GPU cost.

<a id="unreal.PostProcessSettings.lumen_scene_view_distance"></a>

#### lumen_scene_view_distance

```python
@lumen_scene_view_distance.setter
def lumen_scene_view_distance(value: float) -> None
```

<a id="unreal.PostProcessSettings.lumen_scene_lighting_update_speed"></a>

#### lumen_scene_lighting_update_speed

```python
@property
def lumen_scene_lighting_update_speed() -> float
```

(float):  [Read-Write] Controls how much Lumen Scene is allowed to cache lighting results to improve performance.  Larger scales cause lighting changes to propagate faster, but increase GPU cost.

<a id="unreal.PostProcessSettings.lumen_scene_lighting_update_speed"></a>

#### lumen_scene_lighting_update_speed

```python
@lumen_scene_lighting_update_speed.setter
def lumen_scene_lighting_update_speed(value: float) -> None
```

<a id="unreal.PostProcessSettings.lumen_final_gather_quality"></a>

#### lumen_final_gather_quality

```python
@property
def lumen_final_gather_quality() -> float
```

(float):  [Read-Write] Scales Lumen's Final Gather quality.  Larger scales reduce noise, but greatly increase GPU cost.

<a id="unreal.PostProcessSettings.lumen_final_gather_quality"></a>

#### lumen_final_gather_quality

```python
@lumen_final_gather_quality.setter
def lumen_final_gather_quality(value: float) -> None
```

<a id="unreal.PostProcessSettings.lumen_final_gather_lighting_update_speed"></a>

#### lumen_final_gather_lighting_update_speed

```python
@property
def lumen_final_gather_lighting_update_speed() -> float
```

(float):  [Read-Write] Controls how much Lumen Final Gather is allowed to cache lighting results to improve performance.  Larger scales cause lighting changes to propagate faster, but increase GPU cost and noise.

<a id="unreal.PostProcessSettings.lumen_final_gather_lighting_update_speed"></a>

#### lumen_final_gather_lighting_update_speed

```python
@lumen_final_gather_lighting_update_speed.setter
def lumen_final_gather_lighting_update_speed(value: float) -> None
```

<a id="unreal.PostProcessSettings.lumen_final_gather_screen_traces"></a>

#### lumen_final_gather_screen_traces

```python
@property
def lumen_final_gather_screen_traces() -> bool
```

(bool):  [Read-Write] Whether to use screen space traces for Lumen Global Illumination. Screen space traces bypass Lumen Scene and instead sample Scene Depth and Scene Color. This improves quality, as it bypasses Lumen Scene, but causes view dependent lighting.

<a id="unreal.PostProcessSettings.lumen_final_gather_screen_traces"></a>

#### lumen_final_gather_screen_traces

```python
@lumen_final_gather_screen_traces.setter
def lumen_final_gather_screen_traces(value: bool) -> None
```

<a id="unreal.PostProcessSettings.lumen_max_trace_distance"></a>

#### lumen_max_trace_distance

```python
@property
def lumen_max_trace_distance() -> float
```

(float):  [Read-Write] Controls the maximum distance that Lumen should trace while solving lighting.  Values that are too small will cause lighting to leak into large caves, while values that are large will increase GPU cost.

<a id="unreal.PostProcessSettings.lumen_max_trace_distance"></a>

#### lumen_max_trace_distance

```python
@lumen_max_trace_distance.setter
def lumen_max_trace_distance(value: float) -> None
```

<a id="unreal.PostProcessSettings.lumen_diffuse_color_boost"></a>

#### lumen_diffuse_color_boost

```python
@property
def lumen_diffuse_color_boost() -> float
```

(float):  [Read-Write] Allows brightening indirect lighting by calculating material diffuse color for indirect lighting as pow(DiffuseColor, 1 / DiffuseColorBoost). Values above 1 (original diffuse color) aren't physically correct, but they can be useful as an art direction knob to increase the amount of bounced light in the scene. Best to keep below 2 as it also causes reflections to be brighter than the scene.

<a id="unreal.PostProcessSettings.lumen_diffuse_color_boost"></a>

#### lumen_diffuse_color_boost

```python
@lumen_diffuse_color_boost.setter
def lumen_diffuse_color_boost(value: float) -> None
```

<a id="unreal.PostProcessSettings.lumen_skylight_leaking"></a>

#### lumen_skylight_leaking

```python
@property
def lumen_skylight_leaking() -> float
```

(float):  [Read-Write] Controls what fraction of the skylight intensity should be allowed to leak.  This can be useful as an art direction knob (non-physically based) to keep indoor areas from going fully black.

<a id="unreal.PostProcessSettings.lumen_skylight_leaking"></a>

#### lumen_skylight_leaking

```python
@lumen_skylight_leaking.setter
def lumen_skylight_leaking(value: float) -> None
```

<a id="unreal.PostProcessSettings.lumen_full_skylight_leaking_distance"></a>

#### lumen_full_skylight_leaking_distance

```python
@property
def lumen_full_skylight_leaking_distance() -> float
```

(float):  [Read-Write] Controls the distance from a receiving surface where skylight leaking reaches its full intensity.  Smaller values make the skylight leaking flatter, while larger values create an Ambient Occlusion effect.

<a id="unreal.PostProcessSettings.lumen_full_skylight_leaking_distance"></a>

#### lumen_full_skylight_leaking_distance

```python
@lumen_full_skylight_leaking_distance.setter
def lumen_full_skylight_leaking_distance(value: float) -> None
```

<a id="unreal.PostProcessSettings.lumen_surface_cache_resolution"></a>

#### lumen_surface_cache_resolution

```python
@property
def lumen_surface_cache_resolution() -> float
```

(float):  [Read-Write] Scale factor for Lumen Surface Cache resolution, for Scene Capture.  Smaller values save GPU memory, at a cost in quality.  Defaults to 0.5 if not overridden.

<a id="unreal.PostProcessSettings.lumen_surface_cache_resolution"></a>

#### lumen_surface_cache_resolution

```python
@lumen_surface_cache_resolution.setter
def lumen_surface_cache_resolution(value: float) -> None
```

<a id="unreal.PostProcessSettings.reflection_method"></a>

#### reflection_method

```python
@property
def reflection_method() -> ReflectionMethod
```

(ReflectionMethod):  [Read-Write] Chooses the Reflection method. Not compatible with Forward Shading.

<a id="unreal.PostProcessSettings.reflection_method"></a>

#### reflection_method

```python
@reflection_method.setter
def reflection_method(value: ReflectionMethod) -> None
```

<a id="unreal.PostProcessSettings.lumen_reflection_quality"></a>

#### lumen_reflection_quality

```python
@property
def lumen_reflection_quality() -> float
```

(float):  [Read-Write] Scales the Reflection quality.  Larger scales reduce noise in reflections, but increase GPU cost.

<a id="unreal.PostProcessSettings.lumen_reflection_quality"></a>

#### lumen_reflection_quality

```python
@lumen_reflection_quality.setter
def lumen_reflection_quality(value: float) -> None
```

<a id="unreal.PostProcessSettings.lumen_reflections_screen_traces"></a>

#### lumen_reflections_screen_traces

```python
@property
def lumen_reflections_screen_traces() -> bool
```

(bool):  [Read-Write] Whether to use screen space traces for Lumen Reflections. Screen space traces bypass Lumen Scene and instead sample Scene Depth and Scene Color. This improves quality, as it bypasses Lumen Scene, but causes view dependent lighting.

<a id="unreal.PostProcessSettings.lumen_reflections_screen_traces"></a>

#### lumen_reflections_screen_traces

```python
@lumen_reflections_screen_traces.setter
def lumen_reflections_screen_traces(value: bool) -> None
```

<a id="unreal.PostProcessSettings.lumen_front_layer_translucency_reflections"></a>

#### lumen_front_layer_translucency_reflections

```python
@property
def lumen_front_layer_translucency_reflections() -> bool
```

(bool):  [Read-Write] Whether to use high quality mirror reflections on the front layer of translucent surfaces.  Other layers will use the lower quality Radiance Cache method that can only produce glossy reflections.  Increases GPU cost when enabled.

<a id="unreal.PostProcessSettings.lumen_front_layer_translucency_reflections"></a>

#### lumen_front_layer_translucency_reflections

```python
@lumen_front_layer_translucency_reflections.setter
def lumen_front_layer_translucency_reflections(value: bool) -> None
```

<a id="unreal.PostProcessSettings.lumen_max_roughness_to_trace_reflections"></a>

#### lumen_max_roughness_to_trace_reflections

```python
@property
def lumen_max_roughness_to_trace_reflections() -> float
```

(float):  [Read-Write] Sets the maximum roughness value for which Lumen still traces dedicated reflection rays. Higher values improve reflection quality, but greatly increase GPU cost.

<a id="unreal.PostProcessSettings.lumen_max_roughness_to_trace_reflections"></a>

#### lumen_max_roughness_to_trace_reflections

```python
@lumen_max_roughness_to_trace_reflections.setter
def lumen_max_roughness_to_trace_reflections(value: float) -> None
```

<a id="unreal.PostProcessSettings.lumen_max_reflection_bounces"></a>

#### lumen_max_reflection_bounces

```python
@property
def lumen_max_reflection_bounces() -> int
```

(int32):  [Read-Write] Sets the maximum number of recursive reflection bounces. 1 means a single reflection ray (no secondary reflections in mirrors). Currently only supported by Hardware Ray Tracing with Hit Lighting.

<a id="unreal.PostProcessSettings.lumen_max_reflection_bounces"></a>

#### lumen_max_reflection_bounces

```python
@lumen_max_reflection_bounces.setter
def lumen_max_reflection_bounces(value: int) -> None
```

<a id="unreal.PostProcessSettings.lumen_max_refraction_bounces"></a>

#### lumen_max_refraction_bounces

```python
@property
def lumen_max_refraction_bounces() -> int
```

(int32):  [Read-Write] The maximum count of refraction event to trace. When hit lighting is used, Translucent meshes will be traced when LumenMaxRefractionBounces > 0, making the reflection tracing more expenssive.

<a id="unreal.PostProcessSettings.lumen_max_refraction_bounces"></a>

#### lumen_max_refraction_bounces

```python
@lumen_max_refraction_bounces.setter
def lumen_max_refraction_bounces(value: int) -> None
```

<a id="unreal.PostProcessSettings.screen_space_reflection_intensity"></a>

#### screen_space_reflection_intensity

```python
@property
def screen_space_reflection_intensity() -> float
```

(float):  [Read-Write] Enable/Fade/disable the Screen Space Reflection feature, in percent, avoid numbers between 0 and 1 fo consistency

<a id="unreal.PostProcessSettings.screen_space_reflection_intensity"></a>

#### screen_space_reflection_intensity

```python
@screen_space_reflection_intensity.setter
def screen_space_reflection_intensity(value: float) -> None
```

<a id="unreal.PostProcessSettings.screen_space_reflection_quality"></a>

#### screen_space_reflection_quality

```python
@property
def screen_space_reflection_quality() -> float
```

(float):  [Read-Write] 0=lowest quality..100=maximum quality, only a few quality levels are implemented, no soft transition, 50 is the default for better performance.

<a id="unreal.PostProcessSettings.screen_space_reflection_quality"></a>

#### screen_space_reflection_quality

```python
@screen_space_reflection_quality.setter
def screen_space_reflection_quality(value: float) -> None
```

<a id="unreal.PostProcessSettings.screen_space_reflection_max_roughness"></a>

#### screen_space_reflection_max_roughness

```python
@property
def screen_space_reflection_max_roughness() -> float
```

(float):  [Read-Write] Until what roughness we fade the screen space reflections, 0.8 works well, smaller can run faster

<a id="unreal.PostProcessSettings.screen_space_reflection_max_roughness"></a>

#### screen_space_reflection_max_roughness

```python
@screen_space_reflection_max_roughness.setter
def screen_space_reflection_max_roughness(value: float) -> None
```

<a id="unreal.PostProcessSettings.mega_lights"></a>

#### mega_lights

```python
@property
def mega_lights() -> bool
```

(bool):  [Read-Write] Allows forcing MegaLights on or off for this volume, regardless of the project setting for MegaLights.
MegaLights will stochastically sample lights, which allows many shadow casting lights to be rendered efficiently, with a consistent and low GPU cost.
When MegaLights is enabled, other direct lighting algorithms like Deferred Shading will no longer be used, and other shadowing methods like Ray Traced Shadows, Distance Field Shadows and Shadow Maps will no longer be used.
MegaLights requires Hardware Ray Tracing and Shader Model 6.

<a id="unreal.PostProcessSettings.mega_lights"></a>

#### mega_lights

```python
@mega_lights.setter
def mega_lights(value: bool) -> None
```

<a id="unreal.PostProcessSettings.ambient_cubemap_tint"></a>

#### ambient_cubemap_tint

```python
@property
def ambient_cubemap_tint() -> LinearColor
```

(LinearColor):  [Read-Write] AmbientCubemap tint color

<a id="unreal.PostProcessSettings.ambient_cubemap_tint"></a>

#### ambient_cubemap_tint

```python
@ambient_cubemap_tint.setter
def ambient_cubemap_tint(value: LinearColor) -> None
```

<a id="unreal.PostProcessSettings.ambient_cubemap_intensity"></a>

#### ambient_cubemap_intensity

```python
@property
def ambient_cubemap_intensity() -> float
```

(float):  [Read-Write] To scale the Ambient cubemap brightness
>=0: off, 1(default), >1 brighter

<a id="unreal.PostProcessSettings.ambient_cubemap_intensity"></a>

#### ambient_cubemap_intensity

```python
@ambient_cubemap_intensity.setter
def ambient_cubemap_intensity(value: float) -> None
```

<a id="unreal.PostProcessSettings.ambient_cubemap"></a>

#### ambient_cubemap

```python
@property
def ambient_cubemap() -> TextureCube
```

(TextureCube):  [Read-Write] The Ambient cubemap (Affects diffuse and specular shading), blends additively which if different from all other settings here

<a id="unreal.PostProcessSettings.ambient_cubemap"></a>

#### ambient_cubemap

```python
@ambient_cubemap.setter
def ambient_cubemap(value: TextureCube) -> None
```

<a id="unreal.PostProcessSettings.camera_shutter_speed"></a>

#### camera_shutter_speed

```python
@property
def camera_shutter_speed() -> float
```

(float):  [Read-Write] The camera shutter in seconds.

<a id="unreal.PostProcessSettings.camera_shutter_speed"></a>

#### camera_shutter_speed

```python
@camera_shutter_speed.setter
def camera_shutter_speed(value: float) -> None
```

<a id="unreal.PostProcessSettings.camera_iso"></a>

#### camera_iso

```python
@property
def camera_iso() -> float
```

(float):  [Read-Write] The camera sensor sensitivity

<a id="unreal.PostProcessSettings.camera_iso"></a>

#### camera_iso

```python
@camera_iso.setter
def camera_iso(value: float) -> None
```

<a id="unreal.PostProcessSettings.depth_of_field_fstop"></a>

#### depth_of_field_fstop

```python
@property
def depth_of_field_fstop() -> float
```

(float):  [Read-Write] Defines the opening of the camera lens, Aperture is 1/fstop, typical lens go down to f/1.2 (large opening), larger numbers reduce the DOF effect

<a id="unreal.PostProcessSettings.depth_of_field_fstop"></a>

#### depth_of_field_fstop

```python
@depth_of_field_fstop.setter
def depth_of_field_fstop(value: float) -> None
```

<a id="unreal.PostProcessSettings.depth_of_field_min_fstop"></a>

#### depth_of_field_min_fstop

```python
@property
def depth_of_field_min_fstop() -> float
```

(float):  [Read-Write] Defines the maximum opening of the camera lens to control the curvature of blades of the diaphragm. Set it to 0 to get straight blades.

<a id="unreal.PostProcessSettings.depth_of_field_min_fstop"></a>

#### depth_of_field_min_fstop

```python
@depth_of_field_min_fstop.setter
def depth_of_field_min_fstop(value: float) -> None
```

<a id="unreal.PostProcessSettings.depth_of_field_blade_count"></a>

#### depth_of_field_blade_count

```python
@property
def depth_of_field_blade_count() -> int
```

(int32):  [Read-Write] Defines the number of blades of the diaphragm within the lens (between 4 and 16).

<a id="unreal.PostProcessSettings.depth_of_field_blade_count"></a>

#### depth_of_field_blade_count

```python
@depth_of_field_blade_count.setter
def depth_of_field_blade_count(value: int) -> None
```

<a id="unreal.PostProcessSettings.auto_exposure_bias"></a>

#### auto_exposure_bias

```python
@property
def auto_exposure_bias() -> float
```

(float):  [Read-Write] Logarithmic adjustment for the exposure. Only used if a tonemapper is specified.
0: no adjustment, -1:2x darker, -2:4x darker, 1:2x brighter, 2:4x brighter, ...

<a id="unreal.PostProcessSettings.auto_exposure_bias"></a>

#### auto_exposure_bias

```python
@auto_exposure_bias.setter
def auto_exposure_bias(value: float) -> None
```

<a id="unreal.PostProcessSettings.exposure_offset"></a>

#### exposure_offset

```python
@property
def exposure_offset() -> float
```

deprecated: 'exposure_offset' was renamed to 'auto_exposure_bias'.

<a id="unreal.PostProcessSettings.exposure_offset"></a>

#### exposure_offset

```python
@exposure_offset.setter
def exposure_offset(value: float) -> None
```

<a id="unreal.PostProcessSettings.auto_exposure_apply_physical_camera_exposure"></a>

#### auto_exposure_apply_physical_camera_exposure

```python
@property
def auto_exposure_apply_physical_camera_exposure() -> bool
```

(bool):  [Read-Write] Only affects Manual exposure mode.

<a id="unreal.PostProcessSettings.auto_exposure_apply_physical_camera_exposure"></a>

#### auto_exposure_apply_physical_camera_exposure

```python
@auto_exposure_apply_physical_camera_exposure.setter
def auto_exposure_apply_physical_camera_exposure(value: bool) -> None
```

<a id="unreal.PostProcessSettings.auto_exposure_bias_curve"></a>

#### auto_exposure_bias_curve

```python
@property
def auto_exposure_bias_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write] Exposure compensation based on the scene EV100.
Used to calibrate the final exposure differently depending on the average scene luminance.
0: no adjustment, -1:2x darker, -2:4x darker, 1:2x brighter, 2:4x brighter, ...

<a id="unreal.PostProcessSettings.auto_exposure_bias_curve"></a>

#### auto_exposure_bias_curve

```python
@auto_exposure_bias_curve.setter
def auto_exposure_bias_curve(value: CurveFloat) -> None
```

<a id="unreal.PostProcessSettings.auto_exposure_meter_mask"></a>

#### auto_exposure_meter_mask

```python
@property
def auto_exposure_meter_mask() -> Texture
```

(Texture):  [Read-Write] Exposure metering mask. Bright spots on the mask will have high influence on auto-exposure metering
and dark spots will have low influence.

<a id="unreal.PostProcessSettings.auto_exposure_meter_mask"></a>

#### auto_exposure_meter_mask

```python
@auto_exposure_meter_mask.setter
def auto_exposure_meter_mask(value: Texture) -> None
```

<a id="unreal.PostProcessSettings.auto_exposure_low_percent"></a>

#### auto_exposure_low_percent

```python
@property
def auto_exposure_low_percent() -> float
```

(float):  [Read-Write] The eye adaptation will adapt to a value extracted from the luminance histogram of the scene color.
The value is defined as having x percent below this brightness. Higher values give bright spots on the screen more priority
but can lead to less stable results. Lower values give the medium and darker values more priority but might cause burn out of
bright spots.
>0, <100, good values are in the range 70 .. 80

<a id="unreal.PostProcessSettings.auto_exposure_low_percent"></a>

#### auto_exposure_low_percent

```python
@auto_exposure_low_percent.setter
def auto_exposure_low_percent(value: float) -> None
```

<a id="unreal.PostProcessSettings.eye_adaptation_low_percent"></a>

#### eye_adaptation_low_percent

```python
@property
def eye_adaptation_low_percent() -> float
```

deprecated: 'eye_adaptation_low_percent' was renamed to 'auto_exposure_low_percent'.

<a id="unreal.PostProcessSettings.eye_adaptation_low_percent"></a>

#### eye_adaptation_low_percent

```python
@eye_adaptation_low_percent.setter
def eye_adaptation_low_percent(value: float) -> None
```

<a id="unreal.PostProcessSettings.auto_exposure_high_percent"></a>

#### auto_exposure_high_percent

```python
@property
def auto_exposure_high_percent() -> float
```

(float):  [Read-Write] The eye adaptation will adapt to a value extracted from the luminance histogram of the scene color.
The value is defined as having x percent below this brightness. Higher values give bright spots on the screen more priority
but can lead to less stable results. Lower values give the medium and darker values more priority but might cause burn out of
bright spots.
>0, <100, good values are in the range 80 .. 95

<a id="unreal.PostProcessSettings.auto_exposure_high_percent"></a>

#### auto_exposure_high_percent

```python
@auto_exposure_high_percent.setter
def auto_exposure_high_percent(value: float) -> None
```

<a id="unreal.PostProcessSettings.eye_adaptation_high_percent"></a>

#### eye_adaptation_high_percent

```python
@property
def eye_adaptation_high_percent() -> float
```

deprecated: 'eye_adaptation_high_percent' was renamed to 'auto_exposure_high_percent'.

<a id="unreal.PostProcessSettings.eye_adaptation_high_percent"></a>

#### eye_adaptation_high_percent

```python
@eye_adaptation_high_percent.setter
def eye_adaptation_high_percent(value: float) -> None
```

<a id="unreal.PostProcessSettings.auto_exposure_min_brightness"></a>

#### auto_exposure_min_brightness

```python
@property
def auto_exposure_min_brightness() -> float
```

(float):  [Read-Write] Auto-Exposure minimum adaptation. Eye Adaptation is disabled if Min = Max.
Auto-exposure is implemented by choosing an exposure value for which the average luminance generates a pixel brightness equal to the Constant Calibration value.
The Min/Max are expressed in pixel luminance (cd/m2) or in EV100 when using ExtendDefaultLuminanceRange (see project settings).

<a id="unreal.PostProcessSettings.auto_exposure_min_brightness"></a>

#### auto_exposure_min_brightness

```python
@auto_exposure_min_brightness.setter
def auto_exposure_min_brightness(value: float) -> None
```

<a id="unreal.PostProcessSettings.eye_adaptation_min_brightness"></a>

#### eye_adaptation_min_brightness

```python
@property
def eye_adaptation_min_brightness() -> float
```

deprecated: 'eye_adaptation_min_brightness' was renamed to 'auto_exposure_min_brightness'.

<a id="unreal.PostProcessSettings.eye_adaptation_min_brightness"></a>

#### eye_adaptation_min_brightness

```python
@eye_adaptation_min_brightness.setter
def eye_adaptation_min_brightness(value: float) -> None
```

<a id="unreal.PostProcessSettings.auto_exposure_max_brightness"></a>

#### auto_exposure_max_brightness

```python
@property
def auto_exposure_max_brightness() -> float
```

(float):  [Read-Write] Auto-Exposure maximum adaptation. Eye Adaptation is disabled if Min = Max.
Auto-exposure is implemented by choosing an exposure value for which the average luminance generates a pixel brightness equal to the Constant Calibration value.
The Min/Max are expressed in pixel luminance (cd/m2) or in EV100 when using ExtendDefaultLuminanceRange (see project settings).

<a id="unreal.PostProcessSettings.auto_exposure_max_brightness"></a>

#### auto_exposure_max_brightness

```python
@auto_exposure_max_brightness.setter
def auto_exposure_max_brightness(value: float) -> None
```

<a id="unreal.PostProcessSettings.eye_adaptation_max_brightness"></a>

#### eye_adaptation_max_brightness

```python
@property
def eye_adaptation_max_brightness() -> float
```

deprecated: 'eye_adaptation_max_brightness' was renamed to 'auto_exposure_max_brightness'.

<a id="unreal.PostProcessSettings.eye_adaptation_max_brightness"></a>

#### eye_adaptation_max_brightness

```python
@eye_adaptation_max_brightness.setter
def eye_adaptation_max_brightness(value: float) -> None
```

<a id="unreal.PostProcessSettings.auto_exposure_speed_up"></a>

#### auto_exposure_speed_up

```python
@property
def auto_exposure_speed_up() -> float
```

(float):  [Read-Write] In F-stops per second, should be >0

<a id="unreal.PostProcessSettings.auto_exposure_speed_up"></a>

#### auto_exposure_speed_up

```python
@auto_exposure_speed_up.setter
def auto_exposure_speed_up(value: float) -> None
```

<a id="unreal.PostProcessSettings.eye_adaption_speed_up"></a>

#### eye_adaption_speed_up

```python
@property
def eye_adaption_speed_up() -> float
```

deprecated: 'eye_adaption_speed_up' was renamed to 'auto_exposure_speed_up'.

<a id="unreal.PostProcessSettings.eye_adaption_speed_up"></a>

#### eye_adaption_speed_up

```python
@eye_adaption_speed_up.setter
def eye_adaption_speed_up(value: float) -> None
```

<a id="unreal.PostProcessSettings.auto_exposure_speed_down"></a>

#### auto_exposure_speed_down

```python
@property
def auto_exposure_speed_down() -> float
```

(float):  [Read-Write] In F-stops per second, should be >0

<a id="unreal.PostProcessSettings.auto_exposure_speed_down"></a>

#### auto_exposure_speed_down

```python
@auto_exposure_speed_down.setter
def auto_exposure_speed_down(value: float) -> None
```

<a id="unreal.PostProcessSettings.eye_adaption_speed_down"></a>

#### eye_adaption_speed_down

```python
@property
def eye_adaption_speed_down() -> float
```

deprecated: 'eye_adaption_speed_down' was renamed to 'auto_exposure_speed_down'.

<a id="unreal.PostProcessSettings.eye_adaption_speed_down"></a>

#### eye_adaption_speed_down

```python
@eye_adaption_speed_down.setter
def eye_adaption_speed_down(value: float) -> None
```

<a id="unreal.PostProcessSettings.histogram_log_min"></a>

#### histogram_log_min

```python
@property
def histogram_log_min() -> float
```

(float):  [Read-Write] Histogram Min value. Expressed in Log2(Luminance) or in EV100 when using ExtendDefaultLuminanceRange (see project settings)

<a id="unreal.PostProcessSettings.histogram_log_min"></a>

#### histogram_log_min

```python
@histogram_log_min.setter
def histogram_log_min(value: float) -> None
```

<a id="unreal.PostProcessSettings.histogram_log_max"></a>

#### histogram_log_max

```python
@property
def histogram_log_max() -> float
```

(float):  [Read-Write] Histogram Max value. Expressed in Log2(Luminance) or in EV100 when using ExtendDefaultLuminanceRange (see project settings)

<a id="unreal.PostProcessSettings.histogram_log_max"></a>

#### histogram_log_max

```python
@histogram_log_max.setter
def histogram_log_max(value: float) -> None
```

<a id="unreal.PostProcessSettings.local_exposure_method"></a>

#### local_exposure_method

```python
@property
def local_exposure_method() -> LocalExposureMethod
```

(LocalExposureMethod):  [Read-Write] Local Exposure algorithm

<a id="unreal.PostProcessSettings.local_exposure_method"></a>

#### local_exposure_method

```python
@local_exposure_method.setter
def local_exposure_method(value: LocalExposureMethod) -> None
```

<a id="unreal.PostProcessSettings.local_exposure_highlight_contrast_scale"></a>

#### local_exposure_highlight_contrast_scale

```python
@property
def local_exposure_highlight_contrast_scale() -> float
```

(float):  [Read-Write] Local Exposure decomposes luminance of the frame into a base layer and a detail layer.
Contrast of the base layer is reduced based on this value.
Value less than 1 will enable local exposure.
Good values are usually in the range 0.6 .. 1.0.

<a id="unreal.PostProcessSettings.local_exposure_highlight_contrast_scale"></a>

#### local_exposure_highlight_contrast_scale

```python
@local_exposure_highlight_contrast_scale.setter
def local_exposure_highlight_contrast_scale(value: float) -> None
```

<a id="unreal.PostProcessSettings.local_exposure_shadow_contrast_scale"></a>

#### local_exposure_shadow_contrast_scale

```python
@property
def local_exposure_shadow_contrast_scale() -> float
```

(float):  [Read-Write] Local Exposure decomposes luminance of the frame into a base layer and a detail layer.
Contrast of the base layer is reduced based on this value.
Value less than 1 will enable local exposure.
Good values are usually in the range 0.6 .. 1.0.

<a id="unreal.PostProcessSettings.local_exposure_shadow_contrast_scale"></a>

#### local_exposure_shadow_contrast_scale

```python
@local_exposure_shadow_contrast_scale.setter
def local_exposure_shadow_contrast_scale(value: float) -> None
```

<a id="unreal.PostProcessSettings.local_exposure_highlight_contrast_curve"></a>

#### local_exposure_highlight_contrast_curve

```python
@property
def local_exposure_highlight_contrast_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write] Local Exposure Highlight Contrast based on the scene EV100.
Used to calibrate Local Exposure differently depending on the average scene luminance.

<a id="unreal.PostProcessSettings.local_exposure_highlight_contrast_curve"></a>

#### local_exposure_highlight_contrast_curve

```python
@local_exposure_highlight_contrast_curve.setter
def local_exposure_highlight_contrast_curve(value: CurveFloat) -> None
```

<a id="unreal.PostProcessSettings.local_exposure_shadow_contrast_curve"></a>

#### local_exposure_shadow_contrast_curve

```python
@property
def local_exposure_shadow_contrast_curve() -> CurveFloat
```

(CurveFloat):  [Read-Write] Local Exposure Shadow Contrast based on the scene EV100.
Used to calibrate Local Exposure differently depending on the average scene luminance.

<a id="unreal.PostProcessSettings.local_exposure_shadow_contrast_curve"></a>

#### local_exposure_shadow_contrast_curve

```python
@local_exposure_shadow_contrast_curve.setter
def local_exposure_shadow_contrast_curve(value: CurveFloat) -> None
```

<a id="unreal.PostProcessSettings.local_exposure_highlight_threshold"></a>

#### local_exposure_highlight_threshold

```python
@property
def local_exposure_highlight_threshold() -> float
```

(float):  [Read-Write] Threshold used to determine which regions of the screen are considered highlights.

<a id="unreal.PostProcessSettings.local_exposure_highlight_threshold"></a>

#### local_exposure_highlight_threshold

```python
@local_exposure_highlight_threshold.setter
def local_exposure_highlight_threshold(value: float) -> None
```

<a id="unreal.PostProcessSettings.local_exposure_shadow_threshold"></a>

#### local_exposure_shadow_threshold

```python
@property
def local_exposure_shadow_threshold() -> float
```

(float):  [Read-Write] Threshold used to determine which regions of the screen are considered shadows.

<a id="unreal.PostProcessSettings.local_exposure_shadow_threshold"></a>

#### local_exposure_shadow_threshold

```python
@local_exposure_shadow_threshold.setter
def local_exposure_shadow_threshold(value: float) -> None
```

<a id="unreal.PostProcessSettings.local_exposure_detail_strength"></a>

#### local_exposure_detail_strength

```python
@property
def local_exposure_detail_strength() -> float
```

(float):  [Read-Write] Local Exposure decomposes luminance of the frame into a base layer and a detail layer.
Value different than 1 will enable local exposure.
This value should be set to 1 in most cases.

<a id="unreal.PostProcessSettings.local_exposure_detail_strength"></a>

#### local_exposure_detail_strength

```python
@local_exposure_detail_strength.setter
def local_exposure_detail_strength(value: float) -> None
```

<a id="unreal.PostProcessSettings.local_exposure_blurred_luminance_blend"></a>

#### local_exposure_blurred_luminance_blend

```python
@property
def local_exposure_blurred_luminance_blend() -> float
```

(float):  [Read-Write] Local Exposure decomposes luminance of the frame into a base layer and a detail layer.
Blend between bilateral filtered and blurred luminance as the base layer.
Blurred luminance helps preserve image appearance and specular highlights, and reduce ringing.
Good values are usually in the range 0.4 .. 0.6

<a id="unreal.PostProcessSettings.local_exposure_blurred_luminance_blend"></a>

#### local_exposure_blurred_luminance_blend

```python
@local_exposure_blurred_luminance_blend.setter
def local_exposure_blurred_luminance_blend(value: float) -> None
```

<a id="unreal.PostProcessSettings.local_exposure_blurred_luminance_kernel_size_percent"></a>

#### local_exposure_blurred_luminance_kernel_size_percent

```python
@property
def local_exposure_blurred_luminance_kernel_size_percent() -> float
```

(float):  [Read-Write] Kernel size (percentage of screen) used to blur frame luminance.

<a id="unreal.PostProcessSettings.local_exposure_blurred_luminance_kernel_size_percent"></a>

#### local_exposure_blurred_luminance_kernel_size_percent

```python
@local_exposure_blurred_luminance_kernel_size_percent.setter
def local_exposure_blurred_luminance_kernel_size_percent(value: float) -> None
```

<a id="unreal.PostProcessSettings.local_exposure_middle_grey_bias"></a>

#### local_exposure_middle_grey_bias

```python
@property
def local_exposure_middle_grey_bias() -> float
```

(float):  [Read-Write] Logarithmic adjustment for the local exposure middle grey.
0: no adjustment, -1:2x darker, -2:4x darker, 1:2x brighter, 2:4x brighter, ...

<a id="unreal.PostProcessSettings.local_exposure_middle_grey_bias"></a>

#### local_exposure_middle_grey_bias

```python
@local_exposure_middle_grey_bias.setter
def local_exposure_middle_grey_bias(value: float) -> None
```

<a id="unreal.PostProcessSettings.lens_flare_intensity"></a>

#### lens_flare_intensity

```python
@property
def lens_flare_intensity() -> float
```

(float):  [Read-Write] Brightness scale of the image cased lens flares (linear)

<a id="unreal.PostProcessSettings.lens_flare_intensity"></a>

#### lens_flare_intensity

```python
@lens_flare_intensity.setter
def lens_flare_intensity(value: float) -> None
```

<a id="unreal.PostProcessSettings.lens_flare_tint"></a>

#### lens_flare_tint

```python
@property
def lens_flare_tint() -> LinearColor
```

(LinearColor):  [Read-Write] Tint color for the image based lens flares.

<a id="unreal.PostProcessSettings.lens_flare_tint"></a>

#### lens_flare_tint

```python
@lens_flare_tint.setter
def lens_flare_tint(value: LinearColor) -> None
```

<a id="unreal.PostProcessSettings.lens_flare_bokeh_size"></a>

#### lens_flare_bokeh_size

```python
@property
def lens_flare_bokeh_size() -> float
```

(float):  [Read-Write] Size of the Lens Blur (in percent of the view width) that is done with the Bokeh texture (note: performance cost is radius*radius)

<a id="unreal.PostProcessSettings.lens_flare_bokeh_size"></a>

#### lens_flare_bokeh_size

```python
@lens_flare_bokeh_size.setter
def lens_flare_bokeh_size(value: float) -> None
```

<a id="unreal.PostProcessSettings.lens_flare_threshold"></a>

#### lens_flare_threshold

```python
@property
def lens_flare_threshold() -> float
```

(float):  [Read-Write] Minimum brightness the lens flare starts having effect (this should be as high as possible to avoid the performance cost of blurring content that is too dark too see)

<a id="unreal.PostProcessSettings.lens_flare_threshold"></a>

#### lens_flare_threshold

```python
@lens_flare_threshold.setter
def lens_flare_threshold(value: float) -> None
```

<a id="unreal.PostProcessSettings.lens_flare_bokeh_shape"></a>

#### lens_flare_bokeh_shape

```python
@property
def lens_flare_bokeh_shape() -> Texture
```

(Texture):  [Read-Write] Defines the shape of the Bokeh when the image base lens flares are blurred, cannot be blended

<a id="unreal.PostProcessSettings.lens_flare_bokeh_shape"></a>

#### lens_flare_bokeh_shape

```python
@lens_flare_bokeh_shape.setter
def lens_flare_bokeh_shape(value: Texture) -> None
```

<a id="unreal.PostProcessSettings.vignette_intensity"></a>

#### vignette_intensity

```python
@property
def vignette_intensity() -> float
```

(float):  [Read-Write] 0..1 0=off/no vignette .. 1=strong vignette

<a id="unreal.PostProcessSettings.vignette_intensity"></a>

#### vignette_intensity

```python
@vignette_intensity.setter
def vignette_intensity(value: float) -> None
```

<a id="unreal.PostProcessSettings.sharpen"></a>

#### sharpen

```python
@property
def sharpen() -> float
```

(float):  [Read-Write] Controls the strength of image sharpening applied during tonemapping.

<a id="unreal.PostProcessSettings.sharpen"></a>

#### sharpen

```python
@sharpen.setter
def sharpen(value: float) -> None
```

<a id="unreal.PostProcessSettings.film_grain_intensity"></a>

#### film_grain_intensity

```python
@property
def film_grain_intensity() -> float
```

(float):  [Read-Write] 0..1 Film grain intensity to apply. LinearSceneColor *= lerp(1.0, DecodedFilmGrainTexture, FilmGrainIntensity)

<a id="unreal.PostProcessSettings.film_grain_intensity"></a>

#### film_grain_intensity

```python
@film_grain_intensity.setter
def film_grain_intensity(value: float) -> None
```

<a id="unreal.PostProcessSettings.film_grain_intensity_shadows"></a>

#### film_grain_intensity_shadows

```python
@property
def film_grain_intensity_shadows() -> float
```

(float):  [Read-Write] Control over the grain intensity in the regions of the image considered shadow areas.

<a id="unreal.PostProcessSettings.film_grain_intensity_shadows"></a>

#### film_grain_intensity_shadows

```python
@film_grain_intensity_shadows.setter
def film_grain_intensity_shadows(value: float) -> None
```

<a id="unreal.PostProcessSettings.film_grain_intensity_midtones"></a>

#### film_grain_intensity_midtones

```python
@property
def film_grain_intensity_midtones() -> float
```

(float):  [Read-Write] Control over the grain intensity in the mid-tone region of the image.

<a id="unreal.PostProcessSettings.film_grain_intensity_midtones"></a>

#### film_grain_intensity_midtones

```python
@film_grain_intensity_midtones.setter
def film_grain_intensity_midtones(value: float) -> None
```

<a id="unreal.PostProcessSettings.film_grain_intensity_highlights"></a>

#### film_grain_intensity_highlights

```python
@property
def film_grain_intensity_highlights() -> float
```

(float):  [Read-Write] Control over the grain intensity in the regions of the image considered highlight areas.

<a id="unreal.PostProcessSettings.film_grain_intensity_highlights"></a>

#### film_grain_intensity_highlights

```python
@film_grain_intensity_highlights.setter
def film_grain_intensity_highlights(value: float) -> None
```

<a id="unreal.PostProcessSettings.film_grain_shadows_max"></a>

#### film_grain_shadows_max

```python
@property
def film_grain_shadows_max() -> float
```

(float):  [Read-Write] Sets the upper bound used for Film Grain Shadow Intensity.

<a id="unreal.PostProcessSettings.film_grain_shadows_max"></a>

#### film_grain_shadows_max

```python
@film_grain_shadows_max.setter
def film_grain_shadows_max(value: float) -> None
```

<a id="unreal.PostProcessSettings.film_grain_highlights_min"></a>

#### film_grain_highlights_min

```python
@property
def film_grain_highlights_min() -> float
```

(float):  [Read-Write] Sets the lower bound used for Film Grain Highlight Intensity.

<a id="unreal.PostProcessSettings.film_grain_highlights_min"></a>

#### film_grain_highlights_min

```python
@film_grain_highlights_min.setter
def film_grain_highlights_min(value: float) -> None
```

<a id="unreal.PostProcessSettings.film_grain_highlights_max"></a>

#### film_grain_highlights_max

```python
@property
def film_grain_highlights_max() -> float
```

(float):  [Read-Write] Sets the upper bound used for Film Grain Highlight Intensity. This value should be larger than HighlightsMin.. Default is 1.0, for backwards compatibility

<a id="unreal.PostProcessSettings.film_grain_highlights_max"></a>

#### film_grain_highlights_max

```python
@film_grain_highlights_max.setter
def film_grain_highlights_max(value: float) -> None
```

<a id="unreal.PostProcessSettings.film_grain_texel_size"></a>

#### film_grain_texel_size

```python
@property
def film_grain_texel_size() -> float
```

(float):  [Read-Write] Controls the size of the film grain. Size of texel of FilmGrainTexture on screen.

<a id="unreal.PostProcessSettings.film_grain_texel_size"></a>

#### film_grain_texel_size

```python
@film_grain_texel_size.setter
def film_grain_texel_size(value: float) -> None
```

<a id="unreal.PostProcessSettings.film_grain_texture"></a>

#### film_grain_texture

```python
@property
def film_grain_texture() -> Texture2D
```

(Texture2D):  [Read-Write] Defines film grain texture to use.

<a id="unreal.PostProcessSettings.film_grain_texture"></a>

#### film_grain_texture

```python
@film_grain_texture.setter
def film_grain_texture(value: Texture2D) -> None
```

<a id="unreal.PostProcessSettings.ambient_occlusion_intensity"></a>

#### ambient_occlusion_intensity

```python
@property
def ambient_occlusion_intensity() -> float
```

(float):  [Read-Write] 0..1 0=off/no ambient occlusion .. 1=strong ambient occlusion, defines how much it affects the non direct lighting after base pass

<a id="unreal.PostProcessSettings.ambient_occlusion_intensity"></a>

#### ambient_occlusion_intensity

```python
@ambient_occlusion_intensity.setter
def ambient_occlusion_intensity(value: float) -> None
```

<a id="unreal.PostProcessSettings.ambient_occlusion_static_fraction"></a>

#### ambient_occlusion_static_fraction

```python
@property
def ambient_occlusion_static_fraction() -> float
```

(float):  [Read-Write] 0..1 0=no effect on static lighting .. 1=AO affects the stat lighting, 0 is free meaning no extra rendering pass

<a id="unreal.PostProcessSettings.ambient_occlusion_static_fraction"></a>

#### ambient_occlusion_static_fraction

```python
@ambient_occlusion_static_fraction.setter
def ambient_occlusion_static_fraction(value: float) -> None
```

<a id="unreal.PostProcessSettings.ambient_occlusion_radius"></a>

#### ambient_occlusion_radius

```python
@property
def ambient_occlusion_radius() -> float
```

(float):  [Read-Write] >0, in unreal units, bigger values means even distant surfaces affect the ambient occlusion

<a id="unreal.PostProcessSettings.ambient_occlusion_radius"></a>

#### ambient_occlusion_radius

```python
@ambient_occlusion_radius.setter
def ambient_occlusion_radius(value: float) -> None
```

<a id="unreal.PostProcessSettings.ambient_occlusion_radius_in_ws"></a>

#### ambient_occlusion_radius_in_ws

```python
@property
def ambient_occlusion_radius_in_ws() -> bool
```

(bool):  [Read-Write] true: AO radius is in world space units, false: AO radius is locked the view space in 400 units

<a id="unreal.PostProcessSettings.ambient_occlusion_radius_in_ws"></a>

#### ambient_occlusion_radius_in_ws

```python
@ambient_occlusion_radius_in_ws.setter
def ambient_occlusion_radius_in_ws(value: bool) -> None
```

<a id="unreal.PostProcessSettings.ambient_occlusion_fade_distance"></a>

#### ambient_occlusion_fade_distance

```python
@property
def ambient_occlusion_fade_distance() -> float
```

(float):  [Read-Write] >0, in unreal units, at what distance the AO effect disppears in the distance (avoding artifacts and AO effects on huge object)

<a id="unreal.PostProcessSettings.ambient_occlusion_fade_distance"></a>

#### ambient_occlusion_fade_distance

```python
@ambient_occlusion_fade_distance.setter
def ambient_occlusion_fade_distance(value: float) -> None
```

<a id="unreal.PostProcessSettings.ambient_occlusion_fade_radius"></a>

#### ambient_occlusion_fade_radius

```python
@property
def ambient_occlusion_fade_radius() -> float
```

(float):  [Read-Write] >0, in unreal units, how many units before AmbientOcclusionFadeOutDistance it starts fading out

<a id="unreal.PostProcessSettings.ambient_occlusion_fade_radius"></a>

#### ambient_occlusion_fade_radius

```python
@ambient_occlusion_fade_radius.setter
def ambient_occlusion_fade_radius(value: float) -> None
```

<a id="unreal.PostProcessSettings.ambient_occlusion_power"></a>

#### ambient_occlusion_power

```python
@property
def ambient_occlusion_power() -> float
```

(float):  [Read-Write] >0, in unreal units, bigger values means even distant surfaces affect the ambient occlusion

<a id="unreal.PostProcessSettings.ambient_occlusion_power"></a>

#### ambient_occlusion_power

```python
@ambient_occlusion_power.setter
def ambient_occlusion_power(value: float) -> None
```

<a id="unreal.PostProcessSettings.ambient_occlusion_bias"></a>

#### ambient_occlusion_bias

```python
@property
def ambient_occlusion_bias() -> float
```

(float):  [Read-Write] >0, in unreal units, default (3.0) works well for flat surfaces but can reduce details

<a id="unreal.PostProcessSettings.ambient_occlusion_bias"></a>

#### ambient_occlusion_bias

```python
@ambient_occlusion_bias.setter
def ambient_occlusion_bias(value: float) -> None
```

<a id="unreal.PostProcessSettings.ambient_occlusion_quality"></a>

#### ambient_occlusion_quality

```python
@property
def ambient_occlusion_quality() -> float
```

(float):  [Read-Write] 0=lowest quality..100=maximum quality, only a few quality levels are implemented, no soft transition

<a id="unreal.PostProcessSettings.ambient_occlusion_quality"></a>

#### ambient_occlusion_quality

```python
@ambient_occlusion_quality.setter
def ambient_occlusion_quality(value: float) -> None
```

<a id="unreal.PostProcessSettings.ambient_occlusion_mip_blend"></a>

#### ambient_occlusion_mip_blend

```python
@property
def ambient_occlusion_mip_blend() -> float
```

(float):  [Read-Write] Affects the blend over the multiple mips (lower resolution versions) , 0:fully use full resolution, 1::fully use low resolution, around 0.6 seems to be a good value

<a id="unreal.PostProcessSettings.ambient_occlusion_mip_blend"></a>

#### ambient_occlusion_mip_blend

```python
@ambient_occlusion_mip_blend.setter
def ambient_occlusion_mip_blend(value: float) -> None
```

<a id="unreal.PostProcessSettings.ambient_occlusion_mip_scale"></a>

#### ambient_occlusion_mip_scale

```python
@property
def ambient_occlusion_mip_scale() -> float
```

(float):  [Read-Write] Affects the radius AO radius scale over the multiple mips (lower resolution versions)

<a id="unreal.PostProcessSettings.ambient_occlusion_mip_scale"></a>

#### ambient_occlusion_mip_scale

```python
@ambient_occlusion_mip_scale.setter
def ambient_occlusion_mip_scale(value: float) -> None
```

<a id="unreal.PostProcessSettings.ambient_occlusion_mip_threshold"></a>

#### ambient_occlusion_mip_threshold

```python
@property
def ambient_occlusion_mip_threshold() -> float
```

(float):  [Read-Write] to tweak the bilateral upsampling when using multiple mips (lower resolution versions)

<a id="unreal.PostProcessSettings.ambient_occlusion_mip_threshold"></a>

#### ambient_occlusion_mip_threshold

```python
@ambient_occlusion_mip_threshold.setter
def ambient_occlusion_mip_threshold(value: float) -> None
```

<a id="unreal.PostProcessSettings.ambient_occlusion_temporal_blend_weight"></a>

#### ambient_occlusion_temporal_blend_weight

```python
@property
def ambient_occlusion_temporal_blend_weight() -> float
```

(float):  [Read-Write] How much to blend the current frame with previous frames when using GTAO with temporal accumulation

<a id="unreal.PostProcessSettings.ambient_occlusion_temporal_blend_weight"></a>

#### ambient_occlusion_temporal_blend_weight

```python
@ambient_occlusion_temporal_blend_weight.setter
def ambient_occlusion_temporal_blend_weight(value: float) -> None
```

<a id="unreal.PostProcessSettings.ray_tracing_ao"></a>

#### ray_tracing_ao

```python
@property
def ray_tracing_ao() -> bool
```

(bool):  [Read-Write] Enables ray tracing ambient occlusion.

<a id="unreal.PostProcessSettings.ray_tracing_ao"></a>

#### ray_tracing_ao

```python
@ray_tracing_ao.setter
def ray_tracing_ao(value: bool) -> None
```

<a id="unreal.PostProcessSettings.ray_tracing_ao_samples_per_pixel"></a>

#### ray_tracing_ao_samples_per_pixel

```python
@property
def ray_tracing_ao_samples_per_pixel() -> int
```

(int32):  [Read-Write] Sets the samples per pixel for ray tracing ambient occlusion.

<a id="unreal.PostProcessSettings.ray_tracing_ao_samples_per_pixel"></a>

#### ray_tracing_ao_samples_per_pixel

```python
@ray_tracing_ao_samples_per_pixel.setter
def ray_tracing_ao_samples_per_pixel(value: int) -> None
```

<a id="unreal.PostProcessSettings.ray_tracing_ao_intensity"></a>

#### ray_tracing_ao_intensity

```python
@property
def ray_tracing_ao_intensity() -> float
```

(float):  [Read-Write] Scalar factor on the ray-tracing ambient occlusion score.

<a id="unreal.PostProcessSettings.ray_tracing_ao_intensity"></a>

#### ray_tracing_ao_intensity

```python
@ray_tracing_ao_intensity.setter
def ray_tracing_ao_intensity(value: float) -> None
```

<a id="unreal.PostProcessSettings.ray_tracing_ao_radius"></a>

#### ray_tracing_ao_radius

```python
@property
def ray_tracing_ao_radius() -> float
```

(float):  [Read-Write] Defines the world-space search radius for occlusion rays.

<a id="unreal.PostProcessSettings.ray_tracing_ao_radius"></a>

#### ray_tracing_ao_radius

```python
@ray_tracing_ao_radius.setter
def ray_tracing_ao_radius(value: float) -> None
```

<a id="unreal.PostProcessSettings.color_grading_intensity"></a>

#### color_grading_intensity

```python
@property
def color_grading_intensity() -> float
```

(float):  [Read-Write] Color grading lookup table intensity. 0 = no intensity, 1=full intensity

<a id="unreal.PostProcessSettings.color_grading_intensity"></a>

#### color_grading_intensity

```python
@color_grading_intensity.setter
def color_grading_intensity(value: float) -> None
```

<a id="unreal.PostProcessSettings.color_grading_lut"></a>

#### color_grading_lut

```python
@property
def color_grading_lut() -> Texture
```

(Texture):  [Read-Write] Look up table texture to use or none of not used

<a id="unreal.PostProcessSettings.color_grading_lut"></a>

#### color_grading_lut

```python
@color_grading_lut.setter
def color_grading_lut(value: Texture) -> None
```

<a id="unreal.PostProcessSettings.depth_of_field_sensor_width"></a>

#### depth_of_field_sensor_width

```python
@property
def depth_of_field_sensor_width() -> float
```

(float):  [Read-Write] Width of the camera sensor to assume, in mm.

<a id="unreal.PostProcessSettings.depth_of_field_sensor_width"></a>

#### depth_of_field_sensor_width

```python
@depth_of_field_sensor_width.setter
def depth_of_field_sensor_width(value: float) -> None
```

<a id="unreal.PostProcessSettings.depth_of_field_squeeze_factor"></a>

#### depth_of_field_squeeze_factor

```python
@property
def depth_of_field_squeeze_factor() -> float
```

(float):  [Read-Write] This is the squeeze factor for the DOF, which emulates the properties of anamorphic lenses.

<a id="unreal.PostProcessSettings.depth_of_field_squeeze_factor"></a>

#### depth_of_field_squeeze_factor

```python
@depth_of_field_squeeze_factor.setter
def depth_of_field_squeeze_factor(value: float) -> None
```

<a id="unreal.PostProcessSettings.depth_of_field_focal_distance"></a>

#### depth_of_field_focal_distance

```python
@property
def depth_of_field_focal_distance() -> float
```

(float):  [Read-Write] Distance in which the Depth of Field effect should be sharp, in unreal units (cm)

<a id="unreal.PostProcessSettings.depth_of_field_focal_distance"></a>

#### depth_of_field_focal_distance

```python
@depth_of_field_focal_distance.setter
def depth_of_field_focal_distance(value: float) -> None
```

<a id="unreal.PostProcessSettings.depth_of_field_depth_blur_amount"></a>

#### depth_of_field_depth_blur_amount

```python
@property
def depth_of_field_depth_blur_amount() -> float
```

(float):  [Read-Write] CircleDOF only: Depth blur km for 50%

<a id="unreal.PostProcessSettings.depth_of_field_depth_blur_amount"></a>

#### depth_of_field_depth_blur_amount

```python
@depth_of_field_depth_blur_amount.setter
def depth_of_field_depth_blur_amount(value: float) -> None
```

<a id="unreal.PostProcessSettings.depth_of_field_depth_blur_radius"></a>

#### depth_of_field_depth_blur_radius

```python
@property
def depth_of_field_depth_blur_radius() -> float
```

(float):  [Read-Write] CircleDOF only: Depth blur radius in pixels at 1920x

<a id="unreal.PostProcessSettings.depth_of_field_depth_blur_radius"></a>

#### depth_of_field_depth_blur_radius

```python
@depth_of_field_depth_blur_radius.setter
def depth_of_field_depth_blur_radius(value: float) -> None
```

<a id="unreal.PostProcessSettings.depth_of_field_use_hair_depth"></a>

#### depth_of_field_use_hair_depth

```python
@property
def depth_of_field_use_hair_depth() -> bool
```

(bool):  [Read-Write] For depth of field to use the hair depth for computing circle of confusion size. Otherwise use an interpolated distance between the hair depth and the scene depth based on the hair coverage (default).

<a id="unreal.PostProcessSettings.depth_of_field_use_hair_depth"></a>

#### depth_of_field_use_hair_depth

```python
@depth_of_field_use_hair_depth.setter
def depth_of_field_use_hair_depth(value: bool) -> None
```

<a id="unreal.PostProcessSettings.depth_of_field_focal_region"></a>

#### depth_of_field_focal_region

```python
@property
def depth_of_field_focal_region() -> float
```

(float):  [Read-Write] Artificial region where all content is in focus, starting after DepthOfFieldFocalDistance, in unreal units  (cm)

<a id="unreal.PostProcessSettings.depth_of_field_focal_region"></a>

#### depth_of_field_focal_region

```python
@depth_of_field_focal_region.setter
def depth_of_field_focal_region(value: float) -> None
```

<a id="unreal.PostProcessSettings.depth_of_field_near_transition_region"></a>

#### depth_of_field_near_transition_region

```python
@property
def depth_of_field_near_transition_region() -> float
```

(float):  [Read-Write] To define the width of the transition region next to the focal region on the near side (cm)

<a id="unreal.PostProcessSettings.depth_of_field_near_transition_region"></a>

#### depth_of_field_near_transition_region

```python
@depth_of_field_near_transition_region.setter
def depth_of_field_near_transition_region(value: float) -> None
```

<a id="unreal.PostProcessSettings.depth_of_field_far_transition_region"></a>

#### depth_of_field_far_transition_region

```python
@property
def depth_of_field_far_transition_region() -> float
```

(float):  [Read-Write] To define the width of the transition region next to the focal region on the near side (cm)

<a id="unreal.PostProcessSettings.depth_of_field_far_transition_region"></a>

#### depth_of_field_far_transition_region

```python
@depth_of_field_far_transition_region.setter
def depth_of_field_far_transition_region(value: float) -> None
```

<a id="unreal.PostProcessSettings.depth_of_field_scale"></a>

#### depth_of_field_scale

```python
@property
def depth_of_field_scale() -> float
```

(float):  [Read-Write] SM5: BokehDOF only: To amplify the depth of field effect (like aperture)  0=off
          ES3_1: Used to blend DoF. 0=off

<a id="unreal.PostProcessSettings.depth_of_field_scale"></a>

#### depth_of_field_scale

```python
@depth_of_field_scale.setter
def depth_of_field_scale(value: float) -> None
```

<a id="unreal.PostProcessSettings.depth_of_field_near_blur_size"></a>

#### depth_of_field_near_blur_size

```python
@property
def depth_of_field_near_blur_size() -> float
```

(float):  [Read-Write] Gaussian only: Maximum size of the Depth of Field blur (in percent of the view width) (note: performance cost scales with size)

<a id="unreal.PostProcessSettings.depth_of_field_near_blur_size"></a>

#### depth_of_field_near_blur_size

```python
@depth_of_field_near_blur_size.setter
def depth_of_field_near_blur_size(value: float) -> None
```

<a id="unreal.PostProcessSettings.depth_of_field_far_blur_size"></a>

#### depth_of_field_far_blur_size

```python
@property
def depth_of_field_far_blur_size() -> float
```

(float):  [Read-Write] Gaussian only: Maximum size of the Depth of Field blur (in percent of the view width) (note: performance cost scales with size)

<a id="unreal.PostProcessSettings.depth_of_field_far_blur_size"></a>

#### depth_of_field_far_blur_size

```python
@depth_of_field_far_blur_size.setter
def depth_of_field_far_blur_size(value: float) -> None
```

<a id="unreal.PostProcessSettings.depth_of_field_occlusion"></a>

#### depth_of_field_occlusion

```python
@property
def depth_of_field_occlusion() -> float
```

(float):  [Read-Write] Occlusion tweak factor 1 (0.18 to get natural occlusion, 0.4 to solve layer color leaking issues)

<a id="unreal.PostProcessSettings.depth_of_field_occlusion"></a>

#### depth_of_field_occlusion

```python
@depth_of_field_occlusion.setter
def depth_of_field_occlusion(value: float) -> None
```

<a id="unreal.PostProcessSettings.depth_of_field_sky_focus_distance"></a>

#### depth_of_field_sky_focus_distance

```python
@property
def depth_of_field_sky_focus_distance() -> float
```

(float):  [Read-Write] Artificial distance to allow the skybox to be in focus (e.g. 200000), <=0 to switch the feature off, only for GaussianDOF, can cost performance

<a id="unreal.PostProcessSettings.depth_of_field_sky_focus_distance"></a>

#### depth_of_field_sky_focus_distance

```python
@depth_of_field_sky_focus_distance.setter
def depth_of_field_sky_focus_distance(value: float) -> None
```

<a id="unreal.PostProcessSettings.depth_of_field_vignette_size"></a>

#### depth_of_field_vignette_size

```python
@property
def depth_of_field_vignette_size() -> float
```

(float):  [Read-Write] Artificial circular mask to (near) blur content outside the radius, only for GaussianDOF, diameter in percent of screen width, costs performance if the mask is used, keep Feather can Radius on default to keep it off

<a id="unreal.PostProcessSettings.depth_of_field_vignette_size"></a>

#### depth_of_field_vignette_size

```python
@depth_of_field_vignette_size.setter
def depth_of_field_vignette_size(value: float) -> None
```

<a id="unreal.PostProcessSettings.motion_blur_amount"></a>

#### motion_blur_amount

```python
@property
def motion_blur_amount() -> float
```

(float):  [Read-Write] Strength of motion blur, 0:off

<a id="unreal.PostProcessSettings.motion_blur_amount"></a>

#### motion_blur_amount

```python
@motion_blur_amount.setter
def motion_blur_amount(value: float) -> None
```

<a id="unreal.PostProcessSettings.motion_blur_max"></a>

#### motion_blur_max

```python
@property
def motion_blur_max() -> float
```

(float):  [Read-Write] max distortion caused by motion blur, in percent of the screen width, 0:off

<a id="unreal.PostProcessSettings.motion_blur_max"></a>

#### motion_blur_max

```python
@motion_blur_max.setter
def motion_blur_max(value: float) -> None
```

<a id="unreal.PostProcessSettings.motion_blur_target_fps"></a>

#### motion_blur_target_fps

```python
@property
def motion_blur_target_fps() -> int
```

(int32):  [Read-Write] Defines the target FPS for motion blur. Makes motion blur independent of actual frame rate and relative
to the specified target FPS instead. Higher target FPS results in shorter frames, which means shorter
shutter times and less motion blur. Lower FPS means more motion blur. A value of zero makes the motion
blur dependent on the actual frame rate.

<a id="unreal.PostProcessSettings.motion_blur_target_fps"></a>

#### motion_blur_target_fps

```python
@motion_blur_target_fps.setter
def motion_blur_target_fps(value: int) -> None
```

<a id="unreal.PostProcessSettings.motion_blur_per_object_size"></a>

#### motion_blur_per_object_size

```python
@property
def motion_blur_per_object_size() -> float
```

(float):  [Read-Write] The minimum projected screen radius for a primitive to be drawn in the velocity pass, percentage of screen width. smaller numbers cause more draw calls, default: 4%

<a id="unreal.PostProcessSettings.motion_blur_per_object_size"></a>

#### motion_blur_per_object_size

```python
@motion_blur_per_object_size.setter
def motion_blur_per_object_size(value: float) -> None
```

<a id="unreal.PostProcessSettings.translucency_type"></a>

#### translucency_type

```python
@property
def translucency_type() -> TranslucencyType
```

(TranslucencyType):  [Read-Write] Sets the translucency type

<a id="unreal.PostProcessSettings.translucency_type"></a>

#### translucency_type

```python
@translucency_type.setter
def translucency_type(value: TranslucencyType) -> None
```

<a id="unreal.PostProcessSettings.ray_tracing_translucency_max_roughness"></a>

#### ray_tracing_translucency_max_roughness

```python
@property
def ray_tracing_translucency_max_roughness() -> float
```

(float):  [Read-Write] Sets the maximum roughness until which ray tracing translucency will be visible (lower value is faster). Translucency contribution is smoothly faded when close to roughness threshold. This parameter behaves similarly to ScreenSpaceReflectionMaxRoughness.

<a id="unreal.PostProcessSettings.ray_tracing_translucency_max_roughness"></a>

#### ray_tracing_translucency_max_roughness

```python
@ray_tracing_translucency_max_roughness.setter
def ray_tracing_translucency_max_roughness(value: float) -> None
```

<a id="unreal.PostProcessSettings.ray_tracing_translucency_refraction_rays"></a>

#### ray_tracing_translucency_refraction_rays

```python
@property
def ray_tracing_translucency_refraction_rays() -> int
```

(int32):  [Read-Write] Sets the maximum number of ray tracing refraction rays.

<a id="unreal.PostProcessSettings.ray_tracing_translucency_refraction_rays"></a>

#### ray_tracing_translucency_refraction_rays

```python
@ray_tracing_translucency_refraction_rays.setter
def ray_tracing_translucency_refraction_rays(value: int) -> None
```

<a id="unreal.PostProcessSettings.ray_tracing_translucency_samples_per_pixel"></a>

#### ray_tracing_translucency_samples_per_pixel

```python
@property
def ray_tracing_translucency_samples_per_pixel() -> int
```

(int32):  [Read-Write] Sets the samples per pixel for ray traced translucency.

<a id="unreal.PostProcessSettings.ray_tracing_translucency_samples_per_pixel"></a>

#### ray_tracing_translucency_samples_per_pixel

```python
@ray_tracing_translucency_samples_per_pixel.setter
def ray_tracing_translucency_samples_per_pixel(value: int) -> None
```

<a id="unreal.PostProcessSettings.ray_tracing_translucency_shadows"></a>

#### ray_tracing_translucency_shadows

```python
@property
def ray_tracing_translucency_shadows(
) -> ReflectedAndRefractedRayTracedShadows
```

(ReflectedAndRefractedRayTracedShadows):  [Read-Write] Sets the translucency shadows type.

<a id="unreal.PostProcessSettings.ray_tracing_translucency_shadows"></a>

#### ray_tracing_translucency_shadows

```python
@ray_tracing_translucency_shadows.setter
def ray_tracing_translucency_shadows(
        value: ReflectedAndRefractedRayTracedShadows) -> None
```

<a id="unreal.PostProcessSettings.ray_tracing_translucency_refraction"></a>

#### ray_tracing_translucency_refraction

```python
@property
def ray_tracing_translucency_refraction() -> bool
```

(bool):  [Read-Write] Sets whether refraction should be enabled or not (if not rays will not scatter and only travel in the same direction as before the intersection event).

<a id="unreal.PostProcessSettings.ray_tracing_translucency_refraction"></a>

#### ray_tracing_translucency_refraction

```python
@ray_tracing_translucency_refraction.setter
def ray_tracing_translucency_refraction(value: bool) -> None
```

<a id="unreal.PostProcessSettings.path_tracing_max_bounces"></a>

#### path_tracing_max_bounces

```python
@property
def path_tracing_max_bounces() -> int
```

(int32):  [Read-Write] Sets the path tracing maximum bounces

<a id="unreal.PostProcessSettings.path_tracing_max_bounces"></a>

#### path_tracing_max_bounces

```python
@path_tracing_max_bounces.setter
def path_tracing_max_bounces(value: int) -> None
```

<a id="unreal.PostProcessSettings.path_tracing_samples_per_pixel"></a>

#### path_tracing_samples_per_pixel

```python
@property
def path_tracing_samples_per_pixel() -> int
```

(int32):  [Read-Write] Sets the samples per pixel for the path tracer.

<a id="unreal.PostProcessSettings.path_tracing_samples_per_pixel"></a>

#### path_tracing_samples_per_pixel

```python
@path_tracing_samples_per_pixel.setter
def path_tracing_samples_per_pixel(value: int) -> None
```

<a id="unreal.PostProcessSettings.path_tracing_max_path_intensity"></a>

#### path_tracing_max_path_intensity

```python
@property
def path_tracing_max_path_intensity() -> float
```

(float):  [Read-Write] Sets the maximum intensity of indirect samples to reduce fireflies. Lowering this value reduces noise at the expense of accuracy. Increasing it is more accurate but may lead to more noise.

<a id="unreal.PostProcessSettings.path_tracing_max_path_intensity"></a>

#### path_tracing_max_path_intensity

```python
@path_tracing_max_path_intensity.setter
def path_tracing_max_path_intensity(value: float) -> None
```

<a id="unreal.PostProcessSettings.path_tracing_enable_emissive_materials"></a>

#### path_tracing_enable_emissive_materials

```python
@property
def path_tracing_enable_emissive_materials() -> bool
```

(bool):  [Read-Write] Should emissive materials contribute to scene lighting?

<a id="unreal.PostProcessSettings.path_tracing_enable_emissive_materials"></a>

#### path_tracing_enable_emissive_materials

```python
@path_tracing_enable_emissive_materials.setter
def path_tracing_enable_emissive_materials(value: bool) -> None
```

<a id="unreal.PostProcessSettings.path_tracing_enable_reference_dof"></a>

#### path_tracing_enable_reference_dof

```python
@property
def path_tracing_enable_reference_dof() -> bool
```

(bool):  [Read-Write] Enables a reference quality depth-of-field which replaces the post-process effect.

<a id="unreal.PostProcessSettings.path_tracing_enable_reference_dof"></a>

#### path_tracing_enable_reference_dof

```python
@path_tracing_enable_reference_dof.setter
def path_tracing_enable_reference_dof(value: bool) -> None
```

<a id="unreal.PostProcessSettings.path_tracing_enable_reference_atmosphere"></a>

#### path_tracing_enable_reference_atmosphere

```python
@property
def path_tracing_enable_reference_atmosphere() -> bool
```

(bool):  [Read-Write] Enables path tracing in the atmosphere instead of baking the sky atmosphere contribution into a skylight. Any skylight present in the scene will be automatically ignored when this is enabled.

<a id="unreal.PostProcessSettings.path_tracing_enable_reference_atmosphere"></a>

#### path_tracing_enable_reference_atmosphere

```python
@path_tracing_enable_reference_atmosphere.setter
def path_tracing_enable_reference_atmosphere(value: bool) -> None
```

<a id="unreal.PostProcessSettings.path_tracing_enable_denoiser"></a>

#### path_tracing_enable_denoiser

```python
@property
def path_tracing_enable_denoiser() -> bool
```

(bool):  [Read-Write] Run the currently loaded denoiser plugin on the last sample to remove noise from the output. Has no effect if a plug-in is not loaded.

<a id="unreal.PostProcessSettings.path_tracing_enable_denoiser"></a>

#### path_tracing_enable_denoiser

```python
@path_tracing_enable_denoiser.setter
def path_tracing_enable_denoiser(value: bool) -> None
```

<a id="unreal.PostProcessSettings.path_tracing_include_emissive"></a>

#### path_tracing_include_emissive

```python
@property
def path_tracing_include_emissive() -> bool
```

(bool):  [Read-Write] Should the render include directly visible emissive elements?

<a id="unreal.PostProcessSettings.path_tracing_include_emissive"></a>

#### path_tracing_include_emissive

```python
@path_tracing_include_emissive.setter
def path_tracing_include_emissive(value: bool) -> None
```

<a id="unreal.PostProcessSettings.path_tracing_include_diffuse"></a>

#### path_tracing_include_diffuse

```python
@property
def path_tracing_include_diffuse() -> bool
```

(bool):  [Read-Write] Should the render include diffuse lighting contributions?

<a id="unreal.PostProcessSettings.path_tracing_include_diffuse"></a>

#### path_tracing_include_diffuse

```python
@path_tracing_include_diffuse.setter
def path_tracing_include_diffuse(value: bool) -> None
```

<a id="unreal.PostProcessSettings.path_tracing_include_indirect_diffuse"></a>

#### path_tracing_include_indirect_diffuse

```python
@property
def path_tracing_include_indirect_diffuse() -> bool
```

(bool):  [Read-Write] Should the render include indirect diffuse lighting contributions?

<a id="unreal.PostProcessSettings.path_tracing_include_indirect_diffuse"></a>

#### path_tracing_include_indirect_diffuse

```python
@path_tracing_include_indirect_diffuse.setter
def path_tracing_include_indirect_diffuse(value: bool) -> None
```

<a id="unreal.PostProcessSettings.path_tracing_include_specular"></a>

#### path_tracing_include_specular

```python
@property
def path_tracing_include_specular() -> bool
```

(bool):  [Read-Write] Should the render include specular lighting contributions?

<a id="unreal.PostProcessSettings.path_tracing_include_specular"></a>

#### path_tracing_include_specular

```python
@path_tracing_include_specular.setter
def path_tracing_include_specular(value: bool) -> None
```

<a id="unreal.PostProcessSettings.path_tracing_include_indirect_specular"></a>

#### path_tracing_include_indirect_specular

```python
@property
def path_tracing_include_indirect_specular() -> bool
```

(bool):  [Read-Write] Should the render include indirect specular lighting contributions?

<a id="unreal.PostProcessSettings.path_tracing_include_indirect_specular"></a>

#### path_tracing_include_indirect_specular

```python
@path_tracing_include_indirect_specular.setter
def path_tracing_include_indirect_specular(value: bool) -> None
```

<a id="unreal.PostProcessSettings.path_tracing_include_volume"></a>

#### path_tracing_include_volume

```python
@property
def path_tracing_include_volume() -> bool
```

(bool):  [Read-Write] Should the render include volume lighting contributions?

<a id="unreal.PostProcessSettings.path_tracing_include_volume"></a>

#### path_tracing_include_volume

```python
@path_tracing_include_volume.setter
def path_tracing_include_volume(value: bool) -> None
```

<a id="unreal.PostProcessSettings.path_tracing_include_indirect_volume"></a>

#### path_tracing_include_indirect_volume

```python
@property
def path_tracing_include_indirect_volume() -> bool
```

(bool):  [Read-Write] Should the render include volume lighting contributions?

<a id="unreal.PostProcessSettings.path_tracing_include_indirect_volume"></a>

#### path_tracing_include_indirect_volume

```python
@path_tracing_include_indirect_volume.setter
def path_tracing_include_indirect_volume(value: bool) -> None
```

<a id="unreal.PostProcessSettings.user_flags"></a>

#### user_flags

```python
@property
def user_flags() -> int
```

(int32):  [Read-Write] Per-view user flags accessible in materials via TestPostVolumeUserFlag node, allowing per-view overrides of material behavior.

<a id="unreal.PostProcessSettings.user_flags"></a>

#### user_flags

```python
@user_flags.setter
def user_flags(value: int) -> None
```

<a id="unreal.PostProcessSettings.weighted_blendables"></a>

#### weighted_blendables

```python
@property
def weighted_blendables() -> WeightedBlendables
```

(WeightedBlendables):  [Read-Write] Allows custom post process materials to be defined, using a MaterialInstance with the same Material as its parent to allow blending.
For materials this needs to be the "PostProcess" domain type. This can be used for any UObject object implementing the IBlendableInterface (e.g. could be used to fade weather settings).

<a id="unreal.PostProcessSettings.weighted_blendables"></a>

#### weighted_blendables

```python
@weighted_blendables.setter
def weighted_blendables(value: WeightedBlendables) -> None
```

<a id="unreal.WeightedBlendables"></a>