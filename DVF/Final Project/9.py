# blender export (blender version 2.5x and higher)
# created by voodoo camera tracker - www.digilab.uni-hannover.de
# Creation date: Thu Jun 20 23:21:30 2019
# USAGE: load this python script into Blender's text editor and execute the script with ALT-P
#        use the 'voodoo_render_cam' for rendering your scene
#        use the helper object 'voodoo_scene' to rotate, translate and scale the scene

import bpy
import mathutils
import string
import math
scene = bpy.context.scene
dummy = bpy.data.objects.new('voodoo_scene', None)
dummy.location = (0.0, 0.0, 0.0)
dummy.rotation_euler = ( -3.141593/2, 0.0, 0.0)
dummy.scale = (0.2, 0.2, 0.2)
scene.objects.link(dummy)
data = bpy.data.cameras.new('voodoo_render_cam')
data.lens_unit = 'DEGREES'
vcam = bpy.data.objects.new('voodoo_render_cam', data)
vcam.location = (0.0, 0.0, 0.0)
vcam.rotation_euler = (0.0, 0.0, 0.0)
vcam.scale = (1.0, 1.0, 1.0)
data.lens = 35.0
data.shift_x = 0.0
data.shift_y = 0.0
data.dof_distance = 0.0
data.clip_start = 0.1
data.clip_end = 1000.0
data.draw_size = 0.5
scene.objects.link(vcam)
vcam.parent = dummy
data = bpy.data.meshes.new('voodoo_FP3D_cloud')
mesh = bpy.data.objects.new('voodoo_FP3D_cloud', data)
mesh.location = (0.0, 0.0, 0.0)
mesh.rotation_euler = (0.0, 0.0, 0.0)
mesh.scale = (1.0, 1.0, 1.0)
scene.objects.link(mesh)
mesh.parent = dummy

#Camera Parameters
scene.frame_current = 1
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.941056,-0.064656,-0.332015,0.000000], [-0.038633,-0.995683,0.084395,0.000000], [-0.336038,-0.066594,-0.939491,0.000000], [51.546830,14.222407,96.396637,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 2
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.941320,-0.064775,-0.331242,0.000000], [-0.038797,-0.995672,0.084453,0.000000], [-0.335278,-0.066646,-0.939759,0.000000], [51.561495,14.138836,96.365549,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 3
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.941440,-0.065255,-0.330806,0.000000], [-0.039122,-0.995608,0.085057,0.000000], [-0.334904,-0.067134,-0.939858,0.000000], [51.533564,14.052351,96.346892,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 4
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.941870,-0.064065,-0.329814,0.000000], [-0.038417,-0.995749,0.083712,0.000000], [-0.333775,-0.066175,-0.940327,0.000000], [51.598944,14.092779,96.270142,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 5
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.942187,-0.064118,-0.328897,0.000000], [-0.038686,-0.995773,0.083304,0.000000], [-0.332848,-0.065764,-0.940684,0.000000], [51.644511,14.088378,96.234544,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 6
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.942477,-0.063644,-0.328156,0.000000], [-0.038189,-0.995780,0.083447,0.000000], [-0.332082,-0.066115,-0.940931,0.000000], [51.685535,14.010519,96.216952,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 7
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.942695,-0.063333,-0.327591,0.000000], [-0.037579,-0.995726,0.084364,0.000000], [-0.331534,-0.067219,-0.941046,0.000000], [51.694671,13.872984,96.206584,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 8
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.942933,-0.064238,-0.326728,0.000000], [-0.038152,-0.995596,0.085637,0.000000], [-0.330790,-0.068284,-0.941231,0.000000], [51.732492,13.741958,96.206849,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 9
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.943071,-0.064744,-0.326230,0.000000], [-0.038619,-0.995552,0.085938,0.000000], [-0.330343,-0.068447,-0.941376,0.000000], [51.751780,13.702652,96.215871,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 10
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.943152,-0.064569,-0.326029,0.000000], [-0.038301,-0.995527,0.086362,0.000000], [-0.330147,-0.068965,-0.941407,0.000000], [51.740332,13.644110,96.230283,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 11
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.943369,-0.064668,-0.325383,0.000000], [-0.037907,-0.995405,0.087929,0.000000], [-0.329574,-0.070615,-0.941485,0.000000], [51.771932,13.472638,96.253044,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 12
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.943523,-0.064764,-0.324916,0.000000], [-0.037744,-0.995335,0.088792,0.000000], [-0.329150,-0.071514,-0.941566,0.000000], [51.795510,13.360382,96.275546,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 13
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.943741,-0.064718,-0.324289,0.000000], [-0.037279,-0.995232,0.090129,0.000000], [-0.328576,-0.072970,-0.941654,0.000000], [51.833146,13.196669,96.280759,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 14
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.943879,-0.064885,-0.323854,0.000000], [-0.037266,-0.995174,0.090773,0.000000], [-0.328181,-0.073610,-0.941742,0.000000], [51.857664,13.106092,96.305191,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 15
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.943995,-0.065136,-0.323466,0.000000], [-0.037454,-0.995138,0.091086,0.000000], [-0.327827,-0.073870,-0.941845,0.000000], [51.874219,13.054465,96.317085,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 16
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.944128,-0.065085,-0.323088,0.000000], [-0.037493,-0.995153,0.090909,0.000000], [-0.327439,-0.073716,-0.941992,0.000000], [51.877154,13.062247,96.312966,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 17
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.944282,-0.064693,-0.322718,0.000000], [-0.037406,-0.995234,0.090057,0.000000], [-0.327006,-0.072967,-0.942201,0.000000], [51.892551,13.131404,96.302009,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 18
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.944216,-0.064174,-0.323015,0.000000], [-0.037234,-0.995344,0.088907,0.000000], [-0.327216,-0.071920,-0.942209,0.000000], [51.841880,13.225194,96.338308,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 19
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.944139,-0.063969,-0.323279,0.000000], [-0.037685,-0.995502,0.086925,0.000000], [-0.327385,-0.069886,-0.942303,0.000000], [51.790297,13.435243,96.334048,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 20
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.944107,-0.063721,-0.323421,0.000000], [-0.037850,-0.995605,0.085666,0.000000], [-0.327458,-0.068636,-0.942369,0.000000], [51.750583,13.590988,96.337908,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 21
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.944097,-0.063692,-0.323457,0.000000], [-0.037892,-0.995622,0.085449,0.000000], [-0.327483,-0.068415,-0.942377,0.000000], [51.716789,13.657874,96.358613,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 22
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.944216,-0.063662,-0.323115,0.000000], [-0.037598,-0.995561,0.086279,0.000000], [-0.327174,-0.069317,-0.942418,0.000000], [51.721137,13.604367,96.383093,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 23
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.944381,-0.063165,-0.322729,0.000000], [-0.036960,-0.995549,0.086697,0.000000], [-0.326768,-0.069947,-0.942512,0.000000], [51.734091,13.557466,96.391273,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 24
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.944501,-0.062958,-0.322418,0.000000], [-0.036565,-0.995513,0.087278,0.000000], [-0.326466,-0.070645,-0.942565,0.000000], [51.741276,13.485825,96.398698,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 25
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.944665,-0.062830,-0.321964,0.000000], [-0.036266,-0.995473,0.087855,0.000000], [-0.326026,-0.071317,-0.942667,0.000000], [51.761137,13.411693,96.390853,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 26
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.944632,-0.063280,-0.321972,0.000000], [-0.036470,-0.995396,0.088634,0.000000], [-0.326099,-0.071984,-0.942591,0.000000], [51.751844,13.333129,96.416754,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 27
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.944851,-0.064004,-0.321185,0.000000], [-0.036700,-0.995233,0.090362,0.000000], [-0.325438,-0.073591,-0.942695,0.000000], [51.800820,13.156926,96.358936,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 28
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.944649,-0.065539,-0.321470,0.000000], [-0.037675,-0.995032,0.092152,0.000000], [-0.325913,-0.074940,-0.942425,0.000000], [51.709101,13.037505,96.173034,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 29
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.943916,-0.066917,-0.323335,0.000000], [-0.038441,-0.994860,0.093675,0.000000], [-0.327941,-0.075992,-0.941637,0.000000], [51.492587,12.890963,96.115816,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 30
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.943481,-0.067125,-0.324558,0.000000], [-0.037829,-0.994686,0.095753,0.000000], [-0.329261,-0.078063,-0.941007,0.000000], [51.426465,12.636883,96.187918,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 31
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.943049,-0.065567,-0.326129,0.000000], [-0.035296,-0.994571,0.097891,0.000000], [-0.330777,-0.080805,-0.940243,0.000000], [51.327168,12.322332,96.299123,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 32
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.943151,-0.062053,-0.326520,0.000000], [-0.030721,-0.994487,0.100260,0.000000], [-0.330941,-0.084529,-0.939858,0.000000], [51.321031,11.914510,96.372846,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 33
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.943508,-0.058027,-0.326229,0.000000], [-0.025429,-0.994323,0.103319,0.000000], [-0.330373,-0.089187,-0.939627,0.000000], [51.377735,11.406361,96.414792,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 34
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.944170,-0.054188,-0.324973,0.000000], [-0.021149,-0.994315,0.104354,0.000000], [-0.328780,-0.091655,-0.939948,0.000000], [51.506466,11.101235,96.371459,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 35
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.945126,-0.054245,-0.322171,0.000000], [-0.020902,-0.994139,0.106069,0.000000], [-0.326037,-0.093514,-0.940720,0.000000], [51.745883,10.871266,96.233043,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 36
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.946051,-0.057209,-0.318926,0.000000], [-0.024192,-0.994014,0.106545,0.000000], [-0.323113,-0.093081,-0.941772,0.000000], [51.953981,10.871007,96.018143,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 37
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.946823,-0.059266,-0.316249,0.000000], [-0.027798,-0.994282,0.103109,0.000000], [-0.320552,-0.088835,-0.943056,0.000000], [52.124679,11.236030,95.735115,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 38
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.947847,-0.060594,-0.312913,0.000000], [-0.030546,-0.994513,0.100055,0.000000], [-0.317258,-0.085279,-0.944497,0.000000], [52.362368,11.685775,95.444955,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 39
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.948041,-0.063113,-0.311825,0.000000], [-0.033559,-0.994496,0.099257,0.000000], [-0.316373,-0.083635,-0.944941,0.000000], [52.402597,11.953009,95.373468,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 40
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.948294,-0.062617,-0.311154,0.000000], [-0.034284,-0.994819,0.095710,0.000000], [-0.315535,-0.080093,-0.945528,0.000000], [52.422293,12.418322,95.261435,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 41
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.948325,-0.062887,-0.311007,0.000000], [-0.035138,-0.994948,0.094037,0.000000], [-0.315350,-0.078250,-0.945744,0.000000], [52.385701,12.717274,95.224481,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 42
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.947869,-0.066344,-0.311676,0.000000], [-0.038438,-0.994750,0.094845,0.000000], [-0.316332,-0.077920,-0.945443,0.000000], [52.262476,12.816406,95.338781,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 43
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.947183,-0.070823,-0.312775,0.000000], [-0.042469,-0.994421,0.096561,0.000000], [-0.317869,-0.078178,-0.944906,0.000000], [52.081565,12.788295,95.534172,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 44
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.946196,-0.074595,-0.314877,0.000000], [-0.045624,-0.994100,0.098407,0.000000], [-0.320360,-0.078746,-0.944017,0.000000], [51.946948,12.706850,96.045793,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 45
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.947098,-0.074107,-0.312270,0.000000], [-0.043951,-0.993758,0.102535,0.000000], [-0.317920,-0.083386,-0.944444,0.000000], [52.409730,12.313019,96.663145,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 46
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.947887,-0.070462,-0.310718,0.000000], [-0.039685,-0.993755,0.104291,0.000000], [-0.316126,-0.086526,-0.944763,0.000000], [53.153732,12.065290,97.627408,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 47
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.948572,-0.064703,-0.309880,0.000000], [-0.034546,-0.994201,0.101842,0.000000], [-0.314672,-0.085899,-0.945306,0.000000], [54.093560,12.184306,99.094555,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 48
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.950195,-0.060742,-0.305678,0.000000], [-0.030850,-0.994338,0.101690,0.000000], [-0.310124,-0.087195,-0.946689,0.000000], [55.115560,12.156991,100.332987,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 49
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.952308,-0.057362,-0.299699,0.000000], [-0.027793,-0.994395,0.102014,0.000000], [-0.303871,-0.088820,-0.948564,0.000000], [56.253078,12.136451,101.666374,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 50
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.953796,-0.054791,-0.295416,0.000000], [-0.026092,-0.994622,0.100230,0.000000], [-0.299319,-0.087891,-0.950096,0.000000], [56.916955,12.309884,102.272220,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 51
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.954436,-0.055723,-0.293168,0.000000], [-0.027060,-0.994525,0.100933,0.000000], [-0.297188,-0.088400,-0.950718,0.000000], [57.407607,12.427802,103.109331,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 52
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.954132,-0.057255,-0.293859,0.000000], [-0.026965,-0.993988,0.106115,0.000000], [-0.298168,-0.093324,-0.949940,0.000000], [57.413633,12.101716,103.386502,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 53
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.953631,-0.059571,-0.295023,0.000000], [-0.028113,-0.993562,0.109745,0.000000], [-0.299662,-0.096362,-0.949167,0.000000], [57.361488,11.861017,103.567863,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 54
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.952885,-0.063542,-0.296603,0.000000], [-0.030770,-0.993018,0.113883,0.000000], [-0.301768,-0.099391,-0.948187,0.000000], [57.255375,11.571900,103.830067,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 55
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.951671,-0.065436,-0.300067,0.000000], [-0.030367,-0.992299,0.120083,0.000000], [-0.305614,-0.105167,-0.946330,0.000000], [56.993172,10.980045,104.264430,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 56
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.952127,-0.060926,-0.299571,0.000000], [-0.024965,-0.992162,0.122437,0.000000], [-0.304683,-0.109096,-0.946185,0.000000], [57.100544,10.439120,104.326818,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 57
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.953428,-0.058805,-0.295833,0.000000], [-0.022173,-0.991822,0.125690,0.000000], [-0.300805,-0.113277,-0.946935,0.000000], [57.436814,9.977863,104.221955,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 58
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.953946,-0.061347,-0.293638,0.000000], [-0.024274,-0.991442,0.128273,0.000000], [-0.298994,-0.115237,-0.947271,0.000000], [57.607471,9.701514,104.236580,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 59
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.954027,-0.067156,-0.292102,0.000000], [-0.029272,-0.990793,0.132183,0.000000], [-0.298289,-0.117556,-0.947209,0.000000], [57.700512,9.248775,104.391607,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 60
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.954281,-0.069700,-0.290673,0.000000], [-0.033138,-0.991108,0.128866,0.000000], [-0.297070,-0.113342,-0.948105,0.000000], [57.763950,9.376989,104.242846,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 61
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.954649,-0.065684,-0.290397,0.000000], [-0.030594,-0.991839,0.123768,0.000000], [-0.296157,-0.109271,-0.948868,0.000000], [57.795304,9.726984,103.980511,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 62
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.955196,-0.062740,-0.289249,0.000000], [-0.027448,-0.991841,0.124493,0.000000], [-0.294699,-0.110976,-0.949124,0.000000], [57.933511,9.661047,103.809904,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 63
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.956141,-0.061721,-0.286330,0.000000], [-0.027886,-0.992288,0.120776,0.000000], [-0.291576,-0.107494,-0.950488,0.000000], [58.220445,10.203032,103.448812,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 64
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.956236,-0.059956,-0.286389,0.000000], [-0.025129,-0.991992,0.123772,0.000000], [-0.291516,-0.111159,-0.950085,0.000000], [58.252995,10.307170,103.405258,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 65
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.956525,-0.060708,-0.285263,0.000000], [-0.024660,-0.991429,0.128299,0.000000], [-0.290606,-0.115686,-0.949823,0.000000], [58.339984,10.205814,103.425715,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 66
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.957271,-0.059738,-0.282957,0.000000], [-0.023823,-0.991397,0.128706,0.000000], [-0.288211,-0.116466,-0.950458,0.000000], [58.524725,10.347996,103.294090,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 67
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.957223,-0.062428,-0.282538,0.000000], [-0.026660,-0.991324,0.128712,0.000000], [-0.288122,-0.115673,-0.950582,0.000000], [58.602753,10.612835,103.552203,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 68
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.960491,-0.063485,-0.270973,0.000000], [-0.029943,-0.991556,0.126172,0.000000], [-0.276695,-0.113073,-0.954282,0.000000], [60.795374,11.437047,107.557454,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 69
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.961539,-0.058390,-0.268391,0.000000], [-0.053753,-0.998251,0.024599,0.000000], [-0.269358,-0.009227,-0.962996,0.000000], [63.375117,19.851807,114.229143,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 70
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.966147,-0.054633,-0.252140,0.000000], [-0.047176,-0.998255,0.035529,0.000000], [-0.253641,-0.022431,-0.967038,0.000000], [67.411141,19.106967,124.812380,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 71
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.959366,-0.055788,-0.276593,0.000000], [-0.031177,-0.995216,0.092595,0.000000], [-0.280436,-0.080209,-0.956516,0.000000], [67.016133,15.830133,129.599224,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 72
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.964799,-0.058884,-0.256310,0.000000], [-0.040461,-0.996243,0.076571,0.000000], [-0.259856,-0.063506,-0.963557,0.000000], [69.118621,16.629084,132.666724,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 73
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.966152,-0.061590,-0.250512,0.000000], [-0.040383,-0.995219,0.088934,0.000000], [-0.254792,-0.075808,-0.964020,0.000000], [70.883339,15.920968,137.704896,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 74
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.972066,-0.062071,-0.226352,0.000000], [-0.038052,-0.993316,0.108976,0.000000], [-0.231603,-0.097318,-0.967930,0.000000], [72.683818,14.635508,139.829761,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 75
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.980854,-0.059909,-0.185303,0.000000], [-0.041517,-0.993959,0.101595,0.000000], [-0.190270,-0.091956,-0.977416,0.000000], [74.979432,14.689286,140.842631,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 76
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.982186,-0.059930,-0.178097,0.000000], [-0.042243,-0.993939,0.101496,0.000000], [-0.183100,-0.092164,-0.978765,0.000000], [75.559576,14.712174,141.950483,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 77
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.982235,-0.059435,-0.177995,0.000000], [-0.041919,-0.994044,0.100598,0.000000], [-0.182914,-0.091349,-0.978876,0.000000], [75.557493,14.723724,142.048912,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 78
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.982284,-0.056196,-0.178775,0.000000], [-0.038710,-0.994250,0.099839,0.000000], [-0.183358,-0.091150,-0.978811,0.000000], [75.519927,14.726442,142.078177,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 79
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.983269,-0.049198,-0.175390,0.000000], [-0.032451,-0.994745,0.097106,0.000000], [-0.179246,-0.089789,-0.979698,0.000000], [75.674564,14.820907,141.978157,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 80
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.986240,-0.043402,-0.159521,0.000000], [-0.028282,-0.994993,0.095863,0.000000], [-0.162882,-0.090033,-0.982529,0.000000], [76.023688,14.983867,141.813502,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 81
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987105,-0.047703,-0.152801,0.000000], [-0.032635,-0.994488,0.099644,0.000000], [-0.156712,-0.093373,-0.983221,0.000000], [76.019677,14.930795,141.842718,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 82
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987240,-0.054030,-0.149793,0.000000], [-0.038768,-0.993926,0.102999,0.000000], [-0.154448,-0.095878,-0.983338,0.000000], [75.951594,14.839233,141.893997,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 83
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.986871,-0.065873,-0.147469,0.000000], [-0.050560,-0.993156,0.105287,0.000000], [-0.153396,-0.096448,-0.983447,0.000000], [75.925165,14.789107,141.915288,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 84
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.985495,-0.086627,-0.145930,0.000000], [-0.072208,-0.992225,0.101371,0.000000], [-0.153577,-0.089364,-0.984088,0.000000], [76.047246,15.178050,142.958880,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 85
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.993036,-0.090820,-0.075039,0.000000], [-0.088909,-0.995634,0.028428,0.000000], [-0.077293,-0.021559,-0.996775,0.000000], [80.084742,18.523830,145.152818,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 86
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.991650,-0.079082,-0.101867,0.000000], [-0.071580,-0.994587,0.075315,0.000000], [-0.107272,-0.067394,-0.991943,0.000000], [79.769446,17.163574,148.055690,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 87
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.992914,-0.072605,-0.094078,0.000000], [-0.065523,-0.994930,0.076292,0.000000], [-0.099140,-0.069587,-0.992637,0.000000], [80.279815,17.115280,149.193351,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 88
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.994505,-0.063665,-0.083110,0.000000], [-0.057233,-0.995340,0.077612,0.000000], [-0.087664,-0.072429,-0.993513,0.000000], [80.844918,17.065305,150.455466,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 89
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.995844,-0.054246,-0.073151,0.000000], [-0.048459,-0.995721,0.078685,0.000000], [-0.077107,-0.074813,-0.994212,0.000000], [81.315808,17.028800,151.435432,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 90
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.996163,-0.048891,-0.072586,0.000000], [-0.043067,-0.995885,0.079743,0.000000], [-0.076186,-0.076310,-0.994169,0.000000], [81.748993,16.993775,152.370168,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 91
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.996328,-0.048912,-0.070276,0.000000], [-0.043102,-0.995705,0.081936,0.000000], [-0.073982,-0.078606,-0.994157,0.000000], [82.073544,16.964576,153.066929,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 92
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.995885,-0.055863,-0.071358,0.000000], [-0.049952,-0.995372,0.082094,0.000000], [-0.075614,-0.078192,-0.994067,0.000000], [82.090465,16.965619,153.111048,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 93
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.995478,-0.061386,-0.072490,0.000000], [-0.055341,-0.995041,0.082649,0.000000], [-0.077204,-0.078263,-0.993939,0.000000], [82.095498,16.966611,153.112393,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 94
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.995137,-0.064583,-0.074378,0.000000], [-0.058150,-0.994629,0.085629,0.000000], [-0.079509,-0.080888,-0.993547,0.000000], [82.063554,16.953040,153.091625,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 95
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.994233,-0.062369,-0.087242,0.000000], [-0.053605,-0.993601,0.099419,0.000000], [-0.092884,-0.094169,-0.991214,0.000000], [82.046107,16.893228,153.157851,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 96
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.994138,-0.061181,-0.089140,0.000000], [-0.052203,-0.993639,0.099784,0.000000], [-0.094678,-0.094546,-0.991008,0.000000], [82.069745,16.924439,153.193151,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 97
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.993910,-0.062651,-0.090650,0.000000], [-0.053352,-0.993393,0.101605,0.000000], [-0.096417,-0.096150,-0.990686,0.000000], [82.055565,16.906405,153.198066,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 98
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.993757,-0.062041,-0.092722,0.000000], [-0.052283,-0.993182,0.104195,0.000000], [-0.098554,-0.098696,-0.990225,0.000000], [82.050629,16.888132,153.204390,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 99
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.993663,-0.061002,-0.094411,0.000000], [-0.050876,-0.993045,0.106175,0.000000], [-0.100232,-0.100699,-0.989855,0.000000], [82.050470,16.888737,153.209170,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 100
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.993512,-0.060698,-0.096176,0.000000], [-0.050232,-0.992909,0.107739,0.000000], [-0.102033,-0.102209,-0.989516,0.000000], [82.055614,16.888963,153.242895,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 101
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.993345,-0.059742,-0.098469,0.000000], [-0.048855,-0.992787,0.109486,0.000000], [-0.104299,-0.103947,-0.989099,0.000000], [82.025035,16.862986,153.252285,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 102
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.993210,-0.059946,-0.099702,0.000000], [-0.048838,-0.992692,0.110349,0.000000], [-0.105588,-0.104731,-0.988879,0.000000], [82.029246,16.865734,153.269058,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 103
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.993106,-0.060214,-0.100570,0.000000], [-0.048904,-0.992575,0.111367,0.000000], [-0.106529,-0.105681,-0.988677,0.000000], [82.030137,16.863424,153.269635,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 104
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.993061,-0.059606,-0.101371,0.000000], [-0.048102,-0.992502,0.112364,0.000000], [-0.107309,-0.106708,-0.988483,0.000000], [82.034333,16.862956,153.275060,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 105
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.992991,-0.059458,-0.102147,0.000000], [-0.047784,-0.992427,0.113157,0.000000], [-0.108102,-0.107483,-0.988312,0.000000], [82.037710,16.863799,153.285503,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 106
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.992912,-0.059502,-0.102885,0.000000], [-0.047640,-0.992322,0.114141,0.000000], [-0.108886,-0.108430,-0.988123,0.000000], [82.035857,16.862200,153.287334,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 107
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.992800,-0.060229,-0.103542,0.000000], [-0.048141,-0.992138,0.115518,0.000000], [-0.109685,-0.109701,-0.987894,0.000000], [82.026821,16.857068,153.277438,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 108
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.992743,-0.059287,-0.104621,0.000000], [-0.046989,-0.992098,0.116336,0.000000], [-0.110692,-0.110576,-0.987684,0.000000], [82.019191,16.852985,153.286122,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 109
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.992661,-0.059095,-0.105507,0.000000], [-0.046603,-0.992018,0.117169,0.000000], [-0.111589,-0.111392,-0.987492,0.000000], [82.013211,16.851936,153.278843,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 110
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.992577,-0.058945,-0.106375,0.000000], [-0.046285,-0.991959,0.117791,0.000000], [-0.112463,-0.111993,-0.987324,0.000000], [82.012591,16.855237,153.282092,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 111
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.992487,-0.059026,-0.107173,0.000000], [-0.046164,-0.991850,0.118757,0.000000], [-0.113309,-0.112918,-0.987122,0.000000], [82.016240,16.853395,153.285945,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 112
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.992421,-0.058448,-0.108096,0.000000], [-0.045417,-0.991817,0.119313,0.000000], [-0.114185,-0.113499,-0.986955,0.000000], [82.018966,16.855315,153.287056,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 113
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.992305,-0.058768,-0.108983,0.000000], [-0.045556,-0.991730,0.119988,0.000000], [-0.115133,-0.114100,-0.986775,0.000000], [82.018211,16.853835,153.286707,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 114
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.992198,-0.058734,-0.109974,0.000000], [-0.045297,-0.991628,0.120922,0.000000], [-0.116156,-0.114997,-0.986551,0.000000], [82.019183,16.850841,153.293486,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 115
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.992119,-0.058171,-0.110980,0.000000], [-0.044530,-0.991573,0.121659,0.000000], [-0.117122,-0.115758,-0.986348,0.000000], [82.022987,16.847747,153.299427,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 116
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.991984,-0.058125,-0.112203,0.000000], [-0.044250,-0.991491,0.122421,0.000000], [-0.118364,-0.116474,-0.986115,0.000000], [82.012296,16.850484,153.301481,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 117
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.991782,-0.059924,-0.113039,0.000000], [-0.045830,-0.991298,0.123403,0.000000], [-0.119450,-0.117209,-0.985897,0.000000], [82.011147,16.847824,153.316528,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 118
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.991208,-0.063554,-0.116048,0.000000], [-0.048803,-0.990855,0.125794,0.000000], [-0.122982,-0.119024,-0.985246,0.000000], [81.979106,16.841262,153.345143,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 119
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.989797,-0.065313,-0.126632,0.000000], [-0.048887,-0.990473,0.128740,0.000000], [-0.133834,-0.121236,-0.983560,0.000000], [81.978899,16.833496,153.451191,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 120
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.989026,-0.065893,-0.132231,0.000000], [-0.048683,-0.990396,0.129405,0.000000], [-0.139488,-0.121547,-0.982736,0.000000], [81.962827,16.820597,153.466111,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 121
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.988355,-0.066777,-0.136733,0.000000], [-0.048656,-0.990078,0.131823,0.000000], [-0.144179,-0.123635,-0.981798,0.000000], [81.989229,16.780617,153.483010,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 122
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987681,-0.066739,-0.141534,0.000000], [-0.047764,-0.989901,0.133468,0.000000], [-0.149012,-0.125064,-0.980895,0.000000], [82.011524,16.761579,153.500798,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 123
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.988896,-0.065516,-0.133388,0.000000], [-0.047790,-0.990097,0.132001,0.000000], [-0.140715,-0.124161,-0.982234,0.000000], [82.477362,16.789768,153.333942,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 124
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.988871,-0.065118,-0.133765,0.000000], [-0.047452,-0.990213,0.131251,0.000000], [-0.141002,-0.123443,-0.982283,0.000000], [82.693534,16.823881,153.272613,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 125
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.988548,-0.065018,-0.136180,0.000000], [-0.046611,-0.989852,0.134243,0.000000], [-0.143526,-0.126358,-0.981547,0.000000], [82.808259,16.713372,153.023529,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 126
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987750,-0.066630,-0.141101,0.000000], [-0.048108,-0.990236,0.130835,0.000000], [-0.148441,-0.122445,-0.981312,0.000000], [82.847629,16.837164,152.926136,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 127
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987340,-0.067388,-0.143594,0.000000], [-0.048254,-0.989968,0.132798,0.000000], [-0.151103,-0.124188,-0.980686,0.000000], [82.890372,16.775259,152.686704,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 128
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987154,-0.067199,-0.144953,0.000000], [-0.049067,-0.990914,0.125225,0.000000], [-0.152051,-0.116504,-0.981482,0.000000], [82.973080,17.019768,152.562323,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 129
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987369,-0.067442,-0.143368,0.000000], [-0.049095,-0.990576,0.127863,0.000000], [-0.150640,-0.119209,-0.981375,0.000000], [83.075094,16.924579,152.309135,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 130
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987626,-0.067433,-0.141587,0.000000], [-0.050543,-0.991527,0.119668,0.000000], [-0.148457,-0.111031,-0.982666,0.000000], [83.219403,17.192313,152.134121,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 131
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987524,-0.067173,-0.142426,0.000000], [-0.049695,-0.991173,0.122904,0.000000], [-0.149424,-0.114293,-0.982145,0.000000], [83.271415,17.113120,152.136854,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 132
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987416,-0.067852,-0.142846,0.000000], [-0.050987,-0.991634,0.118587,0.000000], [-0.149697,-0.109811,-0.982615,0.000000], [83.365102,17.299706,152.287199,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 133
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987561,-0.068774,-0.141399,0.000000], [-0.051217,-0.990928,0.124255,0.000000], [-0.148661,-0.115468,-0.982124,0.000000], [83.479468,17.157345,152.361968,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 134
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987412,-0.070669,-0.141502,0.000000], [-0.052651,-0.990471,0.127256,0.000000], [-0.149147,-0.118204,-0.981725,0.000000], [83.530807,17.099119,152.331224,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 135
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.986827,-0.072637,-0.144558,0.000000], [-0.054924,-0.990890,0.122965,0.000000], [-0.152173,-0.113405,-0.981826,0.000000], [83.498205,17.297417,152.284993,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 136
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.986824,-0.073560,-0.144107,0.000000], [-0.055869,-0.990810,0.123181,0.000000], [-0.151843,-0.113507,-0.981865,0.000000], [83.575154,17.368754,152.258213,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 137
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.986951,-0.073972,-0.143022,0.000000], [-0.056195,-0.990618,0.124571,0.000000], [-0.150895,-0.114909,-0.981849,0.000000], [83.675266,17.402259,152.230793,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 138
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.989077,-0.072373,-0.128411,0.000000], [-0.056999,-0.991184,0.119605,0.000000], [-0.135935,-0.110979,-0.984482,0.000000], [84.215428,17.606211,152.050535,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 139
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.988605,-0.073838,-0.131181,0.000000], [-0.057290,-0.990410,0.125725,0.000000], [-0.139206,-0.116776,-0.983354,0.000000], [84.165143,17.548249,152.027710,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 140
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.988196,-0.075782,-0.133135,0.000000], [-0.058240,-0.989665,0.131041,0.000000], [-0.141690,-0.121740,-0.982397,0.000000], [84.147091,17.545786,152.039249,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 141
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987842,-0.077349,-0.134852,0.000000], [-0.058903,-0.988986,0.135782,0.000000], [-0.143869,-0.126188,-0.981518,0.000000], [84.143771,17.546913,152.052972,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 142
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987428,-0.078989,-0.136919,0.000000], [-0.059526,-0.988242,0.140835,0.000000], [-0.146433,-0.130915,-0.980520,0.000000], [84.136646,17.538333,152.046646,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 143
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987062,-0.080131,-0.138879,0.000000], [-0.059632,-0.987493,0.145947,0.000000], [-0.148838,-0.135778,-0.979496,0.000000], [84.134441,17.542178,152.057541,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 144
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.986855,-0.080202,-0.140300,0.000000], [-0.059058,-0.987093,0.148861,0.000000], [-0.150428,-0.138618,-0.978855,0.000000], [84.151854,17.565144,152.084457,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 145
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.986620,-0.080529,-0.141757,0.000000], [-0.058924,-0.986852,0.150503,0.000000], [-0.152013,-0.140136,-0.978394,0.000000], [84.157539,17.576045,152.090372,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 146
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.986532,-0.079979,-0.142681,0.000000], [-0.058042,-0.986709,0.151776,0.000000], [-0.152924,-0.141451,-0.978062,0.000000], [84.169867,17.582324,152.085933,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 147
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.986650,-0.079346,-0.142216,0.000000], [-0.057307,-0.986584,0.152863,0.000000], [-0.152438,-0.142672,-0.977961,0.000000], [84.178191,17.585719,152.078118,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 148
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.986830,-0.079101,-0.141098,0.000000], [-0.057063,-0.986436,0.153909,0.000000], [-0.151359,-0.143830,-0.977959,0.000000], [84.184574,17.591090,152.072921,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 149
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987053,-0.078969,-0.139607,0.000000], [-0.056999,-0.986285,0.154897,0.000000], [-0.149925,-0.144934,-0.978017,0.000000], [84.193256,17.594582,152.071234,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 150
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987276,-0.079020,-0.137989,0.000000], [-0.057184,-0.986164,0.155595,0.000000], [-0.148375,-0.145724,-0.978136,0.000000], [84.197033,17.600273,152.068379,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 151
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987475,-0.078942,-0.136603,0.000000], [-0.057200,-0.986045,0.156343,0.000000], [-0.147039,-0.146571,-0.978211,0.000000], [84.197175,17.606409,152.061976,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 152
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987635,-0.078500,-0.135704,0.000000], [-0.056833,-0.986003,0.156743,0.000000], [-0.146109,-0.147092,-0.978272,0.000000], [84.196078,17.615098,152.062465,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 153
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987639,-0.078199,-0.135843,0.000000], [-0.056573,-0.986083,0.156334,0.000000], [-0.146178,-0.146717,-0.978318,0.000000], [84.193696,17.627372,152.074203,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 154
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987630,-0.076708,-0.136761,0.000000], [-0.055203,-0.986430,0.154626,0.000000], [-0.146767,-0.145163,-0.978462,0.000000], [84.195232,17.635224,152.084320,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 155
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987540,-0.076760,-0.137378,0.000000], [-0.055385,-0.986649,0.153153,0.000000], [-0.147300,-0.143636,-0.978607,0.000000], [84.198611,17.637398,152.093744,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 156
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987537,-0.076592,-0.137494,0.000000], [-0.055362,-0.986816,0.152082,0.000000], [-0.147329,-0.142575,-0.978758,0.000000], [84.200758,17.635471,152.089068,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 157
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987582,-0.076188,-0.137394,0.000000], [-0.055093,-0.986954,0.151281,0.000000], [-0.147127,-0.141833,-0.978896,0.000000], [84.197240,17.634509,152.086521,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 158
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987674,-0.075801,-0.136946,0.000000], [-0.054976,-0.987169,0.149915,0.000000], [-0.146553,-0.140538,-0.979169,0.000000], [84.196880,17.641055,152.090874,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 159
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987793,-0.075630,-0.136178,0.000000], [-0.055055,-0.987307,0.148975,0.000000], [-0.145716,-0.139659,-0.979419,0.000000], [84.191805,17.633554,152.083432,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 160
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.988044,-0.073893,-0.135308,0.000000], [-0.053580,-0.987528,0.148047,0.000000], [-0.144560,-0.139027,-0.979681,0.000000], [84.199944,17.637999,152.087488,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 161
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.988330,-0.072919,-0.133741,0.000000], [-0.053023,-0.987757,0.146715,0.000000], [-0.142802,-0.137911,-0.980096,0.000000], [84.190296,17.630541,152.089425,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 162
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.988413,-0.072105,-0.133569,0.000000], [-0.052249,-0.987813,0.146613,0.000000], [-0.142513,-0.137936,-0.980135,0.000000], [84.191907,17.625554,152.080511,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 163
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.988460,-0.071439,-0.133578,0.000000], [-0.051617,-0.987883,0.146368,0.000000], [-0.142416,-0.137784,-0.980170,0.000000], [84.190484,17.623281,152.069236,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 164
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.988426,-0.071207,-0.133951,0.000000], [-0.051388,-0.987950,0.145992,0.000000], [-0.142732,-0.137419,-0.980175,0.000000], [84.189413,17.619352,152.066867,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 165
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.988390,-0.070718,-0.134478,0.000000], [-0.050850,-0.988003,0.145820,0.000000], [-0.143176,-0.137289,-0.980129,0.000000], [84.187710,17.615272,152.066106,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 166
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.988336,-0.070441,-0.135020,0.000000], [-0.050714,-0.988227,0.144342,0.000000], [-0.143598,-0.135811,-0.980273,0.000000], [84.218686,17.691778,152.289047,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 167
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.988264,-0.070699,-0.135409,0.000000], [-0.050929,-0.988227,0.144268,0.000000], [-0.144015,-0.135678,-0.980230,0.000000], [84.231875,17.723534,152.397225,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 168
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.988171,-0.070489,-0.136195,0.000000], [-0.050885,-0.988500,0.142405,0.000000], [-0.144666,-0.133790,-0.980394,0.000000], [84.259976,17.805811,152.613052,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 169
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.988132,-0.070053,-0.136702,0.000000], [-0.050542,-0.988674,0.141311,0.000000], [-0.145053,-0.132725,-0.980481,0.000000], [84.279707,17.842559,152.721848,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 170
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.988117,-0.069420,-0.137132,0.000000], [-0.049998,-0.988843,0.140318,0.000000], [-0.145343,-0.131794,-0.980564,0.000000], [84.283792,17.845207,152.728322,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 171
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.988145,-0.069847,-0.136716,0.000000], [-0.050361,-0.988709,0.141129,0.000000], [-0.145029,-0.132571,-0.980506,0.000000], [84.262052,17.751865,152.463487,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 172
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.988184,-0.070204,-0.136252,0.000000], [-0.050795,-0.988701,0.141032,0.000000], [-0.144614,-0.132445,-0.980584,0.000000], [84.239868,17.702543,152.300559,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 173
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.988140,-0.071137,-0.136085,0.000000], [-0.051801,-0.988697,0.140693,0.000000], [-0.144555,-0.131975,-0.980656,0.000000], [84.240574,17.709321,152.302513,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 174
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.988097,-0.071583,-0.136162,0.000000], [-0.052392,-0.988815,0.139642,0.000000], [-0.144635,-0.130846,-0.980796,0.000000], [84.254394,17.737961,152.345870,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 175
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.988012,-0.071753,-0.136688,0.000000], [-0.053015,-0.989275,0.136105,0.000000], [-0.144988,-0.127227,-0.981220,0.000000], [84.270248,17.782385,152.419470,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 176
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.988064,-0.071601,-0.136394,0.000000], [-0.053683,-0.989955,0.130797,0.000000], [-0.144389,-0.121913,-0.981982,0.000000], [84.272125,17.772078,152.396032,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 177
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.988156,-0.070993,-0.136043,0.000000], [-0.053781,-0.990538,0.126263,0.000000], [-0.143720,-0.117451,-0.982624,0.000000], [84.274560,17.778913,152.399973,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 178
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.988027,-0.071034,-0.136954,0.000000], [-0.054366,-0.991062,0.121822,0.000000], [-0.144383,-0.112918,-0.983058,0.000000], [84.252206,17.788989,152.404135,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 179
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987887,-0.071946,-0.137491,0.000000], [-0.055984,-0.991596,0.116632,0.000000], [-0.144727,-0.107522,-0.983612,0.000000], [84.257695,17.791560,152.398744,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 180
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.988073,-0.071456,-0.136402,0.000000], [-0.055781,-0.991743,0.115471,0.000000], [-0.143527,-0.106486,-0.983901,0.000000], [84.305069,17.659653,152.379378,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 181
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.988202,-0.075202,-0.133424,0.000000], [-0.057158,-0.989296,0.134261,0.000000], [-0.142092,-0.125051,-0.981923,0.000000], [84.369948,16.975774,152.458101,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 182
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987740,-0.078839,-0.134736,0.000000], [-0.060851,-0.989278,0.132765,0.000000], [-0.143759,-0.122938,-0.981947,0.000000], [84.339492,16.947137,152.478896,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 183
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987472,-0.081287,-0.135248,0.000000], [-0.063722,-0.989532,0.129484,0.000000], [-0.144358,-0.119244,-0.982314,0.000000], [84.339935,16.946533,152.484170,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 184
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987326,-0.082460,-0.135601,0.000000], [-0.065301,-0.989820,0.126459,0.000000], [-0.144649,-0.116001,-0.982660,0.000000], [84.345896,16.933464,152.489578,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 185
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987270,-0.083229,-0.135542,0.000000], [-0.066554,-0.990145,0.123219,0.000000], [-0.144461,-0.112629,-0.983080,0.000000], [84.354029,16.930318,152.482957,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 186
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987289,-0.083580,-0.135183,0.000000], [-0.067036,-0.990187,0.122618,0.000000], [-0.144105,-0.111997,-0.983204,0.000000], [84.371153,16.890658,152.473686,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 187
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987096,-0.085218,-0.135571,0.000000], [-0.068641,-0.990083,0.122574,0.000000], [-0.144672,-0.111686,-0.983156,0.000000], [84.373208,16.872399,152.473408,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 188
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.986978,-0.086350,-0.135714,0.000000], [-0.069773,-0.990015,0.122482,0.000000], [-0.144935,-0.111418,-0.983148,0.000000], [84.383744,16.858586,152.468709,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 189
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987411,-0.085448,-0.133110,0.000000], [-0.069238,-0.990115,0.121979,0.000000], [-0.142217,-0.111227,-0.983566,0.000000], [84.465611,16.881224,152.420547,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 190
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987595,-0.086357,-0.131140,0.000000], [-0.069102,-0.988989,0.130864,0.000000], [-0.140997,-0.120179,-0.982689,0.000000], [84.470626,16.803011,152.395460,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 191
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987529,-0.086883,-0.131294,0.000000], [-0.069356,-0.988736,0.132627,0.000000], [-0.141338,-0.121867,-0.982432,0.000000], [84.473635,16.828141,152.398605,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 192
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987527,-0.086129,-0.131803,0.000000], [-0.068286,-0.988575,0.134376,0.000000], [-0.141871,-0.123700,-0.982126,0.000000], [84.453237,16.830151,152.419763,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 193
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987731,-0.085947,-0.130390,0.000000], [-0.068135,-0.988446,0.135397,0.000000], [-0.140520,-0.124852,-0.982174,0.000000], [84.470750,16.833333,152.411123,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 194
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987439,-0.085628,-0.132786,0.000000], [-0.067196,-0.988211,0.137562,0.000000], [-0.143000,-0.126912,-0.981552,0.000000], [84.382234,16.801799,152.471566,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 195
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987493,-0.085779,-0.132283,0.000000], [-0.067334,-0.988127,0.138097,0.000000], [-0.142558,-0.127462,-0.981545,0.000000], [84.382732,16.804841,152.472111,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 196
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987278,-0.087068,-0.133043,0.000000], [-0.068345,-0.987884,0.139336,0.000000], [-0.143562,-0.128471,-0.981267,0.000000], [84.345167,16.792143,152.488083,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 197
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987180,-0.088048,-0.133131,0.000000], [-0.069679,-0.988139,0.136843,0.000000], [-0.143600,-0.125812,-0.981606,0.000000], [84.348812,16.885027,152.474801,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 198
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987315,-0.087731,-0.132332,0.000000], [-0.069887,-0.988523,0.133936,0.000000], [-0.142564,-0.122989,-0.982115,0.000000], [84.377914,16.976398,152.462564,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 199
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987364,-0.087227,-0.132303,0.000000], [-0.069814,-0.988924,0.130982,0.000000], [-0.142263,-0.120090,-0.982517,0.000000], [84.351991,17.064638,152.468435,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 200
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987660,-0.084476,-0.131879,0.000000], [-0.067274,-0.989249,0.129847,0.000000], [-0.141431,-0.119373,-0.982725,0.000000], [84.320446,17.045432,152.472223,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 201
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987735,-0.082659,-0.132468,0.000000], [-0.065345,-0.989345,0.130104,0.000000], [-0.141811,-0.119852,-0.982611,0.000000], [84.279036,16.991371,152.483844,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 202
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987561,-0.081620,-0.134394,0.000000], [-0.064141,-0.989489,0.129609,0.000000], [-0.143560,-0.119376,-0.982415,0.000000], [84.213189,16.957757,152.502492,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 203
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987509,-0.080204,-0.135625,0.000000], [-0.062731,-0.989719,0.128531,0.000000], [-0.144539,-0.118417,-0.982388,0.000000], [84.184113,16.944153,152.501645,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 204
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987488,-0.079444,-0.136220,0.000000], [-0.061986,-0.989845,0.127928,0.000000], [-0.145000,-0.117884,-0.982384,0.000000], [84.185453,16.935453,152.501906,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 205
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987563,-0.079908,-0.135404,0.000000], [-0.062509,-0.989776,0.128205,0.000000], [-0.144265,-0.118146,-0.982461,0.000000], [84.226505,16.909028,152.494633,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 206
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987665,-0.080815,-0.134118,0.000000], [-0.063645,-0.989767,0.127711,0.000000], [-0.143066,-0.117600,-0.982702,0.000000], [84.300152,16.907723,152.485318,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 207
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987691,-0.081382,-0.133583,0.000000], [-0.064230,-0.989688,0.128034,0.000000], [-0.142625,-0.117878,-0.982732,0.000000], [84.324272,16.881741,152.486090,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 208
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987700,-0.081824,-0.133244,0.000000], [-0.064953,-0.989853,0.126382,0.000000], [-0.142233,-0.116173,-0.982992,0.000000], [84.333167,16.923918,152.478850,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 209
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987825,-0.081771,-0.132348,0.000000], [-0.065209,-0.990016,0.124968,0.000000], [-0.141245,-0.114816,-0.983294,0.000000], [84.351581,16.953604,152.469562,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 210
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987770,-0.082027,-0.132600,0.000000], [-0.065448,-0.990010,0.124887,0.000000], [-0.141519,-0.114681,-0.983270,0.000000], [84.328224,16.942185,152.480445,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 211
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.985461,-0.084323,-0.147499,0.000000], [-0.067711,-0.991143,0.114237,0.000000], [-0.155825,-0.102589,-0.982443,0.000000], [83.880105,17.268067,152.769692,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 212
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.986162,-0.084065,-0.142891,0.000000], [-0.068254,-0.991343,0.112166,0.000000], [-0.151084,-0.100860,-0.983362,0.000000], [83.904741,17.032674,152.741492,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 213
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.986909,-0.081311,-0.139278,0.000000], [-0.066462,-0.991911,0.108144,0.000000], [-0.146944,-0.097471,-0.984331,0.000000], [83.994431,16.987559,152.667958,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 214
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987503,-0.082029,-0.134566,0.000000], [-0.068267,-0.992244,0.103881,0.000000], [-0.142044,-0.093396,-0.985444,0.000000], [84.099374,17.053425,152.582422,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 215
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987582,-0.081759,-0.134154,0.000000], [-0.068018,-0.992249,0.103999,0.000000], [-0.141617,-0.093583,-0.985488,0.000000], [84.080921,16.995797,152.580871,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 216
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987565,-0.081741,-0.134292,0.000000], [-0.067744,-0.992089,0.105688,0.000000], [-0.141869,-0.095276,-0.985290,0.000000], [84.057335,16.903545,152.582334,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 217
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987467,-0.082442,-0.134581,0.000000], [-0.068142,-0.991855,0.107611,0.000000], [-0.142356,-0.097092,-0.985042,0.000000], [84.040362,16.823888,152.584875,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 218
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987985,-0.082381,-0.130763,0.000000], [-0.067849,-0.991396,0.111943,0.000000], [-0.138860,-0.101726,-0.985073,0.000000], [84.142559,16.697679,152.504328,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 219
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987879,-0.083707,-0.130720,0.000000], [-0.068522,-0.990808,0.116638,0.000000], [-0.139282,-0.106267,-0.984534,0.000000], [84.142442,16.778657,152.484502,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 220
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987659,-0.083883,-0.132263,0.000000], [-0.068140,-0.990509,0.119373,0.000000], [-0.141021,-0.108887,-0.984000,0.000000], [84.105677,16.844313,152.515306,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 221
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987751,-0.083519,-0.131802,0.000000], [-0.067483,-0.990262,0.121768,0.000000], [-0.140689,-0.111382,-0.983769,0.000000], [84.135421,16.860922,152.513907,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 222
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.988069,-0.082570,-0.130008,0.000000], [-0.066518,-0.990136,0.123309,0.000000], [-0.138907,-0.113190,-0.983815,0.000000], [84.204924,16.913989,152.450818,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 223
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987946,-0.080719,-0.132087,0.000000], [-0.064221,-0.990111,0.124722,0.000000], [-0.140849,-0.114736,-0.983360,0.000000], [84.159419,17.064242,152.450068,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 224
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.988060,-0.079038,-0.132250,0.000000], [-0.061912,-0.989717,0.128944,0.000000], [-0.141081,-0.119217,-0.982794,0.000000], [84.183691,17.120827,152.412396,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 225
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987585,-0.079876,-0.135258,0.000000], [-0.062576,-0.989843,0.127649,0.000000], [-0.144081,-0.117600,-0.982553,0.000000], [84.138762,17.328184,152.460340,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 226
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987486,-0.081378,-0.135088,0.000000], [-0.063494,-0.989242,0.131790,0.000000], [-0.144360,-0.121563,-0.982030,0.000000], [84.149203,17.281801,152.460778,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 227
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987384,-0.081907,-0.135516,0.000000], [-0.063857,-0.989116,0.132558,0.000000], [-0.144898,-0.122232,-0.981868,0.000000], [84.171602,17.323155,152.466157,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 228
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987388,-0.082548,-0.135098,0.000000], [-0.064314,-0.988869,0.134168,0.000000], [-0.144669,-0.123787,-0.981706,0.000000], [84.210123,17.333100,152.453855,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 229
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987518,-0.082854,-0.133953,0.000000], [-0.064491,-0.988601,0.136047,0.000000], [-0.143698,-0.125710,-0.981605,0.000000], [84.266933,17.350755,152.419635,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 230
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987446,-0.083095,-0.134334,0.000000], [-0.064118,-0.988089,0.139892,0.000000], [-0.144358,-0.129523,-0.981012,0.000000], [84.264941,17.343030,152.407383,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 231
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987864,-0.085065,-0.129954,0.000000], [-0.068446,-0.989487,0.127399,0.000000], [-0.139425,-0.116958,-0.983301,0.000000], [84.453079,17.987248,152.207359,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 232
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987667,-0.086239,-0.130679,0.000000], [-0.068340,-0.988382,0.135757,0.000000], [-0.140868,-0.125152,-0.982086,0.000000], [84.456452,17.995293,152.204846,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 233
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987598,-0.086862,-0.130788,0.000000], [-0.067707,-0.987203,0.144385,0.000000], [-0.141656,-0.133739,-0.980840,0.000000], [84.478302,17.992550,152.208554,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 234
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987441,-0.088386,-0.130949,0.000000], [-0.067993,-0.985923,0.152751,0.000000], [-0.142607,-0.141929,-0.979551,0.000000], [84.480067,18.002206,152.197483,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 235
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987301,-0.088851,-0.131689,0.000000], [-0.067321,-0.984857,0.159765,0.000000], [-0.143891,-0.148871,-0.978332,0.000000], [84.477680,18.004616,152.231240,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 236
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987214,-0.088904,-0.132306,0.000000], [-0.066665,-0.984217,0.163928,0.000000], [-0.144792,-0.153011,-0.977560,0.000000], [84.484623,18.005531,152.240220,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 237
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987204,-0.088071,-0.132935,0.000000], [-0.065557,-0.984091,0.165129,0.000000], [-0.145363,-0.154301,-0.977272,0.000000], [84.496085,18.032196,152.240468,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 238
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987180,-0.087118,-0.133738,0.000000], [-0.064251,-0.983918,0.166666,0.000000], [-0.146107,-0.155937,-0.976902,0.000000], [84.502478,18.035521,152.246240,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 239
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987169,-0.086188,-0.134424,0.000000], [-0.063080,-0.983841,0.167567,0.000000], [-0.146694,-0.156937,-0.976653,0.000000], [84.509758,18.048178,152.248225,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 240
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987175,-0.085575,-0.134770,0.000000], [-0.062205,-0.983659,0.168952,0.000000], [-0.147026,-0.158402,-0.976367,0.000000], [84.516385,18.048972,152.244654,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 241
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987065,-0.086436,-0.135023,0.000000], [-0.062764,-0.983329,0.170662,0.000000], [-0.147524,-0.159980,-0.976034,0.000000], [84.522705,18.049198,152.251121,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 242
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987013,-0.086673,-0.135249,0.000000], [-0.062798,-0.983138,0.171746,0.000000], [-0.147854,-0.161022,-0.975813,0.000000], [84.527263,18.050895,152.254728,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 243
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.986970,-0.086863,-0.135442,0.000000], [-0.062754,-0.982907,0.173080,0.000000], [-0.148161,-0.162325,-0.975551,0.000000], [84.529721,18.049340,152.251744,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 244
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.986937,-0.086633,-0.135829,0.000000], [-0.062311,-0.982762,0.174059,0.000000], [-0.148567,-0.163321,-0.975323,0.000000], [84.532286,18.054182,152.251932,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 245
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.986927,-0.086170,-0.136201,0.000000], [-0.061666,-0.982660,0.174860,0.000000], [-0.148907,-0.164175,-0.975127,0.000000], [84.538998,18.056862,152.259871,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 246
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.986885,-0.086070,-0.136565,0.000000], [-0.061384,-0.982536,0.175654,0.000000], [-0.149298,-0.164967,-0.974934,0.000000], [84.535945,18.060279,152.255900,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 247
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.986840,-0.086314,-0.136733,0.000000], [-0.061461,-0.982370,0.176553,0.000000], [-0.149562,-0.165826,-0.974748,0.000000], [84.534468,18.056127,152.254015,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 248
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.986754,-0.086876,-0.137003,0.000000], [-0.061938,-0.982299,0.176786,0.000000], [-0.149937,-0.165959,-0.974668,0.000000], [84.538231,18.061049,152.257606,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 249
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.986643,-0.087773,-0.137227,0.000000], [-0.062773,-0.982222,0.176915,0.000000], [-0.150316,-0.165937,-0.974613,0.000000], [84.545656,18.063205,152.267012,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 250
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.986546,-0.088414,-0.137517,0.000000], [-0.063448,-0.982278,0.176364,0.000000], [-0.150673,-0.165266,-0.974672,0.000000], [84.547206,18.067250,152.275667,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 251
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.986526,-0.088367,-0.137688,0.000000], [-0.063509,-0.982433,0.175475,0.000000], [-0.150776,-0.164366,-0.974808,0.000000], [84.551707,18.065066,152.277596,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 252
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.986460,-0.088743,-0.137918,0.000000], [-0.063938,-0.982513,0.174873,0.000000], [-0.151025,-0.163687,-0.974884,0.000000], [84.550517,18.064610,152.278505,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 253
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.986446,-0.088881,-0.137929,0.000000], [-0.064119,-0.982551,0.174590,0.000000], [-0.151040,-0.163380,-0.974933,0.000000], [84.551199,18.062270,152.276189,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 254
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.986346,-0.089579,-0.138195,0.000000], [-0.064797,-0.982539,0.174407,0.000000], [-0.151405,-0.163071,-0.974928,0.000000], [84.547777,18.063153,152.275060,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 255
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.986254,-0.090425,-0.138295,0.000000], [-0.065589,-0.982448,0.174627,0.000000], [-0.151659,-0.163156,-0.974874,0.000000], [84.548801,18.062572,152.277819,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 256
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.986213,-0.090553,-0.138505,0.000000], [-0.065664,-0.982422,0.174746,0.000000], [-0.151894,-0.163242,-0.974823,0.000000], [84.550682,18.062315,152.277492,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 257
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.986174,-0.090748,-0.138655,0.000000], [-0.065829,-0.982406,0.174772,0.000000], [-0.152076,-0.163228,-0.974797,0.000000], [84.551477,18.062259,152.277963,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 258
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.986094,-0.091347,-0.138833,0.000000], [-0.066437,-0.982411,0.174512,0.000000], [-0.152332,-0.162862,-0.974818,0.000000], [84.549860,18.065030,152.282084,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 259
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.985647,-0.092163,-0.141440,0.000000], [-0.066806,-0.982376,0.174570,0.000000], [-0.155036,-0.162616,-0.974433,0.000000], [84.440949,18.033115,152.108576,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 260
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.985586,-0.090975,-0.142635,0.000000], [-0.065592,-0.982645,0.173513,0.000000], [-0.155944,-0.161656,-0.974448,0.000000], [84.400426,18.024900,152.011899,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 261
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.986045,-0.089257,-0.140528,0.000000], [-0.064588,-0.983111,0.171234,0.000000], [-0.153439,-0.159768,-0.975157,0.000000], [84.514330,18.084215,152.162503,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 262
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.986246,-0.088493,-0.139597,0.000000], [-0.063884,-0.983051,0.171839,0.000000], [-0.152438,-0.160558,-0.975184,0.000000], [84.570909,18.068732,152.302510,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 263
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.986293,-0.088704,-0.139134,0.000000], [-0.064459,-0.983336,0.169984,0.000000], [-0.151894,-0.158685,-0.975575,0.000000], [84.614757,18.114857,152.360918,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 264
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.986166,-0.091675,-0.138103,0.000000], [-0.067972,-0.983525,0.167504,0.000000], [-0.151183,-0.155799,-0.976151,0.000000], [84.523994,18.075999,152.280844,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 265
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.986671,-0.091287,-0.134714,0.000000], [-0.068515,-0.983924,0.164919,0.000000], [-0.147604,-0.153491,-0.977064,0.000000], [84.475028,18.084210,152.099173,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 266
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.986604,-0.090408,-0.135790,0.000000], [-0.067030,-0.983537,0.167813,0.000000], [-0.148726,-0.156463,-0.976422,0.000000], [84.280145,17.992019,151.858309,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 267
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.986713,-0.089435,-0.135643,0.000000], [-0.066109,-0.983628,0.167646,0.000000], [-0.148416,-0.156451,-0.976471,0.000000], [84.144686,17.964614,151.613492,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 268
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.985991,-0.093951,-0.137820,0.000000], [-0.070031,-0.983098,0.169155,0.000000], [-0.151383,-0.157134,-0.975906,0.000000], [83.919588,17.868258,151.183908,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 269
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.985470,-0.096114,-0.140040,0.000000], [-0.071918,-0.983055,0.168615,0.000000], [-0.153874,-0.156094,-0.975683,0.000000], [83.722339,17.816594,150.788595,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 270
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.985902,-0.093389,-0.138834,0.000000], [-0.069607,-0.983457,0.167235,0.000000], [-0.152156,-0.155214,-0.976093,0.000000], [83.703247,17.824327,150.708144,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 271
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.986250,-0.091897,-0.137353,0.000000], [-0.068424,-0.983616,0.166788,0.000000], [-0.150429,-0.155096,-0.976379,0.000000], [83.698399,17.836838,150.706166,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 272
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.986303,-0.092042,-0.136872,0.000000], [-0.068503,-0.983453,0.167712,0.000000], [-0.150044,-0.156038,-0.976288,0.000000], [83.648969,17.809959,150.676700,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 273
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.985496,-0.094972,-0.140634,0.000000], [-0.070673,-0.983134,0.168678,0.000000], [-0.154281,-0.156292,-0.975587,0.000000], [83.377337,17.718729,150.176893,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 274
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.985769,-0.092770,-0.140189,0.000000], [-0.068587,-0.983324,0.168432,0.000000], [-0.153476,-0.156420,-0.975693,0.000000], [83.362347,17.714724,150.113793,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 275
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.985922,-0.089932,-0.140964,0.000000], [-0.065754,-0.983651,0.167650,0.000000], [-0.153736,-0.156021,-0.975716,0.000000], [83.346439,17.723709,150.116261,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 276
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.988002,-0.091917,-0.124113,0.000000], [-0.068229,-0.980711,0.183169,0.000000], [-0.138556,-0.172503,-0.975215,0.000000], [83.708764,17.002167,149.039952,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 277
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987484,-0.095995,-0.125143,0.000000], [-0.072710,-0.981177,0.178899,0.000000], [-0.139961,-0.167560,-0.975876,0.000000], [83.487796,16.951590,147.923950,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 278
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.986846,-0.098184,-0.128436,0.000000], [-0.073986,-0.980659,0.181199,0.000000], [-0.143743,-0.169313,-0.975024,0.000000], [83.196724,16.641537,146.911430,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 279
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.986841,-0.100970,-0.126291,0.000000], [-0.077826,-0.981243,0.176368,0.000000], [-0.141730,-0.164219,-0.976189,0.000000], [83.113303,16.569703,145.847710,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 280
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.986733,-0.100642,-0.127391,0.000000], [-0.077083,-0.981014,0.177958,0.000000], [-0.142882,-0.165777,-0.975757,0.000000], [82.928378,16.293557,145.025629,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 281
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.986237,-0.099723,-0.131880,0.000000], [-0.074805,-0.980455,0.181970,0.000000], [-0.147449,-0.169600,-0.974420,0.000000], [82.545593,15.950262,143.947260,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 282
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.986102,-0.099350,-0.133162,0.000000], [-0.074690,-0.981040,0.178836,0.000000], [-0.148404,-0.166404,-0.974826,0.000000], [82.256018,15.840585,142.467400,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 283
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.985868,-0.099395,-0.134850,0.000000], [-0.074528,-0.981146,0.178320,0.000000], [-0.150031,-0.165750,-0.974688,0.000000], [81.940535,15.610009,140.998131,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 284
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.986619,-0.098430,-0.129981,0.000000], [-0.074685,-0.981490,0.176353,0.000000], [-0.144933,-0.164285,-0.975707,0.000000], [81.954220,15.445708,139.620200,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 285
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987769,-0.096442,-0.122517,0.000000], [-0.074072,-0.981678,0.175559,0.000000], [-0.137204,-0.164336,-0.976816,0.000000], [82.162324,15.286522,138.605217,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 286
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.988288,-0.093965,-0.120242,0.000000], [-0.072143,-0.982018,0.174460,0.000000], [-0.134473,-0.163742,-0.977295,0.000000], [82.273338,15.292032,138.479472,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 287
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.989906,-0.089656,-0.109765,0.000000], [-0.067373,-0.979060,0.192098,0.000000], [-0.124689,-0.182764,-0.975218,0.000000], [82.597615,14.241017,137.540007,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 288
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.989230,-0.093608,-0.112524,0.000000], [-0.070311,-0.978160,0.195602,0.000000], [-0.128376,-0.185583,-0.974207,0.000000], [82.171880,13.774307,135.775964,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 289
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.989285,-0.092382,-0.113053,0.000000], [-0.069022,-0.978287,0.195424,0.000000], [-0.128652,-0.185527,-0.974181,0.000000], [82.032813,13.710954,135.342328,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 290
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.989444,-0.090160,-0.113453,0.000000], [-0.066821,-0.978548,0.194882,0.000000], [-0.128589,-0.185243,-0.974243,0.000000], [82.016948,13.722964,135.355825,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 291
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.989471,-0.089826,-0.113487,0.000000], [-0.066501,-0.978595,0.194756,0.000000], [-0.128552,-0.185159,-0.974264,0.000000], [82.001465,13.729380,135.353946,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 292
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.989389,-0.091256,-0.113057,0.000000], [-0.068023,-0.978530,0.194553,0.000000], [-0.128384,-0.184798,-0.974355,0.000000], [82.004630,13.736058,135.358615,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 293
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.989343,-0.094927,-0.110403,0.000000], [-0.072255,-0.978386,0.193752,0.000000], [-0.126409,-0.183710,-0.974819,0.000000], [82.006431,13.776427,135.363262,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 294
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.989547,-0.097618,-0.106145,0.000000], [-0.075886,-0.978391,0.192336,0.000000], [-0.122627,-0.182271,-0.975572,0.000000], [82.013050,13.788522,135.339411,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 295
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.989562,-0.099675,-0.104077,0.000000], [-0.078765,-0.978892,0.188592,0.000000], [-0.120678,-0.178426,-0.976525,0.000000], [82.022317,13.802908,135.317469,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 296
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.989590,-0.100822,-0.102694,0.000000], [-0.080688,-0.979575,0.184180,0.000000], [-0.119166,-0.173977,-0.977513,0.000000], [82.036698,13.793871,135.306260,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 297
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.989999,-0.097008,-0.102428,0.000000], [-0.077186,-0.980206,0.182316,0.000000], [-0.118086,-0.172586,-0.977890,0.000000], [82.057401,13.771454,135.283109,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 298
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.990156,-0.095802,-0.102044,0.000000], [-0.076081,-0.980328,0.182124,0.000000], [-0.117485,-0.172567,-0.977966,0.000000], [82.058558,13.755117,135.285660,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 299
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.990250,-0.094891,-0.101979,0.000000], [-0.075134,-0.980313,0.182598,0.000000], [-0.117298,-0.173156,-0.977884,0.000000], [82.054802,13.726178,135.293081,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 300
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.990735,-0.087745,-0.103657,0.000000], [-0.067737,-0.980808,0.182829,0.000000], [-0.117710,-0.174114,-0.977665,0.000000], [82.027399,13.700051,135.305529,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 301
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.991346,-0.084101,-0.100794,0.000000], [-0.064528,-0.980852,0.183752,0.000000], [-0.114318,-0.175658,-0.977791,0.000000], [82.323584,13.659848,135.056286,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 302
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.987593,-0.088716,-0.129572,0.000000], [-0.064678,-0.981689,0.179172,0.000000], [-0.143095,-0.168569,-0.975248,0.000000], [80.595563,13.550868,132.288597,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 303
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.989655,-0.085036,-0.115549,0.000000], [-0.062110,-0.979969,0.189220,0.000000], [-0.129325,-0.180085,-0.975112,0.000000], [81.148838,12.657579,130.740436,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 304
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.988808,-0.086621,-0.121473,0.000000], [-0.062518,-0.979830,0.189800,0.000000], [-0.135463,-0.180081,-0.974279,0.000000], [80.608161,12.320401,128.973064,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 305
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.990680,-0.085488,-0.106039,0.000000], [-0.064628,-0.980320,0.186535,0.000000], [-0.119899,-0.177944,-0.976709,0.000000], [81.355791,12.167329,127.286736,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 306
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.990852,-0.084770,-0.105004,0.000000], [-0.064301,-0.980648,0.184919,0.000000], [-0.118648,-0.176476,-0.977128,0.000000], [81.466357,12.208530,127.092190,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 307
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.990622,-0.083324,-0.108279,0.000000], [-0.062089,-0.980494,0.186484,0.000000], [-0.121705,-0.178012,-0.976473,0.000000], [81.296852,12.078912,126.935265,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 308
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.989999,-0.084617,-0.112876,0.000000], [-0.061893,-0.979546,0.191467,0.000000], [-0.126769,-0.182566,-0.974987,0.000000], [80.739021,11.363372,124.524572,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 309
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.990430,-0.081491,-0.111388,0.000000], [-0.059483,-0.980312,0.188281,0.000000], [-0.124538,-0.179853,-0.975778,0.000000], [80.860409,11.381470,123.717123,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 310
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.990651,-0.078611,-0.111497,0.000000], [-0.056624,-0.980497,0.188199,0.000000], [-0.124117,-0.180126,-0.975782,0.000000], [80.950510,11.370532,123.657404,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 311
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.990635,-0.078898,-0.111435,0.000000], [-0.056574,-0.979976,0.190908,0.000000], [-0.124266,-0.182816,-0.975262,0.000000], [80.858608,11.073831,122.776981,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 312
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.991012,-0.077740,-0.108865,0.000000], [-0.056137,-0.980361,0.189051,0.000000], [-0.121424,-0.181240,-0.975914,0.000000], [80.989631,11.106033,122.276820,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 313
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.991187,-0.075847,-0.108611,0.000000], [-0.054424,-0.980634,0.188136,0.000000], [-0.120777,-0.180567,-0.976119,0.000000], [81.062646,11.145589,122.257740,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 314
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.990957,-0.077165,-0.109772,0.000000], [-0.055350,-0.980327,0.189463,0.000000], [-0.122233,-0.181674,-0.975732,0.000000], [80.955639,11.046521,121.905663,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 315
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.991127,-0.078096,-0.107552,0.000000], [-0.056942,-0.980645,0.187331,0.000000], [-0.120100,-0.179544,-0.976391,0.000000], [81.046981,11.107237,121.486822,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 316
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.991031,-0.079481,-0.107421,0.000000], [-0.058350,-0.980585,0.187214,0.000000], [-0.120216,-0.179267,-0.976428,0.000000], [81.051610,11.130321,121.484757,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 317
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.990966,-0.080757,-0.107070,0.000000], [-0.059654,-0.980471,0.187398,0.000000], [-0.120113,-0.179318,-0.976431,0.000000], [81.072530,11.133073,121.484011,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 318
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.990959,-0.080929,-0.107006,0.000000], [-0.059727,-0.980297,0.188284,0.000000], [-0.120135,-0.180190,-0.976268,0.000000], [81.083515,11.087734,121.482593,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 319
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.990958,-0.080931,-0.107014,0.000000], [-0.059729,-0.980299,0.188272,0.000000], [-0.120143,-0.180178,-0.976269,0.000000], [81.083035,11.088533,121.482594,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 320
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.990958,-0.080931,-0.107014,0.000000], [-0.059729,-0.980299,0.188272,0.000000], [-0.120143,-0.180178,-0.976269,0.000000], [81.083035,11.088533,121.482594,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 321
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.990958,-0.080931,-0.107014,0.000000], [-0.059729,-0.980299,0.188272,0.000000], [-0.120143,-0.180178,-0.976269,0.000000], [81.083035,11.088533,121.482594,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 322
vcam.data.lens = 36.150196
vcam.matrix_world = (([0.990958,-0.080931,-0.107014,0.000000], [-0.059729,-0.980299,0.188272,0.000000], [-0.120143,-0.180178,-0.976269,0.000000], [81.083035,11.088533,121.482594,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')

scene.frame_current = 323
vcam.data.lens = 40.208727
vcam.matrix_world = (([0.773510,-0.331098,-0.540422,0.000000], [0.182601,-0.929684,0.319914,0.000000], [-0.632961,-0.360145,-0.685314,0.000000], [-0.159412,1.090438,12.088341,1.000000])) 
vcam.keyframe_insert('location')
vcam.keyframe_insert('scale')
vcam.keyframe_insert('rotation_euler')
vcam.data.keyframe_insert('lens')



# 3D Feature Points
verts = []
verts.append((86.159671,11.470991,185.193210))
verts.append((78.745850,12.462334,186.426744))
verts.append((83.147191,13.472092,183.539736))
verts.append((76.594701,15.382935,185.700379))
verts.append((80.990518,14.713352,183.591640))
verts.append((88.499041,1.459296,182.959222))
verts.append((88.075149,5.669406,178.596508))
verts.append((88.056303,11.499199,184.496007))
verts.append((92.349972,12.124122,184.529631))
verts.append((80.289673,11.231447,186.393971))
verts.append((77.894144,7.577277,185.826238))
verts.append((80.286016,7.350928,186.384958))
verts.append((91.359934,5.433725,185.219158))
verts.append((87.840243,4.607052,183.619883))
verts.append((69.041028,8.538271,187.951212))
verts.append((77.282318,2.812669,185.727221))
verts.append((72.510011,15.645641,185.701593))
verts.append((80.169199,11.990181,185.886305))
verts.append((86.805241,10.737620,168.684585))
verts.append((87.097037,4.868789,184.890319))
verts.append((75.964640,2.393512,185.159934))
verts.append((85.356876,10.294965,184.263559))
verts.append((74.773490,7.980215,188.721501))
verts.append((96.725154,13.644807,183.120014))
verts.append((89.378903,4.931065,180.971982))
verts.append((82.154288,22.952128,184.298554))
verts.append((86.486136,5.924100,182.328418))
verts.append((86.276068,22.586032,183.996242))
verts.append((87.258743,1.299850,182.217612))
verts.append((82.048804,13.881671,184.713658))
verts.append((83.653283,21.807158,184.363735))
verts.append((91.450323,15.893399,183.988445))
verts.append((87.839315,23.948347,184.072484))
verts.append((79.187933,14.102901,185.165479))
verts.append((81.053168,16.694366,185.453969))
verts.append((82.624098,19.977193,184.408498))
verts.append((79.434111,16.270540,185.462987))
verts.append((83.845547,8.944160,185.731558))
verts.append((87.674929,24.653119,174.106491))
verts.append((90.363782,12.891102,183.860575))
verts.append((81.678036,8.043576,186.897989))
verts.append((75.493663,7.865502,188.075610))
verts.append((78.952012,4.845278,188.885901))
verts.append((85.506519,23.640373,181.425721))
verts.append((88.518532,25.010339,183.500886))
verts.append((87.311235,20.947242,184.108748))
verts.append((76.632678,7.696335,188.025480))
verts.append((108.187510,20.560029,180.507803))
verts.append((105.732112,11.429404,181.299214))
verts.append((73.161251,3.218506,183.441852))
verts.append((82.662593,24.525245,182.983090))
verts.append((71.164011,9.973721,186.541715))
verts.append((92.063670,8.354520,182.917179))
verts.append((76.154716,20.298964,184.857259))
verts.append((83.514309,20.962132,184.395946))
verts.append((89.675294,16.460923,183.520660))
verts.append((83.565239,14.340352,185.420046))
verts.append((75.666503,12.977591,186.141535))
verts.append((81.469963,13.816607,185.832305))
verts.append((72.754015,14.075383,187.514632))
verts.append((96.637908,-0.146965,181.794704))
verts.append((82.366697,12.984045,186.538709))
verts.append((77.656273,15.272748,185.727673))
verts.append((76.614035,12.837092,186.094421))
verts.append((90.450204,13.770952,183.445760))
verts.append((89.013015,18.291700,184.792622))
verts.append((89.057293,13.392481,185.166217))
verts.append((85.401829,9.491054,185.047125))
verts.append((78.403648,21.223973,184.202513))
verts.append((81.567941,11.783128,185.583063))
verts.append((81.766657,19.964537,185.103117))
verts.append((82.688413,8.636303,185.376649))
verts.append((74.262388,18.190793,186.205319))
verts.append((93.976657,1.689310,179.988820))
verts.append((77.024362,6.511088,188.089007))
verts.append((93.466202,3.181879,180.523491))
verts.append((77.219166,14.481201,185.936349))
verts.append((92.691825,7.549429,168.623709))
verts.append((98.548664,10.264882,182.796492))
verts.append((81.906836,21.930102,183.505800))
verts.append((78.162385,5.884791,185.609591))
verts.append((81.160105,21.833358,185.147417))
verts.append((93.850278,0.100650,179.969496))
verts.append((88.023391,16.855048,183.394617))
verts.append((88.017492,12.395137,184.026325))
verts.append((76.397490,3.035964,185.950922))
verts.append((105.452967,12.717255,180.622655))
verts.append((118.489396,1.460999,178.516081))
verts.append((89.886729,22.338059,183.170185))
verts.append((89.641648,14.622663,183.036585))
verts.append((73.293496,1.837104,184.288866))
verts.append((70.783593,3.594710,186.879134))
verts.append((124.224657,5.348187,184.232987))
verts.append((66.608888,27.414250,183.661078))
verts.append((85.534827,20.438204,180.618309))
verts.append((103.050533,18.321507,181.839683))
verts.append((81.729373,11.047504,186.688958))
verts.append((96.779936,14.716867,181.459414))
verts.append((85.812949,13.283752,184.689827))
verts.append((82.453232,21.126228,184.776046))
verts.append((82.690841,21.464258,182.625826))
verts.append((75.830053,15.689523,186.108042))
verts.append((86.596030,12.518709,183.123952))
verts.append((86.261034,10.640992,184.165510))
verts.append((85.189731,5.014135,180.052068))
verts.append((104.590611,13.610629,180.914319))
verts.append((76.537371,5.379120,185.929550))
verts.append((80.225842,10.342739,184.392234))
verts.append((96.153171,16.905291,182.445754))
verts.append((102.877384,8.784092,181.250980))
verts.append((73.922009,8.438586,188.713876))
verts.append((83.224881,10.460688,185.252309))
verts.append((86.905069,11.393001,183.957805))
verts.append((90.192235,0.284006,181.771046))
verts.append((79.701646,12.822433,185.603779))
verts.append((89.276180,24.184373,182.505397))
verts.append((104.017731,6.961837,180.738109))
verts.append((70.234047,12.374665,187.557843))
verts.append((104.841337,12.796663,182.292234))
verts.append((83.109211,18.619029,184.238866))
verts.append((88.253653,19.285464,183.450540))
verts.append((78.986215,11.647029,186.184575))
verts.append((101.851925,14.784380,182.883824))
verts.append((101.581543,17.910368,182.677107))
verts.append((81.282624,18.458042,184.538505))
verts.append((114.050771,18.866742,180.344878))
verts.append((77.606760,21.340101,185.124858))
verts.append((73.707322,6.579178,187.603725))
verts.append((98.627348,14.855574,179.652418))
verts.append((79.081883,5.315102,185.820110))
verts.append((118.436232,22.892499,178.006104))
verts.append((66.838424,24.988565,186.662082))
verts.append((104.363208,15.228755,180.944842))
verts.append((83.230323,12.142635,185.701391))
verts.append((81.149923,15.582532,185.017302))
verts.append((113.115535,19.354315,177.521348))
verts.append((107.561660,19.423874,178.603496))
verts.append((91.044473,14.686655,183.978153))
verts.append((85.314249,21.340617,183.936046))
verts.append((70.515161,11.429160,186.733178))
verts.append((82.576683,23.850485,184.261607))
verts.append((84.448615,26.593486,180.844754))
verts.append((109.190013,20.683608,180.392904))
verts.append((78.155234,2.977604,185.635889))
verts.append((89.179864,24.916084,181.726294))
verts.append((81.244897,20.795525,185.021987))
verts.append((82.926140,22.671627,183.438908))
verts.append((107.030039,10.538336,182.306037))
verts.append((56.904287,28.354308,181.705113))
verts.append((112.412654,19.656344,180.680249))
verts.append((69.813364,10.476837,190.037416))
verts.append((85.627616,20.634733,183.744175))
verts.append((102.898546,22.599357,181.235222))
verts.append((80.249748,13.892831,185.727515))
verts.append((85.542953,23.824891,183.302786))
verts.append((81.917346,10.380085,184.069945))
verts.append((84.912614,19.274762,184.248210))
verts.append((79.020055,15.434696,186.066799))
verts.append((81.544953,15.546202,179.940899))
verts.append((87.315697,24.878120,183.077798))
verts.append((89.283908,11.964561,184.899874))
verts.append((110.901629,19.892860,180.817571))
verts.append((89.389175,15.450598,183.192898))
verts.append((82.016721,14.676234,183.975043))
verts.append((105.491126,14.765291,181.160103))
verts.append((102.243989,10.345858,182.501852))
verts.append((74.592261,14.094457,187.125509))
verts.append((77.401888,16.235393,185.551084))
verts.append((75.878496,3.868116,186.103487))
verts.append((68.878313,9.836680,186.610725))
verts.append((71.782093,15.626606,186.266209))
verts.append((72.106769,17.811679,184.974854))
verts.append((89.907165,12.144989,184.068522))
verts.append((84.440988,23.981570,183.505332))
verts.append((75.307185,20.386313,186.019173))
verts.append((84.672066,14.218456,178.480179))
verts.append((85.027365,10.656674,185.865193))
verts.append((123.223681,9.773047,180.405501))
verts.append((121.994424,7.128918,179.875979))
verts.append((123.837291,6.821029,179.251394))
verts.append((77.399609,7.486563,187.612850))
verts.append((122.383276,7.974098,180.085329))
verts.append((102.965301,1.699905,179.727686))
verts.append((85.026672,22.182700,183.992179))
verts.append((125.529749,17.691259,181.431568))
verts.append((125.079648,8.575639,180.003056))
verts.append((124.435848,7.744389,179.658631))
verts.append((79.884153,22.264598,184.693925))
verts.append((122.751648,8.921851,180.106565))
verts.append((92.027433,3.514921,180.837290))
verts.append((130.196985,6.272469,188.002535))
verts.append((125.954185,10.392361,180.337666))
verts.append((124.519589,12.559971,180.980162))
verts.append((87.657844,0.635674,181.202095))
verts.append((70.692961,2.094399,184.546613))
verts.append((123.550200,7.802258,179.968189))
verts.append((84.085053,11.232145,185.761766))
verts.append((102.445122,14.547114,182.157113))
verts.append((125.444265,9.532544,180.151617))
verts.append((102.601172,17.094572,181.435156))
verts.append((123.850632,8.753466,180.053209))
verts.append((79.647416,17.034963,185.096916))
verts.append((135.562020,6.512847,190.656646))
verts.append((124.809930,10.557244,180.501787))
verts.append((78.384875,22.765558,184.372353))
verts.append((125.498909,16.773431,181.256835))
verts.append((110.965348,20.989325,180.584874))
verts.append((84.400961,12.416129,184.767194))
verts.append((80.631851,12.883226,185.619182))
verts.append((124.197880,9.707674,180.176543))
verts.append((79.262279,20.471348,185.145140))
verts.append((92.693425,4.308633,180.039513))
verts.append((75.434245,14.664453,186.489081))
verts.append((107.083856,14.030275,181.791828))
verts.append((118.293858,20.099086,179.403742))
verts.append((90.857400,12.084705,184.086434))
verts.append((124.453900,6.633282,178.578834))
verts.append((117.537632,0.508157,177.913699))
verts.append((91.703374,12.980936,184.214686))
verts.append((125.154739,11.525026,180.623119))
verts.append((98.594629,12.179729,182.735269))
verts.append((82.612839,9.454786,184.961602))
verts.append((126.603626,12.974222,180.857907))
verts.append((84.708369,20.155417,181.325593))
verts.append((80.762781,8.758959,187.013002))
verts.append((91.555184,19.298197,182.348042))
verts.append((90.938275,16.746815,183.733744))
verts.append((118.925365,17.713353,179.416814))
verts.append((89.019059,4.486720,182.317772))
verts.append((106.486416,20.473112,180.829306))
verts.append((99.253702,13.172684,183.606104))
verts.append((70.726214,15.696122,186.513936))
verts.append((86.656667,20.152520,183.079698))
verts.append((126.816710,17.300244,180.673164))
verts.append((86.811592,16.206121,184.053474))
verts.append((79.905142,23.996293,184.353257))
verts.append((79.593820,17.864818,185.321658))
verts.append((72.297841,2.012932,183.911055))
verts.append((89.794042,1.245527,181.580646))
verts.append((78.277143,17.932204,181.265768))
verts.append((77.081740,19.818760,185.168688))
verts.append((75.052800,21.803350,184.946279))
verts.append((78.532257,4.289272,185.431488))
verts.append((81.321378,22.644301,184.580042))
verts.append((71.624806,27.258838,183.788476))
verts.append((88.798133,23.945063,183.666351))
verts.append((77.189486,1.967963,185.003017))
verts.append((75.876443,16.955471,184.628688))
verts.append((72.988559,19.122314,187.284661))
verts.append((115.307400,18.662618,180.551175))
verts.append((81.951299,7.913116,184.722955))
verts.append((81.789688,9.285084,185.544191))
verts.append((124.520277,14.288980,181.419258))
verts.append((103.014278,7.917706,182.472396))
verts.append((74.114605,10.948153,186.699459))
verts.append((84.428124,22.554178,184.799809))
verts.append((73.604475,3.746541,186.425559))
verts.append((80.827959,33.677024,175.507333))
verts.append((123.453591,12.267205,181.137937))
verts.append((77.680755,12.688905,186.114739))
verts.append((77.736424,23.793772,184.676448))
verts.append((79.423710,21.323430,184.515256))
verts.append((81.609558,24.373992,183.912101))
verts.append((88.442112,16.036080,182.982933))
verts.append((91.797400,14.116542,183.366213))
verts.append((96.355088,17.693031,182.392711))
verts.append((71.747548,12.142988,186.703938))
verts.append((113.144419,20.701042,180.151495))
verts.append((125.490534,19.636484,181.660155))
verts.append((115.203394,19.373742,178.847181))
verts.append((78.571129,8.290529,186.161082))
verts.append((118.937076,19.135627,179.634623))
verts.append((93.078550,18.447398,183.328989))
verts.append((58.265737,28.414550,182.075573))
verts.append((84.300018,25.170184,179.848828))
verts.append((86.030158,12.455466,184.856929))
verts.append((78.368429,9.960351,186.508772))
verts.append((78.410403,17.870948,185.147386))
verts.append((87.970402,22.250792,182.623901))
verts.append((105.680551,20.632272,182.014022))
verts.append((86.660196,15.389770,184.771467))
verts.append((66.475051,22.771294,185.526547))
verts.append((70.788927,5.778800,188.342679))
verts.append((107.955027,31.803678,169.689992))
verts.append((86.649256,1.502606,179.954254))
verts.append((97.758966,15.708537,182.223049))
verts.append((75.946324,19.568090,186.332487))
verts.append((68.548156,6.682754,186.676972))
verts.append((79.048188,36.209512,176.082843))
verts.append((67.904141,2.441862,184.873024))
verts.append((72.752281,21.273411,184.230804))
verts.append((102.025492,5.355403,181.750877))
verts.append((103.092367,3.289192,181.319454))
verts.append((83.729192,20.182000,184.583699))
verts.append((104.623684,21.456626,181.360231))
verts.append((74.325944,12.822435,186.745571))
verts.append((75.182537,24.488467,185.144484))
verts.append((84.713200,13.323183,184.192299))
verts.append((60.624957,27.013111,183.600832))
verts.append((109.387065,22.320448,179.792030))
verts.append((89.346474,1.170792,182.624083))
verts.append((80.288591,31.899548,177.399328))
verts.append((112.635333,21.702282,180.354111))
verts.append((88.080560,1.799561,173.358888))
verts.append((56.150834,28.258806,181.551125))
verts.append((95.911240,0.427094,182.328587))
verts.append((81.646945,33.695976,175.220792))
verts.append((106.271261,7.161491,182.465289))
verts.append((78.271891,6.649993,185.820235))
verts.append((87.084917,17.391934,184.421162))
verts.append((107.908099,35.070352,169.467112))
verts.append((98.548955,23.059304,180.255417))
verts.append((102.094414,13.602052,181.187658))
verts.append((85.135952,22.974891,183.881535))
verts.append((99.355091,14.848289,183.095677))
verts.append((70.532688,21.781460,185.548336))
verts.append((104.181165,22.590276,180.800608))
verts.append((84.706724,21.385164,184.823431))
verts.append((71.778182,16.987725,186.799073))
verts.append((69.105343,21.799166,185.239332))
verts.append((119.347831,21.089517,179.281270))
verts.append((125.645373,22.849424,181.820784))
verts.append((114.758835,20.392930,179.421469))
verts.append((94.468874,18.482654,183.701242))
verts.append((73.957414,27.246193,183.743534))
verts.append((101.382095,18.748102,182.103597))
verts.append((87.503626,23.057351,183.644164))
verts.append((99.306417,14.016897,183.572987))
verts.append((99.901483,6.345543,180.184582))
verts.append((86.644669,14.377037,183.945490))
verts.append((91.312550,19.215514,183.958512))
verts.append((92.432182,1.265835,177.647122))
verts.append((106.087482,22.756026,180.480821))
verts.append((121.069066,6.577768,180.205852))
verts.append((105.015993,33.355512,169.835996))
verts.append((75.318263,1.766550,184.230452))
verts.append((86.232382,21.361597,183.880111))
verts.append((72.866035,27.598037,184.506346))
verts.append((70.962523,14.861850,186.290577))
verts.append((107.080610,18.754692,180.879334))
verts.append((110.342122,33.195646,160.284882))
verts.append((76.056448,18.703660,185.563789))
verts.append((73.277878,22.876062,184.489095))
verts.append((66.624114,17.180990,186.804968))
verts.append((122.481999,9.478679,181.047820))
verts.append((73.157923,24.427284,183.648553))
verts.append((67.521445,17.123754,186.700391))
verts.append((81.098867,33.832133,165.494872))
verts.append((96.106480,15.023166,182.027167))
verts.append((97.890443,16.578998,182.533298))
verts.append((84.289489,9.881895,184.964513))
verts.append((102.760486,-0.697476,179.087741))
verts.append((72.354123,7.459009,186.349889))
verts.append((66.973220,26.629656,183.700509))
verts.append((76.121937,10.167562,185.448186))
verts.append((70.290193,19.163920,186.358293))
verts.append((89.668848,18.051037,183.676123))
verts.append((66.440479,19.340666,185.409209))
verts.append((75.753009,5.104411,186.360410))
verts.append((105.922707,5.854263,182.717969))
verts.append((64.555935,33.609619,179.284640))
verts.append((93.284252,19.312226,183.968056))
verts.append((71.814411,21.715063,185.991018))
verts.append((103.844493,19.786563,181.554252))
verts.append((79.741006,34.000732,164.104916))
verts.append((119.554468,1.279175,178.468211))
verts.append((79.674253,23.145200,183.916863))
verts.append((91.014432,0.856547,176.782908))
verts.append((77.487299,11.643815,185.651492))
verts.append((52.756112,34.390142,178.296174))
verts.append((113.280483,19.760608,180.333529))
verts.append((65.817228,27.224411,183.879420))
verts.append((94.284358,18.885881,180.660425))
verts.append((66.705814,3.527530,176.900276))
verts.append((125.462777,13.407482,180.981701))
verts.append((71.360161,17.893663,185.757346))
verts.append((67.321364,20.383310,185.413985))
verts.append((76.941025,10.919349,187.668739))
verts.append((60.422136,34.542644,171.358777))
verts.append((92.494260,22.504615,182.924346))
verts.append((119.440940,22.583571,177.900234))
verts.append((107.763528,31.711591,171.011818))
verts.append((122.582402,10.439579,180.905720))
verts.append((50.497837,26.838201,182.240100))
verts.append((116.395611,21.027975,178.550782))
verts.append((49.779204,34.084841,177.079431))
verts.append((83.328773,16.898754,184.708645))
verts.append((68.748950,19.202360,185.906804))
verts.append((66.457325,20.707633,185.016052))
verts.append((71.922747,23.179897,184.831651))
verts.append((66.164274,16.350829,186.839032))
verts.append((51.797224,23.521955,182.626043))
verts.append((115.284883,21.261398,179.532191))
verts.append((102.223425,11.177389,181.998650))
verts.append((103.777374,13.531336,182.152885))
verts.append((103.671415,32.240683,170.800593))
verts.append((85.737178,24.747785,184.111447))
verts.append((110.942680,23.512839,179.362781))
verts.append((81.426142,25.712237,183.933486))
verts.append((101.245511,9.467458,180.132430))
verts.append((121.527210,7.682466,180.594964))
verts.append((110.744039,29.938354,170.813522))
verts.append((100.742891,22.884334,182.417420))
verts.append((74.779563,7.112203,187.896761))
verts.append((89.456296,23.181096,183.109586))
verts.append((93.132967,25.046963,183.686795))
verts.append((106.133897,33.482845,168.434493))
verts.append((77.517115,32.903415,177.203226))
verts.append((92.278960,2.703211,178.443094))
verts.append((87.893420,18.560491,184.358762))
verts.append((70.153677,20.241361,185.792943))
verts.append((108.005086,19.783105,181.339042))
verts.append((69.276553,25.926749,183.896884))
verts.append((96.978223,13.895481,181.505554))
verts.append((69.489163,16.997433,186.355202))
verts.append((95.856062,15.771546,180.641489))
verts.append((108.150665,23.699116,179.642492))
verts.append((98.408165,32.187108,172.888517))
verts.append((70.201115,10.597608,187.504608))
verts.append((69.331127,20.357951,185.891591))
verts.append((108.325612,28.487196,173.230812))
verts.append((68.591413,15.849040,185.498911))
verts.append((106.692442,28.253089,174.084725))
verts.append((101.391727,16.732439,181.340220))
verts.append((60.340797,34.899146,178.209824))
verts.append((91.191107,22.666407,183.340143))
verts.append((62.005879,34.620332,171.048630))
verts.append((111.264515,22.470451,179.984471))
verts.append((113.656385,32.271405,168.997598))
verts.append((114.447495,31.124466,169.495196))
verts.append((80.371157,35.027875,168.134364))
verts.append((80.833515,20.016238,185.068186))
verts.append((57.880571,34.220593,178.426308))
verts.append((91.937775,2.278832,179.660101))
verts.append((79.869286,14.907386,185.988196))
verts.append((71.279966,13.275113,187.792296))
verts.append((113.650168,17.977969,179.908249))
verts.append((103.419503,7.840759,180.796870))
verts.append((91.805279,4.808538,180.596309))
verts.append((108.229675,30.218107,171.775255))
verts.append((77.579065,22.332061,184.798693))
verts.append((84.844444,11.566142,184.603400))
verts.append((86.049368,25.705311,182.733756))
verts.append((68.983847,35.717620,170.653678))
verts.append((99.311011,15.675839,182.729321))
verts.append((76.729666,4.593061,185.842302))
verts.append((153.600951,24.781651,208.542169))
verts.append((91.951368,25.878308,184.934385))
verts.append((110.235238,23.742310,180.319081))
verts.append((69.092505,28.252166,184.873796))
verts.append((65.540508,28.482002,183.938816))
verts.append((54.817442,24.234191,183.816719))
verts.append((119.253209,18.505769,178.736160))
verts.append((104.658917,28.902123,173.630081))
verts.append((113.341374,29.199191,171.072545))
verts.append((47.577421,11.984700,189.931027))
verts.append((91.002885,20.827670,182.531043))
verts.append((70.525444,2.913779,186.256157))
verts.append((70.212228,17.015052,185.796901))
verts.append((105.567791,30.721152,171.622803))
verts.append((116.196832,-1.823896,176.872055))
verts.append((59.338217,34.798238,171.205947))
verts.append((92.806523,17.659263,183.836213))
verts.append((100.135961,20.539401,181.725347))
verts.append((71.972583,19.209022,186.770404))
verts.append((109.921248,30.312361,171.102309))
verts.append((61.194552,34.732164,178.407008))
verts.append((110.891897,28.280085,173.002600))
verts.append((106.289524,27.293824,175.513368))
verts.append((93.652320,34.249813,164.254201))
verts.append((74.592648,25.946163,183.523525))
verts.append((117.285814,27.769204,171.677926))
verts.append((122.934744,22.788333,180.119428))
verts.append((117.561793,29.413776,168.537057))
verts.append((111.330266,30.845861,170.925722))
verts.append((95.249243,18.147937,182.177021))
verts.append((121.874649,8.628972,180.753431))
verts.append((79.094049,7.443370,186.879156))
verts.append((51.710737,24.597162,182.103959))
verts.append((84.858341,18.245672,184.467828))
verts.append((112.184680,30.883120,169.969860))
verts.append((66.535231,18.135638,185.869920))
verts.append((120.662894,27.590602,172.140528))
verts.append((80.835282,33.343241,177.528724))
verts.append((105.128614,19.520878,180.987536))
verts.append((115.454022,29.592293,169.818315))
verts.append((120.250468,20.437990,179.104333))
verts.append((91.052835,30.034291,177.233908))
verts.append((115.666477,28.002166,171.602926))
verts.append((58.795926,33.189907,179.747566))
verts.append((72.700988,16.624244,185.556861))
verts.append((115.101964,31.158616,166.572373))
verts.append((69.069636,18.070748,185.744475))
verts.append((54.081924,24.234714,183.157817))
verts.append((106.706072,21.987500,179.938304))
verts.append((73.265729,7.426379,186.657731))
verts.append((55.872113,33.014179,178.906143))
verts.append((76.976339,11.954482,186.907556))
verts.append((107.371865,14.891882,182.453552))
verts.append((114.507530,29.607060,170.307655))
verts.append((113.414653,28.416020,171.613944))
verts.append((77.879251,27.045473,182.565463))
verts.append((91.915414,1.582950,178.974850))
verts.append((99.373518,16.870030,183.012798))
verts.append((74.105876,11.725530,186.075317))
verts.append((122.347578,6.140993,179.753619))
verts.append((81.484559,10.088460,185.563539))
verts.append((99.668294,15.917400,181.341489))
verts.append((109.940964,33.845909,168.228424))
verts.append((88.659404,23.100321,183.478451))
verts.append((70.294991,18.127983,187.101840))
verts.append((101.148162,7.458343,183.219144))
verts.append((117.027840,29.009865,170.481293))
verts.append((66.412416,23.777007,184.139376))
verts.append((64.718864,35.916251,178.715364))
verts.append((99.610263,18.187465,182.678588))
verts.append((49.207132,31.370962,184.538515))
verts.append((61.289988,33.503775,179.059906))
verts.append((123.222147,13.340174,180.707107))
verts.append((72.808804,2.524197,185.560528))
verts.append((102.034172,15.631596,183.046405))
verts.append((104.941328,23.999601,180.599003))
verts.append((71.689483,9.157908,186.446031))
verts.append((61.241603,34.171705,170.647302))
verts.append((105.921099,31.681141,171.325120))
verts.append((76.506912,24.097100,184.249635))
verts.append((101.588567,12.021061,179.923619))
verts.append((112.913730,32.154335,166.293168))
verts.append((71.578402,11.273832,187.742360))
verts.append((125.757130,18.646333,181.961576))
verts.append((59.704736,27.679477,182.596099))
verts.append((88.863908,32.177908,175.968848))
verts.append((104.828793,27.907181,175.652610))
verts.append((73.707426,26.544865,184.347509))
verts.append((52.181205,33.643151,174.858323))
verts.append((116.434734,23.004500,178.447324))
verts.append((113.238323,21.772572,179.660581))
verts.append((70.079685,27.823919,184.067737))
verts.append((80.767466,24.161056,184.221140))
verts.append((114.747442,30.639904,165.034541))
verts.append((127.406214,21.061273,181.875980))
verts.append((115.215561,30.545635,167.610750))
verts.append((67.731855,4.941844,186.842582))
verts.append((65.436988,25.053011,184.386739))
verts.append((68.619061,20.531550,186.528423))
verts.append((92.648230,21.605986,182.415542))
verts.append((69.507409,13.946374,187.333043))
verts.append((99.679824,5.582290,179.742232))
verts.append((67.701354,32.919411,179.979589))
verts.append((74.714290,34.148039,177.258178))
verts.append((66.582219,35.711342,178.923468))
verts.append((73.039139,26.108116,185.741274))
verts.append((93.468061,20.237675,183.136024))
verts.append((92.999018,12.551779,183.554236))
verts.append((114.452933,28.655103,170.787483))
verts.append((67.965861,34.934660,178.105643))
verts.append((113.746011,31.116030,170.242934))
verts.append((69.053109,32.831736,178.884167))
verts.append((86.044809,32.489156,175.713454))
verts.append((105.117337,30.729829,172.385676))
verts.append((127.616326,18.250128,181.391043))
verts.append((74.663844,16.706164,185.704755))
verts.append((103.773381,28.647437,173.983830))
verts.append((70.803630,27.142017,183.766722))
verts.append((51.181540,26.826934,181.714672))
verts.append((63.393522,2.129746,177.539280))
verts.append((91.775865,23.158940,181.203280))
verts.append((82.386027,33.951721,163.655704))
verts.append((101.815286,28.297646,166.162122))
verts.append((59.900156,31.801659,180.006392))
verts.append((64.696628,34.417230,169.272110))
verts.append((64.807968,28.547991,184.324021))
verts.append((100.988149,28.627109,175.086859))
verts.append((56.588454,33.774197,178.420707))
verts.append((99.769253,33.371140,160.472514))
verts.append((102.050187,16.234617,180.498992))
verts.append((106.235980,32.733285,170.411871))
verts.append((68.650657,17.055789,186.441489))
verts.append((123.968802,20.452172,181.106312))
verts.append((84.662552,38.467826,172.851902))
verts.append((89.532679,30.265189,176.908532))
verts.append((92.288922,31.053539,174.948994))
verts.append((71.625264,27.952468,183.012434))
verts.append((107.969419,30.795409,170.864014))
verts.append((87.633785,30.431928,177.668166))
verts.append((69.508191,15.903203,185.848968))
verts.append((109.836134,29.600486,171.538592))
verts.append((119.311208,28.528131,170.961787))
verts.append((76.868695,10.744569,184.341228))
verts.append((78.608483,23.598938,184.686428))
verts.append((94.216033,19.228417,182.450431))
verts.append((67.357532,35.307249,170.973026))
verts.append((108.718120,21.512204,181.461451))
verts.append((67.208588,19.378580,185.071053))
verts.append((76.195259,30.474089,180.227741))
verts.append((126.880215,20.148739,181.804619))
verts.append((66.897431,2.955368,185.028660))
verts.append((115.419584,30.936363,169.371939))
verts.append((110.549115,34.501654,166.004675))
verts.append((95.657712,34.914150,170.650542))
verts.append((97.506361,32.267862,172.938560))
verts.append((82.431097,11.159494,185.693185))
verts.append((105.244009,29.028483,173.078230))
verts.append((112.774617,32.064576,162.940052))
verts.append((90.892974,21.611631,182.093863))
verts.append((100.460799,33.436301,162.633800))
verts.append((93.761993,24.023073,183.283569))
verts.append((62.124636,35.156351,178.864262))
verts.append((78.829052,13.213921,185.553097))
verts.append((70.456816,22.904737,184.796452))
verts.append((49.042338,34.333412,174.791869))
verts.append((102.087555,22.494855,181.599740))
verts.append((69.629076,35.341352,178.119344))
verts.append((101.612745,30.407458,173.216909))
verts.append((116.448431,20.245646,179.339447))
verts.append((68.610211,33.470548,178.502549))
verts.append((84.713354,24.928256,183.953619))
verts.append((93.026215,27.397208,179.603964))
verts.append((84.528036,33.013093,175.748274))
verts.append((69.175324,22.835912,184.805058))
verts.append((51.137320,33.204776,177.681188))
verts.append((84.998544,15.769314,184.655911))
verts.append((62.159906,31.505505,180.328739))
verts.append((62.964388,28.179797,183.086710))
verts.append((89.556530,33.517739,164.537861))
verts.append((112.213649,20.848692,180.369779))
verts.append((95.564118,31.173443,175.098213))
verts.append((55.001478,28.428632,181.221842))
verts.append((80.575286,33.649051,166.103270))
verts.append((103.208753,27.220040,176.314705))
verts.append((70.128882,13.344153,186.363925))
verts.append((102.910861,25.718234,179.946134))
verts.append((96.039173,33.236147,171.572203))
verts.append((62.881466,34.527132,178.313094))
verts.append((71.356537,6.554638,187.142857))
verts.append((123.431872,5.976745,179.544164))
verts.append((48.738840,34.065605,176.899437))
verts.append((73.055781,22.077892,184.531808))
verts.append((53.330960,24.060606,182.866837))
verts.append((98.748581,32.808055,172.180398))
verts.append((93.284334,30.861740,175.141431))
verts.append((91.022262,32.520972,175.336635))
verts.append((106.492011,17.836476,180.927721))
verts.append((76.701698,35.462071,168.917524))
verts.append((112.786171,18.722688,180.106353))
verts.append((75.960111,21.166807,185.271558))
verts.append((59.384691,28.905482,185.270348))
verts.append((68.327583,34.181488,169.778001))
verts.append((63.413009,33.498446,178.615877))
verts.append((78.983130,33.785390,176.430981))
verts.append((87.624022,16.059283,183.682000))
verts.append((54.419731,34.816520,169.930909))
verts.append((47.824745,29.334957,186.631835))
verts.append((88.291395,33.698728,162.868531))
verts.append((103.342175,2.436746,180.387947))
verts.append((107.793365,22.556580,179.903458))
verts.append((84.148414,34.568300,164.947667))
verts.append((101.501881,32.495229,171.362944))
verts.append((56.616511,31.579361,179.516432))
verts.append((112.447710,27.375614,173.935472))
verts.append((113.646245,27.571693,173.697971))
verts.append((87.276414,33.932575,165.488280))
verts.append((112.292939,32.683197,167.176805))
verts.append((91.617630,33.087827,174.084702))
verts.append((60.527277,34.629292,169.087520))
verts.append((91.920729,31.917848,174.291450))
verts.append((66.718149,32.601280,179.074213))
verts.append((122.789377,11.411828,181.013935))
verts.append((97.388169,33.221210,172.344751))
verts.append((117.414781,22.668095,178.152184))
verts.append((107.230415,33.509331,168.096301))
verts.append((128.936725,19.563305,182.356583))
verts.append((94.827012,33.134381,172.504698))
verts.append((104.445369,33.041697,170.864305))
verts.append((102.839083,28.360423,174.935582))
verts.append((82.451958,17.459764,184.718502))
verts.append((124.070783,24.749352,178.125314))
verts.append((109.320283,29.488049,172.133574))
verts.append((99.092467,24.180431,182.936355))
verts.append((61.177617,31.485972,180.248788))
verts.append((107.501589,27.477372,174.315500))
verts.append((92.208876,35.356856,170.903428))
verts.append((115.549028,22.888284,178.733860))
verts.append((68.689454,31.596034,180.200315))
verts.append((65.207824,34.928878,178.332568))
verts.append((103.405981,34.454250,169.953241))
verts.append((106.223914,21.594917,181.510601))
verts.append((106.344833,30.750093,171.034661))
verts.append((97.108832,31.069516,173.830322))
verts.append((67.574740,3.510254,186.308851))
verts.append((67.416801,18.473996,185.519757))
verts.append((56.813033,34.693834,171.066471))
verts.append((90.209101,31.547479,176.223664))
verts.append((98.127354,33.739410,162.455837))
verts.append((110.179280,33.076730,161.155729))
verts.append((106.197255,34.302585,168.539542))
verts.append((109.834963,30.931088,170.300603))
verts.append((72.745508,31.320871,181.002484))
verts.append((52.739923,23.351461,182.663894))
verts.append((60.328783,33.866749,179.167418))
verts.append((64.363316,34.944648,178.682049))
verts.append((74.875496,2.886442,178.377471))
verts.append((89.721093,32.973145,175.273772))
verts.append((53.662102,34.112199,178.280732))
verts.append((68.972980,2.291285,184.517296))
verts.append((73.814763,19.236629,185.587512))
verts.append((97.733986,33.673580,163.540678))
verts.append((54.382796,24.880107,182.537726))
verts.append((85.941364,30.994766,177.307602))
verts.append((93.565464,23.150832,182.999415))
verts.append((51.972158,7.727680,186.806495))
verts.append((112.318830,28.714493,171.510809))
verts.append((55.953618,34.650953,170.319460))
verts.append((73.722866,23.944687,186.267111))
verts.append((109.225007,32.622993,169.452365))
verts.append((74.523037,10.083158,186.787306))
verts.append((101.503580,33.148563,159.511780))
verts.append((118.878939,28.117010,172.244971))
verts.append((111.733399,28.150609,172.762711))
verts.append((85.414447,28.515456,180.274650))
verts.append((100.110451,29.986254,174.263485))
verts.append((51.636592,22.835540,182.884372))
verts.append((105.701516,28.263261,174.532837))
verts.append((107.510327,28.223133,173.528049))
verts.append((58.564251,34.647516,169.815875))
verts.append((81.534881,28.572810,181.681267))
verts.append((72.508955,33.866313,177.414392))
verts.append((95.299910,15.777703,182.284396))
verts.append((95.008045,30.237088,174.372992))
verts.append((65.923409,33.234440,179.257151))
verts.append((111.358060,29.331979,172.141852))
verts.append((100.481366,27.358372,177.538859))
verts.append((118.778049,8.494788,180.886813))
verts.append((64.228445,32.324897,180.542551))
verts.append((101.723174,31.059743,172.573286))
verts.append((107.206662,34.202515,165.564563))
verts.append((93.451086,29.082190,177.778618))
verts.append((77.059464,29.821374,180.511531))
verts.append((105.632791,25.283179,178.504777))
verts.append((76.607142,33.905176,177.000896))
verts.append((117.197411,21.908141,178.868479))
verts.append((97.097751,23.452599,183.471846))
verts.append((104.135986,34.310217,169.672289))
verts.append((102.667150,32.735730,170.661535))
verts.append((69.737747,34.122932,177.384414))
verts.append((126.577551,18.582310,181.550436))
verts.append((94.075793,34.001088,170.845583))
verts.append((73.935132,31.948383,179.995598))
verts.append((100.318648,28.241828,175.653740))
verts.append((101.166575,29.692063,174.015560))
verts.append((104.707916,31.440813,153.051592))
verts.append((91.433243,34.773688,172.764243))
verts.append((70.586095,33.912379,177.691843))
verts.append((94.170252,24.850313,182.701558))
verts.append((77.154704,27.385128,184.082524))
verts.append((75.998126,28.117467,179.813916))
verts.append((113.104718,25.962081,175.494578))
verts.append((59.185751,33.636819,178.510811))
verts.append((70.610396,14.093442,186.429139))
verts.append((63.958140,33.040737,180.074809))
verts.append((114.145912,30.257224,169.571901))
verts.append((47.903442,12.719383,189.737755))
verts.append((106.195071,29.845029,171.631839))
verts.append((89.558366,32.105781,174.978637))
verts.append((93.537930,33.483356,173.066575))
verts.append((108.141410,32.671339,169.707275))
verts.append((60.452704,27.126345,182.588942))
verts.append((68.269477,18.440503,185.718773))
verts.append((112.041430,32.488459,168.340632))
verts.append((120.973095,27.298223,173.757076))
verts.append((103.922036,21.802090,181.888774))
verts.append((63.611540,31.364914,180.338631))
verts.append((87.867964,20.170119,183.721407))
verts.append((100.776763,17.067539,182.032500))
verts.append((66.329734,34.684872,178.106292))
verts.append((81.866109,28.211572,179.685136))
verts.append((59.994928,35.580128,176.407379))
verts.append((115.208117,22.117392,179.455308))
verts.append((101.429939,23.290638,181.070197))
verts.append((100.772104,26.958035,176.592086))
verts.append((110.857114,33.410099,167.410982))
verts.append((97.674260,34.261572,167.490533))
verts.append((83.204877,33.144886,176.751498))
verts.append((76.212771,31.741703,178.889556))
verts.append((111.751736,33.916804,164.609829))
verts.append((57.663018,27.205649,182.737024))
verts.append((74.182671,35.574548,174.450209))
verts.append((104.219194,33.248443,159.315141))
verts.append((101.478905,33.681143,169.584271))
verts.append((115.150269,30.188187,166.397582))
verts.append((88.153514,31.954934,176.331479))
verts.append((74.516063,23.642633,184.804342))
verts.append((100.455962,30.414659,172.956522))
verts.append((124.750543,15.181526,181.577761))
verts.append((99.944581,33.346025,163.145078))
verts.append((118.973437,21.937584,178.811898))
verts.append((62.589836,32.960095,179.522269))
verts.append((85.726540,34.030285,163.595710))
verts.append((72.900519,26.806285,184.846429))
verts.append((80.198522,31.095590,179.056275))
verts.append((100.583082,33.418921,171.686169))
verts.append((102.045087,30.171364,172.515812))
verts.append((74.073722,33.782330,177.845314))
verts.append((51.805790,33.155502,177.421211))
verts.append((72.337974,32.369148,179.076175))
verts.append((67.545702,34.477460,167.564612))
verts.append((99.868223,32.821689,172.182389))
verts.append((71.063609,9.206517,187.408420))
verts.append((111.612958,27.558351,174.452723))
verts.append((94.777824,31.222429,175.322975))
verts.append((54.378897,34.297858,178.348161))
verts.append((63.131688,34.478709,169.182809))
verts.append((73.376926,34.178488,166.586184))
verts.append((97.608516,29.979743,173.871580))
verts.append((103.536899,0.342358,179.223163))
verts.append((49.848726,34.491236,175.551854))
verts.append((67.031264,33.637452,179.289891))
verts.append((107.296227,32.835333,170.151728))
verts.append((112.366125,22.537270,179.973886))
verts.append((57.766416,33.492493,179.511327))
verts.append((55.766848,34.886706,173.785568))
verts.append((76.406591,33.335680,177.765497))
verts.append((91.856629,33.473262,160.005588))
verts.append((76.141509,34.860986,176.666398))
verts.append((70.815168,4.354167,186.816694))
verts.append((71.565620,31.443184,179.754347))
verts.append((92.074583,33.958545,172.589212))
verts.append((109.946328,21.571412,180.608699))
verts.append((109.837529,32.048449,170.363039))
verts.append((99.093152,33.681185,160.676439))
verts.append((54.352279,4.977995,185.370614))
verts.append((88.724600,14.993885,183.717203))
verts.append((77.276059,8.300594,186.615804))
verts.append((48.955521,34.782308,171.919842))
verts.append((106.145687,28.840598,172.909854))
verts.append((115.182364,27.778124,173.081288))
verts.append((74.568199,16.593476,183.586410))
verts.append((92.407535,6.334008,183.186987))
verts.append((106.350237,8.942038,182.280980))
verts.append((50.491272,33.690515,176.074912))
verts.append((112.090721,31.621119,169.062738))
verts.append((77.632484,31.552564,178.362025))
verts.append((84.575048,26.668549,182.615041))
verts.append((89.822368,34.702923,172.907690))
verts.append((53.432552,9.091924,183.462345))
verts.append((118.389048,27.289389,173.647187))
verts.append((79.019940,31.199536,179.527475))
verts.append((103.481235,31.891967,171.976380))
verts.append((66.565360,21.816904,185.314261))
verts.append((70.162905,20.951087,184.878404))
verts.append((102.930146,24.452517,183.756708))
verts.append((85.934959,14.094138,184.756185))
verts.append((53.043842,35.066929,176.917091))
verts.append((116.579411,-0.753430,178.021955))
verts.append((72.770399,30.941585,167.181421))
verts.append((98.795037,34.236396,167.575594))
verts.append((80.110616,35.061173,175.665137))
verts.append((118.607231,15.972738,179.123528))
verts.append((70.833810,32.443164,178.828582))
verts.append((95.757342,17.406219,183.505996))
verts.append((55.817147,34.503462,177.938605))
verts.append((81.103445,7.296618,186.130813))
verts.append((66.209235,28.073050,183.017967))
verts.append((72.316108,34.570594,166.473349))
verts.append((101.700964,20.388017,181.666480))
verts.append((75.210818,27.113167,182.131482))
verts.append((96.993222,24.185710,182.566611))
verts.append((113.421512,34.623015,168.174973))
verts.append((100.771895,27.546459,174.842024))
verts.append((101.938034,33.565735,161.183539))
verts.append((69.178566,11.369049,186.367284))
verts.append((106.457233,33.116844,158.611511))
verts.append((102.143503,33.463001,172.107943))
verts.append((104.864715,31.956661,171.178676))
verts.append((52.531689,4.895124,186.278329))
verts.append((69.481109,17.637120,181.019754))
verts.append((66.830631,31.550124,179.993475))
verts.append((65.844175,2.646041,184.193773))
verts.append((93.692043,34.709279,172.646897))
verts.append((103.628610,27.138009,175.471198))
verts.append((99.079879,30.340269,174.132448))
verts.append((112.884864,33.112520,162.423786))
verts.append((48.420631,34.588505,174.340090))
verts.append((70.272261,25.880911,184.712071))
verts.append((78.665393,18.725198,185.357941))
verts.append((103.208624,29.585225,173.425828))
verts.append((127.892594,23.061999,180.906399))
verts.append((47.822618,34.228486,177.058464))
verts.append((109.742978,28.566344,173.254443))
verts.append((70.595926,31.512295,180.928385))
verts.append((114.191752,23.047984,178.397361))
verts.append((94.181799,28.977504,176.835310))
verts.append((60.873449,27.728044,183.430962))
verts.append((74.820077,35.559465,177.131194))
verts.append((87.503948,29.645286,178.500201))
verts.append((76.921519,34.055047,166.518754))
verts.append((98.616367,30.975148,174.859580))
verts.append((89.309242,18.979855,183.141107))
verts.append((80.466978,15.993922,185.653390))
verts.append((105.221586,26.071936,178.064719))
verts.append((117.496455,29.350058,169.764334))
verts.append((105.759923,16.121148,182.880648))
verts.append((74.093306,32.934009,177.894581))
verts.append((73.195576,19.920826,187.272358))
verts.append((103.221212,33.401440,159.245074))
verts.append((84.749460,35.330396,174.236558))
verts.append((92.580147,30.484800,175.996627))
verts.append((90.413397,29.030516,176.644320))
verts.append((94.534237,32.605354,173.868660))
verts.append((84.895458,14.117993,184.455096))
verts.append((78.244856,31.677030,174.576364))
verts.append((64.251276,34.717635,168.064231))
verts.append((96.590888,30.425841,175.304913))
verts.append((113.050424,23.207076,179.333765))
verts.append((114.462975,21.332564,179.897285))
verts.append((57.805749,31.888556,180.782227))
verts.append((74.229838,30.796303,180.680122))
verts.append((109.700539,27.582067,174.115011))
verts.append((67.186981,27.782329,182.323578))
verts.append((71.284881,35.004551,177.896154))
verts.append((88.365050,33.718073,174.667855))
verts.append((91.719946,30.121327,176.497237))
verts.append((108.365306,33.251929,168.237313))
verts.append((88.308091,31.103570,176.024011))
verts.append((107.110802,12.554861,181.641764))
verts.append((95.695899,34.517960,172.031853))
verts.append((99.097790,32.110405,172.538236))
verts.append((110.533363,33.098531,168.382575))
verts.append((90.913893,20.030647,183.517673))
verts.append((92.190966,7.492627,183.340493))
verts.append((97.839430,27.144361,176.671825))
verts.append((101.154884,34.528234,168.999173))
verts.append((49.971767,28.514438,187.722067))
verts.append((53.044960,7.322316,185.366419))
verts.append((55.713209,31.244897,177.702243))
verts.append((51.471108,32.735804,178.540762))
verts.append((73.726965,35.925934,177.766173))
verts.append((91.422598,33.573039,164.800177))
verts.append((65.042415,31.087819,181.074281))
verts.append((95.192359,29.727561,176.114478))
verts.append((77.814902,33.570351,176.228146))
verts.append((89.089831,35.350728,173.122900))
verts.append((47.158823,34.692319,177.268418))
verts.append((127.061347,22.007963,180.025746))
verts.append((116.033587,21.865177,178.877175))
verts.append((127.002179,11.947286,181.432935))
verts.append((111.566053,23.246755,178.813206))
verts.append((119.201324,21.127673,177.341758))
verts.append((54.607464,32.285849,176.207868))
verts.append((55.303715,32.158546,175.607961))
verts.append((119.216242,16.099674,181.018201))
verts.append((60.364702,32.132236,175.761272))
verts.append((65.095105,32.804245,177.638587))
verts.append((61.815248,32.909205,176.914350))
verts.append((67.764543,32.784735,177.047495))
verts.append((51.100913,33.117653,177.304361))
verts.append((119.805668,18.064837,181.752357))
verts.append((119.751913,21.110619,181.236688))
verts.append((51.771350,33.068598,177.116631))
verts.append((52.936230,6.965054,185.476640))
verts.append((64.055182,31.956129,172.094615))
verts.append((68.686686,19.145400,180.118119))
verts.append((90.921588,26.584759,181.874099))
verts.append((92.822655,18.567296,183.197515))
verts.append((73.267736,8.441370,180.853188))
verts.append((91.872824,17.850526,182.243058))
verts.append((92.594676,22.171613,181.393816))
verts.append((96.595736,17.134552,179.690258))
verts.append((95.564617,19.553749,180.427575))
verts.append((94.494348,18.516421,179.281467))
verts.append((71.172062,12.293345,179.509887))
verts.append((102.909167,23.499649,180.406896))
verts.append((94.579338,15.900777,180.808031))
verts.append((91.902910,22.119587,181.964524))
verts.append((96.931816,22.230162,175.773913))
verts.append((101.382683,18.024687,183.031060))
verts.append((98.546091,20.561004,176.995254))
verts.append((67.139813,25.752761,170.765898))
verts.append((89.549288,22.278730,182.669693))
verts.append((89.107982,22.201811,183.532244))
verts.append((92.857982,19.622757,180.951553))
verts.append((89.598305,22.282725,180.720613))
verts.append((88.883173,23.815655,180.899205))
verts.append((91.017473,22.347018,181.627650))
verts.append((90.621510,20.070140,182.986548))
verts.append((69.112972,18.686765,177.700109))
verts.append((68.695901,16.396833,175.361382))
verts.append((68.376651,19.491278,176.649856))
verts.append((68.255169,19.246831,177.738444))
verts.append((67.707295,23.692907,178.677499))
verts.append((69.939701,16.405605,176.768921))
verts.append((90.152717,19.023238,179.627441))
verts.append((67.816288,23.965657,179.782875))
verts.append((70.452242,15.572320,177.340174))
verts.append((68.704691,17.220930,175.844571))
verts.append((68.777372,18.228549,176.628704))
verts.append((68.838431,19.716751,178.201441))
verts.append((68.744111,19.236650,177.489947))
verts.append((69.644957,16.353905,176.269268))
verts.append((70.146568,16.340731,177.279973))
verts.append((69.565596,19.395518,179.353206))
verts.append((69.332187,11.229051,190.575349))
verts.append((84.848057,22.048271,183.395609))
verts.append((86.665439,16.895526,181.190188))
verts.append((87.829700,21.879712,183.593585))
verts.append((91.281591,24.541957,181.691639))
verts.append((92.376326,20.051738,179.153743))
verts.append((86.658854,21.013312,181.146815))
verts.append((90.860140,24.992704,181.223020))
verts.append((91.489921,22.542268,181.789809))
verts.append((91.313211,23.567658,183.039061))
verts.append((96.994634,17.052400,182.596029))
verts.append((89.817507,23.004840,180.300111))
verts.append((89.823604,19.292547,183.763067))
verts.append((91.617639,20.918191,181.941222))
verts.append((92.200241,21.706334,181.710702))
verts.append((91.985378,24.062903,181.083288))
verts.append((92.221739,22.084601,181.683330))
verts.append((93.599425,19.101130,182.998150))
verts.append((91.163202,23.637545,181.633161))
verts.append((91.356855,18.502804,183.864593))
verts.append((90.105032,21.173618,180.721703))
verts.append((92.398591,23.140426,181.182903))
verts.append((93.650767,19.882353,182.947859))
verts.append((90.693487,24.397124,181.886992))
verts.append((92.640748,21.447310,181.953628))
verts.append((89.637516,18.737573,183.789247))
verts.append((92.398514,20.673450,182.096918))
verts.append((90.108703,21.555469,180.546780))
verts.append((92.678931,21.809621,181.858015))
verts.append((89.330195,21.865859,180.737425))
verts.append((87.986218,26.649263,180.299086))
verts.append((91.278752,14.534651,184.165523))
verts.append((88.041694,24.483199,181.760424))
verts.append((89.437694,24.026716,182.373057))
verts.append((90.552430,22.817646,182.324759))
verts.append((92.453337,20.352222,181.489774))
verts.append((89.613496,19.811281,183.593632))
verts.append((90.053851,22.550370,181.083641))
verts.append((91.150080,20.350223,183.286255))
verts.append((90.267505,19.063374,183.540326))
verts.append((68.060980,13.991495,175.105061))
verts.append((87.699659,24.829859,180.741573))
verts.append((88.024189,25.214657,182.967284))
verts.append((87.061122,25.197564,182.108991))
verts.append((87.423780,24.192616,181.149290))
verts.append((90.111871,22.536101,183.035761))
verts.append((88.928493,23.505393,182.697554))
verts.append((94.688069,24.566567,181.362652))
verts.append((95.206281,24.383913,181.293798))
verts.append((88.324235,23.272626,181.685174))
verts.append((67.086576,18.306626,120.305913))
verts.append((98.740768,13.073603,189.095740))
verts.append((89.057705,19.102735,182.731083))
verts.append((89.838440,23.226912,182.500345))
verts.append((88.678390,21.227108,180.443238))
verts.append((96.027615,18.947016,182.039244))
verts.append((88.290947,24.050372,182.470761))
verts.append((95.644679,16.608832,178.571542))
verts.append((94.943909,18.304182,178.464704))
verts.append((92.959932,23.756145,181.367999))
verts.append((93.078532,24.391703,181.340107))
verts.append((88.459700,22.368060,182.938439))
verts.append((93.988108,19.660376,179.440060))
verts.append((90.776577,16.062755,171.674087))
verts.append((91.116820,24.082567,182.065446))
verts.append((87.622111,23.968710,183.019089))
verts.append((87.228269,24.760735,182.947953))
verts.append((87.553886,20.365367,183.489133))
verts.append((94.570770,19.379881,180.989628))
verts.append((94.491744,19.882089,179.737783))
verts.append((87.274213,23.169712,183.082134))
verts.append((87.389268,23.581087,183.062074))
verts.append((92.561751,23.792366,181.604000))
verts.append((94.941050,19.291634,179.835415))
verts.append((93.476132,20.704547,181.324166))
verts.append((94.488454,19.139860,181.486995))
verts.append((85.354834,21.469767,180.381620))
verts.append((93.147009,23.251051,181.343095))
verts.append((92.407025,24.787281,181.143519))
verts.append((94.783903,17.287505,181.282678))
verts.append((86.832663,23.603468,183.288648))
verts.append((88.066590,21.351003,184.149148))
verts.append((87.101741,21.661445,183.484056))
verts.append((86.885438,21.215747,184.448754))
verts.append((86.459067,22.160846,183.789641))
verts.append((93.081263,19.408486,179.165625))
verts.append((88.762009,22.879607,182.853017))
verts.append((95.118497,17.871811,182.998746))
verts.append((94.736243,18.290544,180.263071))
verts.append((90.965752,14.923431,171.815681))
verts.append((95.068220,14.250228,180.464938))
verts.append((95.927318,16.655874,179.157540))
verts.append((113.185667,49.049649,285.972335))
verts.append((94.236348,19.021128,179.786332))
verts.append((95.922980,16.968923,180.562995))
verts.append((95.064477,16.189018,178.730196))
verts.append((95.504723,15.005002,179.795199))
verts.append((95.744862,18.031057,179.589091))
verts.append((95.013633,16.526665,178.703696))
verts.append((93.254624,15.041507,176.707020))
verts.append((95.829103,16.654106,180.533565))
verts.append((96.107228,17.141932,180.345225))
verts.append((95.606811,15.204318,181.073018))
verts.append((94.310227,18.430038,180.367875))
verts.append((86.294634,29.337448,193.227132))
verts.append((94.846743,18.664543,182.356334))
verts.append((92.880122,18.567483,180.169944))
verts.append((91.864960,23.227239,181.993531))
verts.append((97.344103,15.179831,182.536001))
verts.append((93.797732,24.537000,184.839478))
verts.append((93.377913,18.355653,182.883226))
verts.append((92.556445,23.337906,182.427951))
verts.append((96.033290,16.567799,178.462206))
verts.append((93.321656,17.042814,183.459710))
verts.append((96.980421,15.362470,182.816981))
verts.append((94.324214,15.388950,177.688843))
verts.append((95.888996,17.731963,182.586760))
verts.append((95.744812,15.630466,179.418415))
verts.append((84.500449,23.414732,183.140097))
verts.append((96.316143,27.967240,200.155931))
verts.append((95.437386,15.312059,180.385439))
verts.append((94.103447,20.399722,181.324243))
verts.append((102.353651,17.106993,194.597083))
verts.append((94.544229,16.031930,177.105520))
verts.append((93.712430,20.339448,186.070505))
verts.append((91.012210,14.878432,172.001919))
verts.append((92.328249,22.116557,181.641517))
verts.append((94.452189,18.208278,180.200792))
verts.append((95.163651,18.269783,182.338070))
verts.append((92.888482,21.971148,184.355393))
verts.append((95.528070,18.046974,182.517126))
verts.append((92.583269,23.783342,186.769292))
verts.append((98.507462,15.518119,183.986343))
verts.append((96.372805,16.090212,177.914518))
verts.append((93.192538,20.611837,183.229773))
verts.append((92.794770,27.362916,185.534757))
verts.append((96.157106,19.041228,190.410354))
verts.append((92.397862,22.444444,181.812595))
verts.append((91.424188,24.220455,182.414202))
verts.append((93.089828,19.018722,182.546808))
verts.append((94.697613,14.957199,176.946377))
verts.append((91.415692,22.177114,180.422192))
verts.append((88.489195,24.916586,182.747106))
verts.append((88.434598,24.672659,182.852618))
verts.append((91.823920,22.764528,182.862412))
verts.append((93.730174,21.825334,188.345649))
verts.append((92.112384,24.747744,185.366603))
verts.append((84.916605,23.859160,183.801565))
verts.append((91.220585,21.509769,179.719903))
verts.append((96.511851,39.217409,223.437031))
verts.append((87.356899,29.837619,198.310503))
verts.append((90.760930,21.246460,182.045492))
verts.append((92.659971,18.560211,182.865579))
verts.append((87.950407,23.314838,178.388840))
verts.append((90.643022,20.704179,177.112884))
verts.append((88.421094,25.675541,188.027677))
verts.append((85.452312,24.653859,183.195895))
verts.append((89.993877,23.577533,184.945177))
verts.append((94.040072,17.992711,183.062843))
verts.append((97.782796,17.954166,181.892649))
verts.append((91.302619,23.745901,182.825273))
verts.append((90.800104,22.741339,179.809437))
verts.append((95.548402,24.626026,181.931471))
verts.append((97.463629,18.215666,187.495274))
verts.append((90.942958,20.693754,182.995070))
verts.append((94.020465,25.129675,185.970462))
verts.append((92.804107,22.906596,182.887392))
verts.append((99.955393,27.955536,187.303875))
verts.append((93.919531,14.749540,178.693573))
verts.append((93.433467,19.206279,181.520323))
verts.append((92.010089,27.898280,186.977967))
verts.append((96.307571,18.556052,182.525910))
verts.append((98.481282,23.279670,181.095914))
verts.append((90.772937,20.193996,183.022507))
verts.append((94.669643,19.450804,182.958486))
verts.append((98.843451,23.073877,181.542980))
verts.append((97.693234,15.769054,182.990428))
verts.append((93.310084,24.603696,180.930934))
verts.append((97.399560,16.915785,182.252138))
verts.append((76.699303,15.921622,173.752807))
verts.append((93.844514,18.011560,185.443304))
verts.append((92.021801,27.127919,185.214685))
verts.append((91.277723,24.634848,183.946631))
verts.append((92.576184,21.984113,182.721362))
verts.append((91.740119,24.247855,182.467255))
verts.append((91.658449,23.936870,182.960171))
verts.append((91.646513,26.880799,182.889802))
verts.append((90.628463,19.917029,182.886625))
verts.append((96.792979,27.366480,185.718809))
verts.append((93.274215,22.501567,183.385211))
verts.append((92.779546,19.470702,182.244267))
verts.append((91.559746,22.587154,183.283349))
verts.append((92.067360,19.320490,182.793197))
verts.append((96.615505,16.342551,182.749932))
verts.append((98.236707,16.771014,180.881671))
verts.append((91.399437,21.860551,183.351409))
verts.append((98.153736,15.244668,182.347955))
verts.append((98.132168,16.151884,180.339904))
verts.append((98.791654,18.338625,181.572959))
verts.append((94.166845,19.030367,178.427345))
verts.append((97.755635,15.290225,182.172356))
verts.append((92.490249,20.230805,178.670879))
verts.append((90.771993,25.414074,182.414910))
verts.append((98.854956,22.643631,180.713286))
verts.append((90.340379,17.414044,184.125224))
verts.append((92.046758,21.821876,182.974827))
verts.append((98.507193,18.084252,181.436833))
verts.append((98.647535,16.536061,182.369895))
verts.append((93.798299,19.545024,182.419539))
verts.append((99.216199,18.072924,182.496123))
verts.append((90.386201,16.467665,183.789164))
verts.append((95.696157,18.380924,182.251144))
verts.append((99.002657,20.487518,181.156234))
verts.append((98.204394,18.010244,182.117274))
verts.append((69.047186,34.918126,200.896291))
verts.append((76.138340,29.877614,191.738996))
verts.append((195.723195,-136.185060,-298.464454))
verts.append((78.243082,26.335211,182.555991))
verts.append((69.073934,33.862175,200.499298))
verts.append((3.485761,-29.880730,14.139400))
verts.append((63.411059,-6.961916,79.700752))
verts.append((64.146641,-6.899968,79.758064))
verts.append((100.378117,24.162421,179.957901))
verts.append((73.525274,-34.473214,-5.370029))
verts.append((85.776740,27.671505,189.303576))
verts.append((83.309624,4.391995,116.547990))
verts.append((33.739106,-32.383144,-6.647894))
verts.append((106.158894,-49.555981,-32.745106))
verts.append((101.317935,22.314559,181.013227))
verts.append((100.067348,20.024954,181.071049))
verts.append((97.378591,-43.131472,-17.202393))
verts.append((99.855131,23.695943,181.479304))
verts.append((74.789402,15.224619,173.367809))
verts.append((73.927627,15.386020,174.877903))
verts.append((100.598057,23.456904,181.209581))
verts.append((75.198834,15.279111,173.271113))
verts.append((101.323404,22.489137,180.735967))
verts.append((78.774090,15.898449,173.793491))
verts.append((101.155693,23.333844,181.240562))
verts.append((102.394573,23.023194,181.815493))
verts.append((78.678028,15.614020,177.166187))
verts.append((101.815738,22.049035,181.275991))
verts.append((101.620354,23.117931,180.852498))
verts.append((77.229120,15.505119,180.567513))
verts.append((78.989339,15.895133,174.344924))
verts.append((101.419911,23.131869,181.229398))
verts.append((101.569473,22.802622,180.963388))
verts.append((99.666732,21.840024,181.804029))
verts.append((100.908738,23.560930,180.784213))
verts.append((99.573904,20.662074,181.734857))
verts.append((101.161214,20.359525,181.256393))
verts.append((99.533173,22.350446,181.412752))
verts.append((101.125800,22.414106,181.245705))
verts.append((104.250905,22.466708,184.947807))
verts.append((114.612726,27.061138,203.870358))
verts.append((110.233732,23.329723,194.684890))
verts.append((103.987870,24.739189,183.917400))
verts.append((102.106359,22.908619,181.438989))
verts.append((102.285708,22.994948,182.999695))
verts.append((101.357289,22.739779,180.694134))
verts.append((101.852872,22.341913,181.981008))
verts.append((102.831278,23.319519,182.307452))
verts.append((132.904263,31.091667,231.242876))
verts.append((102.430388,20.314970,182.516078))
verts.append((101.752652,22.035627,181.300232))
verts.append((101.389312,18.873438,181.496319))
verts.append((102.826027,22.368696,182.286209))
verts.append((101.317318,18.580248,181.414006))
verts.append((101.450880,19.302111,181.444876))
verts.append((103.646396,22.130860,184.333812))
verts.append((101.211159,15.982616,183.526244))
verts.append((101.952877,23.209665,181.369175))
verts.append((118.103564,28.588195,209.788197))
verts.append((102.587100,24.173765,182.350979))
verts.append((101.703252,19.779465,181.765891))
verts.append((102.663654,16.004956,184.001181))
verts.append((102.552329,18.820805,182.991416))
verts.append((102.214970,22.592317,181.755650))
verts.append((98.644495,24.475021,182.491272))
verts.append((99.824359,22.162730,182.123154))
verts.append((93.077508,23.299135,183.743939))
verts.append((106.166856,27.015802,182.984582))
verts.append((102.695183,15.907636,184.543332))
verts.append((103.060794,26.673726,186.032151))
verts.append((103.080031,20.178543,181.943580))
verts.append((101.472179,14.851453,181.826965))
verts.append((102.426704,16.822010,182.790218))
verts.append((108.387918,27.492068,190.175191))
verts.append((100.588566,22.875529,181.742067))
verts.append((103.308108,19.375194,182.249098))
verts.append((107.653199,22.444421,187.393876))
verts.append((100.925561,16.984381,181.264464))
verts.append((99.774994,20.836056,178.340500))
verts.append((104.307931,26.793875,187.626735))
verts.append((103.408262,23.171106,182.439853))
verts.append((100.547279,18.059057,182.621157))
verts.append((103.018772,23.301230,181.542100))
verts.append((101.336618,20.326208,181.935643))
verts.append((100.714435,20.714900,181.357068))
verts.append((100.900489,24.167686,181.745974))
verts.append((100.187447,21.989210,181.698487))
verts.append((101.968078,23.644455,179.178491))
verts.append((104.134387,21.671045,183.695814))
verts.append((105.062239,27.781798,185.660030))
verts.append((102.814903,21.741669,182.798646))
verts.append((99.691205,21.854540,181.898031))
verts.append((101.519107,19.311692,181.562789))
verts.append((101.444663,18.760328,181.997258))
verts.append((97.645425,22.641097,181.420217))
verts.append((102.802686,21.899031,180.796664))
verts.append((100.592125,19.038870,181.895490))
verts.append((103.985486,21.497654,178.893749))
verts.append((101.597439,26.567332,183.028932))
verts.append((100.697878,20.392906,181.698761))
verts.append((103.504043,24.997867,185.598279))
verts.append((97.781643,16.901719,183.199108))
verts.append((100.515563,17.102741,182.363931))
verts.append((101.856521,18.819565,181.166838))
verts.append((100.148273,23.400861,181.468312))
verts.append((98.209861,20.130272,182.368689))
verts.append((102.051594,20.070807,180.961713))
verts.append((103.720687,21.011698,182.354659))
verts.append((103.352445,22.846878,181.467930))
verts.append((105.316802,23.555808,182.737643))
verts.append((98.586701,15.690203,182.478290))
verts.append((97.656369,19.461907,180.493781))
verts.append((100.235543,17.586687,182.071977))
verts.append((99.455222,20.525545,181.975067))
verts.append((98.463185,15.564732,183.046233))
verts.append((103.197912,24.467230,180.339701))
verts.append((106.888618,25.139227,186.375472))
verts.append((100.100743,16.530396,182.855653))
verts.append((104.714469,22.625360,180.370359))
verts.append((99.742261,16.409200,182.500886))
verts.append((100.823650,19.871028,182.009883))
verts.append((100.764058,20.272672,182.589871))
verts.append((108.431116,26.337191,185.801544))
verts.append((94.499997,24.869087,181.846303))
verts.append((96.823006,23.030485,182.354985))
verts.append((96.236546,18.781949,182.594347))
verts.append((101.193887,15.177262,182.346809))
verts.append((104.425618,24.989766,181.310316))
verts.append((99.175669,18.341482,182.103439))
verts.append((98.758600,24.089011,181.227712))
verts.append((103.627975,23.441268,179.256033))
verts.append((98.043897,15.267596,182.650662))
verts.append((94.700020,17.538638,183.027455))
verts.append((100.400983,22.984171,180.774252))
verts.append((104.338360,25.024995,184.367178))
verts.append((102.671886,21.391486,181.190217))
verts.append((100.344215,24.552801,179.054238))
verts.append((106.775426,24.787187,185.304173))
verts.append((106.685847,21.489404,185.680772))
verts.append((108.595692,28.159639,186.618418))
verts.append((98.192962,18.517014,182.184429))
verts.append((97.505747,19.255188,182.834571))
verts.append((106.571312,24.805468,183.754005))
verts.append((95.347817,22.070556,182.729396))
verts.append((97.158970,19.013286,182.933484))
verts.append((98.111766,19.720776,182.197904))
verts.append((98.530608,16.221887,180.004082))
verts.append((97.445165,18.945138,182.684297))
verts.append((75.841459,15.616649,187.020844))
verts.append((76.676848,15.065118,186.187575))
verts.append((108.498338,27.733122,183.186439))
verts.append((163.552278,27.639113,300.607574))
verts.append((77.435980,15.113300,186.903568))
verts.append((90.096063,27.162500,179.408397))
verts.append((77.468134,14.645944,186.384601))
verts.append((70.476122,15.930238,177.245444))
verts.append((77.274621,15.646035,175.989554))
verts.append((86.020771,25.858881,183.936029))
verts.append((76.533094,15.505223,184.497307))
verts.append((82.361674,15.089283,185.464525))
verts.append((87.815118,27.010832,188.560410))
verts.append((99.751408,16.348900,178.475702))
verts.append((101.855522,20.583517,171.006294))
verts.append((95.996664,13.663087,182.695472))
verts.append((107.898043,14.570668,195.647015))
verts.append((93.982369,17.843555,183.396381))
verts.append((100.016234,23.898925,181.962557))
verts.append((98.378238,21.808430,181.730448))
verts.append((100.588962,23.460428,185.454088))
verts.append((74.376844,16.260806,166.692930))
verts.append((95.988350,18.062745,179.069989))
verts.append((76.930044,14.898527,173.573204))
verts.append((93.598815,20.429439,183.315849))
verts.append((97.479748,23.012606,181.995469))
verts.append((488.217136,333.917816,975.416179))
verts.append((167.480641,80.173686,307.400405))
verts.append((101.558136,22.944329,187.230449))
verts.append((76.568792,15.602896,172.473816))
verts.append((468.467360,879.634307,2407.233512))
verts.append((101.081952,20.752170,178.399908))
verts.append((97.869971,21.597341,180.640506))
verts.append((97.847925,20.866754,181.333098))
verts.append((96.035848,17.200403,182.161711))
verts.append((99.894279,27.049540,181.004490))
verts.append((96.186612,22.660618,173.215909))
verts.append((97.560162,25.688571,181.012620))
verts.append((98.049915,17.542967,181.574977))
verts.append((104.981525,25.060860,189.649016))
verts.append((98.294324,22.831219,174.213464))
verts.append((96.548891,24.595424,181.818540))
verts.append((108.613056,22.934905,179.699054))
verts.append((109.310855,11.473530,190.112871))
verts.append((106.176358,20.593876,179.469682))
verts.append((100.014040,13.474793,171.631424))
verts.append((103.700840,11.333370,178.149269))
verts.append((110.236731,21.296556,184.467819))
verts.append((108.585744,22.134514,179.285836))
verts.append((111.705206,22.276512,183.347935))
verts.append((104.004311,12.609324,180.895560))
verts.append((110.581268,13.344018,191.752952))
verts.append((105.274067,13.781558,182.122328))
verts.append((108.705633,21.852845,181.651692))
verts.append((98.469289,13.201217,167.649861))
verts.append((122.979567,10.858712,220.299840))
verts.append((101.324267,19.672215,170.368677))
verts.append((107.702912,24.357653,184.393426))
verts.append((108.572704,22.352211,180.504632))
verts.append((113.185616,24.306461,189.326594))
verts.append((108.644781,20.688410,183.355419))
verts.append((113.281733,26.654396,184.680549))
verts.append((73.876599,15.322004,165.310282))
verts.append((105.063460,21.212737,176.352177))
verts.append((114.417846,26.324115,190.638257))
verts.append((74.259653,15.329765,165.174649))
verts.append((74.154299,15.605108,165.023737))
verts.append((108.410091,22.280028,181.448288))
verts.append((187.015283,44.977618,314.029423))
verts.append((111.009567,24.515682,184.782029))
verts.append((104.749813,21.845881,174.509698))
verts.append((74.533972,14.710550,166.119651))
verts.append((109.132043,26.740968,180.509166))
verts.append((108.895132,20.215275,183.079172))
verts.append((110.883004,24.337003,186.758920))
verts.append((113.074538,23.234195,190.489034))
verts.append((108.303827,25.754574,187.221874))
verts.append((73.774012,15.635406,165.516122))
verts.append((74.003819,14.730523,165.080493))
verts.append((464.361507,183.798931,840.769531))
verts.append((149.630091,56.246174,264.668701))
verts.append((93.640589,23.518364,182.605727))
verts.append((87.888811,20.759234,183.151002))
verts.append((93.217596,17.747478,183.367337))
verts.append((91.580610,18.378309,183.594259))
verts.append((89.120337,20.720329,182.935818))
verts.append((95.530048,24.499351,181.746959))
verts.append((94.035876,24.329153,184.579049))
verts.append((88.781137,22.166011,183.827907))
verts.append((90.376129,15.368275,183.888281))
verts.append((88.226216,20.926952,183.667772))
verts.append((250.177563,123.196556,430.380290))
verts.append((93.667219,18.329599,183.132782))
verts.append((94.620815,22.038479,182.149310))
verts.append((92.165993,20.741854,183.795952))
verts.append((76.427903,18.270047,127.845280))
verts.append((91.113578,22.155588,183.372595))
verts.append((86.436369,19.481462,184.294773))
verts.append((92.283134,25.496100,181.922475))
verts.append((96.310242,20.111912,181.942018))
verts.append((89.001299,21.201014,183.806029))
verts.append((97.648595,22.806823,181.199505))
verts.append((105.848114,14.462646,181.571361))
verts.append((98.741533,24.592602,179.058921))
verts.append((102.124651,21.136975,176.681260))
verts.append((104.174313,21.928295,181.421072))
verts.append((91.202758,17.231991,184.386025))
verts.append((103.250596,25.705926,177.011732))
verts.append((97.669235,19.031644,181.912845))
verts.append((92.978687,29.120983,184.772331))
verts.append((98.326558,13.327758,182.239575))
verts.append((102.353773,25.792317,176.242572))
verts.append((98.101968,15.545420,182.751318))
verts.append((94.476622,24.643023,181.882391))
verts.append((75.493688,16.162359,164.403554))
verts.append((97.802651,23.514590,181.821865))
verts.append((96.234236,24.133026,181.966417))
verts.append((99.962159,23.033195,181.638742))
verts.append((102.408566,21.346028,180.831265))
verts.append((104.425019,15.579898,181.228807))
verts.append((107.874945,23.083373,179.574397))
verts.append((104.584611,24.578974,182.153248))
verts.append((104.700490,22.615364,180.761184))
verts.append((107.666386,23.664681,179.566445))
verts.append((102.195798,25.049520,181.721709))
verts.append((104.183376,24.024840,179.828228))
verts.append((103.071731,14.572220,179.627452))
verts.append((105.195291,24.263949,181.011526))
verts.append((113.607346,38.867968,183.335477))
verts.append((100.325642,25.388799,183.956438))
verts.append((93.852738,39.582924,196.806644))
verts.append((103.543402,21.741359,182.329783))
verts.append((88.196638,24.451135,180.745549))
verts.append((91.306482,23.881457,180.910989))
verts.append((90.883228,23.837101,183.800817))
verts.append((88.346145,25.193043,182.096722))
verts.append((91.650334,25.066366,185.780140))
verts.append((92.133754,19.748844,183.827548))
verts.append((87.431428,23.423507,180.734566))
verts.append((87.105268,23.736657,180.099149))
verts.append((84.726710,18.479924,184.817531))
verts.append((91.458229,21.839836,184.093750))
verts.append((91.226588,16.656484,183.569648))
verts.append((89.962889,18.134648,183.902947))
verts.append((91.644154,19.569947,183.711296))
verts.append((90.787707,19.374107,181.631590))
verts.append((87.338350,23.215894,187.557622))
verts.append((89.360709,24.892193,181.012241))
verts.append((90.022627,16.833839,186.136002))
verts.append((92.680183,24.488665,183.015697))
verts.append((91.050339,20.295793,184.263164))
verts.append((74.853446,14.196544,167.141627))
verts.append((91.797304,19.454779,186.269442))
verts.append((92.211966,22.529006,182.685474))
verts.append((90.671711,25.422647,183.330475))
verts.append((99.043443,22.189412,179.719368))
verts.append((91.204505,20.958451,183.668287))
verts.append((91.610159,22.732786,181.928942))
verts.append((92.865938,21.609255,182.527754))
verts.append((87.882142,21.895520,183.070611))
verts.append((92.919509,21.006762,184.271599))
verts.append((91.853696,24.753215,181.203132))
verts.append((89.361203,15.264628,183.573803))
verts.append((118.078633,28.110527,187.258674))
verts.append((89.639960,23.870093,182.800047))
verts.append((92.678001,23.480799,182.976465))
verts.append((95.678944,17.798849,183.769145))
verts.append((91.866898,22.134991,182.520361))
verts.append((87.937145,22.958652,182.186637))
verts.append((91.356303,20.062325,182.463971))
verts.append((91.585592,18.858520,182.008089))
verts.append((88.654938,23.633439,184.060160))
verts.append((91.974296,21.434970,184.311918))
verts.append((91.192025,16.118785,182.548214))
verts.append((92.851973,18.512036,183.705618))
verts.append((92.309005,19.212342,183.058799))
verts.append((92.412914,22.066561,182.564951))
verts.append((92.602459,21.872949,183.899946))
verts.append((89.873158,17.496750,184.005428))
verts.append((89.103433,17.046125,183.491570))
verts.append((92.645288,20.462566,183.387431))
verts.append((90.926529,17.464146,182.764903))
verts.append((89.455538,19.039682,183.143055))
verts.append((95.448410,18.175973,182.895585))
verts.append((107.297471,22.830114,179.726810))
verts.append((92.971021,21.944661,182.144003))
verts.append((96.119765,23.296255,182.405712))
verts.append((112.493567,19.833963,178.945500))
verts.append((86.016574,16.924476,185.028060))
verts.append((87.977610,26.190488,189.020582))
verts.append((88.918343,23.031309,183.233816))
verts.append((95.199947,19.220772,183.745753))
verts.append((112.142672,25.077810,181.826957))
verts.append((90.641706,18.526597,183.176621))
verts.append((92.158040,21.047758,182.678420))
verts.append((89.520622,16.221696,183.957836))
verts.append((94.429898,20.626369,182.448701))
verts.append((91.626016,20.690579,183.605601))
verts.append((89.182356,18.075461,183.087850))
verts.append((93.542306,19.645914,183.338818))
verts.append((93.665282,15.287206,182.427255))
verts.append((88.851577,22.475808,183.255802))
verts.append((90.839581,18.393581,181.532684))
verts.append((88.756301,19.036907,183.787370))
verts.append((92.850082,21.371607,183.712170))
verts.append((89.475187,22.786429,183.105228))
verts.append((90.242980,18.678002,184.984374))
verts.append((95.464964,18.691157,183.514723))
verts.append((93.480468,25.085167,182.008145))
verts.append((99.024499,24.238093,182.083610))
verts.append((89.730883,19.874939,183.184730))
verts.append((111.827110,27.162728,180.178668))
verts.append((103.072761,23.036518,179.441636))
verts.append((90.817824,23.090289,180.951877))
verts.append((93.643550,20.022734,183.170513))
verts.append((92.195378,17.887494,183.987139))
verts.append((86.231921,26.439328,184.589499))
verts.append((96.231987,18.479770,182.229728))
verts.append((91.493011,17.787129,182.992945))
verts.append((88.477528,22.578938,178.908158))
verts.append((91.239942,25.454197,183.626685))
verts.append((114.863542,30.502259,180.189976))
verts.append((95.303167,20.436770,184.122139))
verts.append((93.351638,25.547549,184.052039))
verts.append((94.871709,18.713912,183.275746))
verts.append((91.901910,20.065292,182.303322))
verts.append((105.806644,21.524253,182.716743))
verts.append((98.439028,22.761939,178.733269))
verts.append((97.056844,25.066772,183.961352))
verts.append((90.434784,25.608800,186.774215))
verts.append((92.834365,22.341745,181.995730))
verts.append((90.512632,23.679034,184.425629))
verts.append((95.777564,20.273764,182.256978))
verts.append((92.597709,19.984785,183.189033))
verts.append((94.157733,25.198643,183.058355))
verts.append((93.994108,18.520343,182.486100))
verts.append((94.333803,17.975273,182.517022))
verts.append((94.205725,18.284066,183.841542))
verts.append((93.292764,20.644985,180.466001))
verts.append((92.492987,18.884024,184.053493))
verts.append((95.838768,25.306447,183.280082))
verts.append((90.115830,20.780369,184.156330))
verts.append((94.983608,19.948310,183.777869))
verts.append((91.707035,18.254151,183.035730))
verts.append((95.398623,33.651689,190.472456))
verts.append((95.165975,24.619193,186.050154))
verts.append((85.373133,18.332854,184.751464))
verts.append((85.879519,47.141658,211.197536))
verts.append((94.550933,19.393031,182.748531))
verts.append((92.144402,21.964948,184.199261))
verts.append((93.121825,24.015307,183.084685))
verts.append((92.141727,17.331304,182.674729))
verts.append((93.171553,21.110060,182.646839))
verts.append((97.202553,23.568156,184.556852))
verts.append((99.614164,15.771826,182.320751))
verts.append((96.661769,19.332527,182.288519))
verts.append((95.513882,19.937564,183.982833))
verts.append((92.676802,25.265271,183.065511))
verts.append((90.192005,20.902002,182.352419))
verts.append((101.351086,22.449481,177.644885))
verts.append((112.137925,20.405671,179.234643))
verts.append((111.724230,20.950007,178.285249))
verts.append((111.899381,19.713688,179.016804))
verts.append((106.030006,19.982434,180.722917))
verts.append((104.997469,20.652754,181.408381))
verts.append((104.891894,23.013125,180.908567))
verts.append((112.491160,20.650543,178.737818))
verts.append((106.832048,19.805366,179.551156))
verts.append((105.141674,22.335990,179.312834))
verts.append((111.711173,22.640803,176.102647))
verts.append((105.987426,21.062099,179.176270))
verts.append((103.038943,21.950386,180.299824))
verts.append((103.079252,19.474850,169.860042))
verts.append((107.837651,22.322179,180.321107))
verts.append((105.237993,23.711228,179.788955))
verts.append((105.585487,23.563334,179.007298))
verts.append((93.226462,24.481329,183.087752))
verts.append((105.296939,22.306280,181.149046))
verts.append((107.162025,21.525420,179.998053))
verts.append((111.637183,19.986602,176.182113))
verts.append((105.688534,23.183151,181.049900))
verts.append((106.662042,23.010005,179.941782))
verts.append((97.477792,15.077054,182.446646))
verts.append((108.843809,34.287253,183.740221))
verts.append((108.653124,24.193050,181.062050))
verts.append((106.519477,22.624357,180.720810))
verts.append((114.146674,33.109133,183.316123))
verts.append((109.582929,33.683519,181.302421))
verts.append((97.221671,14.489456,181.307193))
verts.append((107.052329,29.871290,184.419685))
verts.append((108.815720,31.627108,183.321700))
verts.append((94.245154,19.507448,183.265746))
verts.append((87.025496,25.098057,184.467627))
verts.append((102.036065,24.112789,180.672796))
verts.append((103.906126,21.818982,181.052676))
verts.append((104.032585,20.507032,176.796719))
verts.append((103.242993,23.467447,181.524425))
verts.append((104.700747,18.330165,178.380274))
verts.append((104.549335,22.684771,181.673971))
verts.append((102.762099,16.202999,180.806523))
verts.append((114.775293,37.090781,190.259560))
verts.append((103.430931,20.764520,178.722621))
verts.append((106.004617,21.657804,177.836533))
verts.append((112.609555,20.750082,177.775772))
verts.append((102.022924,23.833205,179.208242))
verts.append((103.526975,21.260179,178.621959))
verts.append((94.631172,17.507869,183.656561))
verts.append((103.264321,21.157332,180.195185))
verts.append((105.019748,11.150400,180.899425))
verts.append((103.254393,19.244073,178.325892))
verts.append((110.480086,21.363154,175.636258))
verts.append((102.968155,20.150259,177.999396))
verts.append((104.725540,18.697375,177.797261))
verts.append((111.071771,21.309578,178.481150))
verts.append((111.920225,22.178673,179.350865))
verts.append((87.727271,16.064335,184.121509))
verts.append((86.616103,21.374866,184.336034))
verts.append((90.070842,24.323351,180.409638))
verts.append((77.281146,43.072469,205.071592))
verts.append((93.852379,17.370901,182.943388))
verts.append((96.485856,19.971145,184.015056))
verts.append((91.318673,22.276833,182.915320))
verts.append((90.049065,22.778587,182.078879))
verts.append((93.239322,20.229024,183.796725))
verts.append((93.578825,21.824588,182.847121))
mesh.data.from_pydata(verts, [], [])
mesh.data.update()
