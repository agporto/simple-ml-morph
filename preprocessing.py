import argparse
import os
import utils


ap = argparse.ArgumentParser()
ap.add_argument('-i','--input-dir', type=str, default='images', help="input directory containing image files (default = images)", metavar='')
ap.add_argument('-c','--csv-file', type=str, default=None, help="(optional) XY coordinate file in csv format", metavar='')
ap.add_argument('-t','--tps-file', type=str, default=None, help="(optional) tps coordinate file", metavar='')
ap.add_argument('-r','--resolution', type=float, default=float(1), help="(optional) scalar to change image and landmark resolution", metavar='')
ap.add_argument('-m','--method', type=str, default='INTER_LINEAR', help="(optional) interpolation method used to change image resolution. See cv2.resize() for options", metavar='')

    
args = vars(ap.parse_args())

assert os.path.isdir(args['input_dir']), "Could not find the folder {}".format(args['input_dir'])

file_sizes=utils.split_train_test(args['input_dir'],args['resolution'],args['method'])

if args['csv_file'] is not None:
    dict_csv=utils.read_csv(args['csv_file'],scalar = args['resolution'])
    utils.generate_dlib_xml(dict_csv,file_sizes['train'],folder='train',out_file='train.xml')
    utils.generate_dlib_xml(dict_csv,file_sizes['test'],folder='test',out_file='test.xml')
    utils.dlib_xml_to_tps('train.xml')
    utils.dlib_xml_to_tps('test.xml')
    
    
    
if args['tps_file'] is not None:
    dict_tps=utils.read_tps(args['tps_file'],scalar = args['resolution'])
    utils.generate_dlib_xml(dict_tps,file_sizes['train'],folder='train',out_file='train.xml')
    utils.generate_dlib_xml(dict_tps,file_sizes['test'],folder='test',out_file='test.xml')
    utils.dlib_xml_to_tps('train.xml')
    utils.dlib_xml_to_tps('test.xml')
  
